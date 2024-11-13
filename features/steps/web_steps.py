from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Step 1: Button click step definition
@given('I click the "{button}" button')
def step_impl(context, button):
    button_element = context.driver.find_element(By.XPATH, f"//button[text()='{button}']")
    button_element.click()
    time.sleep(1)

# Step 2: Verifying a specific name or text to be present
@then('I should see the message "{message}"')
def step_impl(context, message):
    assert message in context.driver.page_source

# Step 3: Verifying a specific name or text NOT to be present
@then('I should not see the message "{message}"')
def step_impl(context, message):
    assert message not in context.driver.page_source

# Step 4: Verifying a specific message is present
@then('I should see the product with name "{name}"')
def step_impl(context, name):
    product_name = context.driver.find_element(By.XPATH, f"//h2[contains(text(), '{name}')]")
    assert product_name.is_displayed()

from behave import before_all
from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    context.driver.get('http://localhost:5000')  # Replace with your app URL
