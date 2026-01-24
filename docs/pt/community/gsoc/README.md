# Sistema de conteúdo dinâmico GSoC

Este diretório usa uma abordagem baseada em dados para gerar páginas GSoC, eliminando a necessidade de copiar e colar conteúdo entre anos.

## Como funciona

1. **Arquivo de dados**: todo o conteúdo específico do ano é armazenado em `_data/gsoc-data.json`
2. **Generator Script**: `scripts/generate-gsoc-pages.py` lê os dados e gera arquivos markdown
3. **Páginas Geradas**: O script cria arquivos `YYYY.md` para cada ano

## Adicionando um Ano Novo

### Para o ano atual (com ideias de projetos):

1. Abra `_data/gsoc-data.json`
2. Adicione uma nova entrada em `years` com o ano como chave:
   ```json
   "2026": {
     "type": "current",
     "title": "GSoC 2026",
     "description": "Google Summer of Code 2026 program at omegaUp",
     "intro": "Your introduction text here...",
     "project_ideas": [...],
     "application_process": {...},
     "communications": [...],
     "faq": [...],
     "related_docs": [...]
   }
   ```
3. Atualize o `type` do ano anterior para `"past"` e adicione a matriz `projects` em vez de `project_ideas`
4. Execute o gerador:
   ```bash
   python3 scripts/generate-gsoc-pages.py
   ```
5. Revise os arquivos gerados e envie-os

### Para o ano passado (projetos concluídos):

1. Abra `_data/gsoc-data.json`
2. Adicione uma nova entrada em `years`:
   ```json
   "2025": {
     "type": "past",
     "title": "GSoC 2025",
     "description": "Google Summer of Code 2025 projects",
     "intro": "Projects completed during GSoC 2025.",
     "projects": [
       {
         "name": "Project Name",
         "description": "Project description",
         "result": "Project result/outcome"
       }
     ],
     "related_docs": [...]
   }
   ```
3. Execute o script gerador
4. Revise e comprometa-se

## Atualizando conteúdo existente

Simplesmente edite `_data/gsoc-data.json` e execute o script gerador. Todas as páginas serão regeneradas com o conteúdo atualizado.

## Benefícios

- **Sem erros de copiar e colar**: fonte única de verdade para conteúdo compartilhado
- **Consistência**: todas as páginas seguem a mesma estrutura
- **Atualizações fáceis**: atualize o arquivo de dados uma vez, gere novamente todas as páginas
- **Controle de versão**: arquivo de dados mostra exatamente o que mudou entre os anos

## Estrutura do arquivo

```
gsoc/
├── _data/
│   └── gsoc-data.json      # Single source of truth
├── _templates/             # (Legacy - not used anymore)
├── 2023.md                 # Generated file
├── 2024.md                 # Generated file
├── 2025.md                 # Generated file
├── index.md                # Manual file (not generated)
└── README.md               # This file
```
## Notas

- O script gerador usa apenas a biblioteca padrão Python (sem dependências externas)
- Os arquivos gerados devem ser confirmados no git
- O arquivo de dados (`gsoc-data.json`) é a fonte da verdade - edite-o, não os arquivos markdown gerados
- Sempre execute o gerador após atualizar o arquivo de dados
