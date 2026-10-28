"""Configurações e constantes globais do Sistema Help Desk.

Centralizar os valores fixos aqui evita "números mágicos" espalhados pelo
código e facilita a evolução do projeto (ex.: trocar SQLite por PostgreSQL na V3).
"""
import os
from pathlib import Path

# ---------------------------------------------------------------------------
# Caminhos
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
DATABASE_DIR = BASE_DIR / "database"
DATABASE_PATH = DATABASE_DIR / "helpdesk.db"
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "helpdesk.log"

# ---------------------------------------------------------------------------
# Aplicação
# ---------------------------------------------------------------------------
APP_NAME = "Help Desk"
APP_VERSION = "1.0.0"

# ---------------------------------------------------------------------------
# Perfis de acesso
# ---------------------------------------------------------------------------
PERFIL_ADMIN = "Administrador"
PERFIL_TECNICO = "Técnico"
PERFIL_USUARIO = "Usuário"
PERFIS = (PERFIL_ADMIN, PERFIL_TECNICO, PERFIL_USUARIO)

# ---------------------------------------------------------------------------
# Domínio dos chamados
# ---------------------------------------------------------------------------
CATEGORIAS = (
    "Hardware",
    "Software",
    "Rede",
    "Acesso",
    "Impressora",
    "E-mail",
    "Sistemas",
    "Outros",
)

PRIORIDADE_CRITICA = "Crítica"
PRIORIDADES = ("Baixa", "Média", "Alta", PRIORIDADE_CRITICA)

STATUS_ABERTO = "Aberto"
STATUS_EM_ANDAMENTO = "Em andamento"
STATUS_RESOLVIDO = "Resolvido"
STATUS_FECHADO = "Fechado"
STATUS = (STATUS_ABERTO, STATUS_EM_ANDAMENTO, STATUS_RESOLVIDO, STATUS_FECHADO)
STATUS_CONCLUSAO = (STATUS_RESOLVIDO, STATUS_FECHADO)

# Limites de tamanho dos campos
TITULO_MAX = 120
DESCRICAO_MAX = 2000
NOME_MAX = 100

# ---------------------------------------------------------------------------
# Segurança
# ---------------------------------------------------------------------------
# Administrador criado automaticamente quando o banco está vazio.
# Os valores podem ser sobrescritos por variáveis de ambiente para não
# depender de credenciais fixas no código. Troque a senha após o 1º acesso.
ADMIN_PADRAO_NOME = "Administrador"
ADMIN_PADRAO_EMAIL = os.getenv("HELPDESK_ADMIN_EMAIL", "admin@helpdesk.local")
ADMIN_PADRAO_SENHA = os.getenv("HELPDESK_ADMIN_SENHA", "Admin@123")

PBKDF2_ITERACOES = 260_000
SENHA_TAMANHO_MINIMO = 6

# ---------------------------------------------------------------------------
# Datas
# ---------------------------------------------------------------------------
DATA_FORMATO_DB = "%Y-%m-%d %H:%M:%S"
DATA_FORMATO_EXIBICAO = "%d/%m/%Y %H:%M"

# ---------------------------------------------------------------------------
# Identidade visual
# ---------------------------------------------------------------------------
FONTE = "Segoe UI"

CORES = {
    "azul_escuro": "#0F2A4A",
    "azul_escuro_hover": "#1B3D66",
    "azul": "#2563EB",
    "azul_hover": "#1D4ED8",
    "azul_claro": "#93B4E8",
    "fundo": "#F3F5F8",
    "branco": "#FFFFFF",
    "borda": "#D9DEE5",
    "texto": "#1E2733",
    "texto_secundario": "#5B6675",
    "texto_sidebar": "#C9D6E8",
    "linha_alternada": "#F8FAFC",
    "vermelho": "#C0392B",
    "vermelho_hover": "#A93226",
}

# Paleta usada nos gráficos (tons de azul e cinza)
CORES_GRAFICOS = ("#0F2A4A", "#2563EB", "#5B8DEF", "#93B4E8", "#8A94A6", "#B8C0CC", "#1B3D66", "#C9D6E8")
