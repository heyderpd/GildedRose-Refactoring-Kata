# -*- coding: utf-8 -*-
from typing import List

from gilded_rose.update import update

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            update(item)
