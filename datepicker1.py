from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta
from selenium.webdriver import Keys         # to interect with keybord


browser = webdriver.Chrome()
url = 'https://www.globalsqa.com/demo-site/datepicker/#Simple%20Date%20Picker'
browser.get(url)

browser.find_element(By.XPATH, value='//div[@class="single_tab_div resp-tab-content resp-tab-content-active"]/div/a').click()
framel0 = browser.find_element(By.XPATH, value='//*[@id="post-2661"]/div[2]/div/div/div[1]/p/iframe')
browser.switch_to.frame(framel0)
time.sleep(5)
browser.find_element(By.CSS_SELECTOR, value='#datepicker').click()

current_date = datetime.now()

next_date = current_date + timedelta(days=2)

formatted_date = next_date.strftime("%m/%d/%y")

browser.find_element(By.CSS_SELECTOR, value='#datepicker').send_keys(formatted_date + Keys.TAB)
time.sleep(5)
browser.quit()




while True:
    pass