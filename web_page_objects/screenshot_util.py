"""Created by Alysha Kester-Terry 05/05/2021"""
import datetime
import logging


def take_screenshot(driver, environment, name=None):
    created_date = datetime.datetime.utcnow().strftime('%m-%d-%H%M%S')
    add_name = str(name).replace(' ', '')
    file_name = 'test-reports/{}/screenshots/{}_{}.png'.format(environment, created_date, add_name)
    logging.debug('Saving screenshot to {}'.format(file_name))
    driver.save_screenshot(file_name)


def debug_screenshot(driver, name=None):
    created_date = datetime.datetime.utcnow().strftime('%m-%d-%H%M%S')
    add_name = str(name).replace(' ', '')
    file_name = 'test-reports/{}/screenshots/{}_{}.png'.format('debug', created_date, add_name)
    logging.debug('Saving screenshot to {}'.format(file_name))
    driver.save_screenshot(file_name)
