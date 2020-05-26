from craftsmen import identity, rcompose

from .entities import constants
from .behaviours import maturable, legendary, backstage_pass, conjured, common


item_behaviour = {
  constants.MATURABLE: maturable,
  constants.LEGENDARY: legendary,
  constants.BACKSTAGE_PASSES: backstage_pass,
  constants.CONJURED: conjured,
}

def getIdentifier(item):
  if 'Sulfuras' in item.name:
    return constants.LEGENDARY
  if item.name == 'Aged Brie':
    return constants.MATURABLE
  if 'Backstage passes' in item.name:
    return constants.BACKSTAGE_PASSES
  if 'Conjured' in item.name:
    return constants.CONJURED

def update(item):
  item_type = getIdentifier(item)
  processors = item_behaviour.get(item_type, common)
  return processors(item)
