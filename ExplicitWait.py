from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.saucedemo.com/')

driver.find_element(By.ID, value='user-name').send_keys('standard_user')
driver.find_element(By.ID, value='password').send_keys('secret_sauce')
driver.find_element(By.ID, value='login-button').click()        # login

driver.find_element(By.XPATH, value='//*[@id="react-burger-menu-btn"]').click()     # click on menu

element = WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logout_sidebar_link"]')))

element.click()

driver.quit()