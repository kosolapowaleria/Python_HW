from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    cart_button_selector = 'a.shopping_cart_link'

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_single_item(self, item_id):
        add_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f'[data-test="{item_id}"]'))
        )
        if not add_button.is_displayed():
            self.driver.execute_script("arguments.scrollIntoView();", add_button)
        add_button.click()

    def add_multiple_items(self, item_ids):
        for item_id in item_ids:
            self.add_single_item(item_id)

    def go_to_cart(self):
        cart_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, MainPage.cart_button_selector)
            )
        )
        cart_button.click()