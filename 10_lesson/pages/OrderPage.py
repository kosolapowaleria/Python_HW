from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class OrderPage:
    """

    Класс для работы со страницей оформления заказа

    Предоставляет методы взаимодействия с элементами страницы оформления:

    1. Заполнение персональных данных.
    2. Подтверждения заказа.
    3. Получения итоговой суммы.

    """

    def __init__(self, driver):
        """

        Конструктор класс OrderPage.

        :param driver: Webdriver — объект драйвера Selenium

        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step(
        'Заполнение персональных данных '
        '{first_name} {last_name}, {postal_code}'
    )
    def fill_personal_info(self, first_name, last_name, postal_code):
        """

        Заполняет форму с персональными данными для оформления заказа:

        1. Заполняет поле "First name".
        2. Заполняет поле "Last name".
        3. Заполняет поле "Zip/Postal code".

        :param first_name: str — имя покупателя
        :param last_name: str — фамилия покупателя
        :param postal_code: str — почтовый индекс покупателя
        :raises TimeoutException: если какое‑либо поле не стало кликабельным
        в течение 10 секунд.

        """

        first_name_input = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'first-name'))
        )
        first_name_input.clear()
        first_name_input.send_keys(first_name)

        last_name_input = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'last-name'))
        )
        last_name_input.clear()
        last_name_input.send_keys(last_name)

        postal_code_input = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'postal-code'))
        )
        postal_code_input.clear()
        postal_code_input.send_keys(postal_code)

    @allure.step('Подтверждение заказа нажатием кнопки')
    def submit_order(self):
        """

        Подтверждает заказ нажатием кнопки 'Continue':

        1. Ожидает, когда кнопка станет кликабельной.
        2. Если элемент не виден на экране, прокручивает страницу так,
        чтобы элемент оказался в центре.
        3. Выполняет клик по кнопке.

        :raises TimeoutException: если кнопка не стала кликабельной
        в течение 10 секунд.

        """
        continue_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'continue'))
        )
        if not continue_btn.is_displayed():
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                continue_btn
            )
        continue_btn.click()

    @allure.step('Получение итоговой суммы заказа')
    def get_total_price(self):
        """

        Получает итоговую сумму заказа:

        1. Ожидает появление элемента с итоговой суммой.
        2. Извлекает текст элемента.
        3. Обрабатывает текст, выделяя сумму после знака '$'.
        4. Возвращает сумму в формате '$XX.XX'.

        :return: str — итоговая сумма заказа в формате '$XX.XX'
        :raises TimeoutException: если элемент с суммой не появился
        в течение 10 секунд.
        :raises IndexError: если формат текста суммы
        не соответствует ожидаемому.

        """
        total_element = self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'summary_total_label')
            )
        )
        total_text = total_element.text
        total_amount = total_text.split("$")[1]
        return f'${total_amount}'
