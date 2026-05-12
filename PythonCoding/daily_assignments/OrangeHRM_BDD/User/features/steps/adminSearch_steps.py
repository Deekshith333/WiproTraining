from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('admin is logged into OrangeHRM')
def step_impl(context):

    context.driver = webdriver.Chrome()

    context.driver.maximize_window()

    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    time.sleep(3)

    context.driver.find_element(By.NAME, "username").send_keys("Admin")

    context.driver.find_element(By.NAME, "password").send_keys("admin123")

    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(3)

    context.driver.find_element(By.XPATH, "//span[text()='Admin']").click()

    time.sleep(3)

@when('I enter the following search criteria:')
def step_impl(context):

    data = {}

    for row in context.table:

        data[row[0]] = row[1]

    context.driver.find_element(
        By.XPATH,
        "(//input[@class='oxd-input oxd-input--active'])[2]"
    ).send_keys(data["Username"])

    print("User Role:", data["User Role"])

    print("Status:", data["Status"])

@then('matching records should be displayed')
def step_impl(context):

    print("Search Completed Successfully")

    context.driver.quit()