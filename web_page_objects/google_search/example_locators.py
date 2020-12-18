"""Created October 17th, 2020 by Alysha Kester-Terry https://github.com/alyshakt
    This Base Page object locator strategy was gleaned with much gratitude from
    http://elementalselenium.com/tips/9-use-a-base-page-object
"""

from selenium.webdriver.common.by import By


class BasePageLocators(object):
	"""Base Page Locators - Elements on EVERY page"""
	EXAMPLE_EL = (By.TAG_NAME, 'p')


class GoogleSearchPageLocators(object):
	"""Google Search Page Locators"""
	RESULTS_SECTION = (By.ID, 'kp-wp-tab-overview')
	RESULTS_TEXT = (By.CLASS_NAME, 'g')
	SEARCH_INPUT = (By.NAME, 'q')
	LOGO = (By.ID, 'hplogo')
