from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyautogui
from time import sleep


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1000,800', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver

#ACESSANDO O SITE
driver = iniciar_driver()
driver.get('https://membros.devaprender.com/auth/login')
sleep(5)

#ENCONTRANDO CLICANDO E DIGITANDO O LOGIN
campo_login = driver.find_element(By.XPATH,'//*[@id="AcessoEmail"]')
campo_login.click()
sleep(1)
pyautogui.write('#')
sleep(1)

#ENCONTRANDO CLICANDO E DIGITANDO A SENHA
campo_senha = driver.find_element(By.XPATH,'//*[@id="AcessoSenha"]')
campo_senha.click()
sleep(1)
pyautogui.write('#')
sleep(1)

#ENCONTRANDO E CLICANDO NO BOTAO ENTRAR
btn_logar = driver.find_element(By.XPATH,'//*[@id="Form"]/button')
btn_logar.click()
sleep(3)

#FECHAR APLICAÇÃO 
input('')
driver.close()