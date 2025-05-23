import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from teamplates.dash_sys_copy import Ui_Form
from thread.WorkThread import BotWorker
from src.login import btn_start
from database.data import consulta_motorista, conectar
from xlsx.fechamento import exportar_notas
from src.navegador import iniciar_navegador
from PySide6.QtGui import QIcon


class TelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('teamplates/icons/robo.png'))
        self.ui.pushButton_3.setIcon(QIcon('teamplates/icons/pasta-aberta.png'))
        self.ui.pushButton_4.setIcon(QIcon('teamplates/icons/pasta-aberta.png'))
        self.ui.pushButton_5.setIcon(QIcon('teamplates/icons/user.png'))
        self.checkbox_ativado = False
        self.ui.pushButton_2.setDisabled(True)
        
        self.driver = None
        self.bot_thread = None

        self.conn = conectar()
        self.motoristas = [row["nome"] for row in consulta_motorista(self.conn)]
        self.ui.comboBox_7.addItems(self.motoristas)

        self.ui.pushButton.clicked.connect(self.rodar_bot)
        self.ui.pushButton_2.clicked.connect(self.continuar_bot)
        self.ui.checkBox.stateChanged.connect(self.checkbox_marcado)

        self.ui.pushButton_3.clicked.connect(lambda: self.ui.Pagina.setCurrentIndex(0))
        self.ui.pushButton_4.clicked.connect(lambda: self.ui.Pagina.setCurrentIndex(1))
        self.ui.pushButton_5.clicked.connect(lambda: self.ui.Pagina.setCurrentIndex(2))
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.Pagina.setCurrentIndex(1))
        self.ui.pushButton_31.clicked.connect(self.cadastrar_mtr)
        self.ui.pushButton_27.clicked.connect(self.exportar_excel)

    def rodar_bot(self):
        self.ui.pushButton.setDisabled(True)
        self.ui.pushButton_2.setDisabled(True)
        self.ui.progressBar.setValue(0)
        self.ui.checkBox.setChecked(False)

        self.checkbox_ativado = False

        data_inicial = self.ui.dateEdit.date().toString("dd/MM/yyyy")
        data_final = self.ui.dateEdit_2.date().toString("dd/MM/yyyy")

        self.driver = iniciar_navegador()

        if not self.driver:
            self.exibir_erro("❌ Falha ao iniciar o navegador.")
            self.ui.pushButton.setDisabled(False)
            return

        self.bot_thread = BotWorker(data_inicial, data_final, self.driver)
        self.bot_thread.progress.connect(self.ui.progressBar.setValue)
        self.bot_thread.finished.connect(self.ativar_botao)
        self.bot_thread.log.connect(self.exibir_log)  # conecta o sinal de log ao método
        self.bot_thread.log_txt.connect(self.log_text)
        self.bot_thread.start()

    def exibir_log(self, mensagem):
        # Abre uma janela popup para cada mensagem emitida no log do BotWorker
        QMessageBox.information(self, "Mensagem do Bot", mensagem)

    def log_text(self,mensagem):
        self.ui.label_7.setText(mensagem)

    def exibir_erro(self, mensagem):
        QMessageBox.critical(self, "Erro", mensagem)

    def continuar_bot(self):
        if self.bot_thread:
            self.bot_thread.continuar_execucao()

    def checkbox_marcado(self, state):
        try:
            if self.ui.checkBox.isChecked() and self.driver and not self.checkbox_ativado:
                btn_start(self.driver)
                self.checkbox_ativado = True

                if self.bot_thread:
                    self.bot_thread.continuar_execucao()
        except AttributeError:
                pass

    def ativar_botao(self):
        self.ui.pushButton.setDisabled(False)
        self.ui.pushButton_2.setDisabled(False)

    def cadastrar_mtr(self):
        from database.data import cadastrar_motorista, conectar
        
        conn = conectar()
        codigo_serial_motorista = self.ui.lineEdit_3.text()
        nome_motorista = self.ui.lineEdit.text()
        cpf = self.ui.lineEdit_2.text()
        data_nascimento = self.ui.dateEdit_34.date().toString("dd/MM/yyyy")
        
        cadastrar_motorista(conn, codigo_serial_motorista, nome_motorista, cpf, data_nascimento)
        conn.close()

        self.ui.label_77.setText(f"Motorista {nome_motorista} cadastrado!")

        self.ui.lineEdit_3.clear()
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()

    def exportar_excel(self):
        data_inicial = self.ui.dateEdit_28.date().toString("yyyy-MM-dd")
        data_final = self.ui.dateEdit_27.date().toString("yyyy-MM-dd")
        motorista = self.ui.comboBox_7.currentText()

        self.exibir_log(f"Exportando notas de {motorista} de {data_inicial} até {data_final}...")

        exportar_notas(data_inicial, data_final, motorista, log_callback=self.exibir_log)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = TelaPrincipal()
    window.show()
    sys.exit(app.exec())
