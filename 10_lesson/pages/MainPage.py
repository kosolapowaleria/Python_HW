from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:
    """

    Класс для страницы с главной страницей магазина

    Предоставляет методы взаимодействия с элементами главной страницы:

    1. Добавление товаров в корзину.
    2. Переход к просмотру корзины.

    """

    cart_button_selector = 'a.shopping_cart_link'
    """Селектор кнопки корзины — используется для перехода к корзине."""

    def __init__(self, driver):
        """

        Конструктор класса MainPage.

        :param driver: Webdriver — объект драйвера Selenium

        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Добавление товара с ID {item_id} в корзину')
    def add_single_item(self, item_id):
        """

        Добавляет один товар в корзину:

        1. Ожидает, когда кнопка станет кликабельной.
        2. Если элемент не виден на экране, прокручивает к нему страницу.
        3. Выполняет клик по кнопке.

        :param item_id: str — идентификатор товара
        (используется в атрибуте data-test)
        :raises TimeoutException: если кнопка добавления не стала кликабельной
        в течение 10 секунд
        """
        add_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f'[data-test="{item_id}"]')
            )
        )
        if not add_button.is_displayed():
            self.driver.execute_script(
                "arguments.scrollIntoView();", add_button
            )
        add_button.click()

    @allure.step('Добавление нескольких товаров в корзину')
    def add_multiple_items(self, item_ids):
        """

        Добавляет несколько товаров в корзину.

        Для каждого ID товара вызывает метод add_single_item.

        :param item_ids: list[str] — список идентификаторов
        товаров для добавления
        :raises TimeoutException: если какой‑либо из товаров
        не может быть добавлен

        """
        for item_id in item_ids:
            self.add_single_item(item_id)

    @allure.step('Переход в корзину')
    def go_to_cart(self):
        """

        Переходит к просмотру товаров в корзине:

        1. Ожидает, пока кнопка перехода станет кликабельной.
        2. Выполняет клик по кнопке корзины.

        :raises TimeoutException: если кнопка корзины не стала кликабельной
        в течение 10 секунд

        """
        cart_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, MainPage.cart_button_selector)
            )
        )
        cart_button.click()
