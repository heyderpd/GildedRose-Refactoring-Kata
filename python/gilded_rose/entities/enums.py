from enum import Enum

from .item import Item

class ItemType(Enum):
    common = 1
    maturable = 2
    backstage_pass = 3
    legendary = 4
    conjured = 5

    @classmethod
    def from_item(cls, item: Item):
        if item.name == "Aged Brie":
            return cls.maturable
        if item.name == "Sulfuras, Hand of Ragnaros":
            return cls.legendary
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            return cls.backstage_pass
        if item.name == "Conjured":
            return cls.conjured
        return cls.common
