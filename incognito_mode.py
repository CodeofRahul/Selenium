from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Create ChromeOptions object
chrome_options = Options()

# Add the --incognito argument
chrome_options.add_argument("--incognito")

# Create the WebDriver instance
driver = webdriver.Chrome(options=chrome_options)

# maximize the chrome window
driver.maximize_window()
time.sleep(5)

# Navigate to the website
driver.get("https://selenium-python.readthedocs.io/")

time.sleep(5)

# Close the browser
driver.quit()
