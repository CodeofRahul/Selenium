from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
url = "https://the-internet.herokuapp.com/javascript_alerts"
browser.get(url)

# AlertButton = browser.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button')  # to accept the alert
# AlertButton = browser.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')
AlertButton = browser.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button')

AlertButton.click()



alert = browser.switch_to.alert
alert_text = alert.text
print(alert_text)
time.sleep(5)

alert.send_keys('This is Selenium with python tutorial on Handling Alerts')
alert.accept()
# alert.dismiss()
time.sleep(5)



while True:
    pass