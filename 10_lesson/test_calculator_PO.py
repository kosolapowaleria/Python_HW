import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.CalculatorPage import CalculatorPage
import allure


@pytest.fixture()
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера

    Создаёт экземпляр ChromeDriver, разворачивает окно на весь экран,
    открывает страницу калькулятора и закрывает драйвер после теста.

    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'
    )
    yield driver
    driver.quit()


@allure.title('Тестирование веб‑калькулятора: сложение')
@allure.description('Проверка операции сложения с задержкой 45 сек.')
@allure.feature('Калькулятор')
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator_addition(driver):
    """Тест операции сложения (7 + 8 = 15) с задержкой 45 сек."""
    calculator_page = CalculatorPage(driver)

    with allure.step('Установка задержки вычислений: 45 сек.'):
        calculator_page.fill_delay_input('45')

    with allure.step('Ввод выражения: 7+8'):
        calculator_page.enter_expressions('7+8')

    with allure.step('Выполнение расчёта (нажатие =)'):
        calculator_page.calculate_result()

    with allure.step('Ожидание результата на дисплее'):
        WebDriverWait(driver, 60).until(
            EC.text_to_be_present_in_element(
                calculator_page._result_display, '15'
            )
        )

    with allure.step('Получение и проверка результата'):
        result = calculator_page.get_result()
        assert (result == '15'), (
            f'Ошибка: ожидался результат 15, получен {result}'
        )


@allure.title('Тестирование веб‑калькулятора: умножение')
@allure.description('Проверка операции умножения с задержкой 30 сек.')
@allure.feature('Калькулятор')
@allure.severity(allure.severity_level.NORMAL)
def test_slow_calculator_multiplication(driver):
    """Тест операции умножения (5 × 3 = 15) с задержкой 30 сек."""
    calculator_page = CalculatorPage(driver)

    with allure.step('Установка задержки вычислений: 30 сек.'):
        calculator_page.fill_delay_input('30')

    with allure.step('Ввод выражения: 5*3'):
        calculator_page.enter_expressions('5*3')

    with allure.step('Выполнение расчёта (нажатие =)'):
        calculator_page.calculate_result()

    with allure.step('Ожидание результата на дисплее'):
        WebDriverWait(driver, 60).until(
            EC.text_to_be_present_in_element(
                calculator_page._result_display, '15'
            )
        )

    with allure.step('Получение и проверка результата'):
        result = calculator_page.get_result()
        assert (result == '15'), (
            f'Ошибка: ожидался результат 15, получен {result}'
        )


@allure.title('Тестирование веб‑калькулятора: очистка дисплея')
@allure.description('Проверка функции очистки дисплея кнопкой C')
@allure.feature('Калькулятор')
@allure.severity(allure.severity_level.MINOR)
def test_slow_calculator_clear(driver):
    """Тест функции очистки дисплея (кнопка C)."""
    calculator_page = CalculatorPage(driver)

    with allure.step('Ввод начального выражения: 2+2'):
        calculator_page.enter_expressions('2+2')

    with allure.step('Очистка дисплея (нажатие C)'):
        calculator_page._press_clear()

    with allure.step('Проверка, что дисплей очищен'):
        result = calculator_page.get_result()
        assert result == '', f'Ошибка: дисплей не очищен, значение: {result}'
