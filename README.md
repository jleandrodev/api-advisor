# Casamento Manager API

A Casamento Manager API é uma aplicação de gerenciamento de casamentos que permite cadastrar casamentos, convidados, assistentes e usuários.

## Configuração e Instalação

1.  **Clone o Repositório:**

    ```bash

    `git clone https://seurepositorio.com/api-advisor.git`

    ```

2.  **Instale as Dependências:**

    ```bash

    `cd api-advisor
    pip install -r requirements.txt`

    ```

3.  **Configuração do Banco de Dados:**

    - Configure as variáveis no arquivo `config.py` para conectar ao seu banco de dados.

4.  **Aplicar Migrações do Banco de Dados:**

    ```bash

    `flask db upgrade`

    ```

5.  **Executar a Aplicação:**

    ```bash

    `flask run`

    ```

A aplicação estará disponível em [http://localhost:5000](http://localhost:5000/).

## Endpoints da API

A API fornece os seguintes endpoints:

- `/usuarios`: Operações relacionadas a usuários.
- `/convidados`: Operações relacionadas a convidados.
- `/casamentos`: Operações relacionadas a casamentos.
- `/assistentes`: Operações relacionadas a assistentes.

## Documentação da API

A documentação da API, gerada automaticamente com Swagger, está disponível em [http://localhost:5000/apidocs](http://localhost:5000/apidocs).

## Recursos Adicionais

- **Flask-RESTful:** Framework para construção de APIs RESTful em Flask.
- **Flask-SQLAlchemy:** Extensão Flask para interagir com bancos de dados SQL usando SQLAlchemy.
- **Flask-Migrate:** Extensão Flask para gerenciamento de migrações de banco de dados.
- **Flask-Marshmallow:** Integração Flask para a biblioteca de serialização/desserialização Marshmallow.
- **Flask-JWT-Extended:** Extensão Flask para autenticação JWT.

## Endpoints Específicos

### Usuários

#### Cadastrar Novo Usuário

- **Endpoint:** `/usuarios`
- **Método:** `POST`
- **Parâmetros do Corpo:**
  - `nome` (string): Nome do usuário.
  - `email` (string): E-mail do usuário.
  - `senha` (string): Senha do usuário.
- **Exemplo de Requisição:**

  ```bash

  `{
    "nome": "John Doe",
    "email": "john.doe@example.com",
    "senha": "senha123"
  }`

  ```

- **Exemplo de Resposta (Sucesso):**

  ```bash

  `{
    "mensagem": "Usuário cadastrado com sucesso!",
    "id_usuario": 123
  }`

  ```

- **Exemplo de Resposta (Erro):**

  ```bash

  `{
    "erro": "Ocorreu um erro ao cadastrar o usuário."
  }`

  ```

### Convidados

#### Listar Convidados

- **Endpoint:** `/convidados`
- **Método:** `GET`
- **Requer Autenticação JWT:** Sim
- **Exemplo de Resposta:**

  ```bash

  `[
    {
      "id": 1,
      "nome": "Convidado 1",
      "telefone": "123456789",
      "casamento": 1
    },
    {
      "id": 2,
      "nome": "Convidado 2",
      "telefone": "987654321",
      "casamento": 1
    }
  ]`

  ```

#### Cadastrar Novo Convidado

- **Endpoint:** `/convidados`
- **Método:** `POST`
- **Requer Autenticação JWT:** Sim
- **Parâmetros do Corpo:**
  - `nome` (string): Nome do convidado.
  - `telefone` (string): Número de telefone do convidado.
  - `casamento` (int): ID do casamento associado.
- **Exemplo de Requisição:**

  ```bash

  `{
    "nome": "Convidado Novo",
    "telefone": "555123456",
    "casamento": 1
  }`

  ```

- **Exemplo de Resposta (Sucesso):**

  ```bash

  `{
    "id": 3,
    "nome": "Convidado Novo",
    "telefone": "555123456",
    "casamento": 1
  }`

  ```

- **Exemplo de Resposta (Erro):**

  ```bash

  `{
    "erro": "Ocorreu um erro ao cadastrar o convidado."
  }`

  ```

#### Detalhes do Convidado

- **Endpoint:** `/convidados/<id>`
- **Método:** `GET`
- **Requer Autenticação JWT:** Sim
- **Exemplo de Resposta (Sucesso):**

  ```bash

  `{
    "id": 1,
    "nome": "Convidado 1",
    "telefone": "123456789",
    "casamento": 1
  }`

  ```

- **Exemplo de Resposta (Erro):**

  ```bash

  `{
    "erro": "Convidado não encontrado!"
  }`

  ```

### Casamentos

#### Listar Casamentos

- **Endpoint:** `/casamentos`
- **Método:** `GET`
- **Requer Autenticação JWT:** Sim
- **Exemplo de Resposta:**

  ```bash

  `[
    {
      "id": 1,
      "name": "Casamento 1",
      "data_casamento": "2023-05-25",
      "assistentes": ["1", "2"]
    },
    {
      "id": 2,
      "name": "Casamento 2",
      "data_casamento": "2023-06-15",
      "assistentes": ["3", "4"]
    }
  ]`

  ```

#### Cadastrar Novo Casamento

- **Endpoint:** `/casamentos`
- **Método:** `POST`
- **Requer Autenticação JWT:** Sim
- **Parâmetros do Corpo:**
  - `name` (string): Nome do casamento.
  - `data_casamento` (string): Data do casamento (formato YYYY-MM-DD).
  - `assistentes` (array): Lista de IDs dos assistentes associados ao casamento.
- **Exemplo de Requisição:**

  ```bash

  `{
    "name": "Novo Casamento",
    "data_casamento": "2023-07-10",
    "assistentes": ["5", "6"]
  }`

  ```

- **Exemplo de Resposta (Sucesso):**

  ```bash

  `{
    "id": 3,
    "name": "Novo Casamento",
    "data_casamento": "2023-07-10",
    "assistentes": ["5", "6"]
  }`

  ```

- **Exemplo de Resposta (Erro):**

  ```bash

  `{
    "erro": "Ocorreu um erro ao cadastrar o casamento."
  }`

  ```

#### Detalhes do Casamento

- **Endpoint:** `/casamentos/<id>`
- **Método:** `GET`
- **Requer Autenticação JWT:** Sim
- **Exemplo de Resposta (Sucesso):**

  ```bash

  `{
    "id": 1,
    "name": "Casamento 1",
    "data_casamento": "2023-05-25",
    "assistentes": ["1", "2"]
  }`

  ```

- **Exemplo de Resposta (Erro):**

  ```bash

  `{
    "erro": "Casamento não encontrado!"
  }`

  ```

### Assistentes

#### Listar Assistentes

- **Endpoint:** `/assistentes`
- **Método:** `GET`
- **Requer Autenticação JWT:** Sim
- **Exemplo de Resposta:**

  ```bash

  `[
    {
      "id": 1,
      "nome": "Assistente 1",
      "telefone": "123456789"
    },
    {
      "id": 2,
      "nome": "Assistente 2",
      "telefone": "987654321"
    }
  ]`

  ```

#### Cadastrar Novo Assistente

- **Endpoint:** `/assistentes`
- **Método:** `POST`
- **Requer Autenticação JWT:** Sim
- **Parâmetros do Corpo:**
  - `nome` (string): Nome do assistente.
  - `telefone` (string): Número de telefone do assistente.
- **Exemplo de Requisição:**

  ```bash

  `{
    "nome": "Novo Assistente",
    "telefone": "555123456"
  }`

  ```

- **Exemplo de Resposta (Sucesso):**

  ```bash

  `{
    "id": 3,
    "nome": "Novo Assistente",
    "telefone": "555123456"
  }`

  ```

- **Exemplo de Resposta (Erro):**

  ```bash

  `{
    "erro": "Ocorreu um erro ao cadastrar o assistente."
  }`

  ```

#### Detalhes do Assistente

- **Endpoint:** `/assistentes/<id>`
- **Método:** `GET`
- **Requer Autenticação JWT:** Sim
- **Exemplo de Resposta (Sucesso):**

  ```bash

  `{
    "id": 1,
    "nome": "Assistente 1",
    "telefone": "123456789"
  }`

  ```

- **Exemplo de Resposta (Erro):**

  ```bash

  `{
    "erro": "Assistente não encontrado!"
  }`

  ```

## Licença

Este projeto está licenciado sob a [MIT License](https://chat.openai.com/c/LICENSE).
