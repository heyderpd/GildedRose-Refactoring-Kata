from gilded_rose.entities import Item, ItemType
from gilded_rose.entities.item_runner import ItemRunner
from gilded_rose.processors.legacy import LegacyProcessor


class ItemRunnerFactory:

    item_map = {
        ItemType.legendary: []
    }

    @classmethod
    def from_item(cls, item: Item):
        item_type = cls._get_type_from_name(item.name)
        processors = cls.item_map.get(item_type)

        if not processors:
            return ItemRunner(item, [LegacyProcessor()])

        return ItemRunner(item, processors)

    @classmethod
    def _get_type_from_name(cls, name: str) -> ItemType:
        if name == "Aged Brie":
            return ItemType.maturable
        if name == "Sulfuras, Hand of Ragnaros":
            return ItemType.legendary
        if name == "Backstage passes to a TAFKAL80ETC concert":
            return ItemType.backstage_pass
        if name == "Conjured":
            return ItemType.conjured
        return ItemType.common
