from craftsmen import identity, rcompose

from .operators import IncreaseQualityByOne, DecreaseQualityByOne, UpdateSellIn, WhenExpiration, LimitMaximumValueOfQuality, DecreaseQualityBy, WhenSellInEqualOrLowerThan, SetQualityToZero, QualityIsNeverNegative


maturable = rcompose(
  IncreaseQualityByOne,
  UpdateSellIn,
  LimitMaximumValueOfQuality,
  QualityIsNeverNegative,
)

legendary = identity

backstage_pass = rcompose(
  IncreaseQualityByOne,
  WhenSellInEqualOrLowerThan(10, IncreaseQualityByOne),
  WhenSellInEqualOrLowerThan(5, IncreaseQualityByOne),
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
