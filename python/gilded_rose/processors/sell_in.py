from gilded_rose.entities import Item 
from .base import BaseProcessor


class UpdateSellInDate(BaseProcessor):

    def process_item(self, item: Item, **kwargs):
        item.sell_in = item.sell_in - 1
