"""Ponto de entrada do Sistema Help Desk.

Responsável apenas por iniciar logs e banco de dados e alternar entre a
tela de login e a janela principal.
"""
from __future__ import annotations

import logging
import sys
import tkinter as tk
from tkinter import messagebox

from config import APP_NAME
from database import inicializar_banco
from models.usuario import Usuario
from services.auth_service import AuthService
from utils.logger import configurar_logging
from views.login_view import LoginView
from views.main_view import MainView
from views.styles import centralizar_janela, configurar_estilos

logger = logging.getLogger(__name__)

TAMANHO_LOGIN = (460, 540)
TAMANHO_PRINCIPAL = (1320, 800)


def ativar_alta_resolucao() -> None:
    """Deixa as fontes nítidas em monitores com escala no Windows."""
    try:
        from ctypes import windll  # type: ignore[attr-defined]
        windll.shcore.SetProcessDpiAwareness(1)
    except (ImportError, AttributeError, OSError):
        pass  # não é Windows ou a API não está disponível: segue normalmente


class HelpDeskApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title(APP_NAME)
        configurar_estilos(self)
        self._tela_atual: tk.Widget | None = None
        self.mostrar_login()

    def _trocar_tela(self, nova_tela: tk.Widget) -> None:
        if self._tela_atual is not None:
            self._tela_atual.destroy()
        self._tela_atual = nova_tela
        nova_tela.pack(fill="both", expand=True)

    def mostrar_login(self) -> None:
        self.title(APP_NAME)
        self.minsize(420, 500)
        self.resizable(False, False)
        centralizar_janela(self, *TAMANHO_LOGIN)
        self._trocar_tela(LoginView(self, on_login_sucesso=self._ao_logar))

    def _ao_logar(self, usuario: Usuario) -> None:
        self.resizable(True, True)
        self.minsize(1100, 680)
        centralizar_janela(self, *TAMANHO_PRINCIPAL)
        self.title(f"{APP_NAME} — {usuario.nome} ({usuario.perfil})")
        self._trocar_tela(MainView(self, usuario, on_logout=self.mostrar_login))

    def report_callback_exception(self, exc, val, tb) -> None:  # noqa: ANN001
        """Captura erros não tratados da interface: registra no log e avisa o usuário."""
        logger.error("Erro não tratado na interface", exc_info=(exc, val, tb))
        messagebox.showerror("Erro inesperado",
                             "Ocorreu um erro inesperado. Os detalhes foram registrados no arquivo de log.",
                             parent=self)


def main() -> int:
    configurar_logging()
    ativar_alta_resolucao()
    try:
        inicializar_banco()
        AuthService().garantir_admin_inicial()
    except Exception:  # noqa: BLE001
        logger.exception("Falha ao inicializar o banco de dados")
        raiz = tk.Tk()
        raiz.withdraw()
        messagebox.showerror(APP_NAME, "Não foi possível inicializar o banco de dados. Verifique o arquivo de log.")
        raiz.destroy()
        return 1

    HelpDeskApp().mainloop()
    return 0


if __name__ == "__main__":
    sys.exit(main())
