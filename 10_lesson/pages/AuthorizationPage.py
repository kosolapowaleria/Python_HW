from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class AuthorizationPage:
    """
    Класс работы со страницей авторизации.

    Предоставляет методы взаимодействия со страницей:
    ввод логина и пароля, нажатие кнопки входа.

    """

    def __init__(self, driver):
        """
        Конструктор класса AuthorizationPage

        :param driver: Webdriver — объект драйвера Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Ввод логина {login}')
    def enter_login(self, login):
        """

        Вводит логин в соответствующее поле:

        1. Ожидает появление (видимость элемента) поля ввода логин.
        2. Очищает поле.
        3. Вводит указанный логин.

        :param login: str — логин пользователя для авторизации
        :raises TimeoutException: если поле логина не появилось
        в течение 10 секунд

        """
        login_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        login_field.clear()
        login_field.send_keys(login)

    @allure.step('Ввод пароля {password}')
    def enter_password(self, password):
        """

        Вводит пароль в соответствующее поле:

        1. Ожидает, пока поле пароля станет кликабельным.
        2. Очищает поле.
        2. Вводит указанный пароль.

        :param password: str - пароль пользователя для авторизации
        :raises TimeoutException: если поле пароля не стало
        кликабельным в течение 10 секунд

        """
        password_field = self.wait.until(
            EC.element_to_be_clickable((By.ID, "password"))
        )
        password_field.clear()
        password_field.send_keys(password)

    @allure.step('Нажатие кнопки входа')
    def click_login_button(self):
        """

        Нажимает кнопку входа на странице авторизации:

        1. Ожидает, когда кнопка станет кликабельной.
        2. Выполняет нажатие на кнопку.
        :raises TimeoutException: если кнопка входа не стала кликабельной
        в течение 10 секунд

        """
        login_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        login_btn.click()
