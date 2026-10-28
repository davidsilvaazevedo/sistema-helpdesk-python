<h1 align="center">Sistema Help Desk em Python</h1>

<p align="center">
  Sistema desktop para gerenciamento de chamados de TI (Help Desk / Service Desk)
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge" alt="Matplotlib">
</p>

<p align="center">
  <a href="#-descrição">Descrição</a> •
  <a href="#-funcionalidades">Funcionalidades</a> •
  <a href="#-screenshots">Screenshots</a> •
  <a href="#-como-instalar">Instalação</a> •
  <a href="#-perfis-de-acesso">Perfis</a> •
  <a href="#-roadmap">Roadmap</a> •
  <a href="#-autor">Autor</a>
</p>

---

## 📌 Descrição

O **Sistema Help Desk em Python** é uma aplicação desktop para registrar, acompanhar, atualizar e finalizar chamados técnicos de TI. Possui autenticação com senha protegida por hash, controle de acesso por perfil, CRUD completo de chamados e usuários e um dashboard com indicadores e gráficos gerados a partir dos dados reais do banco.

## 🎯 Objetivo

Projeto de portfólio criado para demonstrar, de forma organizada e didática, conhecimentos em:

- Python e Programação Orientada a Objetos
- Banco de dados relacional com **SQLite** e SQL parametrizado
- **CRUD** completo
- Interface gráfica com **Tkinter / ttk**
- Análise de dados com **Pandas** e visualização com **Matplotlib**
- Autenticação, hash de senhas e controle de acesso
- Validação de dados e tratamento de erros
- Arquitetura em camadas e separação de responsabilidades
- Versionamento com Git e GitHub

## ✅ Funcionalidades

- 🔐 Login com e-mail e senha (PBKDF2-SHA256 + salt)
- 👥 Três perfis de acesso: **Administrador**, **Técnico** e **Usuário**
- 📝 Cadastro, edição, exclusão e visualização de chamados
- 🔄 Alteração de status, atribuição de responsável, assumir, resolver e fechar chamados
- 🕒 Registro automático de data de abertura, última atualização e conclusão
- 🔎 Busca por ID ou título e filtros por status, prioridade, categoria e responsável
- 📊 Dashboard com indicadores e 4 gráficos (status, categoria, prioridade e período)
- 👤 Gerenciamento de usuários (criar, editar, redefinir senha, ativar/desativar)
- ⚠️ Validações e mensagens claras de sucesso, erro, aviso e confirmação
- 🧾 Registro de erros técnicos em arquivo de log
- 🧪 Testes automatizados das regras de negócio

## 🛠️ Tecnologias utilizadas

| Tecnologia | Uso no projeto |
|---|---|
| Python 3 | Linguagem principal |
| SQLite (`sqlite3`) | Banco de dados local |
| Tkinter / ttk | Interface gráfica |
| Pandas | Tratamento dos dados do dashboard |
| Matplotlib | Gráficos do dashboard |
| hashlib / secrets | Hash e salt das senhas |
| unittest | Testes automatizados |
| Git / GitHub | Versionamento e publicação |

## 📁 Estrutura do projeto

```text
sistema-helpdesk-python/
├── app.py                     # Ponto de entrada: inicia banco, login e janela principal
├── config.py                  # Constantes, caminhos e identidade visual
├── database.py                # Conexão SQLite e criação das tabelas
├── models/                    # Entidades do domínio
│   ├── usuario.py
│   └── chamado.py
├── repositories/              # Única camada que executa SQL
│   ├── usuario_repository.py
│   └── chamado_repository.py
├── services/                  # Regras de negócio e permissões
│   ├── permissoes.py
│   ├── auth_service.py
│   ├── chamado_service.py
│   ├── usuario_service.py
│   └── dashboard_service.py
├── views/                     # Telas Tkinter
│   ├── styles.py
│   ├── dialogs.py
│   ├── login_view.py
│   ├── main_view.py
│   ├── dashboard_view.py
│   ├── chamados_view.py
│   ├── chamado_form.py
│   ├── chamado_detalhes.py
│   └── usuarios_view.py
├── utils/                     # Segurança, validações, datas, logs e exceções
├── tests/                     # Testes automatizados
├── database/                  # helpdesk.db é criado aqui automaticamente
├── assets/
├── screenshots/
├── requirements.txt
└── .gitignore
```

**Fluxo das camadas:** `views` → `services` → `repositories` → `database`
As telas não executam SQL e os serviços não conhecem o Tkinter. Isso facilita reaproveitar as regras de negócio na versão web (V2).

## 🖼️ Screenshots

| Login | Dashboard |
|---|---|
| ![Tela de login](screenshots/login.png) | ![Dashboard](screenshots/dashboard.png) |

| Lista de chamados | Novo chamado |
|---|---|
| ![Lista de chamados](screenshots/chamados.png) | ![Novo chamado](screenshots/novo-chamado.png) |

## ⚙️ Como instalar

**Pré-requisitos:** Python 3.10 ou superior (com Tkinter, que já acompanha o instalador oficial do Windows).

```bash
# 1. Clone o repositório
git clone https://github.com/davidsilvaazevedo/sistema-helpdesk-python.git
cd sistema-helpdesk-python

# 2. Crie e ative um ambiente virtual
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt
```

> No Linux, caso o Tkinter não esteja instalado: `sudo apt install python3-tk`

## ▶️ Como executar

```bash
python app.py
```

No primeiro acesso, o sistema cria o banco e um administrador inicial:

| E-mail | Senha |
|---|---|
| `admin@helpdesk.local` | `Admin@123` |

> ⚠️ Credenciais apenas para demonstração. Altere a senha em **Usuários → Editar** após o primeiro login.
> Também é possível definir outras credenciais iniciais pelas variáveis de ambiente `HELPDESK_ADMIN_EMAIL` e `HELPDESK_ADMIN_SENHA`.

Para rodar os testes:

```bash
python -m unittest discover -v
```

## 🗄️ Como funciona o banco de dados

O arquivo `database/helpdesk.db` é criado automaticamente na primeira execução.

**Tabela `usuarios`**

| Campo | Tipo | Descrição |
|---|---|---|
| id | INTEGER PK | Identificador |
| nome | TEXT | Nome do usuário |
| email | TEXT UNIQUE | E-mail de login |
| senha_hash | TEXT | `pbkdf2_sha256$iterações$salt$hash` (nunca a senha pura) |
| perfil | TEXT | Administrador, Técnico ou Usuário |
| ativo | INTEGER | 1 = ativo, 0 = inativo |
| data_criacao | TEXT | Data de cadastro |

**Tabela `chamados`**

| Campo | Tipo | Descrição |
|---|---|---|
| id | INTEGER PK | Número do chamado |
| titulo / descricao | TEXT | Dados do problema |
| categoria / prioridade / status | TEXT | Valores validados (CHECK no banco + validação no Python) |
| solicitante_id | INTEGER FK → usuarios | Quem abriu |
| responsavel_id | INTEGER FK → usuarios | Técnico responsável (opcional) |
| data_abertura / data_atualizacao / data_conclusao | TEXT | Preenchidas automaticamente |

Boas práticas aplicadas:

- Todas as consultas usam **parâmetros (`?`)**, evitando SQL Injection.
- `PRAGMA foreign_keys = ON` garante a integridade dos relacionamentos.
- Usuários são **desativados**, não excluídos, preservando o histórico dos chamados.
- O banco **não é versionado** (veja o `.gitignore`): ele contém hashes de senha e dados locais, e é recriado automaticamente.

## 🔑 Perfis de acesso

| Ação | Administrador | Técnico | Usuário |
|---|:---:|:---:|:---:|
| Abrir chamado | ✅ | ✅ | ✅ |
| Ver todos os chamados | ✅ | ✅ | ❌ (apenas os próprios) |
| Editar / alterar status | ✅ | ✅ (sem responsável ou atribuídos a ele) | ❌ |
| Assumir chamado | ✅ | ✅ | ❌ |
| Atribuir responsável | ✅ | ❌ | ❌ |
| Excluir chamado | ✅ | ❌ | ❌ |
| Dashboard | ✅ | ✅ | ❌ |
| Gerenciar usuários | ✅ | ❌ | ❌ |

As permissões são verificadas na **camada de serviços** (`services/permissoes.py`), não apenas escondendo botões na interface.

## 💡 Exemplo de utilização

1. O **administrador** faz login e cadastra um técnico e um usuário em **Usuários**.
2. O **usuário** entra no sistema e abre o chamado *"Impressora do financeiro não imprime"* (categoria Impressora, prioridade Alta).
3. O **técnico** vê o chamado na lista, clica em **Assumir** — o status muda para *Em andamento*.
4. Após resolver o problema, o técnico clica em **Resolver**; a data de conclusão é registrada.
5. O **usuário** consulta o status em **Meus chamados**, e o dashboard é atualizado com os novos números.

## 🗺️ Roadmap

- [x] **V1 — Desktop**: Python, Tkinter, SQLite
- [ ] **V2 — Web**: Flask, HTML, CSS, JavaScript e API REST (reaproveitando `services/` e `repositories/`)
- [ ] **V3 — Sistema Web completo**: autenticação aprimorada (tokens/JWT), API, PostgreSQL e deploy

Outras ideias:

- [ ] Histórico de interações/comentários por chamado
- [ ] Anexos nos chamados
- [ ] SLA por prioridade com alertas de atraso
- [ ] Exportação de relatórios em Excel/PDF
- [ ] Notificações por e-mail
- [ ] Troca de senha pelo próprio usuário

## 👨‍💻 Autor

**David Azevedo**

[![GitHub](https://img.shields.io/badge/GitHub-davidsilvaazevedo-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/davidsilvaazevedo)

---

<p align="center">Feito com Python 🐍 para fins de estudo e portfólio.</p>
#   s i s t e m a - h e l p d e s k - p y t h o n  
 