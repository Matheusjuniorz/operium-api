# Operium — API de Gerenciamento de Solicitações Empresariais

O **Operium** é uma API REST desenvolvida em Python com Django e Django REST Framework para organizar e centralizar o fluxo de solicitações internas entre funcionários e gerentes de uma empresa. O projeto substitui pedidos informais por um processo rastreável de registro, encaminhamento e aprovação.

---

##  Sobre o Projeto

Em muitas empresas, pedidos internos são feitos de maneira descentralizada, dificultando o acompanhamento de prazos e responsáveis. O Operium resolve esse problema por meio de uma arquitetura backend focada em regras de negócio, relacionamentos entre entidades e controle de acesso.

* **Categoria:** Backend / API REST
* **Status:** Em desenvolvimento (foco exclusivo na camada backend)
* **Autor:** Matheus Junior Z.

---

##  Tecnologias Utilizadas

* **Python:** Linguagem principal para regras de negócio e validações.
* **Django:** Estrutura da aplicação, ORM, autenticação, painel administrativo e migrações.
* **Django REST Framework (DRF):** Construção de endpoints REST, serializers, permissões e interface navegável.
* **PostgreSQL:** Banco de dados relacional para armazenamento seguro de registros.
* **Python Decouple:** Gerenciamento de variáveis de ambiente (`.env`).

---

##  Arquitetura do Projeto

```text
OPERIUM/
└── Backend/
    ├── .venv/               # Ambiente virtual Python
    └── operium/
        ├── core/            # Aplicação principal (models, views, serializers, urls, tests)
        ├── operium/         # Configurações globais do projeto (settings, urls, wsgi/asgi)
        ├── .env             # Variáveis de ambiente (não versionado)
        ├── manage.py        # Utilitário de linha de comando do Django
        └── requirements.txt # Dependências do projeto
```


---

##  Funcionalidades e Fluxo de Funcionamento

O sistema opera com três perfis principais (**Funcionário**, **Gerente** e **Administrador**) e gerencia o seguinte ciclo de vida:

1. **Autenticação e Cadastro:** Usuários são autenticados na API (via Token/Bearer) com permissões restritas por perfil.
2. **Gestão de Cargos:** Gerentes podem atribuir ou escolher cargos para funcionários.
3. **Registro de Solicitações:** Funcionários autenticados criam solicitações contendo título, descrição e destinatário.
4. **Encaminhamento e Análise:** O pedido fica vinculado ao funcionário solicitante e ao gerente responsável.
5. **Aprovação ou Rejeição:** O gerente consulta as solicitações direcionadas a ele e atualiza o status (`Pendente`, `Aprovado` ou `Rejeitado`).

---

##  Principais Endpoints da API

A API conta com a interface navegável padrão do Django REST Framework para exploração e testes.

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `GET` / `POST` | `/api/auth/users/` | Listagem e cadastro de usuários (requer autenticação para consulta). |
| `POST` | `/api/funcionarios/` | Criação e manipulação de registros de funcionários. |
| `GET` | `/api/lista-funcionarios/` | Listagem geral dos funcionários cadastrados. |
| `POST` | `/api/gerente-funcionario/{id}/escolher-cargo/` | Atribuição ou alteração de cargo de um funcionário pelo gerente. |
| `POST` | `/api/nova-solitacao/` | Registro de uma nova solicitação interna. |
| `POST` | `/api/receber-solitacao/` | Recebimento e processamento de solicitações (Título, Descrição, Status, Funcionário, Gerente). |
| `GET` | `/api/lista-solitacao/` | Consulta de solicitações cadastradas no sistema. |

*(Nota: Endpoints configurados exclusivamente para envio de dados retornarão `HTTP 405 Method Not Allowed` caso sejam acessados via `GET` diretamente no navegador).*

---

##  Como Executar o Projeto Localmente

### Pré-requisitos
* Python 3.10+ instalado
* PostgreSQL instalado e em execução
* Git

### Passo a passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com
   cd operium/Backend
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # Linux / macOS
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r operium/requirements.txt
   ```

4. **Configure as variáveis de ambiente:**
   Entre na pasta onde está o `manage.py` (`cd operium`) e crie um arquivo chamado `.env` com as credenciais do seu banco PostgreSQL:
   ```env
   SECRET_KEY=sua_chave_secreta_django
   DEBUG=True
   DB_NAME=operium_db
   DB_USER=postgres
   DB_PASSWORD=sua_senha_aqui
   DB_HOST=localhost
   DB_PORT=5432
   ```

5. **Execute as migrações do banco de dados:**
   ```bash
   python manage.py migrate
   ```

6. **Crie um superusuário (opcional, para acessar o Django Admin):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```
   A API estará disponível em `http://127.0.0`.

---

##  Testes Automatizados

Para rodar a suíte de testes unitários e de integração configurada em `core/tests.py`, execute:

```bash
python manage.py test
```

---

##  Melhorias Futuras (Roadmap)

* Documentação interativa automatizada com OpenAPI / Swagger (`drf-spectacular`).
* Histórico de auditoria e logs de alteração de status.
* Sistema de comentários e anexos nas solicitações.
* Notificações por e-mail para funcionários e gerentes.
* Desenvolvimento de interface frontend em React.
