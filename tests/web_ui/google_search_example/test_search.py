"""Created October 17th, 2020 by Alysha Kester-Terry https://github.com/alyshakt"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from setup_helpers import screenshots, web_app_setup
from setup_helpers.SearchEngineType import SearchEngineType
from web_page_objects.google_search import example_pages
from web_page_objects.google_search.example_locators import GoogleSearchPageLocators


def test_search_google(record_xml_attribute):
	"""Example test for using a search engine to look up a phrase and verify
	that one part of the phrase exists in all top results
	"""
	record_xml_attribute(
		'name', 'Example Web UI Python Test: Search Google for a term and verify results contain search terms.')
	# Setup Driver, define options
	options = FirefoxOptions()
	options.add_argument('-headless')
	options.add_argument("-window-size=1366,768")
	driver = webdriver.Firefox(options=options)

	# Define the SearchEngineType and the page object
	web_app_setup.navigate_to_search_engine(driver, SearchEngineType.google)
	search_page = example_pages.GoogleSearchPage(driver)

	# I recommend beginning with a try-catch-finally format
	try:
		# Expect some lag time for a page to load
		search_page.wait_for_load_complete()
		# Take a screenshot
		screenshots.take_screenshot(driver, 'step1')
		search_term = 'Lloyd Miller at the Ends of the World'
		# Enter text into the search input field
		search_page.enter_text(GoogleSearchPageLocators.SEARCH_INPUT, search_term+Keys.RETURN)
		screenshots.take_screenshot(driver, 'step2')
		# Get a results list and iterate through it looking for your search terms
		list_text_results = search_page.get_results_list()
		result_count = len(list_text_results)
		print('There are {}'.format(result_count) + ' results found.')
		screenshots.take_screenshot(driver, 'step3')
		assert result_count > 0
		for result in list_text_results:
			result_text = result.lower()
			print('This result says: {}'.format(result_text))
			assert 'lloyd miller' in result_text
	except AssertionError as failure:
		# If any assertions above fail, then mark the test as failed and capture a screenshot
		pytest.fail('The test failed. {}'.format(failure), True)
		screenshots.take_screenshot(driver, 'Failed')
	finally:
		# Finally, quit the webdriver!
		driver.quit()
