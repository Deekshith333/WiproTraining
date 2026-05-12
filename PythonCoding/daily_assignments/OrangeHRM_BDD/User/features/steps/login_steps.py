from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('user launches OrangeHRM application')
def step_impl(context):

    context.driver = webdriver.Chrome()

    context.driver.maximize_window()

    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    time.sleep(3)

@when('user enters username "{username}" and password "{password}"')
def step_impl(context, username, password):

    context.driver.find_element(By.NAME, "username").send_keys(username)

    context.driver.find_element(By.NAME, "password").send_keys(password)

@when('user clicks login button')
def step_impl(context):

    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(3)

@then('user should navigate to dashboard page')
def step_impl(context):

    current_url = context.driver.current_url

    assert "dashboard" in current_url

    print("Login Successful")

    context.driver.quit()