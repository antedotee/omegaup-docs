---
title: Glossário
description: Terminologia e definições usadas no omegaUp
icon: bootstrap/book
---
# Glossário

Referência abrangente de termos e definições usados em toda a documentação do omegaUp e na plataforma.

---

## Termos Gerais

### omegaUp
A plataforma de programação educacional que ajuda os alunos a melhorar suas habilidades de programação por meio de problemas práticos, concursos e cursos.

### Problema
Um desafio de programação que consiste em uma declaração de problema, especificações de entrada/saída, restrições e casos de teste. Os problemas são a unidade principal do conteúdo do omegaUp.

### Concurso
Uma competição de programação cronometrada onde os participantes resolvem um conjunto de problemas. Os concursos têm horários de início/término definidos, regras de pontuação e podem incluir recursos como participação virtual.

### Curso
Um caminho de aprendizagem estruturado contendo tarefas com problemas, organizados por tópicos. Os cursos incluem acompanhamento do progresso e prazos.

### Envio (Executar)
Código enviado por um usuário para resolver um problema. Cada envio é compilado, executado em casos de teste e recebe um veredicto.

###Arena
A interface do concurso onde os participantes resolvem problemas durante as competições. Fornece placar em tempo real, editor de código e sistema de envio.

---

## Funções do usuário

### Concorrente/Participante
Um usuário participando de um concurso ou praticando problemas.

### Criador de problemas
Um usuário que cria problemas para omegaUp. Os criadores de problemas definem declarações, casos de teste e validadores.

### Organizador do Concurso
Um usuário que cria e gerencia concursos. Pode adicionar problemas, gerenciar participantes e definir configurações de concurso.

### Administrador do curso
Um usuário que gerencia cursos, atribui problemas, acompanha o progresso dos alunos e analisa os envios.

### Assistente de Ensino (TA)
Um ajudante de curso que pode fornecer revisões de código e responder aos esclarecimentos dos alunos.

### Administrador do Sistema (Administrador de Sistemas)
Um usuário com acesso administrativo total à plataforma omegaUp.

---

## Termos Técnicos

### Graduador
O microsserviço Go que gerencia a fila de envio e coordena a avaliação. O Grader recebe envios do frontend, atribui-os aos Runners e armazena os resultados.

### Corredor
Uma instância de serviço que compila e executa código enviado pelo usuário em uma sandbox segura. Vários Runners podem operar em paralelo para lidar com a carga de envio.

### Minijail
A sandbox do Linux usada para execução segura de código, derivada do Chrome OS. Fornece isolamento de processos, filtragem de syscall e limites de recursos.

###GitServer
O serviço que gerencia repositórios de problemas usando Git. Fornece controle de versão, gerenciamento de filiais e fornecimento de conteúdo para problemas.

### Emissora
O servidor WebSocket que fornece atualizações em tempo real aos clientes, incluindo alterações no placar, notificações de veredicto e esclarecimentos.

### DAO (objeto de acesso a dados)
Classes PHP que lidam com interações de banco de dados. DAOs fornecem métodos para operações CRUD em tabelas de banco de dados.

### VO (objeto de valor)
Classes PHP que mapeiam para tabelas de banco de dados. VOs representam registros individuais do banco de dados com propriedades digitadas.

### MVC (Model-View-Controller)
O padrão de arquitetura usado no aplicativo PHP do omegaUp. Os controladores lidam com a lógica de negócios, os DAOs/VOs lidam com os dados e os modelos lidam com a apresentação.

### Controlador
Classes PHP que implementam endpoints de API e lógica de negócios. Localizado em `frontend/server/src/Controllers/`.

---

## Veredictos

### AC (Aceito)
A solução produz resultados corretos para todos os casos de teste e passa dentro dos limites de recursos.

### PA (parcialmente aceito)
A solução passa em alguns casos de teste, mas não em todos. Usado com problemas de pontuação parcial.

### WA (resposta errada)
A solução produz saída incorreta para um ou mais casos de teste.

### TLE (Prazo excedido)
A solução excedeu o limite de tempo em um ou mais casos de teste.

### MLE (limite de memória excedido)
A solução excedeu o limite de memória durante a execução.

### RTE (erro de tempo de execução)
A solução travou durante a execução (por exemplo, falha de segmentação, divisão por zero, estouro de pilha).

### CE (erro de compilação)
O código falhou ao compilar. Causas comuns: erros de sintaxe, inclusões ausentes, incompatibilidades de tipo.

### JE (erro do juiz)
Ocorreu um erro interno durante a avaliação. Normalmente indica um problema com os dados de teste ou com o validador.

### OLE (limite de saída excedido)
A solução produziu muita saída, excedendo o limite permitido.

---

## Pontuação do concurso

### Estilo IOI
Modelo de pontuação onde cada caso de teste atribui pontos parciais. A pontuação final é a soma dos pontos de todos os casos de teste.

### Estilo ICPC
Modelo de pontuação onde os problemas valem pontos iguais (normalmente 1). O tempo de penalidade é adicionado para envios errados.

### Penalidade
Dedução baseada no tempo ou no envio em concursos do tipo ICPC. Normalmente 20 minutos por envio errado.

### Congelamento do placar
Período antes do final da competição, quando o placar deixa de ser atualizado publicamente, criando suspense para os resultados finais.

### Concurso Virtual
Simulando uma competição passada sob condições de tempo originais. Permite praticar com concursos históricos.

---

## Componentes do problema

### Declaração
A descrição do problema incluindo a tarefa, formato de entrada/saída, restrições e exemplos.

### Caso de teste
Um par de dados de entrada e resultados esperados usados para avaliar os envios.

### Grupo de teste
Uma coleção de casos de teste relacionados, geralmente com pontos compartilhados. Usado para pontuação de subtarefas.

### Validador
Um programa que verifica a saída da solução, especialmente para problemas com múltiplas respostas válidas.

### Problema interativo
Um problema onde a solução deve interagir com um programa juiz através de E/S padrão.

### Gerador
Um programa que cria casos de teste, normalmente para entradas grandes ou aleatórias.

### Subtarefa
Um subconjunto de casos de teste com restrições específicas, permitindo crédito parcial para soluções mais simples.

---

## Configurações de problemas

### Prazo
Tempo máximo de execução permitido por caso de teste, em segundos (por exemplo, 1,0s, 2,0s).

### Limite de memória
Memória máxima que a solução pode usar, em bytes ou megabytes (por exemplo, 256 MB).

### Limite de saída
Tamanho máximo de saída da solução, evita impressão infinita.

### Tipo de validador
Como a saída é comparada: `token-caseless`, `token-numeric`, `literal` ou `custom`.

### Visibilidade do problema
Nível de acesso: `private` (somente proprietário), `public` (qualquer pessoa) ou específico do concurso.

---

## Termos da API

### Ponto final
Um URL de API específico que lida com uma operação específica (por exemplo, `/api/Problem/create/`).

### Parâmetro de solicitação
Dados enviados para um endpoint de API, na string de consulta do URL ou no corpo da solicitação.

### Resposta
Dados JSON retornados por um endpoint de API, incluindo status e dados solicitados.

### Token de autenticação
O cookie `ouat` que identifica e autentica usuários para solicitações de API.

### Limitação de taxa
Restrição na frequência de chamadas de API para evitar abusos. Os limites variam de acordo com o endpoint.

---

## Termos de infraestrutura

### Redis
Armazenamento de dados na memória usado para armazenamento de sessão, cache e mensagens em tempo real.

### CoelhoMQ
Fila de mensagens usada para processamento de tarefas assíncronas, como geração de certificados.

### PHP-FPM
PHP FastCGI Process Manager que lida com o processamento de solicitações PHP.

###Nginx
Servidor Web e proxy reverso que roteia solicitações para serviços de back-end apropriados.

### Docker
Plataforma de conteinerização usada para ambientes de desenvolvimento e implantação.

---

## Termos de Desenvolvimento

### PR (solicitação pull)
Uma proposta de alteração de código enviada para revisão antes de ser mesclada na base de código principal.

### CI (Integração Contínua)
Testes automatizados executados em cada alteração de código para garantir a qualidade.

### Linter
Ferramenta que verifica o código em busca de estilo e possíveis erros (por exemplo, ESLint, Psalm).

### Migração
Script de alteração do esquema do banco de dados que atualiza a estrutura do banco de dados.

### Calendário
Dados de teste usados para configurar um estado conhecido para teste.

---

## Abreviações

| Abreviatura | Prazo completo |
|--------------|-----------|
| API | Interface de programação de aplicativos |
| CRUD | Criar, ler, atualizar, excluir |
| CSRF | Falsificação de solicitação entre sites |
| DAO | Objeto de acesso a dados |
| GSoC | Verão de código do Google |
| ICPC | Concurso Internacional de Programação Universitária |
| IOI | Olimpíada Internacional de Informática |
| JSON | Notação de objeto JavaScript |
| JWT | Token Web JSON |
| MVC | Controlador de visualização de modelo |
| REST | Transferência de Estado Representacional |
| SQL | Linguagem de consulta estruturada |
| TLS | Segurança da Camada de Transporte |
| VO | Objeto de valor |
| WS | WebSocket |
| XSS | Scripting entre sites |

---

## Documentação Relacionada

- **[Visão geral da arquitetura](../architecture/index.md)** - Arquitetura do sistema
- **[Referência da API](../api/index.md)** - Documentação da API
- **[Veredictos](../features/verdicts.md)** - Informações detalhadas do veredicto
- **[Guias de desenvolvimento](../development/index.md)** - Recursos para desenvolvedores
