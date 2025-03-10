from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = "https://demo.automationtesting.in/FileUpload.html"
driver.get(url=url)

file = driver.find_element(By.ID, value='input-4')
file.send_keys(r"F:\Web-Scrape\Selenium\testdata.pdf")
time.sleep(5)
