from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta



browser = webdriver.Chrome()
url = 'https://demo.automationtesting.in/Datepicker.html'
browser.get(url)
browser.find_element(By.ID, value="datepicker2").click()
time.sleep(5)

current_date = datetime.now()
print(current_date)

next_day = current_date + timedelta(days=1)
print(next_day)
Next_day = (str(next_day.day))
print(Next_day)
current_month = datetime.now().month
current_year = current_date.year

next_month = (current_month % 12) + 1
next_month_year = f"{next_month}/{current_year}"
Month_Dropdown = browser.find_element(By.XPATH, value='/html/body/div[2]/div/div[2]/div/div/select[1]')
select = Select(Month_Dropdown)
select.select_by_value(str(next_month_year))
Year_Dropdown = browser.find_element(By.XPATH, value='/html/body/div[2]/div/div[2]/div/div/select[2]')
select = Select(Year_Dropdown)
select.select_by_visible_text("2024")
browser.find_element(By.LINK_TEXT, Next_day).click()
time.sleep(5)
