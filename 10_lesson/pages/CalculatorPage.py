from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    """
    Класс для работы с веб-калькулятором:

    Предоставляет методы для работы с калькулятором:

    1. Установка задержки вычислений.
    2. Ввод математических выражений.
    3. Получение результатов вычислений.
    4. Выполнение вычислений.

    """

    def __init__(self, driver):
        """

        Конструктор класса CalculatorPage

        :param driver: Webdriver — объект драйвера Selenium

        Атрибуты класса:
        self._delay_input (tuple): локатор поля ввода задержки вычислений
            (By.ID, 'delay').
        self._result_display (tuple): локатор дисплея для отображения
        результата (By.CSS_SELECTOR, 'div.screen').

        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self._delay_input = (By.ID, 'delay')
        self._result_display = (By.CSS_SELECTOR, 'div.screen')
        self._equals_button = (
            By.XPATH,
            "//span[text()='=']"
        )

    @allure.step('Установка задержки {delay} секунд')
    def fill_delay_input(self, delay):
        """

        Заполняет поле задержки для вычислений:

        1. Ожидает кликабельности поля ввода задержки.
        2. Очищает поле.
        3. Вводит значение задержки в секундах.

        :param delay: int — задержка в секундах
        :raises TimeoutException: если поле ввода не стало кликабельным
        в течение 10 секунд
        """

        input_field = self.wait.until(
            EC.element_to_be_clickable(self._delay_input)
        )
        input_field.clear()
        input_field.send_keys(str(delay))

    @allure.step('Ввод выражения {expression}')
    def enter_expressions(self, expression):
        """

        Вводит математическое выражение в калькулятор:

        1. Проходит по каждому символу выражения.
        2. Для цифр вызывает метод _press_digit().
        3. Для операторов вызывает метод _press_operator().
        4. Для '=' вызывает _press_equals().
        5. Для 'C' вызывает _press_clear().
        6. При неподдерживаемом символе выбрасывает исключение.

        :param expression: str — математическое выражение
        :raises ValueError: если символ не поддерживается калькулятором
        :raises TimeoutException: если какая‑либо кнопка не стала кликабельной
        в течение 10 с

        """
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

    @allure.step('Получение результата с дисплея')
    def get_result(self):
        """

        Получает текущий результат с дисплея калькулятора.

        1. Ожидает видимости элемента дисплея.
        2. Извлекает текст элемента.
        3. Возвращает текст результата.

        :return: str — текст с дисплея калькулятора
        :raises TimeoutException: если элемент дисплея не появился
        в течение 10 секунд

        """
        element = self.wait.until(
            EC.visibility_of_element_located(self._result_display)
        )
        return element.text

    @allure.step('Выполнение расчёта(нажатие "="')
    def calculate_result(self):
        """

        Нажимает кнопку «=» для выполнения расчёта.

        1. Ожидает кликабельности кнопки «=».
        2. Выполняет клик по кнопке.

        :raises TimeoutException: если кнопка «=» не стала кликабельным
        в течение 10 секунд

        """
        self._press_equals()

    @allure.step('Нажатие цифры {digit}')
    def _press_digit(self, digit):
        """

        Нажимает кнопку с указанной цифрой.

        1. Формирует локатор для кнопки цифры.
        2. Ожидает кликабельности кнопки.
        3. Выполняет клик.

        :param digit: int — цифра от 0 до 9
        :raises TimeoutException: если кнопка цифры не стала кликабельной
         в течение 10 секунд

        """
        locator = (
            By.XPATH,
            f'//span[text()="{digit}"]'
        )
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    @allure.step('Нажатие оператора {symbol}')
    def _press_operator(self, symbol):
        """

        Нажимает кнопку с указанным оператором.

        1. Формирует локатор для кнопки оператора.
        2. Ожидает кликабельности кнопки.
        3. Выполняет клик.

        :param symbol: str — оператор (+, -, ×, ÷)
        :raises TimeoutException: если кнопка оператора не стала кликабельной
        в течение 10 секунд

        """
        locator = (
            By.XPATH,
            f'//span[text()="{symbol}"]'
        )
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    @allure.step('Нажатие кнопки "="')
    def _press_equals(self):
        """

        Нажимает кнопку "=" для подтверждения расчёта:

        1. Ожидает кликабельности кнопки "=".
        2. Выполняет клик.

        :raises TimeoutException: если кнопка не стала кликабельной
        в течение 10 секунд

        """
        self.wait.until(
            EC.element_to_be_clickable(self._equals_button)
        ).click()

    @allure.step('Очистка дисплея — нажатие на "С"')
    def _press_clear(self):
        """

        Нажимает кнопку отчистки дисплея "С":

        1. Формирует локатор для кнопки "С".
        1. Ожидает кликабельности кнопки.
        2. Выполняет клик.

        :raises TimeoutException: если кнопка не стала кликабельной
        в течение 10 секунд

        """
        locator = (
            By.XPATH,
            '//span[text()="C"]'
        )
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()
