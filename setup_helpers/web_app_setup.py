def get_app_url(SearchEngineType):
	switcher = {
		SearchEngineType.google: 'https://google.com',
		SearchEngineType.bing: 'https://bing.com',
		SearchEngineType.yandex: 'http://yandex.com'
	}
	print(switcher.get(SearchEngineType,
					   'Invalid search engine, or not yet implemented. Valid types are: Google, Bing or Yandex.'))
	return switcher.get(SearchEngineType)


def navigate_to_search_engine(driver, SearchEngineType):
	driver.get(get_app_url(SearchEngineType))
	link = driver.current_url
	print('The current url is: {}'.format(link))
