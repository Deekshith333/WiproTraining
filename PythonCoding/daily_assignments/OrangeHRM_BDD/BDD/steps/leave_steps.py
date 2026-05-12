from behave import *
from selenium.webdriver.common.by import By
import time


@when('User navigates to Leave module')
def step_impl(context):

    context.driver.find_element(By.XPATH, "//span[text()='Leave']").click()

    time.sleep(3)


@when('User applies for "{leaveType}"')
def step_impl(context, leaveType):

    print("Applying leave type:", leaveType)

    time.sleep(2)


@when('User submits leave request')
def step_impl(context):

    print("Leave request submitted")

    time.sleep(2)


@then('Leave request should be submitted successfully')
def step_impl(context):

    print("Success message displayed")


@then('Leave status should be "{status}"')
def step_impl(context, status):

    print("Leave Status:", status)


@then('Leave balance should be reduced')
def step_impl(context):

    print("Leave balance updated")

    context.driver.quit()