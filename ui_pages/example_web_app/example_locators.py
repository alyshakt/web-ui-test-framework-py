from selenium.webdriver.common.by import By


class BasePageLocators(object):
	"""Base Page Locators - Elements on EVERY page"""
	MENU_ITEMS = (By.CSS_SELECTOR, "[data-automation='menuItemLink']")

class GoogleSearchPageLocators(object):
	"""Google Search Page Locators"""
	RESULTS_SECTION = (By.ID, 'kp-wp-tab-overview')
	RESULTS_TEXT = (By.CLASS_NAME, 'g')
	SEARCH_INPUT = (By.NAME, 'q')
	LOGO = (By.ID, 'hplogo')

