import datetime


def take_screenshot(driver, name=None):
	created_date = str(datetime.datetime.utcnow().strftime("%Y-%m-%d"))
	file_name = 'test-reports/screenshots/' + str(name) + created_date + '.png'
	driver.save_screenshot(file_name)
