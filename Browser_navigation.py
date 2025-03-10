from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
browser.get(url)
browser.fullscreen_window()
time.sleep(5)

browser.find_element(By.CSS_SELECTOR, value='#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.orangehrm-login-forgot > p')
time.sleep(3)
browser.back()      # to go backword
time.sleep(5)
browser.forward()   # to go forward
time.sleep(5)
browser.refresh()   # to refresh the page
time.sleep(5)
browser.close()
