def get_app_type(PlatformType):
	switcher = {
		PlatformType.ios: 'iOS',
		PlatformType.android: 'Android'
	}
	print(switcher.get(PlatformType, 'Invalid app type.'))
	return switcher.get(PlatformType)


def get_desired_caps(PlatformType, app_path):
	desired_caps = {}
	apptype = get_app_type(PlatformType)
	if apptype == PlatformType.ios:
		desired_caps = dict(
			platformName=PlatformType.ios,
			platformVersion='13.4',
			automationName='xcuitest',
			deviceName='iPhone Simulator',
			app=app_path
		)
		if apptype == PlatformType.android:
			desired_caps = dict(
				platformName='Android',
				platformVersion='10',
				automationName='uiautomator2',
				deviceName='Android Emulator',
				app=app_path
			)
	return desired_caps
