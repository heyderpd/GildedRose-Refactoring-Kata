# -*- coding: utf-8 -*-
from gilded_rose.entities import Item, ItemType
from gilded_rose.entities.constants import MAXIMUM_QUALITY
from gilded_rose.factories.item import ItemWrapperFactory

class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.item_wrappers = [ItemWrapperFactory.from_item(it) for it in items]

    def update_quality(self):
        for item in self.items:
            item_type = ItemType.from_item(item)
            if item_type is ItemType.legendary:
                pass
            elif item_type is ItemType.maturable:
                if item.quality < MAXIMUM_QUALITY:
                    if item.sell_in <= 0:
                        item.quality = item.quality + 2
                    else:
                        item.quality = item.quality + 1
                item.sell_in = item.sell_in - 1
            else:
                self._process_item_as_legacy(item, item_type)

    def _process_item_as_legacy(self, item: Item, item_type: ItemType):
        if item_type not in (ItemType.maturable, ItemType.backstage_pass):
            if item.quality > 0:
                if item_type != ItemType.legendary:
                    item.quality = item.quality - 1
        else:
            if item.quality < MAXIMUM_QUALITY:
                item.quality = item.quality + 1
                if item_type == ItemType.backstage_pass:
                    if item.sell_in < 11:
                        if item.quality < MAXIMUM_QUALITY:
                            item.quality = item.quality + 1
                    if item.sell_in < 6:
                        if item.quality < MAXIMUM_QUALITY:
                            item.quality = item.quality + 1
        if item_type != ItemType.legendary:
            item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if item_type != ItemType.maturable:
                if item_type != ItemType.backstage_pass:
                    if item.quality > 0:
                        if item_type != ItemType.legendary:
                            item.quality = item.quality - 1
                else:
                    item.quality = item.quality - item.quality
            else:
                if item.quality < MAXIMUM_QUALITY:
                    item.quality = item.quality + 1
