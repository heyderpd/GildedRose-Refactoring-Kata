# -*- coding: utf-8 -*-
from .src.entities import Item
from .src import update


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        list(map(update, self.items))
