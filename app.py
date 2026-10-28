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
from views.styles import centralizar_janela, configurar_estilos, escalar

logger = logging.getLogger(__name__)

# Tamanhos de referência para escala 100% (são ajustados à escala da tela)
TAMANHO_PRINCIPAL = (1280, 780)
TAMANHO_MINIMO_PRINCIPAL = (960, 600)


def ativar_alta_resolucao() -> None:
    """Deixa as fontes nítidas em monitores com escala no Windows."""
    try:
        from ctypes import windll  # type: ignore[attr-defined]
        windll.shcore.SetProcessDpiAwareness(1)
    except (ImportError, AttributeError, OSError):
        logger.debug("Ajuste de DPI não disponível neste sistema")


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
        self.state("normal")
        self.minsize(1, 1)
        self._trocar_tela(LoginView(self, on_login_sucesso=self._ao_logar))
        self.geometry("")             # libera o tamanho anterior
        centralizar_janela(self)      # usa o tamanho que o login precisa
        self.resizable(False, False)

    def _ao_logar(self, usuario: Usuario) -> None:
        self.resizable(True, True)
        self.title(f"{APP_NAME} — {usuario.nome} ({usuario.perfil})")
        self._trocar_tela(MainView(self, usuario, on_logout=self.mostrar_login))

        largura_tela, altura_tela = self.winfo_screenwidth(), self.winfo_screenheight()
        self.minsize(min(escalar(self, TAMANHO_MINIMO_PRINCIPAL[0]), largura_tela - 40),
                     min(escalar(self, TAMANHO_MINIMO_PRINCIPAL[1]), altura_tela - 80))
        largura, altura = (escalar(self, v) for v in TAMANHO_PRINCIPAL)
        self.geometry("")
        self.update_idletasks()
        # Em telas menores que o tamanho ideal, abre maximizado
        if largura >= largura_tela - 40 or altura >= altura_tela - 80:
            centralizar_janela(self, largura, altura)
            self._maximizar()
        else:
            self.geometry(f"{largura}x{altura}")
            x = (largura_tela - largura) // 2
            y = max((altura_tela - altura) // 2 - 20, 0)
            self.geometry(f"{largura}x{altura}+{x}+{y}")

    def _maximizar(self) -> None:
        try:
            self.state("zoomed")  # Windows / macOS
        except tk.TclError:
            self.attributes("-zoomed", True)  # Linux

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
