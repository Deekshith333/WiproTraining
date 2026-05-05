import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#Start driver
driver = webdriver.Edge()
driver.maximize_window()

driver.get("https://www.elements.dev/selenium/web/web-form.html")
time.sleep(1)


# ---------text input----------
text_input = driver.find_element(By.ID, "my-text-id")
text_input.clear()
text_input.send_keys("Selenium Webdriver Demo")
time.sleep(5)
driver.quit()

#password input
password_input = driver.find_element(By.NAME, "my-password")
password_input.clear()
password_input.send_keys("secret123")

#text area
textarea = driver.find_element(By.NAME, "my-textarea")
textarea.clear()
textarea.send_keys("This is a sample message.")

#Checkbox
checkbox = driver.find_element(By.ID, "my-check-2")
checkbox.click()

#radio button
radio = driver.find_element(By.ID, "my-radio-2")
radio.click()

#dropdown
dropdown = driver.find_element(By.NAME, "my-select")
dropdown.click()
option = driver.find_element(By.CSS_SELECTOR, "select[name='my-select'] option[value='2']")
option.click()

#multi-select
multi_select = driver.find_element(By.NAME, "my-datalist")
multi_select.send_keys('New York')

#File upload
file_upload = driver.find_element(By.NAME, "my-file")
file_upload.send_keys("C:\VnV Training\Selenium\AutomationBasics\selenium_basics")

# range slider
range_slider = driver.find_element(By.NAME, "my_range")
driver.execute_script("arguments[0].value = 10;", range_slider)

#color picker
color_picker = driver.find_element(By.NAME, "my-colors")
color_picker.send_keys("#00ff00") #green

# Date picker
date_input = driver.find_element(By.NAME, "my-date")
date_input.send_keys("2025-12-25")

#submit button
submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
time.sleep(20)
submit_btn.click()

time.sleep(10)
driver.quit()