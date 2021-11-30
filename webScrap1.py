#https://www.youtube.com/watch?v=0AvX54Rp4sc

#librerias
#selenium necesita la version correcta de chrome!
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

import time
import pandas as pd

#opciones de navegacion
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
EC=expected_conditions

driver_path = 'C:\\Users\\Marc\\Downloads\\chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options = options)

driver.get('https://www.eltiempo.es')

#se tiene que copiar buttom.(nombre de la clase del objeto al inspeccionar elementos)
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.didomi-components-button didomi-button didomi-dismiss-button didomi-components-button--color didomi-button-highlight highlight-button'.replace(' ','.'))))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#term')))\
    .send_keys('Barcelona')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.nav-link ')))\
    .click()

