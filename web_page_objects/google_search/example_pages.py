"""Created October 17th, 2020 by Alysha Kester-Terry https://github.com/alyshakt
"""
import logging

import pytest
from selenium.webdriver import ActionChains

from web_page_objects import screenshot_util, LocatorsUtil
from web_page_objects.google_search.example_locators import GoogleSearchPageLocators


class BasePage(object):
    """Base class to initialize the page class that will be called from all pages"""

    """Base page class to initialize the page class that will be called from all pages"""

    def __init__(self, driver):
        """Initialize the driver"""
        self.driver = driver

    # Functional/Interaction with Page Elements
    def enter_text(self, element, text_to_enter):
        """Enter text into an element"""
        element.clear()
        element.send_keys(text_to_enter)

    def get_element_text(self, element):
        """Get an element's text"""
        return_text = element.text
        logging.debug('Element text: {}'.format(return_text))
        return return_text

    def scroll_to_element(self, element):
        """Click an element by a defined locator"""
        coordinates = element.location_once_scrolled_into_view  # returns dict of X, Y coordinates
        self.driver.execute_script('window.scrollTo({}, {});'.format(
            coordinates['x'], coordinates['y']))
        self.wait_for_seconds(3)

    def scroll_down_page(self):
        self.driver.execute_script('window.scrollBy(0,350)')

    def get_tabs(self):
        logging.debug(msg="Parent window title: " + self.driver.title)
        # get current window handle
        parent_handle = self.driver.current_window_handle
        child_handles = None
        try:
            # from https://www.browserstack.com/guide/how-to-switch-tabs-in-selenium-python

            # get first child window
            child_handles = self.driver.window_handles
        except (BaseException, Exception) as n:
            logging.debug('An exception occurred: {}'.format(n), True)
        return parent_handle, child_handles

    def close_child_tabs(self):
        parent, children = self.get_tabs()
        for child in children:
            if child != parent:
                self.driver.switch_to.window(child)
                self.driver.close()
        self.driver.switch_to.window(parent)

    def switch_tab(self):
        parent, children = self.get_tabs()
        for child in children:
            if child != parent:
                self.driver.switch_to.window(child)
                break
        self.wait_for_seconds(5)

    def click_element(self, element):
        """Click an element"""
        try:
            element.click()
        except (Exception, BaseException) as exc_a:
            try:
                element.click()
            except (Exception, BaseException) as exc_b:
                logging.debug(msg='Could not click on the element {}, {}'.format(exc_a, exc_b))
                ActionChains(self.driver).click(element)
        self.wait_for_seconds(3)

    def screenshot(self, environment=None, name=None):
        if environment is None:
            screenshot_util.debug_screenshot(self.driver, name)
        else:
            screenshot_util.take_screenshot(self.driver, environment, name)

    def get_page_src_info(self):
        source_hierarchy = self.driver.page_source
        return str(source_hierarchy)

    def navigate_back(self):
        self.driver.back()

    def wait_for_seconds(self, secs):
        LocatorsUtil.wait_for_seconds(secs)

    def refresh_screen(self):
        self.driver.refresh()

    def take_pass_fail_screenshots(self, environment, failure, test_name=None):
        logging.info(msg='Failures if any: {}'.format(str(failure)))
        if failure is not None:
            self.screenshot(environment, '{} FAILED'.format(test_name))
            logging.debug(
                msg='The workflow failures if any are: {}'.format(failure),
                exc_info=True)
        else:
            self.screenshot(environment, '{} PASSED'.format(test_name))
            logging.info('PASSED')

    def prep_failures(self, fails_list, exception_error):
        # Add the list of failures to the failures list
        fails_list.append(str(exception_error))
        # Get all the failure text
        fail_text = ';'.join(fails_list)
        # Log the output for humans
        logging.warning(msg='A failure is logged: {}'.format(str(fail_text)), exc_info=True)
        return fail_text

    def tear_down(self, environment, failure=None, test_number=None, get_src=False):
        self.take_pass_fail_screenshots(environment, failure=failure, test_name=test_number)
        if get_src:
            logging.debug(self.get_page_src_info())
        logging.info(msg='Shutting down the driver...')
        self.driver.quit()
        if failure is not None:
            pytest.fail(msg='The test failed. {}'.format(str(failure)))
        logging.basicConfig(level=logging.DEBUG,
                            format=('%(filename)s: '
                                    '%(levelname)s: '
                                    '%(funcName)s(): '
                                    '%(lineno)d:\t'
                                    '%(message)s')
                            )


class GoogleSearchPage(BasePage):
    """Main Search Page Action Methods"""

    def wait_for_load_complete(self):
        """Wait until the page is loaded"""
        return bool(GoogleSearchPageLocators.search_input(self))

    def enter_search_text(self, text):
        search_bar = GoogleSearchPageLocators.search_input(self)
        self.enter_text(search_bar, text)

    def get_results_list(self):
        """Get a list of all the results"""
        if GoogleSearchPageLocators.results_section(self):
            options = GoogleSearchPageLocators.results_text(self)
            results_list = list()
            for option in options:
                option_text = self.get_element_text(option)
                results_list.append(option_text)
            return results_list
