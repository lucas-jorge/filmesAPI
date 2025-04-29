# API de Filmes (CRUD)

Este projeto implementa uma API simples para gerenciamento de filmes (CRUD - Create, Read, Update, Delete) utilizando Django e Django Rest Framework. A persistência dos dados é feita em um banco de dados SQLite, e a aplicação é conteinerizada com Docker e Docker Compose.

## Tecnologias Utilizadas

*   **Python:** Linguagem de programação.
*   **Django:** Framework web para desenvolvimento rápido.
*   **Django Rest Framework (DRF):** Toolkit flexível para construir APIs web com Django.
*   **SQLite:** Banco de dados leve e embarcado (para este exemplo).
*   **Docker:** Plataforma para desenvolver, enviar e executar aplicações em contêineres.
*   **Docker Compose:** Ferramenta para definir e executar aplicações Docker multi-container.

## Pré-requisitos

Para executar este projeto, você precisa ter o Docker e o Docker Compose instalados em sua máquina. Você pode baixar o Docker Desktop (que inclui o Docker Compose) no site oficial do Docker.

## Configuração e Execução

1.  **Clone o repositório:**
    ```bash
    # Se o projeto ainda não estiver na sua máquina
    # git clone <url_do_seu_repositorio>
    # cd filmesAPI
    ```

2.  **Construa e execute os contêineres com Docker Compose:**
    Abra um terminal na pasta raiz do projeto (`filmesAPI/`) e execute o seguinte comando:

    ```bash
    docker-compose up --build
    ```

    Este comando irá:
    *   Construir a imagem Docker da aplicação (baseada no `Dockerfile`).
    *   Criar e iniciar o contêiner da aplicação web.
    *   Aplicar as migrações do banco de dados automaticamente (se houver novas migrações).
    *   O servidor da API estará rodando em `http://localhost:8000/`.

## Endpoints da API

A API estará disponível em `http://localhost:8000/api/`. Os seguintes endpoints estão disponíveis:

*   **`GET /api/filmes/`**: Retorna uma lista com todos os filmes cadastrados.
*   **`POST /api/filmes/`**: Cadastra um novo filme.
    *   Envie os dados do filme no corpo da requisição no formato JSON (ex: `{"title": "Nome do Filme", "year": 2023, "genre": "Ação"}`).
*   **`GET /api/filmes/{id}/`**: Retorna os detalhes de um filme específico com base no seu ID.

## Exemplo de Uso (com `curl`)

Você pode usar ferramentas como `curl` ou clientes HTTP (como Postman ou a extensão Thunder Client no VS Code) para interagir com a API.

**Cadastrar um novo filme (POST):**

```bash
curl -X POST http://localhost:8000/api/filmes/ -H "Content-Type: application/json" -d '{"title": "Meu Novo Filme", "year": 2024, "genre": "Drama"}'
```

**Listar todos os filmes (GET):**

```bash
curl http://localhost:8000/api/filmes/
```

**Obter detalhes de um filme por ID (GET):**

```bash
# Substitua 1 pelo ID do filme que você deseja buscar
curl http://localhost:8000/api/filmes/1/
```
