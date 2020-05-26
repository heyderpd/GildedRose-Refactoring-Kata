from craftsmen import identity, curry, placeholder, p, compose, rcompose, cmap, map

item_behaviour = {
  ItemType.legendary: [],

  ItemType.maturable: [
    IncreaseQuality(),
    UpdateSellInDate(),
    WhenPastExpiration(IncreaseQuality()),
    CapQualityOnMaximum(),
    QualityIsNeverNegative(),
  ],

  ItemType.common: [
    DecreaseQuality(),
    UpdateSellInDate(),
    WhenPastExpiration(DecreaseQuality()),
    QualityIsNeverNegative(),
  ],

  ItemType.backstage_pass: [
    IncreaseQuality(),
    WhenSellInPast(11, IncreaseQuality()),
    WhenSellInPast(6, IncreaseQuality()),
    UpdateSellInDate(),
    WhenPastExpiration(SetQualityTo(0)),
    CapQualityOnMaximum(),
    QualityIsNeverNegative(),
  ],

  ItemType.conjured: [
    DecreaseQuality(2),
    UpdateSellInDate(),
    WhenPastExpiration(DecreaseQuality(2)),
    QualityIsNeverNegative(),
  ],
}

def update(self, item):
  pass
