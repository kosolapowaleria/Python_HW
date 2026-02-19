from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self._delay_input = (By.ID, 'delay')
        self._result_display = (By.CSS_SELECTOR, 'div.screen')
        self._equals_button = (
            By.XPATH,
            "//span[text()='=']"
        )

    def fill_delay_input(self, delay):
        input_field = self.wait.until(
            EC.element_to_be_clickable(self._delay_input)
        )
        input_field.clear()
        input_field.send_keys(str(delay))

    def enter_expressions(self, expression):
        for char in expression.strip():
            if char == '0':
                self._press_digit(0)
            elif char == '1':
                self._press_digit(1)
            elif char == '2':
                self._press_digit(2)
            elif char == '3':
                self._press_digit(3)
            elif char == '4':
                self._press_digit(4)
            elif char == '5':
                self._press_digit(5)
            elif char == '6':
                self._press_digit(6)
            elif char == '7':
                self._press_digit(7)
            elif char == '8':
                self._press_digit(8)
            elif char == '9':
                self._press_digit(9)
            elif char == '+':
                self._press_operator('+')
            elif char == '-':
                self._press_operator('-')
            elif char == '*':
                self._press_operator('×')
            elif char == '/':
                self._press_operator('÷')
            elif char == '=':
                self._press_equals()
            elif char.upper() == 'C':
                self._press_clear()
            else:
                raise ValueError(
                    f'Неподдерживаемый символ в выражении: {char}'
                )

    def get_result(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self._result_display)
        )
        return element.text

    def calculate_result(self):
        self._press_equals()

    def _press_digit(self, digit):
        locator = (
            By.XPATH,
            f'//span[text()="{digit}"]'
        )
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def _press_operator(self, symbol):
        locator = (
            By.XPATH,
            f'//span[text()="{symbol}"]'
        )
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def _press_equals(self):
        self.wait.until(
            EC.element_to_be_clickable(self._equals_button)
        ).click()

    def _press_clear(self):
        locator = (
            By.XPATH,
            '//span[text()="C"]'
        )
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()
