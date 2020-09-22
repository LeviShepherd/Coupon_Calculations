import unittest
from store.coupon_calculations import *


class MyTestCase(unittest.TestCase):

    # Tests under 10
    def test_price_under_10(self):
        expected = 14.43
        actual = calculate_price(8, 0, 0)
        self.assertEqual(expected, actual)

    def test_price_under_10_with_cash(self):
        expected = 9.13
        actual = calculate_price(8, 5, 0)
        self.assertEqual(expected, actual)

    def test_price_under_10_with_percent(self):
        expected = 12.73
        actual = calculate_price(8, 0, 20)
        self.assertAlmostEqual(expected, actual, 2)

    def test_price_under_10_with_both(self):
        expected = 4.15
        actual = calculate_price(8, 10, 15)
        # Set number of places to 2 due to the small difference in rounding
        self.assertAlmostEqual(expected, actual, 2)


if __name__ == '__main__':
    unittest.main()
