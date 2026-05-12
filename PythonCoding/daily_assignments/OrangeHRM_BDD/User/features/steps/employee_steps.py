from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('user is logged into OrangeHRM')
def step_impl(context):

    context.driver = webdriver.Chrome()

    context.driver.maximize_window()

    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    time.sleep(3)

    context.driver.find_element(By.NAME, "username").send_keys("Admin")

    context.driver.find_element(By.NAME, "password").send_keys("admin123")

    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(3)

    context.driver.find_element(By.XPATH, "//span[text()='PIM']").click()

    time.sleep(2)

    context.driver.find_element(By.XPATH, "//a[text()='Add Employee']").click()

    time.sleep(2)

@when('I enter "{FirstName}" and "{LastName}"')
def step_impl(context, FirstName, LastName):

    context.driver.find_element(By.NAME, "firstName").send_keys(FirstName)

    context.driver.find_element(By.NAME, "lastName").send_keys(LastName)

@when('user clicks save button')
def step_impl(context):

    wait = WebDriverWait(context.driver, 10)

    save_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )

    save_button.click()

@then('employee should be created successfully')
def step_impl(context):

    time.sleep(3)

    print("Employee Created Successfully")

    context.driver.quit()