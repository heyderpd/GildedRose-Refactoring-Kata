from unittest import TestCase
from typing import NamedTuple

from gilded_rose import Item, GildedRose

class ExpectedResult(NamedTuple):
    sell_in: int
    quality: int


class BaseApplicationTest(TestCase):

    def assertItemAfterUpdate(self, item: Item, expected: ExpectedResult):
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertItemEqual(item, sell_in=expected.sell_in, quality=expected.quality)

    def assertItemEqual(self, item: Item, **kwargs: dict):
        for attr, expected in kwargs.items():
            actual = getattr(item, attr)
            self.assertEqual(
                actual, expected, f"Assertion failed on {attr}: {actual} != {expected}")
