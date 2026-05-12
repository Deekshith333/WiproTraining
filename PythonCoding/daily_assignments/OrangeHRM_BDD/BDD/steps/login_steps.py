from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given('User launches OrangeHRM application')
def step_impl(context):

    context.driver = webdriver.Chrome()

    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    context.driver.maximize_window()

    time.sleep(2)


@given('User is on login page')
def step_impl(context):

    print("Login page opened")


@given('User logs in with valid credentials')
def step_impl(context):

    time.sleep(2)

    context.driver.find_element(By.NAME, "username").send_keys("Admin")

    time.sleep(2)

    context.driver.find_element(By.NAME, "password").send_keys("admin123")

    time.sleep(2)

    context.driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    time.sleep(3)

@when('User enters username "{username}"')
def step_impl(context, username):

    context.driver.find_element(By.NAME, "username").send_keys(username)


@when('User enters password "{password}"')
def step_impl(context, password):

    context.driver.find_element(By.NAME, "password").send_keys(password)


@when('User clicks login button')
def step_impl(context):

    context.driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    time.sleep(3)


@then('User should navigate to dashboard')
def step_impl(context):

    print("Dashboard displayed")

    context.driver.quit()


@then('User should see invalid credentials message')
def step_impl(context):

    print("Invalid credentials displayed")

    context.driver.quit()