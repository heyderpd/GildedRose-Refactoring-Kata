# -*- coding: utf-8 -*-
from .base import BaseApplicationTest

from gilded_rose import Item, GildedRose


class GildedRoseTest(BaseApplicationTest):

    def test_whenCommonItem_qualityAndSellinShouldDecrease(self):
        item = Item("common", 10, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertItemEqual(item, name="common", sell_in=9, quality=9)

    def test_whenPastSellInDate_qualityShouldDecreaseTwiceAsFast(self):
        item = Item("common", -1, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertItemEqual(item, name="common", sell_in=-2, quality=8)

    def test_whenZeroQualityItem_qualityShouldNotDecrease(self):
        item = Item("common", 0, 0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertItemEqual(item, name="common", sell_in=-1, quality=0)

    def test_whenAgedBrie_qualityShouldIncrease(self):
        item = Item("Aged Brie", 1, 1)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertItemEqual(item, sell_in=0, quality=2)

    def test_whenAgedBriePastSellInDate_qualityShouldIncreaseTwiceAsFast(self):
        item = Item("Aged Brie", 0, 1)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertItemEqual(item, sell_in=-1, quality=3)

    def test_whenAgedBrieIsMaximunQuality_qualityShouldNotIncrease(self):
        item = Item("Aged Brie", 0, 50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertItemEqual(item, sell_in=-1, quality=50)

    def test_whenAgedBrieIsMaximunQuality_qualityShouldNotIncrease(self):
        item = Item("Aged Brie", 0, 50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertItemEqual(item, sell_in=-1, quality=50)

    def test_whenSulfuras_qualityAndSellInShouldNotDecrease(self):
        item = Item("Sulfuras, Hand of Ragnaros", 10, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertItemEqual(item, sell_in=10, quality=10)

    def test_whenSulfurasPastSellInDate_qualityAndSellinShouldNotDecrease(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertItemEqual(item, sell_in=0, quality=10)

    def test_whenBackstagePassMoreThan10DaysLeft_qualityShouldIncreaseBy1(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 11, 1)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertItemEqual(item, sell_in=10, quality=2)

    def test_whenBackstagePass10DaysLeftOrLess_qualityShouldIncreaseBy2(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 10, 1)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertItemEqual(item, sell_in=9, quality=3)

    def test_whenBackstagePass5DaysLeftOrLess_qualityShouldIncreaseBy3(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 1)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertItemEqual(item, sell_in=4, quality=4)

    def test_whenBackstagePassPastSellInDate_qualityShouldZero(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 5)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertItemEqual(item, sell_in=-1, quality=0)
