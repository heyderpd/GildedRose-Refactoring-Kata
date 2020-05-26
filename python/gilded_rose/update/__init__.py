from craftsmen import identity, curry, placeholder, p, compose, rcompose, cmap, map

from .operators import IncreaseQuality, DecreaseQuality, CapQualityOnMaximum, QualityIsNeverNegative, SetQualityTo, WhenPastExpiration, WhenSellInPast, UpdateSellInDate


legendary = identity

maturable = compose([
  IncreaseQuality(),
  UpdateSellInDate(),
  WhenPastExpiration(IncreaseQuality()),
  CapQualityOnMaximum(),
  QualityIsNeverNegative(),
])

common = compose([
  DecreaseQuality(),
  UpdateSellInDate(),
  WhenPastExpiration(DecreaseQuality()),
  QualityIsNeverNegative(),
])

backstage_pass = compose([
  IncreaseQuality(),
  WhenSellInPast(11, IncreaseQuality()),
  WhenSellInPast(6, IncreaseQuality()),
  UpdateSellInDate(),
  WhenPastExpiration(SetQualityTo(0)),
  CapQualityOnMaximum(),
  QualityIsNeverNegative(),
])

conjured = compose([
  DecreaseQuality(2),
  UpdateSellInDate(),
  WhenPastExpiration(DecreaseQuality(2)),
  QualityIsNeverNegative(),
])

def update(self, item):
  pass
