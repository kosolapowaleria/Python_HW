from pages.AuthorizationPage import AuthorizationPage
from pages.MainPage import MainPage
from pages.CartPage import CartPage
from pages.OrderPage import OrderPage
import pytest
from selenium import webdriver
import allure


@pytest.fixture()
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('https://www.saucedemo.com/')
    yield driver
    driver.quit()


@allure.title('Полный сценарий покупки в онлайн-магазине')
@allure.description('Покупка: авторизация → корзина → заказ → сумма')
@allure.feature('Полный цикл покупки')
@allure.severity(allure.severity_level.CRITICAL)
def test_online_shop(driver):
    with allure.step('Авторизация в системе'):
        authorization_page = AuthorizationPage(driver)
        authorization_page.enter_login('standard_user')
        authorization_page.enter_password('secret_sauce')
        authorization_page.click_login_button()

    with allure.step('Добавление товаров в корзину'):
        main_page = MainPage(driver)
        items = [
            'add-to-cart-sauce-labs-backpack',
            'add-to-cart-sauce-labs-bolt-t-shirt',
            'add-to-cart-sauce-labs-onesie'
        ]
        main_page.add_multiple_items(items)

    with allure.step('Переход в корзину'):
        main_page.go_to_cart()

    with allure.step('Проверка наличия товаров в корзине'):
        cart_page = CartPage(driver)
        items_to_check = [
            'Sauce Labs Backpack',
            'Sauce Labs Bolt T-Shirt',
            'Sauce Labs Onesie'
        ]

        for item in items_to_check:
            with allure.step(f'Проверка наличия товара: {item}'):
                assert cart_page.is_item_in_cart(item), (
                    f'Товар {item} не найден в корзине'
                )

    with allure.step('Переход к оформлению заказа'):
        cart_page.checkout()

    with allure.step('Заполнение персональных данных'):
        order_page = OrderPage(driver)
        order_page.fill_personal_info(
            'Валерия',
            'Пак',
            '350000')

    with allure.step('Подтверждение заказа'):
        order_page.submit_order()

    with allure.step('Получение и проверка итоговой суммы'):
        total = order_page.get_total_price()

        with allure.step('Проверка корректности суммы заказа'):
            assert total == '$58.29', (
                f'Ожидаемая сумма: $58.29, фактическая: {total}'
            )
