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

    # Tests under 30
    def test_price_under_30(self):
        expected = 34.45
        actual = calculate_price(25, 0, 0)
        self.assertEqual(expected, actual)

    def test_price_under_30_with_cash(self):
        expected = 29.15
        actual = calculate_price(25, 5, 0)
        self.assertAlmostEqual(expected, actual)

    def test_price_under_30_with_percent(self):
        expected = 30.48
        actual = calculate_price(25, 0, 15)
        self.assertAlmostEqual(expected, actual, 2)

    def test_price_under_30_with_both(self):
        expected = 27.03
        actual = calculate_price(25, 5, 10)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
