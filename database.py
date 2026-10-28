"""Conexão e criação do banco de dados SQLite.

Este módulo só sabe *como* falar com o banco. As consultas de cada
entidade ficam nos repositórios (pasta ``repositories``).
"""
from __future__ import annotations

import logging
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from config import DATABASE_PATH

logger = logging.getLogger(__name__)

_caminho_banco: Path = DATABASE_PATH

SCHEMA = """
CREATE TABLE IF NOT EXISTS usuarios (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    nome          TEXT    NOT NULL,
    email         TEXT    NOT NULL UNIQUE COLLATE NOCASE,
    senha_hash    TEXT    NOT NULL,
    perfil        TEXT    NOT NULL CHECK (perfil IN ('Administrador', 'Técnico', 'Usuário')),
    ativo         INTEGER NOT NULL DEFAULT 1 CHECK (ativo IN (0, 1)),
    data_criacao  TEXT    NOT NULL
);

CREATE TABLE IF NOT EXISTS chamados (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo            TEXT    NOT NULL,
    descricao         TEXT    NOT NULL,
    categoria         TEXT    NOT NULL,
    prioridade        TEXT    NOT NULL CHECK (prioridade IN ('Baixa', 'Média', 'Alta', 'Crítica')),
    status            TEXT    NOT NULL CHECK (status IN ('Aberto', 'Em andamento', 'Resolvido', 'Fechado')),
    solicitante_id    INTEGER NOT NULL REFERENCES usuarios (id),
    responsavel_id    INTEGER REFERENCES usuarios (id),
    data_abertura     TEXT    NOT NULL,
    data_atualizacao  TEXT    NOT NULL,
    data_conclusao    TEXT
);

CREATE INDEX IF NOT EXISTS idx_chamados_status      ON chamados (status);
CREATE INDEX IF NOT EXISTS idx_chamados_solicitante ON chamados (solicitante_id);
CREATE INDEX IF NOT EXISTS idx_chamados_responsavel ON chamados (responsavel_id);
"""


def definir_caminho_banco(caminho: Path | str) -> None:
    """Permite trocar o arquivo do banco (usado pelos testes automatizados)."""
    global _caminho_banco
    _caminho_banco = Path(caminho)


@contextmanager
def get_connection() -> Iterator[sqlite3.Connection]:
    """Abre uma conexão, faz commit em caso de sucesso e rollback em caso de erro.

    Uso:
        with get_connection() as conn:
            conn.execute("SELECT ...", (parametro,))
    """
    conn = sqlite3.connect(_caminho_banco)
    conn.row_factory = sqlite3.Row  # permite acessar colunas pelo nome
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def inicializar_banco() -> None:
    """Cria a pasta e as tabelas do banco caso ainda não existam."""
    _caminho_banco.parent.mkdir(parents=True, exist_ok=True)
    with get_connection() as conn:
        conn.executescript(SCHEMA)
    logger.info("Banco de dados pronto em %s", _caminho_banco)
