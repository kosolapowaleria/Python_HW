from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    driver = webdriver.Edge()
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/data-types.html'
    )
    driver.fullscreen_window()
    wait = WebDriverWait(driver, 10)

    # Заполняем поля формы
    wait.until(
        EC.visibility_of_element_located((By.NAME, 'first-name'))
    ).send_keys('Иван')
    wait.until(
        EC.visibility_of_element_located((By.NAME, 'last-name'))
    ).send_keys('Петров')
    wait.until(
        EC.visibility_of_element_located((By.NAME, 'address'))
    ).send_keys('Ленина, 55-3')
    wait.until(
        EC.visibility_of_element_located((By.NAME, 'city'))
    ).send_keys('Москва')
    wait.until(
        EC.visibility_of_element_located((By.NAME, 'country'))
    ).send_keys('Россия')
    wait.until(
        EC.visibility_of_element_located((By.NAME, 'e-mail'))
    ).send_keys('test@skypro.com')
    wait.until(
        EC.visibility_of_element_located((By.NAME, 'phone'))
    ).send_keys('+7985899998787')
    wait.until(
        EC.visibility_of_element_located((By.NAME, 'job-position'))
    ).send_keys('QA')
    wait.until(
        EC.visibility_of_element_located((By.NAME, 'company'))
    ).send_keys('SkyPro')

    # Нажимаем кнопку отправки
    submit_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             'button.btn-outline-primary')
        )
    )
    wait.until(EC.visibility_of(submit_button))
    submit_button.click()

    # Проверка: Zip code должен быть красным (alert-danger)
    zip_code_alert = wait.until(
        EC.visibility_of_element_located((By.ID, 'zip-code'))
    )
    zip_classes = zip_code_alert.get_attribute('class')
    assert 'alert-danger' in zip_classes

    # Проверка: остальные поля должны быть зелёными (alert-success)
    success_fields = [
        'first-name', 'last-name', 'address', 'city', 'country',
        'e-mail', 'phone', 'job-position', 'company'
    ]
    for field_id in success_fields:
        field_alert = wait.until(
            EC.visibility_of_element_located((By.ID, field_id))
        )
        field_classes = field_alert.get_attribute('class')
        assert 'alert-success' in field_classes

    driver.quit()
