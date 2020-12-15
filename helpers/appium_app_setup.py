import PATH as PATH
from appium import webdriver


def get_app_type(PlatformType):
	switcher = {
		PlatformType.ios: 'iOS',
		PlatformType.android: 'Android'
	}
	print(switcher.get(PlatformType, 'Invalid app type.'))
	return switcher.get(PlatformType)


def get_desired_caps(PlatformType, app_path):
	desired_caps = {}
	if PlatformType.ios:
		desired_caps = dict(
			platformName=PlatformType.ios,
			platformVersion='13.4',
			automationName='xcuitest',
			deviceName='iPhone Simulator',
			app=PATH(app_path)
		)
		if PlatformType.android:
			desired_caps = dict(
				platformName='Android',
				platformVersion='10',
				automationName='uiautomator2',
				deviceName='Android Emulator',
				app=PATH(app_path)
			)
	return desired_caps


def get_appium_driver(PlatformType, app_path):
	desired_caps = get_desired_caps(PlatformType, app_path)
	driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
	return driver
