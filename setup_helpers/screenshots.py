"""To take a screenshot and save it to report output"""
import datetime


def take_screenshot(driver, name=None):
	"""To take a screenshot and save it to report output"""
	created_date = str(datetime.datetime.utcnow().strftime("%Y-%m-%d"))
	file_name = 'test-reports/screenshots/' + str(name) + created_date + '.png'
	driver.save_screenshot(file_name)
