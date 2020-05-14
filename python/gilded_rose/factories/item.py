from gilded_rose.entities import Item, ItemType
from gilded_rose.entities.item_wrapper import ItemWrapper


class ItemWrapperFactory:

    item_map = {
            ItemType.legendary: [0, 0, None],
            ItemType.maturable: [1, -1, None]
        }


    @classmethod
    def from_item(cls, item: Item):
        item_type = cls._get_type_from_name(item.name) 
        config = cls.item_map.get(item_type)

        if not config:
            return None

        return ItemWrapper(
                item=item,
                item_type=item_type,
                quality_velocity=config[0],
                sell_in_velocity=config[1],
                updates=config[2],
            )

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
