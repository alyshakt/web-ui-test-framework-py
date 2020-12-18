"""To set up the search engine environment"""


def get_app_url(SearchEngineType):
	"""To define the search engine URL by type given"""
	switcher = {
		SearchEngineType.google: 'https://google.com',
		SearchEngineType.bing: 'https://bing.com',
		SearchEngineType.yandex: 'http://yandex.com'
	}
	print(switcher.get(SearchEngineType, 'Invalid search engine, or not yet implemented.'))
	return switcher.get(SearchEngineType)


def navigate_to_search_engine(driver, SearchEngineType):
	"""To navigate to the search engine URL by type given"""
	driver.get(get_app_url(SearchEngineType))
	link = driver.current_url
	print('The current url is: {}'.format(link))
