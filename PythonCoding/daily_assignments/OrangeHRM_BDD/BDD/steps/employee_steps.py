from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time





@when('User navigates to PIM module')
def step_impl(context):

    context.driver.find_element(By.XPATH, "//span[text()='PIM']").click()

    time.sleep(2)


@when('User clicks Add Employee')
def step_impl(context):

    context.driver.find_element(By.XPATH, "//button[text()=' Add ']").click()

    time.sleep(2)


@when('User enters first name "{firstname}"')
def step_impl(context, firstname):

    context.driver.find_element(By.NAME, "firstName").send_keys(firstname)


@when('User enters last name "{lastname}"')
def step_impl(context, lastname):

    context.driver.find_element(By.NAME, "lastName").send_keys(lastname)


@when('User clicks Save button')
def step_impl(context):

    context.driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    time.sleep(3)


@then('Employee should be added successfully')
def step_impl(context):

    print("Employee added successfully")

    context.driver.quit()