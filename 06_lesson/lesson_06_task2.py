from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# думаю, что для этого задания использование любого ожидания избыточно, но
# для практики сюда может подойти явное ожидание

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('http://uitestingplayground.com/textinput')

wait = WebDriverWait(driver, 10)
input_field = wait.until(
    EC.presence_of_element_located((By.ID, 'newButtonName'))
)

input_field.send_keys('SkyPro')

button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,'#updatingButton'))
)
button.click()
print(button.text)

driver.quit()