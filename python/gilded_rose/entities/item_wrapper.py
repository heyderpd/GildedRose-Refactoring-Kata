from typing import Dict, List
from types import FunctionType

from . import Item, ItemType
from .constants import MAXIMUM_QUALITY


class ItemWrapper:
    item: Item = None
    item_type: ItemType = None

    quality_velocity: int = 0
    sell_in_velocity: int = 0

    updates: Dict[int, List[FunctionType]] = None

    def __init__(self, item: Item, item_type: ItemType = ItemType.common, quality_velocity=-1, sell_in_velocity=-1, updates=None):
        self.item = item
        self.item_type = item_type
        self.quality_velocity = quality_velocity
        self.sell_in_velocity = sell_in_velocity

    def update_quality(self):
        if self.item.quality < MAXIMUM_QUALITY:
            self.item.quality = self.item.quality + self.quality_velocity

    def update_sellin(self):
        self.item.sell_in = self.item.sell_in + self.sell_in_velocity

    def update_velocity(self):
        if not self.updates:
            return
        updates = self.updates.get(self.item.sell_in)
        if not updates:
            return
        if not isinstance(updates, list):
            updates = [updates]
        for f_update in updates:
            f_update(self)

    def legacy_update(self):
        if self.item_type not in (ItemType.maturable, ItemType.backstage_pass):
            if self.item.quality > 0:
                if self.item_type != ItemType.legendary:
                    self.item.quality = self.item.quality - 1
        else:
            if self.item.quality < MAXIMUM_QUALITY:
                self.item.quality = self.item.quality + 1
                if self.item_type == ItemType.backstage_pass:
                    if self.item.sell_in < 11:
                        if self.item.quality < MAXIMUM_QUALITY:
                            self.item.quality = self.item.quality + 1
                    if self.item.sell_in < 6:
                        if self.item.quality < MAXIMUM_QUALITY:
                            self.item.quality = self.item.quality + 1
        if self.item_type != ItemType.legendary:
            self.item.sell_in = self.item.sell_in - 1
        if self.item.sell_in < 0:
            if self.item_type != ItemType.maturable:
                if self.item_type != ItemType.backstage_pass:
                    if self.item.quality > 0:
                        if self.item_type != ItemType.legendary:
                            self.item.quality = self.item.quality - 1
                else:
                    self.item.quality = self.item.quality - self.item.quality
            else:
                if self.item.quality < MAXIMUM_QUALITY:
                    self.item.quality = self.item.quality + 1
