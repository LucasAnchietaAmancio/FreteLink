from janelas.janela_pricipal import TelaPrincipal
from janelas.janela_licence import TelaLicenca
from PySide6.QtWidgets import QApplication
import sys
from utils.licenca import precisa_validar_licenca

if __name__ == '__main__':
    app = QApplication(sys.argv)

    if precisa_validar_licenca():
        window = TelaLicenca()
    else:
        window = TelaPrincipal()

    window.show()
    sys.exit(app.exec())
