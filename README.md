# Sistema Help Desk em Python

Sistema desktop para gerenciamento de chamados de TI (Help Desk / Service Desk).

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

---

## 📌 Descrição

O **Sistema Help Desk em Python** é uma aplicação desktop para registrar, acompanhar, atualizar e finalizar chamados técnicos de TI.

Possui autenticação com senha protegida por hash, controle de acesso por perfil, CRUD completo de chamados e usuários e um dashboard com indicadores e gráficos gerados a partir dos dados reais do banco.

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
- 🕒 Registro automático das datas de abertura, última atualização e conclusão
- 🔎 Busca por ID ou título e filtros por status, prioridade, categoria e responsável
- 📊 Dashboard com indicadores e 4 gráficos (status, categoria, prioridade e período)
- 👤 Gerenciamento de usuários (criar, editar, redefinir senha, ativar e desativar)
- ⚠️ Validações e mensagens claras de sucesso, erro, aviso e confirmação
- 🖥️ Interface adaptada à escala de tela do Windows e a telas pequenas
- 🧾 Registro de erros técnicos em arquivo de log
- 🧪 Testes automatizados das regras de negócio

## 🛠️ Tecnologias utilizadas

| Tecnologia | Uso no projeto |
|---|---|
| Python 3 | Linguagem principal |
| SQLite | Banco de dados local |
| Tkinter / ttk | Interface gráfica |
| Pandas | Tratamento dos dados do dashboard |
| Matplotlib | Gráficos do dashboard |
| hashlib / secrets | Hash e salt das senhas |
| unittest | Testes automatizados |
| Git / GitHub | Versionamento e publicação |

## 📁 Estrutura do projeto

```text
sistema-helpdesk-python/
├── app.py                  # Ponto de entrada da aplicação
├── config.py               # Constantes, caminhos e cores
├── database.py             # Conexão SQLite e criação das tabelas
├── models/                 # Entidades: Usuario e Chamado
├── repositories/           # Única camada que executa SQL
├── services/               # Regras de negócio e permissões
├── views/                  # Telas em Tkinter
├── utils/                  # Segurança, validações, datas, logs e exceções
├── tests/                  # Testes automatizados
├── database/               # O arquivo helpdesk.db é criado aqui
├── assets/
├── screenshots/
├── requirements.txt
└── .gitignore
```

**Fluxo das camadas:** `views` → `services` → `repositories` → `database`

As telas não executam SQL e os serviços não dependem do Tkinter. Assim, as regras de negócio podem ser reaproveitadas na versão web (V2).

## 🖼️ Screenshots

> As imagens serão adicionadas em breve.

<!--
Quando adicionar as imagens na pasta screenshots, apague esta linha de comentário e a última linha (a que tem -->).

### Login
![Tela de login](<img width="763" height="770" alt="Tela de login" src="https://github.com/user-attachments/assets/e0cb9f55-900d-47b2-9d94-25e101b123b2" />
))

### Dashboard
![Dashboard](<img width="1905" height="1071" alt="Dashboard" src="https://github.com/user-attachments/assets/3a4d0906-abe7-4841-ba67-d1a422ff2ce6" />)

### Lista de chamados
![Lista de chamados](<img width="1917" height="1071" alt="lista de chamado" src="https://github.com/user-attachments/assets/ae088ec7-4719-40b1-9a0e-c240e15e3097" />)

### Novo chamado
![Novo chamado](<img width="954" height="905" alt="Novo chamado" src="https://github.com/user-attachments/assets/3e21b4de-99e7-4462-a5a6-ef4bdad83272" />
-->

## ⚙️ Como instalar

**Pré-requisito:** Python 3.10 ou superior. No Windows, o Tkinter já vem junto com o instalador oficial.

**1. Clone o repositório**

```bash
git clone https://github.com/davidsilvaazevedo/sistema-helpdesk-python.git
cd sistema-helpdesk-python
```

**2. Crie e ative um ambiente virtual**

```bash
python -m venv venv
```

No Windows:

```bash
venv\Scripts\activate
```

No Linux ou macOS:

```bash
source venv/bin/activate
```

**3. Instale as dependências**

```bash
pip install -r requirements.txt
```

> No Linux, caso o Tkinter não esteja instalado: `sudo apt install python3-tk`

## ▶️ Como executar

```bash
python app.py
```

No primeiro acesso, o sistema cria o banco de dados e um administrador inicial:

| E-mail | Senha |
|---|---|
| `admin@helpdesk.local` | `Admin@123` |

> ⚠️ Credenciais apenas para demonstração. Altere a senha em **Usuários → Editar** após o primeiro login.

Para rodar os testes:

```bash
python -m unittest discover -v
```

## 🗄️ Como funciona o banco de dados

O arquivo `database/helpdesk.db` é criado automaticamente na primeira execução.

### Tabela `usuarios`

| Campo | Tipo | Descrição |
|---|---|---|
| id | INTEGER (PK) | Identificador |
| nome | TEXT | Nome do usuário |
| email | TEXT (único) | E-mail de login |
| senha_hash | TEXT | Hash da senha (nunca a senha pura) |
| perfil | TEXT | Administrador, Técnico ou Usuário |
| ativo | INTEGER | 1 = ativo, 0 = inativo |
| data_criacao | TEXT | Data de cadastro |

### Tabela `chamados`

| Campo | Tipo | Descrição |
|---|---|---|
| id | INTEGER (PK) | Número do chamado |
| titulo | TEXT | Título do problema |
| descricao | TEXT | Descrição detalhada |
| categoria | TEXT | Hardware, Software, Rede etc. |
| prioridade | TEXT | Baixa, Média, Alta ou Crítica |
| status | TEXT | Aberto, Em andamento, Resolvido ou Fechado |
| solicitante_id | INTEGER (FK) | Usuário que abriu o chamado |
| responsavel_id | INTEGER (FK) | Técnico responsável (opcional) |
| data_abertura | TEXT | Preenchida automaticamente |
| data_atualizacao | TEXT | Preenchida automaticamente |
| data_conclusao | TEXT | Preenchida ao resolver ou fechar |

### Boas práticas aplicadas

- Todas as consultas usam parâmetros (`?`), o que evita SQL Injection.
- As chaves estrangeiras garantem a integridade dos relacionamentos.
- Usuários são desativados, e não excluídos, para preservar o histórico dos chamados.
- O banco não é enviado ao GitHub (está no `.gitignore`), pois contém dados locais e é recriado automaticamente.

## 🔑 Perfis de acesso

| Ação | Administrador | Técnico | Usuário |
|---|:---:|:---:|:---:|
| Abrir chamado | ✅ | ✅ | ✅ |
| Ver todos os chamados | ✅ | ✅ | Só os próprios |
| Editar e alterar status | ✅ | ✅ | ❌ |
| Assumir chamado | ✅ | ✅ | ❌ |
| Atribuir responsável | ✅ | ❌ | ❌ |
| Excluir chamado | ✅ | ❌ | ❌ |
| Acessar dashboard | ✅ | ✅ | ❌ |
| Gerenciar usuários | ✅ | ❌ | ❌ |

O técnico só edita chamados sem responsável ou atribuídos a ele. As permissões são verificadas nas regras de negócio (`services/permissoes.py`), e não apenas escondendo botões na tela.

## 💡 Exemplo de utilização

1. O **administrador** faz login e cadastra um técnico e um usuário.
2. O **usuário** abre o chamado *"Impressora do financeiro não imprime"*, com prioridade Alta.
3. O **técnico** encontra o chamado na lista e clica em **Assumir**. O status muda para *Em andamento*.
4. Depois de resolver o problema, o técnico clica em **Resolver**, e a data de conclusão é registrada.
5. O **usuário** acompanha o status em **Meus chamados**, e o dashboard é atualizado.

## 🗺️ Roadmap

- [x] **V1 – Desktop:** Python, Tkinter e SQLite
- [ ] **V2 – Web:** Flask, HTML, CSS, JavaScript e API REST
- [ ] **V3 – Sistema web completo:** autenticação aprimorada, API, PostgreSQL e deploy

Outras ideias:

- [ ] Comentários e histórico em cada chamado
- [ ] Anexos nos chamados
- [ ] SLA por prioridade com alerta de atraso
- [ ] Exportação de relatórios em Excel e PDF
- [ ] Notificações por e-mail
- [ ] Troca de senha pelo próprio usuário

## 👨‍💻 Autor

**David Azevedo**

[![GitHub](https://img.shields.io/badge/GitHub-davidsilvaazevedo-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/davidsilvaazevedo)

---

Feito com Python 🐍 para fins de estudo e portfólio.
