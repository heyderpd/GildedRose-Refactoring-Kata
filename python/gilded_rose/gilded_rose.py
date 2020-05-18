# -*- coding: utf-8 -*-
from typing import List

from gilded_rose.entities import Item, ItemType, ItemRunner
from gilded_rose.entities.constants import MAXIMUM_QUALITY
from gilded_rose.factories.item import ItemRunnerFactory


class GildedRose:

    items: List[Item]
    item_wrappers: List[ItemRunner]

    def __init__(self, items):
        self.items = items
        self.runners = [ItemRunnerFactory.from_item(it) for it in items]

    def update_quality(self):
        for runner in self.runners:
            runner.update()
