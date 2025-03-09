from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://the-internet.herokuapp.com/nested_frames")

# Swithing to TOP Frame

browser.switch_to.frame("frame-top")

# Swithching to Middle Frame

browser.switch_to.frame("frame-middle")

content = browser.find_element(By.ID, value='content').text
print("Content in middle frame", content)

# Switch to Default content

browser.switch_to.default_content()

# switch to Bottom Frame

browser.switch_to.frame("frame-bottom")
content_Bottom = browser.find_element(By.TAG_NAME, value="body").text
print("Content in Bottom Frame", content_Bottom)
