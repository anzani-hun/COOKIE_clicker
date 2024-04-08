from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://orteil.dashnet.org/cookieclicker")

title = driver.title

def clickBtn(clickable_btn_xpath):
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, clickable_btn_xpath))
    )
    button.click()