"""Created December 15th, 2020 by Alysha Kester-Terry https://github.com/alyshakt

    This Base Page object locator strategy was gleaned with much gratitude from 
    http://elementalselenium.com/tips/9-use-a-base-page-object
"""


class BasePageLocators(object):
	"""Base Page Locators - Elements on EVERY page"""
	SIGNUP_LINK = ('By.NAME', 'Sign Up')


class IosConsumerLoginLocators(object):
	"""iOS App Login Page Locators"""
	USERNAME_FIELD = ('By.NAME', 'Username')
