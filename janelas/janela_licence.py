import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from teamplates.dash_sys_licence import Ui_Form
from utils.licenca import validar_licenca
from janelas.janela_pricipal import TelaPrincipal
from PySide6.QtGui import QIcon

class TelaLicenca(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon('teamplates/icons/robo.png'))
        self.ui.pushButton.clicked.connect(self.verificar_licenca)

    def verificar_licenca(self):
        serial = self.ui.lineEdit.text()

        if validar_licenca(serial):
            QMessageBox.information(self, "Licença", "Licença aprovada!")
            self.close()
            self.tela_principal = TelaPrincipal()
            self.tela_principal.show()
        else:
            QMessageBox.critical(self, "Licença", "Licença inválida!")

