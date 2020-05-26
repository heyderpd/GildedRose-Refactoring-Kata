from craftsmen import identity, rcompose

from .operators import IncreaseQuality, DecreaseQuality, CapQualityOnMaximum, QualityIsNeverNegative, SetQualityTo, WhenPastExpiration, WhenSellInPast, UpdateSellInDate
from ..entities import constants


maturable = rcompose(
  IncreaseQuality(1),
  UpdateSellInDate,
  WhenPastExpiration(IncreaseQuality(1)),
  CapQualityOnMaximum(constants.MAXIMUM_QUALITY),
  QualityIsNeverNegative(0),
)

legendary = identity

backstage_pass = rcompose(
  IncreaseQuality(1),
  WhenSellInPast(11, IncreaseQuality(1)),
  WhenSellInPast(6, IncreaseQuality(1)),
  UpdateSellInDate,
  WhenPastExpiration(SetQualityTo(0)),
  CapQualityOnMaximum(constants.MAXIMUM_QUALITY),
  QualityIsNeverNegative(0),
)

conjured = rcompose(
  DecreaseQuality(2),
  UpdateSellInDate,
  WhenPastExpiration(DecreaseQuality(2)),
  QualityIsNeverNegative(0),
)

common = rcompose(
  DecreaseQuality(1),
  UpdateSellInDate,
  WhenPastExpiration(DecreaseQuality(1)),
  QualityIsNeverNegative(0),
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
