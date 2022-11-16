import pytest
from web_page_objects.frequentlyAskedQuestions_page import *
faq_page = FAQ_page()
#
@pytest.mark.faq
def test_psychiatricServices():
    """test Psychiatric Services (Medication Management), age must be 18+, if not will return -
    Age is not matches requirements"""
    faq_page.faqpage()
    faq_page.click_age()
    psychiatric_age = faq_page.psychiatric_services()

    assert psychiatric_age == butt_expected_age_psychiatric_services
    print(psychiatric_age)


@pytest.mark.faq2
def test_therapy_services():
    """Therapy Services (Individual and Group Therapy)age must be 18+, if not will return -
    Age is not matches requirements"""
    faq_page.faqpage()
    faq_page.click_age()
    faq_page.therapy_services()


@pytest.mark.faq3
def test_substance_use_counseling():
    """Substance Use Counseling age must be 18+, if not will return -
        Age is not matches requirements"""
    faq_page.faqpage()
    faq_page.click_age()
    faq_page.substance_use_counseling()
    # with pytest.raises(Exception):
    #     assert faq_page.substance_use_counseling()
    # faq_page.close()


@pytest.mark.faq4
def test_inperson_virtually():
    """patients must be virtually and in person at any of our locations if not will return
    actual result is not matches expected result"""
    faq_page.faqpage()
    faq_page.inperson_virtually()
    faq_page.close()