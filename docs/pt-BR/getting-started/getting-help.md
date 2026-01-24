---
title: Obtendo ajuda
description: Aprenda como fazer perguntas de maneira eficaz e obter ajuda da comunidade omegaUp
icon: bootstrap/help-circle
---
# Obtendo ajuda

Sabemos que você terá dúvidas sobre como as coisas funcionam na omegaUp – questões técnicas, questões de processo e muito mais. Este guia o ajudará a obter respostas melhores com mais rapidez.

## Antes de perguntar

### 1. Pesquise recursos existentes

Antes de postar uma pergunta, pesquise estes recursos:

#### Documentação
- **Este site de documentação** - Pesquise seu tópico
- **[Guia de configuração de desenvolvimento](development-setup.md)** - Problemas de instalação e configuração
- **[Documentação de arquitetura](../architecture/index.md)** - Perguntas sobre design do sistema

#### Recursos da comunidade
- **Pesquisa no Discord** - Pesquise o histórico de mensagens em nosso [#dev_training channel](https://discord.com/invite/K3JFd9d3wk)
  - O Discord tem um recurso de pesquisa poderoso – muitas perguntas já foram feitas antes
  - Pesquise por palavras-chave relacionadas à sua pergunta

#### Recursos Externos
- **Google** – Para dúvidas gerais sobre Git, Docker, PHP, JavaScript, etc.
  - Se sua pergunta não for específica do omegaUp, o Google provavelmente terá a resposta

!!! dica "Dicas de pesquisa"
    Experimente diferentes combinações de palavras-chave. Freqüentemente, alguém já fez uma pergunta semelhante antes.

## Fazendo perguntas de maneira eficaz

### Onde perguntar

Poste sua pergunta no canal **#dev_training** do nosso [servidor Discord](https://discord.com/invite/K3JFd9d3wk).

!!! importante "Somente canais públicos"
    - ✅ Postar em canais públicos (não DMs)
    - ✅ Marque o canal apropriado
    - ❌ Não envie mensagens diretas
    - ❌ Não marque pessoas específicas desnecessariamente

### Como perguntar

Siga estas diretrizes para obter melhores respostas:

#### 1. Forneça contexto

Explique o que você está tentando fazer:

```markdown
I'm trying to set up my development environment on macOS, and I'm getting
an error when running `docker compose up`.
```
#### 2. Descreva o problema

Incluir:
- **O que você esperava que acontecesse**
- **O que realmente aconteceu**
- **Etapas que você seguiu**
- **Mensagens de erro** (copie e cole o erro completo)
- **Trechos de código relevantes** (se aplicável)
- **Registros** (se aplicável)

#### 3. Mostre o que você tentou

Mencione o que você já tentou:

```markdown
I've already tried:
- Reinstalling Docker
- Checking the documentation
- Searching Discord history for similar issues
```
#### 4. Incluir informações do sistema

Se relevante, inclua:
- Sistema operacional e versão
- Versão Docker
- Versão Node.js (se aplicável)
- Quaisquer outros detalhes ambientais relevantes

### Exemplo de boa pergunta

```markdown
Hi! I'm setting up the development environment on Ubuntu 22.04 and getting
an error when running `docker compose up`.

**Expected:** Containers should start successfully
**Actual:** Getting "port already in use" error

**Steps I followed:**
1. Installed Docker and Docker Compose
2. Cloned the repository
3. Ran `docker compose up`

**Error message:**
```
ERRO: para frontend Não é possível iniciar o frontend de serviço: 
driver falhou ao programar conectividade externa no endpoint 
omegaup-frontend-1: Falha na ligação para 0.0.0.0:8001: a porta já está alocada
```

**What I've tried:**
- Checked if port 8001 is in use: `lsof -i :8001`
- Found process using the port and killed it
- Still getting the same error

Any help would be appreciated!
```
### Exemplo de pergunta ruim

```markdown
docker not working help pls
```
!!! fracasso "Por que isso é ruim"
    - Nenhum contexto sobre o que significa "não funcionar"
    - Nenhuma mensagem de erro
    - Nenhuma informação do sistema
    - Nenhuma indicação do que foi tentado

## Acompanhamento

### Se sua pergunta for respondida

1. **Agradeça à pessoa** que ajudou você
2. **Confirme se a solução funcionou**
3. **Atualize o tópico** com o que o corrigiu (se for diferente da solução sugerida)

Isso ajuda futuras pessoas com o mesmo problema!

### Se você resolver sozinho

Se você descobrir a solução:

1. **Atualize o tópico** explicando como você resolveu o problema
2. **Marque como resolvido** (se a plataforma suportar)

Isso evita que outras pessoas percam tempo tentando ajudar depois de você já ter resolvido o problema.

### Se sua pergunta foi feita antes

Se você encontrar um tópico existente com sua pergunta:

- **Responda a esse tópico** em vez de criar um novo
- **Adicione novas informações** se sua situação for diferente
- **Faça perguntas de acompanhamento** no mesmo tópico

Isso mantém as informações relacionadas juntas e torna mais fácil encontrá-las.

## Ajudando os outros

Incentivamos você a **ajudar seus colegas** com suas dúvidas!

### Por que ajudar os outros?

- **Aprendizado**: explicar conceitos ajuda você a entendê-los melhor
- **Comunidade**: Construindo uma comunidade útil e inclusiva
- **Reconhecimento**: Levamos em consideração a utilidade ao selecionar candidatos ao GSoC

### Como ajudar

- **Leia as perguntas** postadas por outras pessoas regularmente
- **Responda a perguntas** que você conhece
- **Compartilhe recursos** que possam ajudar
- **Seja paciente e gentil** - todos estão aprendendo

## O que evitar

### ❌ Não faça essas coisas

1. **Não envie DMs** - Publique em canais públicos para que outras pessoas possam se beneficiar
2. **Não marque pessoas específicas** - Poste publicamente para que qualquer pessoa possa ajudar
3. **Não reposte perguntas** - Pesquise primeiro, responda aos tópicos existentes
4. **Não faça a mesma pergunta várias vezes** - Seja paciente nas respostas

### ✅ Faça essas coisas

1. **Pesquise primeiro** - Verifique a documentação e o histórico do Discord
2. **Publicar publicamente** - Use os canais apropriados
3. **Seja específico** – Forneça contexto, erros e o que você tentou
4. **Acompanhamento** - Atualize os tópicos quando os problemas forem resolvidos
5. **Ajude os outros** - Responda a perguntas para as quais você sabe a resposta

## Recursos Adicionais

### Aprendendo a fazer perguntas melhores

Recomendamos a leitura:
- **[Como fazer perguntas de maneira inteligente](https://www.mikeash.com/getting_answers.html)** - Excelente guia sobre como fazer perguntas eficazes

### Recursos específicos do omegaUp

- **[Configuração de desenvolvimento](development-setup.md)** - Problemas de configuração do ambiente
- **[Guia de contribuição](contributing.md)** - Perguntas de relações públicas e fluxo de trabalho
- **[Documentação de arquitetura](../architecture/index.md)** - Perguntas sobre design do sistema
- **[Documentação da API](../api/index.md)** - Perguntas relacionadas à API

### Canais da comunidade

- **Discord**: [#dev_training channel](https://discord.com/invite/K3JFd9d3wk) - Principal canal de suporte
- **Problemas do GitHub**: [Relatar bugs](https://github.com/omegaup/omegaup/issues) - Para bugs confirmados
- **Discussões no GitHub**: [Discussões gerais](https://github.com/omegaup/omegaup/discussions) - Para ideias de recursos e discussões

## Resumo

1. ✅ **Pesquise primeiro** - Documentação, histórico do Discord, Google
2. ✅ **Pergunte publicamente** - Use canais apropriados, não DMs
3. ✅ **Seja específico** - Forneça contexto, erros, etapas e informações do sistema
4. ✅ **Acompanhamento** - Atualize os tópicos quando resolvidos
5. ✅ **Ajude outras pessoas** - Responda perguntas nas quais você pode ajudar

---

**Ainda precisa de ajuda?** Junte-se ao nosso [servidor Discord](https://discord.com/invite/K3JFd9d3wk) e pergunte no canal #dev_training!
