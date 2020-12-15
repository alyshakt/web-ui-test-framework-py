from app_page_objects.ios_objects.ios_locators import IosConsumerLoginLocators

"""Created December 15th, 2020 by Alysha Kester-Terry https://github.com/alyshakt
"""


class BasePage(object):
	"""Base class to initialize the page class that will be called from all pages"""

	def __init__(self, driver):
		self.driver = driver

	# Functional/Interaction with Page Elements
	def enter_text(self, by_locator, text_to_enter):
		element = self.driver.find_element(*by_locator)
		element.clear()
		element.send_keys(text_to_enter)

	def get_element_text(self, by_locator):
		element = self.driver.find_element(*by_locator)
		return element.text

	def click_element(self, by_locator):
		element = self.driver.find_element(*by_locator)
		element.click()


class IosLoginPage(BasePage):
	"""Main Search Page Action Methods"""

	def username_field_exists(self):
		return self.driver.find_element(self, IosConsumerLoginLocators.USERNAME_FIELD)

	def wait_for_load_complete(self):
		self.driver.find_element(self, IosConsumerLoginLocators.USERNAME_FIELD)
