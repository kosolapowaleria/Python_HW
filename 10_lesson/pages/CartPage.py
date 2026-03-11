from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartPage:
    """

    Класс для работы со страницей корзины.

    Предоставляет методы взаимодействия с элементами
    корзины:

    1. Просмотр товаров
    2. Проверки наличия товаров
    3. Переход к оформлению заказа

    """

    def __init__(self, driver):
        """

        Конструктор класса CartPage.

        :param driver: Webdriver — объект драйвера Selenium

        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.step('Переход к оформлению заказа')
    def checkout(self):
        """

        Нажимает кнопку оформления заказа:

        1. Ожидает, когда кнопка 'checkout' станет кликабельной.
        2. Если элемент не виден на экране, прокручивает страницу так,
        чтобы он оказался в центре.
        3. Выполняет клик по кнопке.

        :raises TimeoutException: если кнопка не стала кликабельной
         в течение 20 секунд

        """
        element = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'checkout'))
        )
        if not element.is_displayed():
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                element
            )
        element.click()

    @allure.step('Получение списка товаров в корзине')
    def get_cart_items(self):
        """

        Получает список товаров в корзине:

        1. Прокручивает страницу до конца вниз.
        2. Ожидает появление всех контейнеров с товарами
        (по классу 'cart_item').
        3. Для каждого товара извлекает название и цену.
        4. Возвращает список словарей по каждому товару.

        :return: list[dict] — список словарей вида
        {'name': str, 'price': str}
        :raises TimeoutException: если контейнеры с товарами не появились
        в течение 20 секунд

        """
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

        item_containers = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, 'cart_item'))
        )

        items = []
        for container in item_containers:
            name = container.find_element(
                By.CSS_SELECTOR, "[data-test='inventory-item-name']"
            ).text
            price = container.find_element(
                By.CLASS_NAME, 'inventory_item_price'
            ).text

            items.append({
                'name': name,
                'price': price
            })
        return items

    @allure.step('Проверка наличия товара {item_name} в корзине')
    def is_item_in_cart(self, item_name):
        """

        Проверяет наличие указанного товара в корзине

        :param item_name: str — название товара для поиска
        :return: bool — True, если товар найден в корзине, иначе False

        """
        items = self.get_cart_items()
        for item in items:
            if item['name'] == item_name:
                return True
        return False
