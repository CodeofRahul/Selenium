from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set the download directory

download_dir = r"F:\Web-Scrape\Selenium"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name='prefs', value= {
    'download_default_directory' : download_dir
})

driver = webdriver.Chrome(options=chrome_options)

url = "https://demo.automationtesting.in/FileDownload.html"
driver.get(url)
time.sleep(5)
element = driver.find_element(By.XPATH, value="/html/body/section/div[1]/div/div/div[1]/a")
element.click()
time.sleep(30)
driver.quit()
