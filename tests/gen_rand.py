"""Util to help generate randomized values"""
import logging
import random
import string
from datetime import datetime, timedelta
from decimal import Decimal

from tests import amount_util


def random_number(max_num=10):
    """Generates a random number, defaulted to a range of up to 10
    :param max_num: the max number to produce
    """
    if max_num < 1:
        max_num = 1
    num = random.randrange(max_num)
    if num < 1:
        num = num + 1
    return num


def random_string(length=10):
    """Generates a random string, defaulted to a length of up to 10 characters
    :param length: the max length to produce
    """
    if length < 1:
        length = 1
    letters = string.ascii_letters
    final_string = ''.join(random.choice(letters) for i in range(length)).lower()
    return final_string


def random_usd_price():
    """Generates a random price, defaulted to a max of 999.99
    """
    amount = amount_util.string_to_decimal(amount_util.decimal_to_string(round(random.random(), 2)))
    if amount < Decimal(0.01):
        amount = amount_util.string_to_decimal("0.01")
    price = str(random_number(999) + amount)
    formatted_price = amount_util.string_to_float(price)
    logging.debug(msg='Raw calculation: {}, Formatted: {}'.format(price, formatted_price))
    return round(formatted_price, 2)


def random_dob(min_days_back=None):
    """Generates a random date of birth, in YYYY-MM-DD Format
    :param min_days_back: The minimum value subtracted from today's date
    """
    if min_days_back is None:
        min_days_back = 6550
    today = datetime.utcnow().today()
    dob_calc = today + timedelta(days=-min_days_back)
    return dob_calc.strftime('%Y%m%d')


def get_excel_date():
    """Generates a date in Excel serial number format
    """
    today = datetime.utcnow().today()
    date_calc = today + timedelta(days=-600)
    temp = datetime(1899, 12, 30)  # Note, not 31st Dec but 30th!
    delta = date_calc - temp
    return float(delta.days) + (float(delta.seconds) / 86400)