---
id: exchange-rate-dynamics
title: Exchange Rate Dynamics and Purchasing Power Parity
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: mundell-fleming-open-economy
  type: hard
- id: exchange-rates-macroeconomics
  type: hard
builds-toward:
- balance-of-payments-capital-flows
tags:
- exchange-rates
- ppp
- currency
stage: expert
status: draft
---

# Exchange Rate Dynamics and Purchasing Power Parity

## Core Idea
Exchange rates equilibrate the supply and demand for currencies in foreign exchange markets. Purchasing power parity (PPP) states that the real exchange rate (purchasing power) is equalized across countries in the long run; the nominal rate adjusts to offset inflation differences. Deviations from PPP reflect differences in asset returns, interest rates, and inflation expectations. Exchange rate dynamics are highly volatile in the short run because currency markets respond immediately to financial news about interest rates and return differentials; connections to fundamentals are weaker in the short run.

## Questions

```yaml
- question: "The Federal Reserve unexpectedly raises U.S. interest rates. According to the Dornbusch overshooting model, what happens to the dollar in the short run versus the long run?"
  type: multiple-choice
  options:
    - "The dollar depreciates immediately as investors sell U.S. assets anticipating future inflation, then appreciates gradually"
    - "The dollar appreciates gradually over several years as capital flows in from abroad seeking higher returns"
    - "The dollar appreciates immediately beyond its new long-run equilibrium, then depreciates gradually back toward it"
    - "The dollar remains stable in the short run because goods prices offset the interest rate effect quickly"
  answer: 2
  explanation: "This is the Dornbusch overshooting mechanism. Asset prices (exchange rates) adjust instantly; goods prices are sticky. Higher U.S. rates attract capital immediately, causing a large, sudden appreciation — beyond the new PPP-justified long-run level. Then, as uncovered interest parity must hold over time, the dollar gradually depreciates back. The overshoot is necessary: if the dollar jumped only to its long-run level, there would be no expected future depreciation to equalize returns, violating UIP."

- question: "Relative PPP predicts that if U.S. inflation exceeds European inflation by 2%, the dollar should depreciate 2% annually. This prediction works reasonably over decades but fails over months. Why?"
  type: multiple-choice
  options:
    - "PPP only applies to non-traded goods, which are excluded from standard inflation measures"
    - "In the short run, currencies are traded as financial assets responding to interest rate differentials, risk sentiment, and capital flows — not primarily to price level differences"
    - "Central banks systematically intervene to prevent the exchange rate changes that PPP predicts"
    - "Inflation data is published with a multi-year lag, preventing markets from responding to it"
  answer: 1
  explanation: "Currencies are financial assets whose prices reflect expected future returns, not just the current price level. In the short run, a 25-basis-point surprise interest rate change moves exchange rates more than years of accumulated inflation differential. Capital flows respond to return differentials instantaneously; goods arbitrage operates over months or years. PPP reasserts itself over long horizons as goods markets gradually adjust, but it is dominated by financial market forces in the short run."

- question: "Relative purchasing power parity holds much better as a prediction over horizons of several decades than over short horizons of months or quarters."
  type: true-false
  answer: true
  explanation: "Empirically, this is well-established. Over horizons of 20–30 years, real exchange rates do tend to revert toward PPP-implied levels, and inflation differentials explain a large portion of nominal exchange rate movements. Over months or quarters, however, real exchange rates can diverge dramatically from PPP, driven by capital flows, interest rate differentials, and sentiment. The short-run disconnect is precisely what Dornbusch's overshooting model explains."

- question: "When a country's interest rates rise, investors buy its currency to earn higher returns, and the currency will continue appreciating for as long as the interest rate differential persists."
  type: true-false
  answer: false
  explanation: "Uncovered interest parity (UIP) predicts the opposite trajectory after the initial jump. The currency appreciates immediately (often overshooting), but must then be expected to depreciate over time to equalize returns. If domestic rates are 2% above foreign rates, the currency must be expected to depreciate by roughly 2% per year for returns to equalize. An investor who bought the currency at the peak gets the interest rate gain but loses on the subsequent depreciation — in theory, the two exactly offset. Continued appreciation would create a free-money arbitrage that markets would eliminate."

- question: "Explain exchange rate overshooting: why does a monetary contraction cause a currency to appreciate beyond its new long-run equilibrium, and what drives it back?"
  type: short-answer
  answer: "Monetary contraction raises interest rates. Asset prices (exchange rates) adjust instantly — capital flows in, appreciating the currency immediately. But goods prices are sticky and adjust slowly, so the real exchange rate overshoots its new equilibrium. Uncovered interest parity requires that the now-overvalued currency be expected to depreciate going forward, which provides the return equalization. As goods prices eventually adjust and inflation falls in line with the lower money growth, the exchange rate gradually depreciates back toward the new long-run PPP-consistent level."
  explanation: "The key to overshooting is the asymmetry between asset market adjustment (instantaneous) and goods market adjustment (gradual). The exchange rate must do extra work in the short run to compensate for prices that cannot yet move. This explains why exchange rate volatility far exceeds what inflation differentials alone would predict: currencies absorb all the adjustment that sticky prices cannot, and then partially reverse as those prices catch up. Dornbusch (1976) formalized this insight and it remains one of the most influential results in open-economy macroeconomics."
```

## Explainer

From the Mundell-Fleming model, you know that in an open economy with capital mobility, monetary and fiscal policy have different effects depending on whether the exchange rate is fixed or floating. Exchange rate dynamics takes this further by asking: what determines the level and movement of exchange rates over time, and why are currency markets so much more volatile than the goods markets they supposedly reflect?

**Purchasing power parity** (PPP) provides the long-run anchor. The idea is intuitive: if the same basket of goods costs $100 in the United States and €90 in Europe, the exchange rate should be roughly $1.11 per euro, because otherwise identical goods would be cheaper in one country, creating arbitrage opportunities. **Absolute PPP** says the exchange rate equals the ratio of price levels; **relative PPP** says the exchange rate changes at a rate equal to the inflation differential. If U.S. inflation runs 2 percentage points above European inflation, the dollar should depreciate by 2% per year against the euro. Empirically, relative PPP holds reasonably well over decades but fails badly over months and years — real exchange rates can deviate from PPP for prolonged periods.

The short-run disconnect between exchange rates and price levels arises because currencies are financial assets, not just units for pricing goods. The **uncovered interest parity** (UIP) condition states that the expected return on holding domestic and foreign bonds should be equal when expressed in a common currency. If U.S. interest rates rise above European rates, investors buy dollar-denominated assets, appreciating the dollar *immediately* — but UIP predicts the dollar must then be expected to *depreciate* over time to equalize returns. This creates the characteristic pattern of exchange rate **overshooting**, formalized by Rudiger Dornbusch: because goods prices are sticky while asset prices adjust instantly, a monetary contraction causes the exchange rate to jump beyond its new long-run equilibrium and then gradually return. The exchange rate does more work in the short run precisely because prices cannot adjust quickly enough.

This framework explains why exchange rates are notoriously difficult to forecast. In the short run, they respond to interest rate surprises, risk sentiment, capital flow reversals, and speculative positioning — all of which move faster and less predictably than inflation or trade balances. The connection to fundamentals (PPP, current accounts, productivity differentials) reasserts itself only over horizons of several years. For policymakers, the implication is that exchange rate movements are a powerful but unpredictable transmission channel: a central bank raising interest rates will strengthen the currency, tightening financial conditions through both the interest rate and the exchange rate, but the magnitude and timing of the currency response are inherently uncertain.
