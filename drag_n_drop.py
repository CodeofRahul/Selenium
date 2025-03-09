import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# ActionChains: A class in Selenium that allows you to create complex user interactions, such as mouse movements, clicks, drag-and-drop, and keyboard actions

browser = webdriver.Chrome()
url = 'https://the-internet.herokuapp.com/drag_and_drop'
browser.get(url)
source_element = browser.find_element(By.ID, value='column-a')
destination_element = browser.find_element(By.ID, value='column-b')
actions = ActionChains(browser)
actions.drag_and_drop(source_element,destination_element).perform()
time.sleep(5)
browser.quit()
