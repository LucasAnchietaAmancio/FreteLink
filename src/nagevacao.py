from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def filtrar_data(driver, data_inicial, data_final):
    wait = WebDriverWait(driver, 20)

    time.sleep(20)
    campo_data_inicial = driver.find_element(By.ID, "filter_start_date")  # ajuste o seletor
    campo_data_final = driver.find_element(By.ID, "filter_end_date")      # ajuste o seletor

    campo_data_inicial.clear()
    campo_data_inicial.send_keys(data_inicial)
    time.sleep(2)

    campo_data_final.clear()
    campo_data_final.send_keys(data_final)
    time.sleep(2)

    start_date_filter = wait.until(EC.element_to_be_clickable((By.ID, "filter_sender")))
    start_date_filter.click()

def acessar_cte(driver):
    wait = WebDriverWait(driver, 20)

    time.sleep(4)
    menu_emissao = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Emissão de Notas']")))
    menu_emissao.click()

    time.sleep(4)
    cte_opcao = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//a[contains(text(), 'Conhecimento de Transporte (Cte)')]"
    )))
    cte_opcao.click()


