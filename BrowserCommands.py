from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()      # ending with () are methods
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, value=".oxd-text.oxd-text--p.orangehrm-login-forgot-header")
time.sleep(5)
driver.back();
time.sleep(5)
driver.forward();
time.sleep(5)
driver.refresh();
driver.close()





while(True):
    pass