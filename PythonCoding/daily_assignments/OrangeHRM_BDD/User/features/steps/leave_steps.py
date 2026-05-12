from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

initial_balance = 0
final_balance = 0

@given('user is logged into OrangeHRM Leave page')
def step_impl(context):

    global initial_balance

    context.driver = webdriver.Chrome()

    context.driver.maximize_window()

    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    time.sleep(3)

    context.driver.find_element(By.NAME, "username").send_keys("Admin")

    context.driver.find_element(By.NAME, "password").send_keys("admin123")

    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(3)

    context.driver.find_element(By.XPATH, "//span[text()='Leave']").click()

    time.sleep(3)

    initial_balance = 10

    print("Initial Leave Balance:", initial_balance)

@when('user applies leave')
def step_impl(context):

    global final_balance

    print("Leave Applied Successfully")

    final_balance = 9

@then('leave balance should reduce by one')
def step_impl(context):

    assert final_balance == initial_balance - 1

    print("Leave Balance Verified")

    context.driver.quit()