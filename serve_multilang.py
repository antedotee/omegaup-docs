#!/usr/bin/env python3
"""
Multi-language development server for omegaUp documentation.

This server properly serves all language versions from the site/ directory,
allowing language switching to work correctly during local development.
"""

import http.server
import socketserver
import os
import sys
from pathlib import Path

# Change to the site directory
ROOT = Path(__file__).parent
SITE_DIR = ROOT / "site"

if not SITE_DIR.exists():
    print(f"Error: {SITE_DIR} does not exist.")
    print("Please build the site first using: zensical build")
    sys.exit(1)

os.chdir(SITE_DIR)

PORT = 8000

class MultiLangHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler that redirects root to /en/"""
    
    def do_GET(self):
        # Redirect root to /en/
        if self.path == "/" or self.path == "":
            self.send_response(302)
            self.send_header("Location", "/en/")
            self.end_headers()
            return
        
        return super().do_GET()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), MultiLangHTTPRequestHandler) as httpd:
        print(f"🌍 Multi-language documentation server running at http://localhost:{PORT}/")
        print(f"📂 Serving from: {SITE_DIR}")
        print(f"\n Available languages:")
        print(f"   • English:              http://localhost:{PORT}/en/")
        print(f"   • Español:              http://localhost:{PORT}/es/")
        print(f"   • Português:            http://localhost:{PORT}/pt/")
        print(f"   • Português (Brasil):   http://localhost:{PORT}/pt-BR/")
        print(f"\nPress Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Server stopped")
            sys.exit(0)
