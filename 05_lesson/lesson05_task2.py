from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get('http://uitestingplayground.com/dynamicid')
    wait = WebDriverWait(driver,10)
    dynamic_id_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn-primary'))
    )
    dynamic_id_button.click()

finally:
    driver.quit()

