"""Created October 17th, 2020 by Alysha Kester-Terry https://github.com/alyshakt"""
import logging

from selenium.webdriver.common.keys import Keys

from env_setup import BrowserSetup
from env_setup.App import App
from env_setup.AppSetup import navigate_to_search_engine
from web_page_objects.google_search import example_pages

# Define the App Type
app = App.google
test_num = 'Test Number'


def test_search_google(environment, browser, headless, record_xml_attribute):
    """Example test for using a search engine to look up a phrase and verify
    that one part of the phrase exists in all top results
    """
    record_xml_attribute(
        'name', 'Example Web UI Python Test: Search Google for a term and verify results contain search terms.')

    # define your driver
    driver = BrowserSetup.get_driver(browser, headless)

    # define your page objects
    base_page = example_pages.BasePage(driver)
    search_page = example_pages.GoogleSearchPage(driver)

    # Set up test failure capture:
    fails = list()
    fail_text = None
    try:
        navigate_to_search_engine(driver=driver, app=app, environment=environment)
        # Expect some lag time for a page to load
        assert search_page.wait_for_load_complete()
        # Take a screenshot
        base_page.screenshot(environment, 'Search Page')
        search_term = 'Lloyd Miller at the Ends of the World'
        # Enter text into the search input field
        search_page.enter_search_text(search_term + Keys.RETURN)
        logging.info(msg='Entering search term: {}'.format(search_term))
        base_page.screenshot(environment, 'Search Term')
        # Get a results list and iterate through it looking for your search terms
        list_text_results = search_page.get_results_list()
        logging.info(msg='The results list is: {}'.format(list_text_results))
        result_count = len(list_text_results)
        print('There are {}'.format(result_count) + ' results found.')
        base_page.screenshot(environment, 'Results')
        assert result_count > 0
        for result in list_text_results:
            result_text = result.lower()
            print('This result says: {}'.format(result_text))
            assert 'lloyd miller' in result_text
    except (AssertionError, Exception, BaseException) as failure:
        fail_text = base_page.prep_failures(fails, exception_error=str(failure))
        logging.warning(msg='There was a failure: {}'.format(fail_text))
    finally:
        base_page.tear_down(environment, failure=fail_text, test_number=test_num)




