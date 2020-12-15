def get_app_url(Search_Engine_type):
    switcher = {
        Search_Engine_type.google: 'https://google.com',
        Search_Engine_type.bing: 'https://bing.com',
        Search_Engine_type.yandex: 'http://yandex.com'
    }
    print(switcher.get(Search_Engine_type,
                       'Invalid search engine, or not yet implemented. Valid types are: Google, Bing or Yandex.'))
    return switcher.get(Search_Engine_type)


def navigate_to_search_engine(driver, Search_Engine_type):
    driver.get(get_app_url(Search_Engine_type))
    link = driver.current_url
    print('The current url is: {}'.format(link))
