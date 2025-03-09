from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://selenium.dev/")
browser.maximize_window()
title = browser.title       # title is a property
print(title)
assert "Selenium123" in title


