import logging
import os
import platform

from selenium.webdriver import Edge, Firefox, Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def get_browser_options(browser, headless):
    """ Will set Chrome Options and return Options"""
    logging.info(msg='The browser we are setting up is: {}'.format(str(browser).upper()))
    if 'edge' in browser:
        options = EdgeOptions()
        options.use_chromium = True
    else:
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
    elif 'edge' in browser:
        pathway = None
        op_sys = platform.system().lower()
        logging.info(msg='The OS System is: {}'.format(op_sys))
        base_dir = os.path.abspath('./env_setup/edge_driver')
        if 'windows' in op_sys:
            logging.info(msg='We are on a Windows operating system: {}'.format(op_sys))
            pathway = '{}/{}/msedgedriver.exe'.format(base_dir, 'windows')
        elif 'darwin' in op_sys:
            pathway = '{}/{}/msedgedriver'.format(base_dir, 'mac')
        elif 'linux' in op_sys:
            pathway = '{}/{}/msedgedriver'.format(base_dir, 'linux')
        logging.info(msg='The webdriver location: {}'.format(pathway))
        driver = Edge(executable_path=pathway, capabilities={})
        # .edge_service
    else:
        # Make Firefox default
        driver = Firefox(options=options)
        driver.execute_script("window.onunload = null; window.onbeforeunload=null")
    return driver