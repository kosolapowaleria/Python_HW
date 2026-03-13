# нажатие на кнопку с помощью CSS-селектора:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get('http://uitestingplayground.com/classattr')
    wait = WebDriverWait(driver,10)
    blue_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary"))
    )
    blue_button.click()

finally:
    driver.quit()

# поиск по Xpath с явным ожиданием

try:
    driver.get("http://uitestingplayground.com/classattr")

    wait = WebDriverWait(driver, 10)
    button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]"))
    )
    button.click()

finally:
    driver.quit()