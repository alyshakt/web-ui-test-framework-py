import pytest

from app_page_objects import ios_pages
from helpers import screenshots, appium_app_setup
from helpers.PlatformType import PlatformType


def test_ios_login(record_xml_attribute):
	"""Created December 15th, 2020 by Alysha Kester-Terry https://github.com/alyshakt"""
	record_xml_attribute(
		"name",
		"Example iOS Appium Python Test")
	# Setup Driver, define options

	# Define the Platform Type and the page object
	driver = appium_app_setup.get_appium_driver(PlatformType.ios,
												'/Users/akesterterry/Library/Developer/Xcode/DerivedData/DXCDCaribe-btkwbovgtxxexeadalamhzeyuyrt/Build/Products/Debug-iphonesimulator/Dev - Merchant.app')
	login_page = ios_pages.IosLoginPage(driver)

	# I recommend beginning with a try-catch-finally format
	try:
		# Expect some lag time for a page to load
		# Take a screenshot
		screenshots.take_screenshot(driver, 'step1')
		assert login_page.username_field_exists()
	except AssertionError as e:
		# If any assertions above fail, then mark the test as failed and capture a screenshot
		pytest.fail('The test failed. {}'.format(e), True)
		screenshots.take_screenshot(driver, 'Failed')
	finally:
		# Finally, quit the webdriver!
		driver.quit()
