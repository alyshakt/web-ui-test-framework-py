"""Created October 17th, 2020 by Alysha Kester-Terry https://github.com/alyshakt"""
import logging

from selenium.webdriver.common.keys import Keys

from env_setup import BrowserSetup
from env_setup.App import App
from env_setup.AppSetup import navigate_to_search_engine
from web_page_objects.google_search import example_pages

# Define the App Type
app = App.mindful_care
print(app)
test_num = 'Test mindful care FAQ page'


def test_faq_page(environment, browser, headless, record_xml_attribute):
    """Test FAQ page , log questions and check the answers"""
    record_xml_attribute(
        'faq page', 'Test FAQ page questions and answers')
    # define your driver
    driver = BrowserSetup.get_driver(browser, headless)
    # define your page objects
    base_page = example_pages.BasePage(driver)
    home_page = example_pages.MindfulCaresHomePage(driver) # Mindful Care Home
    # Set up test failure capture:
    fails = list()
    fail_text = None
    try:
        print(app)
        navigate_to_search_engine(driver=driver, app=app, environment=environment)
        # Expect some lag time for a page to load
        assert home_page.wait_for_load_complete()
        # Take a screenshot
        base_page.screenshot(environment, 'Mindful Care Home Page')
        home_page.scroll_down_page()
        home_page.click_FAQ_link()
        # Take a screenshot
        base_page.screenshot(environment, 'Mindful Care FAQ Page')
        questions_and_answers = home_page.get_questions_and_answers()
        logging.info(msg='The list of questions and answers: {}'.format(questions_and_answers))
        result_count = len(questions_and_answers)
        # Take a screenshot
        base_page.screenshot(environment, 'All FAQ expanded')
        assert result_count > 0
    except (AssertionError, Exception, BaseException) as failure:
        fail_text = base_page.prep_failures(fails, exception_error=str(failure))
        logging.warning(msg='There was a failure: {}'.format(fail_text))
    finally:
        base_page.tear_down(environment, failure=fail_text, test_number=test_num)


def test_psychiatric_services(environment, browser, headless, record_xml_attribute):
    """Test psychiatric_services answer"""
    record_xml_attribute(
        'psychiatric_services', 'Test psychiatric services answer, check age')
    # define your driver
    driver = BrowserSetup.get_driver(browser, headless)
    # define your page objects
    base_page = example_pages.BasePage(driver)
    home_page = example_pages.MindfulCaresHomePage(driver) # Mindful Care Home
    # Set up test failure capture:
    fails = list()
    fail_text = None
    try:
        print(app)
        navigate_to_search_engine(driver=driver, app=app, environment=environment)
        # Expect some lag time for a page to load
        assert home_page.wait_for_load_complete()
        # Take a screenshot
        base_page.screenshot(environment, 'Mindful Care Home Page')
        home_page.scroll_down_page()
        home_page.click_FAQ_link()
        # Take a screenshot
        base_page.screenshot(environment, 'Mindful Care FAQ Page')
        question_xpath = '/html/body/main/div/section[2]/details[8]/summary/div/span'
        expected_age = "Psychiatric Services (Medication Management) - Ages 18+"
        age_of_psychiatric_services_xpath = "/html/body/main/div/section[2]/details[8]/div/p[1]"
        home_page.expand_answer(question_xpath)
        actual_age = home_page.get_actual_answer(age_of_psychiatric_services_xpath)
        assert actual_age == expected_age
    except (AssertionError, Exception, BaseException) as failure:
        fail_text = base_page.prep_failures(fails, exception_error=str(failure))
        logging.warning(msg='There was a failure: {}'.format(fail_text))
    finally:
        base_page.tear_down(environment, failure=fail_text, test_number=test_num)



def test_therapy_services(environment, browser, headless, record_xml_attribute):
    """test_therapy_services answer"""
    record_xml_attribute(
        'therapy_services', 'test_therapy_services answer, check age')
    # define your driver
    driver = BrowserSetup.get_driver(browser, headless)
    # define your page objects
    base_page = example_pages.BasePage(driver)
    home_page = example_pages.MindfulCaresHomePage(driver)  # Mindful Care Home
    # Set up test failure capture:
    fails = list()
    fail_text = None
    try:
        print(app)
        navigate_to_search_engine(driver=driver, app=app, environment=environment)
        # Expect some lag time for a page to load
        assert home_page.wait_for_load_complete()
        # Take a screenshot
        base_page.screenshot(environment, 'Mindful Care Home Page')
        home_page.scroll_down_page()
        home_page.click_FAQ_link()
        # Take a screenshot
        base_page.screenshot(environment, 'Mindful Care FAQ Page')
        question_xpath = '/html/body/main/div/section[2]/details[8]/summary/div/span'
        expected_age = "Therapy Services (Individual and Group Therapy) - Ages 18+"
        age_of_therapy_services_xpath = "/html/body/main/div/section[2]/details[8]/div/p[2]"
        home_page.expand_answer(question_xpath)
        actual_age = home_page.get_actual_answer(age_of_therapy_services_xpath)
        assert actual_age == expected_age
    except (AssertionError, Exception, BaseException) as failure:
        fail_text = base_page.prep_failures(fails, exception_error=str(failure))
        logging.warning(msg='There was a failure: {}'.format(fail_text))
    finally:
        base_page.tear_down(environment, failure=fail_text, test_number=test_num)


def test_substance_use_counseling_services(environment, browser, headless, record_xml_attribute):
    """test_substance_use_counseling_services answer"""
    record_xml_attribute(
        'substance_use_counseling', 'test_substance_use_counseling_services answer, check age')
    # define your driver
    driver = BrowserSetup.get_driver(browser, headless)
    # define your page objects
    base_page = example_pages.BasePage(driver)
    home_page = example_pages.MindfulCaresHomePage(driver)  # Mindful Care Home
    # Set up test failure capture:
    fails = list()
    fail_text = None
    try:
        print(app)
        navigate_to_search_engine(driver=driver, app=app, environment=environment)
        # Expect some lag time for a page to load
        assert home_page.wait_for_load_complete()
        # Take a screenshot
        base_page.screenshot(environment, 'Mindful Care Home Page')
        home_page.scroll_down_page()
        home_page.click_FAQ_link()
        # Take a screenshot
        base_page.screenshot(environment, 'Mindful Care FAQ Page')
        question_xpath = '/html/body/main/div/section[2]/details[8]/summary/div/span'
        expected_age = "Substance Use Counseling - Ages 18+"
        age_of_substance_use_counseling_xpath = "/html/body/main/div/section[2]/details[8]/div/p[3]"
        home_page.expand_answer(question_xpath)
        actual_age = home_page.get_actual_answer(age_of_substance_use_counseling_xpath)
        assert actual_age == expected_age
    except (AssertionError, Exception, BaseException) as failure:
        fail_text = base_page.prep_failures(fails, exception_error=str(failure))
        logging.warning(msg='There was a failure: {}'.format(fail_text))
    finally:
        base_page.tear_down(environment, failure=fail_text, test_number=test_num)


def test_inperson_virtually(environment, browser, headless, record_xml_attribute):
    """test_inperson_virtually """
    record_xml_attribute(
        'in person and virtually', 'test Currently, all patient visits are virtual and in person')
    # define your driver
    driver = BrowserSetup.get_driver(browser, headless)
    # define your page objects
    base_page = example_pages.BasePage(driver)
    home_page = example_pages.MindfulCaresHomePage(driver)  # Mindful Care Home
    # Set up test failure capture:
    fails = list()
    fail_text = None
    try:
        print(app)
        navigate_to_search_engine(driver=driver, app=app, environment=environment)
        # Expect some lag time for a page to load
        assert home_page.wait_for_load_complete()
        # Take a screenshot
        base_page.screenshot(environment, 'Mindful Care Home Page')
        home_page.scroll_down_page()
        home_page.click_FAQ_link()
        # Take a screenshot
        base_page.screenshot(environment, 'Mindful Care FAQ Page')
        question_xpath = '/html/body/main/div/section[2]/details[7]/summary/div/span'
        expected_answer = "Currently, all patient visits are virtual and in person."
        inperson_virtually_xpath = "/html/body/main/div/section[2]/details[7]/div/p"
        home_page.expand_answer(question_xpath)
        actual_answer = home_page.get_actual_answer(inperson_virtually_xpath)
        assert actual_answer == expected_answer
    except (AssertionError, Exception, BaseException) as failure:
        fail_text = base_page.prep_failures(fails, exception_error=str(failure))
        logging.warning(msg='There was a failure: {}'.format(fail_text))
    finally:
        base_page.tear_down(environment, failure=fail_text, test_number=test_num)