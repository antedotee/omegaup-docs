#!/usr/bin/env python3
"""
Translate docs from docs/en -> docs/{es,pt,pt-BR} using the public
Google Translate HTTP endpoint (no API key).

This is a best-effort machine translation intended to make the site
production-ready quickly. It preserves:
- YAML frontmatter keys (translating only title/description values)
- fenced code blocks
- inline code spans
- markdown link/image URLs
"""

from __future__ import annotations

import argparse
import json
import os
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "docs" / "en"
TARGETS = {
    "es": ROOT / "docs" / "es",
    "pt": ROOT / "docs" / "pt",
    "pt-BR": ROOT / "docs" / "pt-BR",
}


_INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
_MD_LINK_URL_RE = re.compile(r"(\]\()([^)]+)(\))")
_MD_IMAGE_URL_RE = re.compile(r"(\!\[[^\]]*\]\()([^)]+)(\))")
_HTML_TAG_RE = re.compile(r"<[^>\n]+>")
_ATTR_LIST_RE = re.compile(r"\{[^}\n]*\}")
_ICON_TOKEN_RE = re.compile(r":[A-Za-z0-9][A-Za-z0-9_-]*:")


@dataclass(frozen=True)
class ProtectResult:
    text: str
    placeholders: Dict[str, str]


def http_translate(text: str, target_lang: str, *, source_lang: str = "en") -> str:
    if not text.strip():
        return text

    # Public endpoint used by the web UI; keep requests small and polite.
    q = urllib.parse.quote(text, safe="")
    url = (
        "https://translate.googleapis.com/translate_a/single"
        f"?client=gtx&sl={urllib.parse.quote(source_lang)}"
        f"&tl={urllib.parse.quote(target_lang)}&dt=t&q={q}"
    )
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "omegaup-docs-translate/1.0 (+https://github.com/omegaup/omegaup)",
        },
        method="GET",
    )
    # Network to public endpoints can be flaky/rate-limited. Retry a few times,
    # and fall back to an unverified SSL context if the environment lacks CAs.
    last_err: Optional[BaseException] = None
    for attempt in range(4):
        timeouts = [30, 30, 45, 60]
        timeout = timeouts[min(attempt, len(timeouts) - 1)]

        # Determine whether to skip verified context.
        contexts: List[Optional[ssl.SSLContext]] = [None]
        if attempt > 0:
            contexts.append(ssl._create_unverified_context())  # noqa: SLF001

        for ctx in contexts:
            try:
                if ctx is None:
                    with urllib.request.urlopen(req, timeout=timeout) as resp:
                        raw = resp.read().decode("utf-8")
                else:
                    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
                        raw = resp.read().decode("utf-8")
                last_err = None
                break
            except urllib.error.URLError as e:
                last_err = e
                # If cert verification fails, retry immediately with unverified.
                if isinstance(getattr(e, "reason", None), ssl.SSLCertVerificationError):
                    try:
                        uctx = ssl._create_unverified_context()  # noqa: SLF001
                        with urllib.request.urlopen(req, timeout=timeout, context=uctx) as resp:
                            raw = resp.read().decode("utf-8")
                        last_err = None
                        break
                    except Exception as e2:  # noqa: BLE001
                        last_err = e2
                continue
            except Exception as e:  # noqa: BLE001
                last_err = e
                continue

        if last_err is None:
            break
        # Backoff
        time.sleep(0.5 * (attempt + 1))
    if last_err is not None:
        raise last_err
    data = json.loads(raw)
    # data[0] is list of [translated, original, ...]
    return "".join(part[0] for part in data[0] if part and part[0])


def split_frontmatter(content: str) -> Tuple[Optional[str], str]:
    if not content.startswith("---\n"):
        return None, content
    # Find second --- on its own line
    idx = content.find("\n---\n", 4)
    if idx == -1:
        return None, content
    fm = content[: idx + len("\n---\n")]
    body = content[idx + len("\n---\n") :]
    return fm, body


def translate_frontmatter(frontmatter: str, target_lang: str, cache: Dict[Tuple[str, str], str]) -> str:
    # Translate only title/description values, keep keys and formatting stable.
    lines = frontmatter.splitlines(keepends=True)
    out: List[str] = []
    kv_re = re.compile(r"^(title|description):\s*(.*)\s*$")
    for line in lines:
        m = kv_re.match(line.rstrip("\n"))
        if not m:
            out.append(line)
            continue
        key, value = m.group(1), m.group(2)
        # Strip wrapping quotes but re-emit same quoting if present
        quote = ""
        raw_value = value
        if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
            quote = value[0]
            raw_value = value[1:-1]
        translated = translate_chunk(raw_value, target_lang, cache)
        if quote:
            out.append(f"{key}: {quote}{translated}{quote}\n")
        else:
            out.append(f"{key}: {translated}\n")
    return "".join(out)


def protect(text: str, patterns: List[re.Pattern], prefix: str) -> ProtectResult:
    placeholders: Dict[str, str] = {}
    counter = 0

    def repl(m: re.Match) -> str:
        nonlocal counter
        # Use a placeholder token that is very unlikely to be altered by MT.
        # Avoid underscores and punctuation that may be stripped/translated.
        key = f"ZX{prefix}{counter}ZX"
        placeholders[key] = m.group(0)
        counter += 1
        return key

    for pat in patterns:
        text = pat.sub(repl, text)
    return ProtectResult(text=text, placeholders=placeholders)


def protect_markdown(text: str) -> ProtectResult:
    # Preserve HTML tags, attribute lists, inline code and URLs.
    #
    # This is critical for Zensical/MkDocs Markdown extensions:
    # - `<div class="grid cards" markdown>` must not be translated
    # - `{ width="300" style="..." }` must not be translated (attr_list)
    res = protect(text, [_HTML_TAG_RE, _ATTR_LIST_RE, _ICON_TOKEN_RE, _INLINE_CODE_RE], "PROT")
    text = res.text
    placeholders = dict(res.placeholders)

    # Protect image URLs first, then normal link URLs.
    def protect_grouped(pat: re.Pattern, pfx: str, current_text: str) -> Tuple[str, Dict[str, str]]:
        ph: Dict[str, str] = {}
        counter = 0

        def repl(m: re.Match) -> str:
            nonlocal counter
            key = f"ZX{pfx}{counter}ZX"
            ph[key] = m.group(2)
            counter += 1
            return f"{m.group(1)}{key}{m.group(3)}"

        return pat.sub(repl, current_text), ph

    text, img_ph = protect_grouped(_MD_IMAGE_URL_RE, "IMGURL", text)
    placeholders.update(img_ph)
    text, link_ph = protect_grouped(_MD_LINK_URL_RE, "LINKURL", text)
    placeholders.update(link_ph)

    return ProtectResult(text=text, placeholders=placeholders)


def restore(text: str, placeholders: Dict[str, str]) -> str:
    # Placeholders can be nested (e.g. `{...}` inside an inline code span that is
    # also protected). Do iterative replacement until convergence.
    keys = sorted(placeholders.keys(), key=len, reverse=True)
    for _ in range(6):
        changed = False
        for key in keys:
            value = placeholders[key]
            for variant in (key, key.lower(), key.upper()):
                if variant in text:
                    text = text.replace(variant, value)
                    changed = True
        if not changed:
            break
    return text


def chunk_text(text: str, max_chars: int) -> Iterable[str]:
    # Chunk by paragraphs to keep structure, but enforce size limit.
    parts = re.split(r"(\n\s*\n)", text)
    buf = ""
    for part in parts:
        if not part:
            continue
        if len(buf) + len(part) <= max_chars:
            buf += part
            continue
        if buf:
            yield buf
            buf = ""
        # If still too large (single huge paragraph), hard split.
        if len(part) <= max_chars:
            buf = part
        else:
            for i in range(0, len(part), max_chars):
                yield part[i : i + max_chars]
    if buf:
        yield buf


def translate_chunk(text: str, target_lang: str, cache: Dict[Tuple[str, str], str]) -> str:
    key = (target_lang, text)
    if key in cache:
        return cache[key]
    translated = http_translate(text, target_lang)
    cache[key] = translated
    time.sleep(0.05)  # be polite
    return translated


def translate_markdown_body(body: str, target_lang: str, cache: Dict[Tuple[str, str], str]) -> str:
    # Preserve fenced code blocks. Translate only outside.
    lines = body.splitlines(keepends=True)
    out: List[str] = []
    buf: List[str] = []
    in_fence = False
    fence_pat = re.compile(r"^\s*```")

    def flush_buf() -> None:
        if not buf:
            return
        text = "".join(buf)
        # Preserve trailing newlines exactly to avoid headings gluing to fences.
        m = re.search(r"\n*\Z", text)
        trailing = m.group(0) if m else ""
        core = text[: len(text) - len(trailing)] if trailing else text

        protected = protect_markdown(core)
        translated_chunks: List[str] = []
        # Larger chunks reduce request count significantly.
        for chunk in chunk_text(protected.text, max_chars=9000):
            translated_chunks.append(translate_chunk(chunk, target_lang, cache))
        translated = "".join(translated_chunks)
        restored = restore(translated, protected.placeholders)
        out.append(restored + trailing)
        buf.clear()

    for line in lines:
        if fence_pat.match(line):
            if not in_fence:
                flush_buf()
                in_fence = True
                out.append(line)
            else:
                in_fence = False
                out.append(line)
            continue
        if in_fence:
            out.append(line)
        else:
            buf.append(line)
    flush_buf()
    return "".join(out)


def translate_file(src_path: Path, dst_path: Path, target_lang: str, cache: Dict[Tuple[str, str], str]) -> None:
    content = src_path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(content)
    if fm is not None:
        fm = translate_frontmatter(fm, target_lang, cache)
    translated_body = translate_markdown_body(body, target_lang, cache)
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    dst_path.write_text((fm or "") + translated_body, encoding="utf-8")


def iter_md_files(root: Path) -> List[Path]:
    return sorted([p for p in root.rglob("*.md") if p.is_file()])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--langs", default="es,pt,pt-BR", help="comma-separated target langs")
    ap.add_argument("--only", default="", help="translate only paths containing this substring (debug)")
    ap.add_argument("--start", type=int, default=0, help="start index in sorted file list")
    ap.add_argument("--limit", type=int, default=0, help="max files to translate (0 = no limit)")
    args = ap.parse_args()

    langs = [x.strip() for x in args.langs.split(",") if x.strip()]
    for l in langs:
        if l not in TARGETS:
            raise SystemExit(f"Unsupported lang: {l}")

    src_files = iter_md_files(SRC)
    if args.only:
        src_files = [p for p in src_files if args.only in str(p)]
    if args.start < 0:
        raise SystemExit("--start must be >= 0")
    if args.limit < 0:
        raise SystemExit("--limit must be >= 0")
    if args.start:
        src_files = src_files[args.start :]
    if args.limit:
        src_files = src_files[: args.limit]

    cache: Dict[Tuple[str, str], str] = {}
    total = len(src_files) * len(langs)
    done = 0
    for lang in langs:
        dst_root = TARGETS[lang]
        for src in src_files:
            rel = src.relative_to(SRC)
            dst = dst_root / rel
            translate_file(src, dst, lang, cache)
            done += 1
            if done % 10 == 0 or done == total:
                print(f"[{done}/{total}] translated {lang}:{rel}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit(130)
