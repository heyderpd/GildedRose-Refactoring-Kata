# -*- coding: utf-8 -*-
from .base import BaseApplicationTest, ExpectedResult

from gilded_rose import Item, GildedRose


class GildedRoseTest(BaseApplicationTest):

    def testCommonItem(self):
        with self.subTest("whenBeforeExpirationDate_qualityAndSellinShouldDecrease"):
            self.assertItemAfterUpdate(Item("common", 10, 10), ExpectedResult(9, 9))

        with self.subTest("whenPastExpirationDate_qualitynShouldDecreaseTwiceAsFast"):
            self.assertItemAfterUpdate(Item("common", -1, 10), ExpectedResult(-2, 8))

        with self.subTest("whenZeroQualityItem_qualityShouldNotDecrease"):
            self.assertItemAfterUpdate(Item("common", 0, 0), ExpectedResult(-1, 0))

    def testAgedBrie(self):
        with self.subTest("whenBeforeExpirationDate_qualityShouldIncrease"):
            self.assertItemAfterUpdate(Item("Aged Brie", 1, 1), ExpectedResult(0, 2))

        with self.subTest("whenPastSellInDate_qualityShouldIncreaseTwiceAsFast"):
            self.assertItemAfterUpdate(Item("Aged Brie", 0, 1), ExpectedResult(-1,3))

        with self.subTest("whenIsMaximunQuality_qualityShouldNotIncrease"):
            self.assertItemAfterUpdate(Item("Aged Brie", 0, 50), ExpectedResult(-1,50))

    def testSulfuras(self):
        with self.subTest("whenBeforeSellInDate_qualityAndSellInShouldNotChange"):
            self.assertItemAfterUpdate(Item("Sulfuras, Hand of Ragnaros", 10, 10), ExpectedResult(10,10))

        with self.subTest("whenPastSellInDate_qualityAndSellinShouldNotChange"):
            self.assertItemAfterUpdate(Item("Sulfuras, Hand of Ragnaros", 10, 10), ExpectedResult(10,10))

    def testBackstagePass(self):
        with self.subTest("whenMoreThan10DaysLeft_qualityShouldIncreaseBy1"):
            self.assertItemAfterUpdate(Item("Backstage passes to a TAFKAL80ETC concert", 11, 1), ExpectedResult(10,2))

        with self.subTest("when10DaysLeftOrLess_qualityShouldIncreaseBy2"):
            self.assertItemAfterUpdate(Item("Backstage passes to a TAFKAL80ETC concert", 10, 1), ExpectedResult(9,3))

        with self.subTest("when5DaysLeftOrLess_qualityShouldIncreaseBy3"):
            self.assertItemAfterUpdate(Item("Backstage passes to a TAFKAL80ETC concert", 5, 1), ExpectedResult(4,4))

        with self.subTest("whenPastSellInDate_qualityShouldZero"):
            self.assertItemAfterUpdate(Item("Backstage passes to a TAFKAL80ETC concert", 0, 5), ExpectedResult(-1,0))

    def testConjured(self):
        with self.subTest("whenBeforeExpirationDate_qualityAndSellinShouldDecreaseTwiceAsFast"):
            self.assertItemAfterUpdate(Item("Conjured", 10, 10), ExpectedResult(9, 8))

        with self.subTest("whenPastExpirationDate_qualitynShouldDecrease4TimesAsFast"):
            self.assertItemAfterUpdate(Item("Conjured", -1, 10), ExpectedResult(-2, 6))

        with self.subTest("whenZeroQualityItem_qualityShouldNotDecrease"):
            self.assertItemAfterUpdate(Item("Conjured", 0, 1), ExpectedResult(-1, 0))
