from selenium import webdriver

def iniciar_navegador():
    try:
        options = webdriver.FirefoxOptions()
        options.add_argument('--incognito')
        driver = webdriver.Firefox(options=options)
        return driver
    except Exception as e:
        print(f"Erro ao iniciar navegador: {e}")
        return None