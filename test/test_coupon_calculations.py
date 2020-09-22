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

    # Tests under 50
    def test_price_under_50(self):
        expected = 59.65
        actual = calculate_price(45, 0, 0)
        self.assertAlmostEqual(expected, actual)

    def test_price_under_50_with_cash(self):
        expected = 49.05
        actual = calculate_price(45, 10, 0)
        self.assertEqual(expected, actual)

    def test_price_under_50_with_percent(self):
        expected = 54.88
        actual = calculate_price(45, 0, 10)
        self.assertAlmostEqual(expected, actual)

    def test_price_under_50_with_both(self):
        expected = 45.34
        actual = calculate_price(45, 10, 10)
        self.assertEqual(expected, actual)

    # Tests over 50
    def test_price_over_50(self):
        expected = 79.50
        actual = calculate_price(75, 0, 0)
        self.assertEqual(expected, actual)

    def test_price_over_50_with_cash(self):
        expected = 74.20
        actual = calculate_price(75, 5, 0)
        self.assertEqual(expected, actual)

    def test_price_over_50_with_percent(self):
        expected = 67.58
        actual = calculate_price(75, 0, 15)
        self.assertAlmostEqual(expected, actual, 2)

    def test_price_over_50_with_both(self):
        expected = 55.12
        actual = calculate_price(75, 10, 20)
        self.assertAlmostEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
