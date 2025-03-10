from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.maveryx.com/en/web-testing-of-an-airways-booking-system-the-easyjet-case/')
time.sleep(3)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")     # scroll to down
time.sleep(3)
driver.execute_script("window.scrollTo(0,0);")
time.sleep(3)
driver.find_element(By.LINK_TEXT, value="Contacts").click()
time.sleep(3)
