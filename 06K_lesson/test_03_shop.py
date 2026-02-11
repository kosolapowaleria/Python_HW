from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_online_shop():
    driver = webdriver.Firefox()
    driver.get('https://www.saucedemo.com/')
    wait = WebDriverWait(driver, 10)

    # Авторизация
    wait.until(
        EC.visibility_of_element_located((By.ID, 'user-name'))
    ).send_keys('standard_user')
    wait.until(
        EC.visibility_of_element_located((By.ID, 'password'))
    ).send_keys('secret_sauce')
    wait.until(
        EC.element_to_be_clickable((By.ID, 'login-button'))
    ).click()

    # Добавление товаров в корзину
    wait.until(
        EC.visibility_of_element_located(
            (By.ID, 'add-to-cart-sauce-labs-backpack')
        )
    ).click()
    wait.until(
        EC.visibility_of_element_located(
            (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
        )
    ).click()

    sauce_labs_onesie = wait.until(
        EC.presence_of_element_located(
            (By.ID, 'add-to-cart-sauce-labs-onesie')
        )
    )
    driver.execute_script("arguments[0].scrollIntoView();", sauce_labs_onesie)
    wait.until(
        EC.element_to_be_clickable(
            (By.ID, 'add-to-cart-sauce-labs-onesie')
        )
    ).click()

    # Переход в корзину
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a.shopping_cart_link')
        )
    ).click()

    # Оформление заказа
    checkout = wait.until(
        EC.presence_of_element_located((By.ID, 'checkout'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", checkout)
    wait.until(
        EC.element_to_be_clickable((By.ID, 'checkout'))
    ).click()

    wait.until(
        EC.visibility_of_element_located((By.ID, 'first-name'))
    ).send_keys('Валерия')
    wait.until(
        EC.visibility_of_element_located((By.ID, 'last-name'))
    ).send_keys('Пак')
    wait.until(
        EC.visibility_of_element_located((By.ID, 'postal-code'))
    ).send_keys('350000')
    wait.until(
        EC.element_to_be_clickable((By.ID, 'continue'))
    ).click()

    # Проверка итоговой суммы
    total = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.summary_total_label')
        )
    )
    driver.execute_script("arguments[0].scrollIntoView();", total)
    total_text = total.text
    numeric_value = total_text.replace("Total: ", "").replace("$", "")
    assert numeric_value == '58.29'

    driver.quit()
