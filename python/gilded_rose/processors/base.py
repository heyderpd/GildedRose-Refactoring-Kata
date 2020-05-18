from abc import ABC, abstractmethod

from gilded_rose.entities import Item

class BaseProcessor(ABC):

    @abstractmethod
    def process_item(self, item: Item, **kwargs):
        pass
