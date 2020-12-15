from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from page_objects.google_search.example_locators import GoogleSearchPageLocators
"""Created October 17th, 2020 by Alysha Kester-Terry https://github.com/alyshakt
"""

class BasePage(object):
	"""Base class to initialize the page class that will be called from all pages"""

	def __init__(self, driver):
		self.driver = driver

	# Expected Conditions
	def wait_for_element_visibility(self, by_locator, timeout=10):
		WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))

	def wait_for_element_invisibility(self, by_locator, timeout=10):
		WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element(by_locator))

	# Functional/Interaction with Page Elements
	def enter_text(self, by_locator, text_to_enter):
		self.wait_for_element_visibility(by_locator)
		element = self.driver.find_element(*by_locator)
		element.clear()
		element.send_keys(text_to_enter)

	def get_element_text(self, by_locator):
		self.wait_for_element_visibility(by_locator)
		element = self.driver.find_element(*by_locator)
		return element.text

	def click_element(self, by_locator):
		self.wait_for_element_visibility(by_locator)
		element = self.driver.find_element(*by_locator)
		element.click()


class GoogleSearchPage(BasePage):
	"""Main Search Page Action Methods"""

	def wait_for_load_complete(self):
		self.wait_for_element_visibility(GoogleSearchPageLocators.SEARCH_INPUT)

	def get_results_list(self):
		self.wait_for_element_visibility(GoogleSearchPageLocators.RESULTS_SECTION)
		options = self.driver.find_elements(*GoogleSearchPageLocators.RESULTS_TEXT)
		results_list = list()
		for option in options:
			results_list.append(option.text)
		return results_list
