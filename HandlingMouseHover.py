from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
# ActionChains: A class in Selenium that allows you to create complex user interactions, such as mouse movements, clicks, drag-and-drop, and keyboard actions.


browser = webdriver.Chrome()
url = 'https://demo.automationtesting.in/Datepicker.html'
browser.get(url)
browser.find_element(By.XPATH, value='//*[@id="header"]/nav/div/div[2]/ul/li[4]/ul/li[3]/a')

actions = ActionChains(browser)

hover_element = browser.find_element(By.XPATH, value='//*[@id="header"]/nav/div/div[2]/ul/li[4]/a')
time.sleep(5)
actions.move_to_element(hover_element).perform()
browser.find_element(By.XPATH, value='//*[@id="header"]/nav/div/div[2]/ul/li[4]/ul/li[3]/a').click()
time.sleep(5)
