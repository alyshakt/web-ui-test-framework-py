"""Created by Alysha Kester-Terry 3/12/2021 for GoodRx
This file is to set up the driver for a specific site.
We want to make this scalable in case there could be multiple environments or web UI URLs we may want to hit.
"""
import logging


def get_app_url(App, environment='stage'):
    """To define the search engine URL by type given"""
    # TODO define your different environments and how you'd want them to switch
    mindful = ''
    if 'test' in environment:
        env = 'stage'
        mindful = 'https://app-40572.on-aptible.com'
    else:
        env = 'prod'
        mindful = 'https://mindful.care'

    switcher = {
        # TODO you can add the environment into the URLs as vars here if needed
        App.google: 'https://google.com',
        App.bing: 'https://bing.com',
        App.yandex: 'http://yandex.com',
        App.mindful_care: mindful
    }
    app_type = switcher.get(App, 'Invalid environment option, or not yet implemented')
    env_url = app_type
    logging.debug(msg='The environment url is: {}'.format(env_url))
    logging.info(msg='The URL is: {}'.format(env_url))
    return env_url


def navigate_to_search_engine(driver, app, environment='test'):
    """To navigate to the appropriate URL
    :param app: Web app to hit
    :param driver: The webdriver
    :param environment: Test, UAT, Dev etc. Comes from run args
    """
    url = get_app_url(app, environment)
    driver.get(url)
    link = driver.current_url
    logging.debug(msg='The current url is: {}'.format(link))
