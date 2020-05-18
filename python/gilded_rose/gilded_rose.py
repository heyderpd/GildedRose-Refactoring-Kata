# -*- coding: utf-8 -*-
from typing import List

from gilded_rose.entities import Item, ItemType, ItemWrapper
from gilded_rose.entities.constants import MAXIMUM_QUALITY
from gilded_rose.factories.item import ItemWrapperFactory


class GildedRose:

    items: List[Item]
    item_wrappers: List[ItemWrapper]

    def __init__(self, items):
        self.items = items
        self.item_wrappers = [ItemWrapperFactory.from_item(it) for it in items]

    def update_quality(self):
        for iw in self.item_wrappers:
            if iw.item_type not in [ItemType.legendary]:
                iw.legacy_update()
            else:
                iw.update_quality()
                iw.update_sellin()
                iw.update_velocity()
