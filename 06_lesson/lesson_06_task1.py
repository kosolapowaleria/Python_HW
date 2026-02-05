from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# на уроке для такого задания было использовано неявное ожидание, но
# для ajax-запроса лучше использовать явное ожидание

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('http://uitestingplayground.com/ajax')

wait = WebDriverWait(driver,15)

driver.find_element(By.ID,'ajaxButton').click()

message = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR,'p.bg-success'))
)

print(message.text)

driver.quit()