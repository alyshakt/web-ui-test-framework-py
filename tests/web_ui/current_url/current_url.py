import logging

from selenium.webdriver.common.keys import Keys

from env_setup import BrowserSetup
from env_setup.App import App
from env_setup.AppSetup import navigate_to_search_engine
from web_page_objects.google_search import example_pages

# Define the App Type
app = App.google
test_num = 'Test Number'


def test_search_google(browser, headless):

    # define your driver
    driver = BrowserSetup.get_driver(browser, headless)

    # return current url
    print(driver.current_url)