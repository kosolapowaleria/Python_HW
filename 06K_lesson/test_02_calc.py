import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_slow_calculator():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    wait = WebDriverWait(driver,60)

    delay_input = wait.until(
        EC.visibility_of_element_located((By.ID,'delay')
        )
    )
    delay_input.clear()
    delay_input.send_keys('45')

    wait.until(
        EC.element_to_be_clickable((By.XPATH,"//span[text()='7']"))
    ).click()
    wait.until(
        EC.element_to_be_clickable((By.XPATH,"//span[text()='+']"))
    ).click()
    wait.until(
        EC.element_to_be_clickable((By.XPATH,"//span[text()='8']"))
    ).click()
    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'span.btn-outline-warning'))
    ).click()


    result = wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR,'div.screen'),'15')
    )
    assert result is True

    driver.quit()

