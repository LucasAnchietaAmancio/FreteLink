from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def clicar_botao_proximo(driver):
    wait = WebDriverWait(driver, 15)

    try:
        botao_next = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.next")))
        if "disabled" in botao_next.get_attribute("class"):
            return False  # Última página

        # Armazena os ids atuais
        ids_antes = [linha.get_attribute("data-id") for linha in driver.find_elements(By.CSS_SELECTOR, "tr[data-id]")]

        # Clica com ActionChains
        actions = ActionChains(driver)
        actions.move_to_element(botao_next).click().perform()

        # Aguarda os ids mudarem
        wait.until(lambda d: any(
            linha.get_attribute("data-id") not in ids_antes
            for linha in d.find_elements(By.CSS_SELECTOR, "tr[data-id"])))
        
        return True  # Foi para próxima página
    except Exception as e:
        print(f"⛔ Erro ao clicar em 'Próximo': {e}")
        return False