from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def fazer_login(driver, usuario, senha):
    driver.get("https://sso.iob.com.br/signin?response_type=code&scope=&client_id=c17d4225-9d57-401b-b4fd-32503121f55b&redirect_uri=https%3A%2F%2Femissor.iob.com.br&lblcontinue=Acessar%20Emissor")

    wait = WebDriverWait(driver, 20)

    # Esperar o campo de usuário
    time.sleep(5)
    campo_usuario = wait.until(EC.presence_of_element_located((By.ID, "username")))
    campo_usuario.clear()
    campo_usuario.send_keys(usuario)

    # Esperar o campo de senha
    time.sleep(3)
    campo_senha = wait.until(EC.presence_of_element_located((By.ID, "password")))
    campo_senha.clear()
    campo_senha.send_keys(senha)

    time.sleep(3)

def btn_start(driver):
    wait = WebDriverWait(driver, 20)
    botao_login = wait.until(EC.element_to_be_clickable((By.ID, "formButton")))
    botao_login.click()
