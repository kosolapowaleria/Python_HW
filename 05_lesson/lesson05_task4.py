from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.implicitly_wait(5)

driver.get('http://the-internet.herokuapp.com/login')

login_input = driver.find_element(By.CSS_SELECTOR, '#username')
login_input.send_keys('tomsmith')

password_input = driver.find_element(By.CSS_SELECTOR,'#password')
password_input.send_keys('SuperSecretPassword!')

button_login = driver.find_element(By.CSS_SELECTOR,'button.radius')
button_login.click()

wait = WebDriverWait(driver, 10)
message_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#flash')))
print(message_element.text)

driver.quit()