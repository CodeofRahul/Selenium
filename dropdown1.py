from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
login_url = "https://the-internet.herokuapp.com/dropdown"
driver.get(login_url)

dropdown_element = driver.find_element(By.ID, value="dropdown")
# Select = Select(dropdown_element)
# Select the value by visible text
# Select the value by Index
# Select the option by using a value

# Select.select_by_visible_text("Option 2")
# Select.select_by_index(2)
# Select.select_by_value("2")


# option_count = len(Select.options)

# expected_count = 3

# if option_count == expected_count:
#     print("Test case passed. Count is correct")
# else:
#     print("Test case failed. Count is incorrect")

# while True:
#     pass



target_value = "Option 2"
select = Select(dropdown_element)

for option in select.options:
    if option.text == target_value:
        option.click()
        print(f"Selected Option is {target_value}")
        break
    else:
        print(f"Option '{target_value}' not found")


while True:
    pass