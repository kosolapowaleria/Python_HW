from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def checkout(self, locator=(By.ID, 'checkout')):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        if not element.is_displayed():
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                element
            )
        element.click()

    def get_cart_items(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

        item_containers = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME,'cart_item'))
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

    def is_item_in_cart(self, item_name):
        items = self.get_cart_items()
        for item in items:
            if item['name'] == item_name:
                return True
        return False














