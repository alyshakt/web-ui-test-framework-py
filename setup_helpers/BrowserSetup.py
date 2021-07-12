import logging
import os
import platform

from selenium.webdriver import Edge, Firefox, Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def get_browser_options(browser, headless):
    """ Will set Chrome Options and return Options"""
    logging.info(msg='The browser we are setting up is: {}'.format(str(browser).upper()))
    if 'chrome' in browser:
        options = Options()
    elif 'firefox' in browser:
        options = FirefoxOptions()
    else:
        options = Options()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--enable-javascript')
    options.add_argument('--disable-extensions')
    if headless == 'true':
        options.add_argument('--headless')
    return options


def get_driver(browser, headless):
    options = get_browser_options(browser, headless)
    if 'chrome' in browser:
        driver = Chrome(options=options)
        driver.set_window_size(1920, 1080)
    elif 'firefox' in browser:
        driver = Firefox(options=options)
        driver.execute_script("window.onunload = null; window.onbeforeunload=null")
    else:
        # Make Firefox default
        driver = Firefox(options=options)
        driver.execute_script("window.onunload = null; window.onbeforeunload=null")
    return driver
