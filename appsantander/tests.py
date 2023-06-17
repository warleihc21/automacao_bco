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

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get('https://www.parceirosantander.com.br/')

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
pyautogui.typewrite("Iago Tomás Fábio Gonçalves")
sleep(1)
pyautogui.press('TAB')
sleep(1)
pyautogui.typewrite("721.869.968-55")
sleep(1)
pyautogui.press('TAB')
sleep(1)
pyautogui.typewrite("(16) 99209-8400")
sleep(1)
pyautogui.press('enter')


sleep(20)






