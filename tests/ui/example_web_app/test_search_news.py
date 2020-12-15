import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ui_pages.example_web_app import example_pages
from ui_pages.example_web_app.example_locators import GoogleSearchPageLocators
from ui_setup import web_app_setup, screenshots
from ui_setup.SearchEngineType import SearchEngineType


def test_search_google_news(record_xml_attribute):
	record_xml_attribute(
		"name",
		"Example Web UI Python Test: Search Google for a term in the News category and verify results contain search terms.")
	# Setup Driver, define options
	options = Options()
	options.add_argument('--headless')
	driver = webdriver.Chrome(chrome_options=options)

	# Imports & Pages
	web_app_setup.navigate_to_search_engine(driver, SearchEngineType.google)
	search_page = example_pages.GoogleSearchPage(driver)

	try:
		search_page.wait_for_load_complete()
		screenshots.take_screenshot(driver, 'step1')
		search_term = 'Lloyd Miller at the Ends of the World'
		search_page.enter_text(GoogleSearchPageLocators.SEARCH_INPUT,
		                       search_term + 'Lloyd Miller at the Ends of the World \n')
		screenshots.take_screenshot(driver, 'step2')
		list_text_results = search_page.get_results_list()
		result_count = len(list_text_results)
		print('There are {}'.format(result_count) + ' results found.')
		assert result_count > 0
		for result in list_text_results:
			result_text = result.lower()
			print('This result says: {}'.format(result_text))
			assert 'lloyd miller' in result_text
	except AssertionError as e:
		driver.quit()
		pytest.fail('The test failed. {}'.format(e), True)
	finally:
		driver.quit()
