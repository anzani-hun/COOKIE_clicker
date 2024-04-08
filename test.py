from selenium import webdriver
# import time
from selenium.webdriver.common.by import By                         # enum meghívása.. ez kell az XPATHhoz
from selenium.webdriver.support.ui import WebDriverWait             # a kirenderelést megvárja és utána kattint, alul 10sec be van állítva
from selenium.webdriver.support import expected_conditions as EC    # egy elemtől mit várunk el, rá lehessen kattintani

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)          # options a felette lévő két sor azért kell, hogy a böngészőt nyitva hagyja, ne zárja be

driver.get("https://orteil.dashnet.org/cookieclicker/")

title = driver.title
print(title)            # a title kiíratása 

def clickBtn(clickable_btn_xpath):
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, clickable_btn_xpath))
    )
    button.click()

# első gombra kattint automatán: CONSENT
clickBtn("/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]")

# második gombra kattint automatán: ENGLISH nyelv kiválasztása gomb
clickBtn("/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[2]")

title = driver.title
print(title)            # a title kiíratása 

cookies = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'cookies'))
    )
cookies.click()