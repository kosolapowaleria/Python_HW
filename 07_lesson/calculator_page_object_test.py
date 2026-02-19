import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CalculatorPage import CalculatorPage


@pytest.fixture()
def driver():
  driver = webdriver.Chrome()
  driver.maximize_window()
  driver.get(
      'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'
  )
  yield driver
  driver.quit()

def test_slow_calculator(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.fill_delay_input('45')
    calculator_page.enter_expressions('7+8')
    calculator_page.calculate_result()
    WebDriverWait(driver, 60).until(
        EC.text_to_be_present_in_element(
            calculator_page._result_display, '15')
    )
    result = calculator_page.get_result()
    assert result == '15'