from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = 'https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php'
driver.get(url)
time.sleep(3)

checkbox = driver.find_element(By.ID, value='hobbies')
if not checkbox.is_selected():
    checkbox.click()
    time.sleep(5)
    