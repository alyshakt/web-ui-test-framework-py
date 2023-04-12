"""Initializes the webdriver and gets webelements. This util is to make sure that there's not a ton of repeated
extensive code to access webelements"""
import logging
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from tests import conftest

# Define the default wait factor. I like doing between ~30-45 seconds especially to allow for page loading
default_wait = 45


def wait_for_seconds(seconds_to_wait=5):
    """Hard sleep if absolutely needed. Defaults to 5 seconds"""
    logging.debug('Waiting for {} seconds...'.format(seconds_to_wait))
    time.sleep(seconds_to_wait)


class DriverInitialization(object):
    """Initializes the driver for use on all other pages and defines objects that are on almost every page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


class BaseLocators(DriverInitialization):
    """Initializes the driver for use on all other pages and defines objects that are on almost every page.
    The following functions automatically search for an element by a given type of locator, with a wait for visibility
    These methods have 2 different outputs:
    1) The element itself if it is found, or
    2) The boolean value of False if it is not found. This is particularly helpful in asserting that an element exists.

    Each function allows for an explicit max wait time to be passed through as some elements may need extra care for
    loading
    """

    """Single Element Returned"""

    def element_by_name(self, identifier, wait_time=default_wait):
        findby = By.NAME
        driver = self.driver
        return get_single_element(driver, findby, identifier, wait_time)

    def element_by_id(self, identifier, wait_time=default_wait):
        findby = By.ID
        driver = self.driver
        return get_single_element(driver, findby, identifier, wait_time)

    def element_by_xpath(self, identifier, wait_time=default_wait):
        findby = By.XPATH
        driver = self.driver
        return get_single_element(driver, findby, identifier, wait_time)

    def element_by_css(self, identifier, wait_time=default_wait):
        findby = By.CSS_SELECTOR
        driver = self.driver
        return get_single_element(driver, findby, identifier, wait_time)

    def element_by_classname(self, identifier, wait_time=default_wait):
        findby = By.CLASS_NAME
        driver = self.driver
        return get_single_element(driver, findby, identifier, wait_time)

    def element_by_xpath_text(self, text_to_find, tag='*', wait_time=default_wait):
        findby = By.XPATH
        timeout = conftest.get_timeout_timestamp(wait_time)
        el = None
        try:
            el = self.driver.find_element(findby, './/{}[contains(text(),"{}")]'.format(tag, text_to_find))
            logging.debug(msg='Using {} to find {} by containing text {}'.format(findby, tag, text_to_find))
            logging.debug(msg='Does the element exist right now? {}'.format(bool(el)))
        except NoSuchElementException:
            while bool(el) is False and time.perf_counter() < timeout:
                wait_for_seconds(2)
                logging.debug(msg='Element was not found. Trying to find it again...')
                wait_for_seconds(2)
                try:
                    el = self.driver.find_element(findby, './/{}[contains(text(),"{}")]'.format(tag, text_to_find))
                    logging.debug(msg='We found the element? {}'.format(bool(el)))
                    if bool(el):
                        el = self.driver.find_element(findby, './/{}[contains(text(),"{}")]'.format(tag, text_to_find))
                        break
                except NoSuchElementException:
                    el = False
                    logging.debug(msg='Waiting for the element...')
        finally:
            logging.debug(msg='Element found: {}'.format(bool(el)))
        return el

    """Element Lists / Multiple Elements Returned"""

    def elements_by_name(self, identifier, wait_time=default_wait):
        findby = By.NAME
        driver = self.driver
        return get_element_list(driver, findby, identifier, wait_time)

    def elements_by_xpath(self, identifier, wait_time=default_wait):
        findby = By.XPATH
        driver = self.driver
        return get_element_list(driver, findby, identifier, wait_time)

    def elements_by_css(self, identifier, wait_time=default_wait):
        findby = By.CSS_SELECTOR
        driver = self.driver
        return get_element_list(driver, findby, identifier, wait_time)

    def elements_by_classname(self, identifier, wait_time=default_wait):
        findby = By.CLASS_NAME
        driver = self.driver
        return get_element_list(driver, findby, identifier, wait_time)

    def elements_by_id(self, identifier, wait_time=default_wait):
        findby = By.ID
        driver = self.driver
        return get_element_list(driver, findby, identifier, wait_time)

    def elements_by_xpath_text(self, text_to_find, tag='*', wait_time=default_wait):
        findby = By.XPATH
        timeout = conftest.get_timeout_timestamp(wait_time)
        el_list = None
        try:
            el_list = self.driver.find_elements(findby, './/{}[contains(text(),"{}")]'.format(tag, text_to_find))
            logging.debug(msg='Using {} to find {} by containing text {}'.format(findby, tag, text_to_find))
            logging.debug(msg='Does the element exist right now? {}'.format(bool(el_list)))
        except NoSuchElementException:
            while bool(el_list) is False and time.perf_counter() < timeout:
                wait_for_seconds(2)
                logging.debug(msg='Element was not found. Trying to find it again...')
                wait_for_seconds(2)
                try:
                    el_list = self.driver.find_elements(findby,
                                                        './/{}[contains(text(),"{}")]'.format(tag, text_to_find))
                    logging.debug(msg='We found the element? {}'.format(bool(el_list)))
                    if bool(el_list):
                        el_list = self.driver.find_elements(findby,
                                                            './/{}[contains(text(),"{}")]'.format(tag, text_to_find))
                        break
                except NoSuchElementException:
                    el_list = False
                    logging.debug(msg='Waiting for the element...')
        finally:
            logging.debug(msg='Element found: {}'.format(bool(el_list)))
        return el_list

    """Nested Element and Element Lists"""

    def nested_element_by_css(self, element, identifier, wait_time=default_wait):
        findby = By.CSS_SELECTOR
        driver = self.driver
        return get_nested_element(driver, findby, element, identifier, wait_time)

    def nested_elements_by_css(self, element, identifier, wait_time=default_wait):
        findby = By.CSS_SELECTOR
        driver = self.driver
        return get_nested_elements(driver, findby, element, identifier, wait_time)

    def nested_element_by_xpath(self, element, identifier, wait_time=default_wait):
        findby = By.XPATH
        driver = self.driver
        return get_nested_element(driver, findby, element, identifier, wait_time)

    def nested_elements_by_xpath(self, element, identifier, wait_time=default_wait):
        findby = By.XPATH
        driver = self.driver
        return get_nested_elements(driver, findby, element, identifier, wait_time)

    def nested_element_by_id(self, element, identifier, wait_time=default_wait):
        findby = By.ID
        driver = self.driver
        return get_nested_element(driver, findby, element, identifier, wait_time)

    def nested_elements_by_id(self, element, identifier, wait_time=default_wait):
        findby = By.ID
        driver = self.driver
        return get_nested_elements(driver, findby, element, identifier, wait_time)

    def nested_elements_by_classname(self, element, identifier, wait_time=default_wait):
        findby = By.CLASS_NAME
        driver = self.driver
        return get_nested_elements(driver, findby, element, identifier, wait_time)


"""Functions used to handle the driver timeout and exceptions"""


def get_single_element(driver, findby, identifier, wait_time=default_wait):
    timeout = conftest.get_timeout_timestamp(wait_time)
    el = None
    try:
        el = driver.find_element(findby, identifier)
        logging.debug(msg='Using {} to find identifier {}'.format(findby, identifier))
        logging.debug(msg='Does the element exist right now? {}'.format(bool(el)))
    except NoSuchElementException:
        while bool(el) is False and time.perf_counter() < timeout:
            wait_for_seconds(2)
            logging.debug(msg='Element was not found. Trying to find it again...')
            wait_for_seconds(2)
            try:
                el = driver.find_element(findby, identifier)
                logging.debug(msg='We found the element? {}'.format(bool(el)))
                if bool(el):
                    el = driver.find_element(findby, identifier)
                    break
            except NoSuchElementException:
                el = False
                logging.debug(msg='Waiting for the element...')
    finally:
        logging.debug(msg='Element found: {}'.format(bool(el)))
    return el


def get_element_list(driver, findby, identifier, wait_time=default_wait):
    timeout = conftest.get_timeout_timestamp(wait_time)
    el_list = None
    try:
        el_list = driver.find_elements(findby, identifier)
        logging.debug(msg='Using {} to find identifier {}'.format(findby, identifier))
        logging.debug(msg='Do the elements exist right now? {}'.format(bool(el_list)))
    except NoSuchElementException:
        while bool(el_list) is False and time.perf_counter() < timeout:
            wait_for_seconds(2)
            logging.debug(msg='Elements were not found. Trying to find them again...')
            wait_for_seconds(2)
            try:
                el_list = driver.find_elements(findby, identifier)
                logging.debug(msg='We found the elements? {}'.format(bool(el_list)))
                if bool(el_list):
                    el_list = driver.find_elements(findby, identifier)
                    break
            except NoSuchElementException:
                el_list = False
                logging.debug(msg='Waiting for the element...')
    finally:
        logging.debug(msg='Elements found: {}'.format(bool(el_list)))
    return el_list


def get_nested_element(driver, findby, element, identifier, wait_time=default_wait):
    timeout = conftest.get_timeout_timestamp(wait_time)
    el = None
    try:
        el = element.find_element(findby, identifier)
        logging.debug(msg='Using {} to find identifier {}'.format(findby, identifier))
        logging.debug(msg='Does the element exist right now? {}'.format(bool(el)))
    except NoSuchElementException:
        while bool(el) is False and time.perf_counter() < timeout:
            wait_for_seconds(2)
            logging.debug(msg='Element was not found. Trying to find it again...')
            wait_for_seconds(2)
            try:
                el = element.find_element(findby, identifier)
                logging.debug(msg='We found the element? {}'.format(bool(el)))
                if bool(el):
                    el = element.find_element(findby, identifier)
                    break
            except NoSuchElementException:
                el = False
                logging.debug(msg='Waiting for the element...')
    finally:
        logging.debug(msg='Element found: {}'.format(bool(el)))
    return el


def get_nested_elements(driver, findby, element, identifier, wait_time=default_wait):
    timeout = conftest.get_timeout_timestamp(wait_time)
    el_list = None
    try:
        el_list = element.find_elements(findby, identifier)
        logging.debug(msg='Using {} to find identifier {}'.format(findby, identifier))
        logging.debug(msg='Do the elements exist right now? {}'.format(bool(el_list)))
    except NoSuchElementException:
        while bool(el_list) is False and time.perf_counter() < timeout:
            wait_for_seconds(2)
            logging.debug(msg='Elements were not found. Trying to find them again...')
            wait_for_seconds(2)
            try:
                el_list = element.find_elements(findby, identifier)
                logging.debug(msg='We found the elements? {}'.format(bool(el_list)))
                if bool(el_list):
                    el_list = element.find_elements(findby, identifier)
                    break
            except NoSuchElementException:
                el_list = False
                logging.debug(msg='Waiting for the element...')
    finally:
        logging.debug(msg='Elements found: {}'.format(bool(el_list)))
    return el_list


def select_from_dropdown(driver, drpdwn_id, optionparent_id, options_classname, list_option):
    logging.debug(msg='Trying to select option: {} for {}'.format(list_option, drpdwn_id))
    drpdwn = get_single_element(driver, By.ID, drpdwn_id)
    drpdwn.click()
    logging.debug(msg='Checking for dropdown options')
    option_table = get_single_element(driver, By.ID, optionparent_id)
    drpdwn_ops = get_nested_elements(driver, By.CLASS_NAME, option_table, options_classname)
    for item in drpdwn_ops:
        option_text = item.text
        logging.debug(
            msg='There are {} options in the list. Option {}: {}'.format(len(drpdwn_ops), drpdwn_ops.index(item),
                                                                         option_text))
        if list_option.lower() == option_text.lower():
            logging.debug(msg='Found option: {} for {}'.format(option_text, drpdwn_id))
            item.click()
            break