from PySide6.QtCore import QThread, Signal, QWaitCondition, QMutex
from src.login import fazer_login
from src.nagevacao import acessar_cte, filtrar_data
from src.coleta_de_dados import filter_state_select_cte
from dotenv import load_dotenv
import os

load_dotenv()

email = os.getenv('LOGIN_EMAIL')
senha = os.getenv('LOGIN_SENHA')

class BotWorker(QThread):
    progress = Signal(int)
    finished = Signal()
    log = Signal(str)
    log_txt = Signal(str)

    def __init__(self, data_inicial, data_final, driver):
        super().__init__()
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.driver = driver
        self._continue_condition = QWaitCondition()
        self._mutex = QMutex()

    def run(self):
        try:
            print("🔄 Iniciando execução do bot.")
            self.progress.emit(10)
            

            print("🛠️ Fazendo login...")
            try:
                fazer_login(self.driver, email, senha)
                self.log.emit("✅ Login realizado com sucesso.")
            except Exception as e:
                self.log.emit(f"❌ Erro no login: {e}")
                self.progress.emit(0)
                return

            self.progress.emit(40)
            print("⏸ Aguardando checkbox para continuar...")

            self._mutex.lock()
            self._continue_condition.wait(self._mutex)
            self._mutex.unlock()

            print("▶ Continuando após o checkbox!")
            self.progress.emit(60)

            try:
                acessar_cte(self.driver)
                print("✅ Acessou CTE.")
            except Exception as e:
                self.log.emit(f"❌ Erro ao acessar CTE: {e}")
                self.progress.emit(0)
                return

            self.progress.emit(80)
            filtrar_data(self.driver, self.data_inicial, self.data_final)
            print("✅ Filtro de data aplicado.")

            self.progress.emit(90)
            dados = filter_state_select_cte(self.driver, log_callback=self.log.emit, log_text=self.log_txt.emit)
            print(f"📦 Documentos extraídos: {dados}")
            
            self.progress.emit(100)
            self.log.emit("✅ Execução finalizada.")
        finally:
            self.finished.emit()

    def continuar_execucao(self):
        self._continue_condition.wakeAll()
        