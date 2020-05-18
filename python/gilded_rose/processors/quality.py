from gilded_rose.entities import Item
from gilded_rose.entities.constants import MAXIMUM_QUALITY

from .base import BaseProcessor


class UpdateQuality(BaseProcessor):
    delta: int

    def process_item(self, item: Item, **kwargs):
        item.quality = item.quality + self.delta


class IncreaseQuality(UpdateQuality):
    delta = 1


class DecreaseQuality(UpdateQuality):
    delta = -1

class SetQualityTo(BaseProcessor):
    target: int

    def __init__(self, target: int):
        self.target = target

    def process_item(self, item: Item, **kwargs):
        item.quality = self.target

class CapQuality(BaseProcessor):

    cap: int

    def __init__(self, cap: int):
        self.cap = cap

    def process_item(self, item: Item, **kwargs):
        if item.quality > self.cap:
            item.quality = self.cap


class CapQualityOnMaximum(CapQuality):
    def __init__(self):
        self.cap = MAXIMUM_QUALITY


class QualityIsNeverNegative(BaseProcessor):
    def process_item(self, item: Item, **kwargs):
        if item.quality < 0:
            item.quality = 0
