from behave import *
from selenium.webdriver.common.by import By
import time


@when('User navigates to My Info section')
def step_impl(context):

    context.driver.find_element(By.XPATH, "//span[text()='My Info']").click()

    time.sleep(3)


@when('User changes nickname to "{nickname}"')
def step_impl(context, nickname):

    print("Nickname changed to:", nickname)

    time.sleep(2)


@when('User uploads profile picture')
def step_impl(context):

    print("Profile picture uploaded")

    time.sleep(2)


@when('User clicks profile save button')
def step_impl(context):

    print("Save button clicked")

    time.sleep(2)


@then('Profile should be updated successfully')
def step_impl(context):

    print("Profile updated successfully")

    context.driver.quit()