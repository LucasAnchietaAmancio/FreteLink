from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from database.data import conectar, inserir_nota
import time

def filter_state_select_cte(driver, log_callback=None,log_text = None):
    wait = WebDriverWait(driver, 20)
    dados = []

    while True:
        time.sleep(2)
        if log_callback:
            log_text("🔍 Coletando página de documentos...")

        try:
            linhas_tr = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tr[data-id]")))
        except:
            if log_callback:
                log_callback("⚠️ Nenhuma linha encontrada.")
            break

        for linha in linhas_tr:
            try:
                status_element = linha.find_element(By.CSS_SELECTOR, "td span")
                if "badge-green" in status_element.get_attribute("class") and status_element.text.strip() == "Autorizada":
                    doc_id = linha.get_attribute("data-id")
                    colunas = linha.find_elements(By.CSS_SELECTOR, "td.grid-data")
                    remetente = colunas[0].text.strip()
                    destinatario = colunas[1].text.strip()
                    numero_data = colunas[2].text.strip()
                    data_emissao = colunas[3].text.strip()
                    valor = colunas[4].text.strip()

                    driver.execute_script("window.open('');")
                    driver.switch_to.window(driver.window_handles[1])
                    driver.get(f"https://emissor2.iob.com.br/notafiscal/ctes/{doc_id}")

                    try:
                        aba_rodoviario = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-element="select-tab"][href="#rodoviario"]')))
                        aba_rodoviario.click()
                        time.sleep(1)
                        codigo_motorista = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#cte_rntrc'))).get_attribute("value")
                    except Exception as e:
                        if log_callback:
                            log_callback(f"❌ Erro ao extrair motorista do ID {doc_id}: {e}")
                        codigo_motorista = ""

                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    time.sleep(1)

                    dados.append({
                        "id_documento": doc_id,
                        "remetente": remetente,
                        "destinatario": destinatario,
                        "numero_data": numero_data,
                        "data_emissao": data_emissao,
                        "valor": valor,
                        "codigo_motorista": codigo_motorista
                    })

            except Exception as e:
                if log_callback:
                    log_callback(f"❌ Erro ao processar linha: {e}")
                continue

        try:
            pagina_atual = driver.find_element(By.ID, "current_page").get_attribute("value")
            driver.execute_script("document.querySelector('ul.navigation a.next').click();")
            WebDriverWait(driver, 10).until(lambda d: d.find_element(By.ID, "current_page").get_attribute("value") != pagina_atual)
        except:
                log_text("📄 Última página atingida ou botão não clicável.")
                break

    conn = conectar()
    for dado in dados:
        try:
            inserir_nota(conn, dado)
        except Exception as e:
            if log_callback:
                print(f"❌ Erro ao inserir no banco: {e}")
    conn.close()

    log_text("💾 Dados inseridos no banco com sucesso.")

    return dados
