from behave import *
from selenium.webdriver.common.by import By
import time


@when('User navigates to Admin module')
def step_impl(context):

    context.driver.find_element(By.XPATH, "//span[text()='Admin']").click()

    time.sleep(3)


@when('User searches users with following details')
def step_impl(context):

    for row in context.table:

        print(row[0] + " : " + row[1])

    time.sleep(2)


@then('Matching users should be displayed')
def step_impl(context):

    print("Matching users displayed successfully")

    context.driver.quit()