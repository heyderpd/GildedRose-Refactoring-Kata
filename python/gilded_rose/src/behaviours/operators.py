from craftsmen import curry

from ..entities import constants


def __setQuality(value, item):
  item.quality = value
  return item

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
  return item

def __whenSellInEqualOrLowerThan(limit, processor, item):
  if item.sell_in <= limit:
    processor(item)
  return item

def __updateSellInDate(item):
  __setSellIn(item.sell_in  -1, item)
  return item


SetQualityTo = curry(__setQuality)
IncreaseQualityBy = curry(__increaseQuality)
DecreaseQualityBy = curry(__decreaseQuality)
SetTopLimitOnQuality = curry(__setTopLimit)
SetLowerLimitOnQuality = curry(__setLowerLimit)
WhenSellInEqualOrLowerThan = curry(__whenSellInEqualOrLowerThan)
UpdateSellIn = curry(__updateSellInDate)


WhenExpiration = WhenSellInEqualOrLowerThan(0)
SetQualityToZero = SetQualityTo(0)
IncreaseQualityByOne = IncreaseQualityBy(1)
DecreaseQualityByOne = DecreaseQualityBy(1)
LimitMaximumValueOfQuality = SetTopLimitOnQuality(constants.MAXIMUM_QUALITY)
QualityIsNeverNegative = SetLowerLimitOnQuality(0)
