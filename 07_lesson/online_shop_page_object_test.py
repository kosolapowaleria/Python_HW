from pages_online_shop.AuthorizationPage import AuthorizationPage
from pages_online_shop.MainPage import MainPage
from pages_online_shop.CartPage import CartPage
from pages_online_shop.OrderPage import OrderPage
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('disable-notifications')
    chrome_options.add_argument("--disable-extensions")
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "safebrowsing.enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(' https://www.saucedemo.com/')
    yield driver
    driver.quit()

def test_online_shop(driver):
    authorization_page = AuthorizationPage(driver)
    authorization_page.enter_login('standard_user')
    authorization_page.enter_password('secret_sauce')
    authorization_page.click_login_button()

    main_page = MainPage(driver)

    items = [
        ('add-to-cart-sauce-labs-backpack'),
        ('add-to-cart-sauce-labs-bolt-t-shirt'),
        ('add-to-cart-sauce-labs-onesie')
    ]
    main_page.add_multiple_items(items)
    main_page.go_to_cart()

    cart_page = CartPage(driver)
    items_to_check = [
        'Sauce Labs Backpack',
        'Sauce Labs Bolt T-Shirt',
        'Sauce Labs Onesie'
    ]

    for item in items_to_check:
        if cart_page.is_item_in_cart(item):
            print(f'{item} — присутствует в корзине')
        else:
            print(f'{item} — отсутствует в корзине')

    cart_page.checkout()

    order_page = OrderPage(driver)
    order_page.fill_personal_info('Валерия', 'Пак', '350000')
    order_page.submit_order()
    total = order_page.get_total_price()

    assert total == '$58.29'




