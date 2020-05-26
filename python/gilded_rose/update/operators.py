from craftsmen import curry


def __sumValueWithQuality(delta, item):
  item.quality += delta

def __increaseQuality(delta, item):
  __sumValueWithQuality(delta, item)

def __decreaseQuality(delta, item):
  __sumValueWithQuality(-1 * delta, item)

def __capQualityOnMaximum(maximum, item):
  if item.quality > maximum:
      item.quality = maximum


IncreaseQuality = curry(__increaseQuality)

DecreaseQuality = curry(__decreaseQuality)

CapQualityOnMaximum = curry(__capQualityOnMaximum)

def QualityIsNeverNegative():
  pass

def SetQualityTo():
  pass

def WhenPastExpiration():
  pass

def WhenSellInPast():
  pass

def UpdateSellInDate():
  pass
