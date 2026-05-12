from behave import *
from selenium.webdriver.common.by import By
import time

@given('user opens My Info page')
def step_impl(context):

    print("Opened My Info Page")

@when('user uploads profile image')
def step_impl(context):

    print("Uploading Image")

@then('profile should update successfully')
def step_impl(context):

    print("Profile Updated")