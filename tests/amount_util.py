"""This util is for converting amounts to different formats"""
# pylint: disable=W0703, C0301, C0103, R0913, R0914, R0915, W0511, R0912
import logging
from decimal import Decimal, InvalidOperation


def decimal_to_string(amount):
    """Method for converting int amount to string per Standardized amounts"""
    amount = str(amount)
    if '.' in amount:
        split_amount = amount.split('.')[1]
        if len(split_amount) < 2:
            amount = amount + '0'
    else:
        amount = amount + ".00"
    return amount


def string_to_decimal(amount):
    """Converts a string amount back to int. Removes all commas, splits the string at decimal and returns
    the number(s) before the decimal point"""
    try:
        prep_amount = decimal_to_string(amount)
        return_amount = Decimal(prep_amount)
    except InvalidOperation as i:
        logging.debug(msg='The exception: {}'.format(i))
        return_amount = amount
    return return_amount


def string_to_float(price):
    """Converts a string amount back to int. Removes all commas, splits the string at decimal and returns
the number(s) before the decimal point"""
    prep_amount = price
    try:
        prep_amount = decimal_to_string(price)
        return_amount = float(prep_amount)
    except InvalidOperation as i:
        logging.debug(
            msg='The String amount was: {} we will try to return the int amount cast to Decimal instead of the string: {}'.format(
                prep_amount, price))
        return_amount = float(price)
    return return_amount


def decimal_to_int_string(amount):
    """Method for converting decimal amount to int"""
    amount = str(amount)
    if '.' in amount:
        return amount.split('.')[0]
