"""Created by Alysha Kester-Terry 05/05/2021"""

from web_page_objects.LocatorsUtil import BaseLocators

default_wait = 45


class BasePageLocators(BaseLocators):
    """Initializes the driver for use on all other pages and defines objects that are on almost every page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

class GoogleSearchPageLocators(object):
    """Google Search Page Locators"""

    def results_section(self):
        return BaseLocators.element_by_id(self, 'kp-wp-tab-overview')

    def search_input(self):
        return BaseLocators.element_by_name(self, 'q')

    def logo(self):
        return BaseLocators.element_by_id(self, 'hplogo')

    def results_text_list(self):
        return BaseLocators.elements_by_classname(self, 'g')
