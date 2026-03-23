---
id: relative-purchasing-power-parity
title: Relative Purchasing Power Parity and Inflation Differentials
domain: economics
course: macroeconomics
prerequisites:
- id: purchasing-power-parity-absolute
  type: hard
- id: inflation-and-price-level
  type: soft
builds-toward:
- exchange-rate-dynamics
tags:
- ppp
- relative
- inflation
- exchange-rates
stage: advanced
status: validated
---

# Relative Purchasing Power Parity and Inflation Differentials

## Core Idea
Relative PPP states that percentage change in exchange rate should equal inflation rate differential between countries. If US inflation exceeds eurozone by 2%, dollar should depreciate 2%.

## How It's Best Learned
Compare inflation rates across countries over a decade and track exchange rate changes. Show high-inflation currencies tend to depreciate. Verify the formula.

## Common Misconceptions
- Assuming relative PPP predicts short-term movements.
- Treating PPP as only exchange rate determinant.
- Forgetting real exchange rates can vary persistently.

## Questions

```yaml
- question: "Country A has 6% annual inflation; Country B has 2% annual inflation. According to relative PPP, what should happen to Country A's exchange rate over time?"
  type: multiple-choice
  options:
    - "Country A's currency should appreciate by 4%, since higher inflation reflects a stronger growing economy"
    - "Country A's currency should depreciate by approximately 4% to offset the higher inflation and maintain equal purchasing power"
    - "The exchange rate should remain unchanged, since PPP only describes price levels, not exchange rate changes"
    - "The outcome depends on which country has higher nominal interest rates"
  answer: 1
  explanation: "Relative PPP states that %ΔS ≈ π_domestic − π_foreign. Country A's prices are rising 4 percentage points faster than Country B's, making Country A's goods progressively more expensive in international terms. For purchasing power to remain equalized, Country A's currency must depreciate by approximately 4% — enough to offset its higher inflation. The misconception in option A reverses the direction: higher inflation erodes purchasing power, it does not strengthen the currency."

- question: "A country has 12% annual inflation, yet its currency appreciates for three consecutive years due to surging capital inflows. The best interpretation of this pattern is:"
  type: multiple-choice
  options:
    - "Relative PPP must be wrong as a theory, since inflation should cause depreciation"
    - "Short-run exchange rates are driven by many forces beyond inflation differentials — PPP describes a long-run tendency, not a short-run prediction"
    - "Capital inflows will automatically cause domestic inflation to fall, eventually validating PPP"
    - "The real exchange rate must therefore be appreciating, contradicting PPP"
  answer: 1
  explanation: "Relative PPP is a long-run equilibrium condition, not a short-run forecasting tool. In the short and medium run, capital flows, risk sentiment, monetary policy surprises, and commodity prices can dominate over inflation differentials, causing large and sustained deviations from PPP-implied rates. The theory is most useful for diagnosing long-run misalignment and for explaining exchange rate trends over decades across large inflation differentials — not for predicting next quarter's moves."

- question: "Relative PPP implies that the real exchange rate between two countries should remain constant over time."
  type: true-false
  answer: true
  explanation: "The real exchange rate equals the nominal exchange rate adjusted for relative price levels: Q = S × (P_foreign / P_domestic). Relative PPP states that the nominal exchange rate changes by exactly the inflation differential (%ΔS = π_d − π_f), which means the ratio of price levels does not change in real terms. Therefore Q remains constant — PPP is precisely the claim that real exchange rates are stable. The empirical finding that real exchange rates drift persistently is the main evidence against PPP holding in practice."

- question: "Relative PPP is most useful for predicting exchange rate movements over the next quarter in response to monthly inflation data."
  type: true-false
  answer: false
  explanation: "Relative PPP is a long-run relationship, not a short-run predictor. Over quarters or even a few years, the factors that drive exchange rates in the short run — capital flows, interest rate differentials, risk appetite, central bank intervention — overwhelm the inflation differential signal. Relative PPP has its strongest empirical support over multi-decade horizons and when comparing countries with large inflation gaps. Using it for quarterly forecasting leads to poor predictions."

- question: "Explain what it means for the real exchange rate to deviate from its PPP-implied value, and why relative PPP implies it should be constant in the long run."
  type: short-answer
  answer: "The real exchange rate (Q = S × P_foreign/P_domestic) measures whether goods in one country are systematically cheaper or more expensive than in another after adjusting for the nominal exchange rate. A real exchange rate above 1 means domestic goods are expensive relative to foreign goods in international terms; below 1 means they are cheap. Relative PPP claims that nominal exchange rate changes exactly offset inflation differentials, leaving Q unchanged — purchasing power parity is maintained. In practice, capital flows, monetary policy, and risk premiums cause Q to deviate persistently, meaning currencies can be fundamentally over- or undervalued for years."
  explanation: "The deviation of the real exchange rate from PPP is the core concept for diagnosing currency misalignment. Countries with persistently overvalued real exchange rates (e.g., export competitiveness eroded by inflation without commensurate depreciation) often face current account deficits and eventual currency crises."
```

## Explainer

From absolute PPP, you know the core arbitrage logic: if a basket of goods costs $100 in the US and €90 in the eurozone, the exchange rate should be roughly $1.11 per euro so that purchasing power is equalized. Relative PPP takes that idea one step further by asking: not what is the exchange rate level today, but how should the exchange rate change over time as price levels in the two countries evolve at different rates?

The answer follows directly from the absolute PPP logic. If the US has 4% inflation and the eurozone has 2% inflation, then US prices are rising 2 percentage points faster than eurozone prices. The same basket that equalizes purchasing power today will no longer do so next year, because US prices have grown faster. For purchasing power to remain equalized, the **dollar must depreciate** by approximately 2% — enough to offset the US's higher inflation rate. The relative PPP formula states: %ΔS ≈ π_domestic − π_foreign, where S is the exchange rate (domestic currency per unit of foreign) and π denotes inflation rates. The currency of the higher-inflation country should depreciate.

This relationship has strong intuitive logic: a country that persistently inflates faster than its trading partners is making its goods progressively more expensive in global terms. Unless its currency depreciates to compensate, its exporters lose competitiveness and demand for the currency falls — the market mechanism that drives the depreciation. Historically, this holds quite well over long horizons and across large inflation differentials. Countries with hyperinflation (Argentina, Zimbabwe, Turkey) have seen their currencies depreciate in rough proportion to their excess inflation over time.

The critical limitation is that relative PPP is a **long-run relationship**, not a short-run predictor. Over quarters or even a few years, exchange rates deviate substantially from PPP-implied levels because of capital flows, risk sentiment, central bank intervention, commodity prices, and monetary policy surprises. A country can have high inflation while its currency appreciates for years if capital inflows are strong enough. This means the **real exchange rate** — the nominal exchange rate adjusted for the inflation differential — can deviate from 1 for extended periods. Relative PPP implies the real exchange rate should be constant over time; in practice, real exchange rates drift persistently, reflecting the many forces beyond inflation that determine currency values. The theory is most useful as a benchmark for long-run forecasting and for diagnosing whether a currency is fundamentally misaligned, not for predicting next quarter's moves.
