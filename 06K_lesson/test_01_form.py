import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form_validation():
    driver = webdriver.Edge()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.fullscreen_window()
    wait = WebDriverWait(driver, 10)


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



    submit_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-outline-primary"))
        )

    wait.until(EC.visibility_of(submit_button))
    submit_button.click()

    def get_border_color(element):
        return element.value_of_css_property('border-color').lower()

    zip_code = wait.until(
        EC.visibility_of_element_located((By.ID,'zip-code')
        )
    )
    zip_color = get_border_color(zip_code)
    assert zip_color == 'rgb(245, 194, 199)'

    green_fields = [
        'first-name', 'last-name', 'address', 'city', 'country',
        'e-mail', 'phone', 'job-position', 'company'
    ]

    expected_green = 'rgb(186, 219, 204)'

    for field_name in green_fields:
        field = wait.until(EC.visibility_of_element_located((By.ID,field_name)))
        field_color = get_border_color(field)
        assert field_color == expected_green


    driver.quit()