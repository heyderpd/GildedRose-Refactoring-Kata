# -*- coding: utf-8 -*-
from enum import Enum

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item_type = ItemType.from_item(item)
            if item_type not in (ItemType.aged_brie, ItemType.backstage_pass):
                if item.quality > 0:
                    if item_type != ItemType.legendary:
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item_type == ItemType.backstage_pass:
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item_type != ItemType.legendary:
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item_type != ItemType.aged_brie:
                    if item_type != ItemType.backstage_pass:
                        if item.quality > 0:
                            if item_type != ItemType.legendary:
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class ItemType(Enum):
    common = 1
    aged_brie = 2
    backstage_pass = 3
    legendary = 4
    conjured = 5

    @classmethod
    def from_item(cls, item: Item):
        if item.name == "Aged Brie":
            return cls.aged_brie
        if item.name == "Sulfuras, Hand of Ragnaros":
            return cls.legendary
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            return cls.backstage_pass
        if item.name == "Conjured":
            return cls.conjured
        return cls.common
