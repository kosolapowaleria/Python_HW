from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.implicitly_wait(5)

driver.get('http://the-internet.herokuapp.com/inputs')
search_input = driver.find_element(By.CSS_SELECTOR, 'input')

search_input.send_keys('Sky')
sleep(1)

search_input.clear()
sleep(1)

search_input.send_keys('Pro')
sleep(1)

driver.quit()
