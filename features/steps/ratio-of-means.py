# Tests for the ratio of means link

import setupSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from behave import *

driver = setupSelenium.driver
host = setupSelenium.local_ip

@given('I\'m an sml portal user trying to get to the ratio of means method')
def auth_user(context):
    WebDriverWait(driver, timeout=10).until(host)

@when('I navigate to the ratio of means page')
def navigate_to_date_adjustment_method(context):
    WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, value='title1')).click()
    WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.LINK_TEXT, value='Ratio of Means')).click()


@then('The title of the ratio of means page is "{title}"')
def check_title(context, title):
    page_title = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.TAG_NAME, "h1")).text
    assert page_title == title
