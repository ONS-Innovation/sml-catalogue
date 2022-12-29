# Step definitions for help center page

from lib2to3.pgen2 import driver
from urllib.parse import urljoin
import webbrowser
from pytest_bdd import scenario, given, when, then


@scenario('help-center.feature')
def test_publish():
    pass


@given('I\'m an sml portal user')
def navigate_to_url():
    webbrowser.open('http://127.0.0.1:5000')


@when('I am on the help center page')
def navigate_to_url():
    webbrowser.find_element_by_id('title2').click()


@then('The title of the page is "Help center"')
def check_title(title):
    assert title in driver.page_source
