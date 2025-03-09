from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome()
url = "https://demo.automationtesting.in/Resizable.html"
browser.get(url)

resizable_element = browser.find_element(By.XPATH, value='//div[@class="ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se"]')
Initial_element_size = browser.find_element(By.XPATH, value='//div[@id="resizable"]')
Initial_size = Initial_element_size.size
print("Initial size is:", Initial_size)
time.sleep(5)
action_chains = ActionChains(browser)
action_chains.click_and_hold(resizable_element).move_by_offset(xoffset=100, yoffset=100).release().perform()
time.sleep(5)
resized_element = Initial_element_size.size
print("Resized Element:", resized_element)
browser.quit()
