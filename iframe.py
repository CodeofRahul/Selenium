
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import time

browser = webdriver.Chrome()
browser.get("https://the-internet.herokuapp.com/iframe")

iframe = browser.find_element(By.ID, value="mce_0_ifr")
browser.switch_to.frame(iframe)

Text_Editor = browser.find_element(By.ID, value="tinymce")
Text_Editor.clear()
Text_Editor.send_keys("This is Selenium with Python Iframe Tutorial")
time.sleep(10)

browser.switch_to.default_content()
selenium_link = browser.find_element(By.XPATH, value='//div[@id="page-footer"]/div/div/a')
selenium_link.click()


if True:
    pass