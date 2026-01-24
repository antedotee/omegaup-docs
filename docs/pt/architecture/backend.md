---
title: Arquitetura de back-end
description: Controladores PHP, padrões DAO/VO e estrutura API
icon: bootstrap/server
---
# Arquitetura de back-end

O backend do omegaUp é construído em PHP seguindo o padrão MVC, com uma separação clara entre controladores, acesso a dados e lógica de negócios.

## Estrutura de diretório

```
frontend/server/src/
├── Controllers/           # API controllers
├── DAO/                  # Data Access Objects
│   ├── VO/               # Value Objects
│   └── Base/             # Base DAO classes
└── libs/                 # Libraries and utilities
```
## Controladores

Os controladores lidam com solicitações HTTP e implementam lógica de negócios:

- Localizado em `frontend/server/src/Controllers/`
- Um controlador por recurso API (por exemplo, `RunController`, `ContestController`)
- Os métodos correspondem aos endpoints da API (por exemplo, `apiCreate`, `apiDetails`)

## Padrão DAO/VO

### Objetos de valor (VO)
- Mapeie diretamente para tabelas de banco de dados
- Gerado automaticamente a partir do esquema
- Localizado em `frontend/server/src/DAO/VO/`

### Objetos de acesso a dados (DAO)
- Classes estáticas para operações de banco de dados
- Métodos: `search()`, `getByPK()`, `save()`, `delete()`
- Localizado em `frontend/server/src/DAO/`

### Exemplo de uso

```php
// Create a VO
$user = new Users();
$user->setEmail('user@example.com');

// Search using DAO
$results = UsersDAO::search($user);

// Access results
if (count($results) > 0) {
    $foundUser = $results[0];
    echo $foundUser->getUserId();
}
```
## Documentação Relacionada

- **[Padrões de banco de dados](../development/database-patterns.md)** - Guia detalhado de DAO/VO
- **[Padrão MVC](mvc-pattern.md)** - Implementação MVC
- **[Referência de API](../api/index.md)** - Terminais de API
