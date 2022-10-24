import unittest

from tests import amount_util, gen_rand


class TestAmountMethods(unittest.TestCase):

    def test_decimal_to_string(self):
        dec_w_whole = amount_util.decimal_to_string(3.33)
        self.assertEqual(dec_w_whole.upper(), '3.33')
        dec_only = amount_util.decimal_to_string(.33)
        self.assertEqual(dec_only.upper(), '0.33')
        another_dec = amount_util.decimal_to_string(0.3025)
        self.assertEqual(another_dec.upper(), '0.3025')

    def test_string_to_decimal(self):
        whole_w_dec = amount_util.string_to_decimal('3')
        dec_only = amount_util.string_to_decimal('.33')
        test_sum = whole_w_dec + dec_only
        conv_sum = amount_util.decimal_to_string(test_sum)
        self.assertEqual(conv_sum, amount_util.decimal_to_string(3.33))
        self.assertNotEqual(whole_w_dec, conv_sum)

    def test_string_to_float(self):
        price = '999.123456'
        formatted_price = amount_util.string_to_float(price)
        rounded = round(formatted_price, 4)
        self.assertEqual(rounded, 999.1235)

    def test_random_num_gen(self):
        max_num = [5, 0, 100, 999999, 10000]
        for maxn in max_num:
            gen_num = gen_rand.random_number(maxn)
            if maxn < 1:
                maxn = 1
            self.assertLessEqual(gen_num, maxn)

    def test_random_string_gen(self):
        max_num = [5, 0, 100, 999999, 10000]
        for maxn in max_num:
            gen_string = gen_rand.random_string(maxn)
            string_len = len(gen_string)
            if maxn < 1:
                maxn = 1
            self.assertLessEqual(string_len, maxn)

    def test_random_price_gen(self):
        i = 0
        while i <= 10:
            gen_price = gen_rand.random_usd_price()
            self.assertGreater(gen_price, 0)
            len_price = len(str(gen_price))
            max_value = 999.99
            self.assertLessEqual(len_price, len(str(max_value)))
            self.assertLessEqual(gen_price, max_value)
            i += 1
