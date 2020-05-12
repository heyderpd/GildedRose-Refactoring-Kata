# -*- coding: utf-8 -*-
from .base import BaseApplicationTest

from gilded_rose import Item, GildedRose


class GildedRoseTest(BaseApplicationTest):

    def test_whenUpdatingZeroQualityItem_qualityShouldNotDecrease(self):
        item = Item("foo", 0, 0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertItemEqual(item, quality=0, name="foo", sell_in=-1)
