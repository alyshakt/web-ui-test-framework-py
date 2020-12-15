import pytest
from appium import webdriver

from helpers import screenshots, appium_setup
from helpers.PlatformType import PlatformType
from appium import ios_pages


def test_ios_login(record_xml_attribute):
	"""Created December 15th, 2020 by Alysha Kester-Terry https://github.com/alyshakt"""
	record_xml_attribute(
		"name",
		"Example iOS Appium Python Test")
	# Setup Driver, define Platform Type and the page object
	apptype = PlatformType.ios
	desired_caps = appium_setup.get_desired_caps(apptype,
													 '/Users/akesterterry/Library/Developer/Xcode/DerivedData/DXCDCaribe-btkwbovgtxxexeadalamhzeyuyrt/Build/Products/Debug-iphonesimulator/Dev - Merchant.app')
	driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
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
