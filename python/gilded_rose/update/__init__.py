from craftsmen import identity, rcompose

from .operators import IncreaseQualityByOne, DecreaseQualityByOne, UpdateSellIn, WhenExpiration, LimitMaximumValueOfQuality, DecreaseQualityBy, WhenSellInLowerThan, SetQualityToZero, QualityIsNeverNegative
from ..entities import constants


maturable = rcompose(
  IncreaseQualityByOne,
  UpdateSellIn,
  WhenExpiration(IncreaseQualityByOne),
  LimitMaximumValueOfQuality,
  QualityIsNeverNegative,
)

maturable = rcompose(
  IncreaseQualityByOne,
  UpdateSellIn,
  WhenExpiration(IncreaseQualityByOne),
  LimitMaximumValueOfQuality,
  QualityIsNeverNegative,
)

legendary = identity

backstage_pass = rcompose(
  IncreaseQualityByOne,
  WhenSellInLowerThan(11, IncreaseQualityByOne),
  WhenSellInLowerThan(6, IncreaseQualityByOne),
  UpdateSellIn,
  WhenExpiration(SetQualityToZero),
  LimitMaximumValueOfQuality,
  QualityIsNeverNegative,
)

conjured = rcompose(
  DecreaseQualityBy(2),
  UpdateSellIn,
  WhenExpiration(DecreaseQualityBy(2)),
  QualityIsNeverNegative,
)

common = rcompose(
  DecreaseQualityByOne,
  UpdateSellIn,
  WhenExpiration(DecreaseQualityByOne),
  QualityIsNeverNegative,
)

def update(item):
  if item.name == "Aged Brie":
      return maturable(item)
  if item.name == "Sulfuras, Hand of Ragnaros":
      return legendary(item)
  if item.name == "Backstage passes to a TAFKAL80ETC concert":
      return backstage_pass(item)
  if item.name == "Conjured":
      return conjured(item)
  return common(item)
