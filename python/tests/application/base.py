from unittest import TestCase

from gilded_rose import Item


class BaseApplicationTest(TestCase):

    def assertItemEqual(self, item: Item, **kwargs: dict):
        for attr, expected in kwargs.items():
            actual = item.__getattribute__(attr)
            self.assertEqual(
                actual, expected, f"Assertion failed on {attr}: {actual} != {expected}")
