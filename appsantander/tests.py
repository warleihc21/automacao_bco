from time import sleep
from django.test import TestCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pyautogui
from anticaptchaofficial.recaptchav2proxyless import *


servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get('https://www.parceirosantander.com.br/')
sleep(5)
navegador.find_element('xpath', '/html/body/fve-root/fve-access-area/main/section/fve-login/form/div[2]/div/button').click()
sleep(3)

# Obter o identificador da guia original
guia_original = navegador.current_window_handle

# Trocar para a nova guia
if len(navegador.window_handles) > 1:
    navegador.switch_to.window(navegador.window_handles[1])
else:
    print("Não foi possível trocar para a nova guia")

sleep(3)

pyautogui.typewrite("151.016.836-20")
sleep(1)
pyautogui.press('TAB')
sleep(1)
pyautogui.typewrite("Cfp@2023")
sleep(1)
pyautogui.press('enter')

sleep(20)

# Retornar à guia original
navegador.switch_to.window(guia_original)


navegador.find_element('xpath', '/html/body/fve-root/fve-logged-area/main/fve-mfe-home-element/fve-products/div/div/dss-product-card[1]/div/div/dss-product-card-content/button').click()
sleep(10)

pyautogui.press('TAB')
sleep(1)
pyautogui.typewrite("Benedito Anthony Viana")
sleep(1)
pyautogui.press('TAB')
sleep(1)
pyautogui.typewrite("072.290.928-41")
sleep(1)
pyautogui.press('TAB')
sleep(1)
pyautogui.typewrite("31996955552")
sleep(1)
pyautogui.press('enter')
sleep(5)
navegador.find_element('xpath', '//*[@id="scroll"]/div[2]/div/button').click()
sleep(10)
pyautogui.press('TAB')
sleep(1)
pyautogui.press('TAB')
sleep(1)
pyautogui.typewrite("benedito-viana74@oerlikon.com")
sleep(1)
navegador.find_element('xpath', '/html/body/fve-root/fve-logged-area/main/fve-mfe-recommendation-element/fve-notification/fveui-form-navigation/footer/button[2]').click()
sleep(10)


solver = recaptchaV2Proxyless()
solver.set_verbose(1)
solver.set_key('cf9a5e8bd1c48e29eaa7d6c406161789')
solver.set_website_url("https://www.parceirosantander.com.br/spa-base/logged-area/recommendation/confirmation")
solver.set_website_key('6LdyED0UAAAAAA7dlfCxE0zEMtpnq9u5mw1Wpx-a')

resposta = solver.solve_and_return_solution()

if resposta != 0:
    print(resposta)
    # preencher o campo do token do captcha
    # g-recaptcha-response
    navegador.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{resposta}'")
    navegador.find_element('xpath', '/html/body/fve-root/fve-logged-area/main/fve-mfe-recommendation-element/fve-confirmation/fveui-form-navigation/footer/button[2]').click()
else:
    print(solver.err_string)

time.sleep(100)



sleep(20)





