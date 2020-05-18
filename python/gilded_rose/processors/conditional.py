from gilded_rose.entities import Item 
from .base import BaseProcessor


class WhenSellInPast(BaseProcessor):

    processor: BaseProcessor
    date: int

    def __init__(self, date, processor: BaseProcessor):
        self.date = date
        self.processor = processor

    def process_item(self, item: Item, **kwargs):
        if item.sell_in < self.date:
            self.processor.process_item(item)


class WhenPastExpiration(WhenSellInPast):
    def __init__(self, processor: BaseProcessor):
        self.date = 0
        self.processor = processor
