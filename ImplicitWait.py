import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
url = 'https://www.saucedemo.com/'
driver.get(url)

driver.find_element(By.ID, value='user-name').send_keys('standard_user')
driver.find_element(By.ID, value='password').send_keys('secret_sauce')
driver.find_element(By.ID, value='login-button').click()        # login

driver.find_element(By.XPATH, value='//*[@id="react-burger-menu-btn"]').click()     # click on menu
driver.find_element(By.XPATH, value='//*[@id="logout_sidebar_link"]').click()       # click on Logout

