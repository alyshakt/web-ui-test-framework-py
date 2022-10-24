"""Configuration for Pytest arguments"""
import logging
import time


def pytest_addoption(parser):
    """Arguments allowed to pass through on run"""
    parser.addoption("--environment",
                     action="store",
                     default="stage",
                     help="Environment to run tests in")
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     help="Browser to run tests in")
    parser.addoption("--headless",
                     action="store",
                     default="true",
                     help="Headless browser functionality")


def pytest_generate_tests(metafunc):
    """Initialize arguments allowed to pass through on run"""
    if 'environment' in metafunc.fixturenames:
        logging.debug(msg=metafunc.config.option.environment)
        metafunc.parametrize("environment",
                             [str(metafunc.config.option.environment)])
    if 'browser' in metafunc.fixturenames:
        logging.debug(msg=metafunc.config.option.browser)
        metafunc.parametrize("browser",
                             [str(metafunc.config.option.browser)])
    if 'headless' in metafunc.fixturenames:
        logging.debug(msg=metafunc.config.option.headless)
        metafunc.parametrize("headless",
                             [str(metafunc.config.option.headless)])


def get_timeout_timestamp(seconds_to_wait: int = None):
    """ time.perf_counter() returns the current elapsed time of execution including sleep.
    Method returns timeout based on current execution elapsed time."""
    if seconds_to_wait is None:
        seconds_to_wait = max_wait_time_seconds()
    total_wait = time.perf_counter() + seconds_to_wait
    return total_wait


def wait_for_seconds(seconds_to_wait=5):
    """Hard sleep if absolutely needed. Defaults to 5 seconds"""
    logging.info('Waiting for {} seconds...'.format(seconds_to_wait))
    time.sleep(seconds_to_wait)


def max_wait_time_seconds(seconds_to_wait=45):
    return seconds_to_wait


def timer(this_method):
    """Returns a duration for method that is annotated with @timer"""

    def start_timer(*args, **kwargs):
        start_time = time.perf_counter()
        val = this_method(*args, **kwargs)
        end_time = time.perf_counter()
        result = {
            'start_time': '{} seconds'.format(start_time),
            'end_time': '{} seconds'.format(end_time),
            'delta': '{} seconds'.format(end_time - start_time),
            'method_name': this_method.__name__
        }
        logging.info(msg='Duration result: {}'.format(result))
        return val

    return start_timer
