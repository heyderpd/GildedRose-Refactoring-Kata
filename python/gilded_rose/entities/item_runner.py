from typing import Dict, List
from types import FunctionType

from gilded_rose.processors.base import BaseProcessor

from . import Item, ItemType
from .constants import MAXIMUM_QUALITY


class ItemRunner:
    item: Item = None

    processors: List[BaseProcessor] = None

    def __init__(self, item: Item, processors: List[BaseProcessor]):
        self.item = item
        self.processors = processors

    def update(self):
        for processor in self.processors:
            processor.process_item(self.item)
