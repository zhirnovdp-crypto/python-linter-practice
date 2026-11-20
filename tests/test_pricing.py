import unittest

from shop.pricing import total_price


class TotalPriceTests(unittest.TestCase):
    def test_without_discount(self) -> None:
        self.assertEqual(total_price(120, 3), 360)

    def test_with_discount(self) -> None:
        self.assertEqual(total_price(120, 3, 25), 270)

    def test_fractional_ruble_is_rounded_down(self) -> None:
        self.assertEqual(total_price(99, 1, 50), 49)

    def test_discount_boundaries(self) -> None:
        self.assertEqual(total_price(120, 3, 0), 360)
        self.assertEqual(total_price(120, 3, 100), 0)

    def test_zero_quantity(self) -> None:
        self.assertEqual(total_price(120, 0), 0)

    def test_negative_price_or_quantity(self) -> None:
        for unit_price, quantity in [(-1, 3), (120, -1)]:
            with self.subTest(unit_price=unit_price, quantity=quantity):
                with self.assertRaises(ValueError):
                    total_price(unit_price, quantity)

    def test_invalid_discount(self) -> None:
        for discount in [-1, 101]:
            with self.subTest(discount=discount):
                with self.assertRaises(ValueError):
                    total_price(120, 3, discount)
