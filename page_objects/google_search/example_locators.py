from selenium.webdriver.common.by import By

""" Page object locator strategy gleaned with much gratitude to http://elementalselenium.com/tips/9-use-a-base-page-object"""


class BasePageLocators(object):
	"""Base Page Locators - Elements on EVERY page"""
	EXAMPLE_EL = (By.TAG_NAME, 'p')


class GoogleSearchPageLocators(object):
	"""Google Search Page Locators"""
	RESULTS_SECTION = (By.ID, 'kp-wp-tab-overview')
	RESULTS_TEXT = (By.CLASS_NAME, 'g')
	SEARCH_INPUT = (By.NAME, 'q')
	LOGO = (By.ID, 'hplogo')
