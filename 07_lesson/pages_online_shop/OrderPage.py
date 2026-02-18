from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_personal_info(self, first_name, last_name, postal_code):
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

    def submit_order(self):
        continue_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'continue'))
        )
        if not continue_btn.is_displayed():
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                continue_btn
            )
        continue_btn.click()

    def get_total_price(self):
        total_element = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'summary_total_label'))
        )
        total_text = total_element.text
        total_amount = total_text.split("$")[1]
        return f'${total_amount}'

