from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://demoqa.com/buttons')
time.sleep(5)
driver.maximize_window()

actions = ActionChains(driver)

# Double click the button
# double_click_btn = driver.find_element(By.ID, value='doubleClickBtn')
# time.sleep(3)
# driver.execute_script("arguments[0].scrollIntoView();", double_click_btn)
# time.sleep(3)
# actions.double_click(double_click_btn).perform()
# time.sleep(5)

# Right click the button
right_click_btn = driver.find_element(By.ID, value='rightClickBtn')
time.sleep(3)
driver.execute_script("arguments[0].scrollIntoView()", right_click_btn)
actions.context_click(right_click_btn).perform()
time.sleep(5)

