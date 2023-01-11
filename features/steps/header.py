# Step definitions for methods catalogue page

import setupSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from behave import *

driver = setupSelenium.driver
host = setupSelenium.local_ip

@given('I\'m an sml portal user on the home page')
def auth_user(context):
    driver.get(host)
    
@when('I click the "{page}" link in the header')
def navigate_to_url(context, page):
    if page == "methods catalogue":
        main_navigation =  WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, value='main-navigation'))
        main_navigation.find_element(By.LINK_TEXT, value='Methods catalogue').click()
    elif page == "help centre":
        main_navigation =  WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, value='main-navigation'))
        main_navigation.find_element(By.LINK_TEXT, value='Help centre').click()


@then('The title of this page is "{title}"')
def check_title(context, title):
    page_title =  WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.TAG_NAME, "h1")).text
    assert page_title == title
