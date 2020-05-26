from craftsmen import curry


def __setQuality(value, item):
  item.quality = value

def __sumValueWithQuality(value, item):
  __setQuality(item.quality + value, item)
  return item

def __increaseQuality(value, item):
  __sumValueWithQuality(value, item)
  return item

def __decreaseQuality(value, item):
  __sumValueWithQuality(-1 * value, item)
  return item

def __setTopLimit(limit, item):
  if item.quality > limit:
    __setQuality(limit, item)
  return item

def __setLowerLimit(limit, item):
  if item.quality < limit:
    __setQuality(limit, item)
  return item


def __setSellIn(value, item):
  item.sell_in = value

def __whenPastExpiration(processor, item):
  limit = 0
  WhenSellInPast(limit, processor, item)
  return item

def __whenSellInPast(limit, processor, item):
  if item.sell_in < limit:
    processor(item)
  return item

def __updateSellInDate(item):
  __setSellIn(item.sell_in  -1, item)
  return item


IncreaseQuality = curry(__increaseQuality)

DecreaseQuality = curry(__decreaseQuality)

CapQualityOnMaximum = curry(__setTopLimit)

QualityIsNeverNegative = curry(__setLowerLimit)

SetQualityTo = curry(__setQuality)

WhenPastExpiration = curry(__whenPastExpiration)

WhenSellInPast = curry(__whenSellInPast)

UpdateSellInDate = curry(__updateSellInDate)

