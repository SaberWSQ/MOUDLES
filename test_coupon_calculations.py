import unittest
from store import coupon_calculations


class TestCouponCalculation(unittest.TestCase):
    def test_price_under_10(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(8, 5, 0.1), 8.812, places=4)
        self.assertAlmostEqual(coupon_calculations.calculate_price(8, 5, 0.15), 8.653, places=4)
        self.assertAlmostEqual(coupon_calculations.calculate_price(8, 5, 0.2), 8.494, places=4)
        self.assertAlmostEqual(coupon_calculations.calculate_price(8, 10, 0.1), 5.95, places=4)
        self.assertAlmostEqual(coupon_calculations.calculate_price(8, 10, 0.15), 5.95, places=4)
        self.assertAlmostEqual(coupon_calculations.calculate_price(8, 10, 0.2), 5.95, places=4)

    def test_price_10_to_less_than_30(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(20, 5, 0.1), 22.26, places=4)
        self.assertAlmostEqual(coupon_calculations.calculate_price(20, 5, 0.15), 21.465, places=4)
        self.assertAlmostEqual(coupon_calculations.calculate_price(20, 5, 0.2), 20.67, places=4)
        self.assertAlmostEqual(coupon_calculations.calculate_price(20, 10, 0.1), 15.49, places=4)
        self.assertAlmostEqual(coupon_calculations.calculate_price(20, 10, 0.15), 14.96, places=4)
        self.assertAlmostEqual(coupon_calculations.calculate_price(20, 10, 0.2), 14.43, places=4)

    def test_price_30_to_less_than_50(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(40, 5, 0.1), 45.34, places=4)
        self.assertAlmostEqual(coupon_calculations.calculate_price(40, 5, 0.15), 39.485, places=4)
        self.assertAlmostEqual(coupon_calculations.calculate_price(40, 5, 0.2), 37.63, places=4)
        self.assertAlmostEqual(coupon_calculations.calculate_price(40, 10, 0.1), 36.57, places=4)
        self.assertAlmostEqual(coupon_calculations.calculate_price(40, 10, 0.15), 34.98, places=4)
        self.assertAlmostEqual(coupon_calculations.calculate_price(40, 10, 0.2), 33.39, places=4)

    def test_price_50_or_over(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(60, 5, 0.1), 64.42, places=4)
        self.assertAlmostEqual(coupon_calculations.calculate_price(60, 5, 0.15), 61.505, places=4)
        self.assertAlmostEqual(coupon_calculations.calculate_price(60, 5, 0.2), 58.59, places=4)
        self.assertAlmostEqual(coupon_calculations.calculate_price(60, 10, 0.1), 59.65, places=4)
        self.assertAlmostEqual(coupon_calculations.calculate_price(60, 10, 0.15), 57.0, places=4)
        self.assertAlmostEqual(coupon_calculations.calculate_price(60, 10, 0.2), 54.35, places=4)


if __name__ == '__main__':
    unittest.main()
