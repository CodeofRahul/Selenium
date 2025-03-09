from selenium import webdriver
from selenium.webdriver.common.by import By
import time

username = 'admin'
password = 'admin'

driver = webdriver.Chrome()

url = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
driver.get(url=url)
time.sleep(5)


# append the username and password to login : "https://username:password@domain/path"