from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthorizationPage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_login(self,login):
        login_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        login_field.clear()
        login_field.send_keys(login)

    def enter_password(self,password):
        password_field = self.wait.until(
            EC.element_to_be_clickable((By.ID, "password"))
        )
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        login_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        login_btn.click()

