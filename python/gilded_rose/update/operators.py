from craftsmen import curry


def __setQuality(delta, item):
  item.quality = delta

def __sumValueWithQuality(delta, item):
  __setQuality(item.quality + delta, item)

def __increaseQuality(delta, item):
  __sumValueWithQuality(delta, item)

def __decreaseQuality(delta, item):
  __sumValueWithQuality(-1 * delta, item)

def __setTopLimit(limit, item):
  if item.quality > limit:
    __setQuality(limit, item)

def __setLowerLimit(limit, item):
  if item.quality < limit:
    __setQuality(limit, item)


IncreaseQuality = curry(__increaseQuality)

DecreaseQuality = curry(__decreaseQuality)

CapQualityOnMaximum = curry(__setTopLimit)

QualityIsNeverNegative = curry(__setLowerLimit)

SetQualityTo = curry(__setQuality)


def WhenPastExpiration():
  pass

def WhenSellInPast():
  pass

def UpdateSellInDate():
  pass
