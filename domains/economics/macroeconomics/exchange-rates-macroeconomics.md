---
id: exchange-rates-macroeconomics
title: Exchange Rates
domain: economics
course: macroeconomics
prerequisites:
- id: comparative-advantage-and-trade
  type: hard
- id: supply-and-demand-basics
  type: hard
- id: inflation-and-price-level
  type: soft
builds-toward:
- balance-of-payments
- open-economy-macroeconomics
tags:
- exchange-rate
- nominal
- real
- appreciation
- depreciation
- purchasing-power-parity
stage: abstract-reasoning
status: validated
---

# Exchange Rates

## Core Idea
The exchange rate is the price of one currency in terms of another. The nominal exchange rate is the quoted market price; the real exchange rate adjusts for relative price levels, measuring international competitiveness. A currency appreciates when it buys more foreign currency (domestic goods become more expensive to foreigners, hurting exports) and depreciates when it buys less (boosting exports but raising import costs). Purchasing power parity (PPP) predicts that exchange rates equalize the price of identical goods across countries in the long run. Exchange rates are determined by trade flows, interest rate differentials, inflation expectations, and speculation.

## How It's Best Learned
Compute a real exchange rate from nominal rate and price level data. Analyze what happens to US net exports when the dollar appreciates 10%. Examine the Big Mac Index as an illustration of PPP.

## Common Misconceptions
- A stronger (appreciated) currency is not always better — it hurts exporters and can worsen the trade balance.
- Nominal and real exchange rate movements often diverge substantially over short periods.
- PPP holds in the very long run but is a poor predictor of short-run exchange rate movements.

## Questions

```yaml
- question: "The US dollar appreciates significantly against the euro. Which of the following effects would this most directly cause?"
  type: multiple-choice
  options:
    - "US exports become cheaper for European buyers, boosting US export sales"
    - "US exports become more expensive for European buyers, hurting US export sales"
    - "US imports become more expensive for American consumers"
    - "European tourists find the US more affordable to visit"
  answer: 1
  explanation: "When the dollar appreciates, each euro buys fewer dollars — meaning foreigners must spend more of their own currency to buy the same US goods. This makes US exports more expensive to foreign buyers and reduces demand for them. Option C is wrong: a stronger dollar makes imports *cheaper* for Americans, not more expensive. Option D is wrong: a stronger dollar makes the US *more* expensive for foreign tourists, not less."

- question: "Country A has 8% annual inflation while Country B has 2%. The nominal exchange rate between them is unchanged over the year. What has happened to Country A's real exchange rate and trade competitiveness?"
  type: multiple-choice
  options:
    - "Country A has become more competitive because its currency remained stable"
    - "Country A has become less competitive because its goods are now relatively more expensive in real terms"
    - "Competitiveness is unchanged because the nominal exchange rate did not move"
    - "Country A has become more competitive because inflation signals faster economic growth"
  answer: 1
  explanation: "The real exchange rate adjusts the nominal rate for relative price levels. If Country A's prices rose 8% while Country B's rose only 2%, Country A's goods are now about 6% more expensive in real terms — even though the nominal rate is unchanged. This is why economists focus on real exchange rates when analyzing trade: a nominal rate that holds steady while domestic inflation exceeds foreign inflation represents a real appreciation and a loss of competitiveness."

- question: "A currency appreciation that merely reflects higher domestic inflation relative to a trading partner does not represent a genuine loss of international competitiveness."
  type: true-false
  answer: true
  explanation: "The real exchange rate = (Nominal rate × Domestic price level) / Foreign price level. If the nominal rate depreciates (currency weakens) by exactly as much as domestic inflation exceeds foreign inflation, the real exchange rate is unchanged — goods are no more or less expensive in real terms. Conversely, a nominal appreciation that only tracks inflation differentials leaves the real rate and competitiveness unchanged. This is why the real exchange rate, not the nominal rate, is the appropriate measure of trade competitiveness."

- question: "A stronger national currency is generally beneficial for the overall economy because it increases purchasing power and therefore improves economic welfare."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about exchange rates. A stronger currency creates winners and losers: it benefits importers (cheaper foreign goods), consumers of imported products, and those traveling abroad, but it hurts exporters (their goods become more expensive to foreign buyers) and import-competing domestic manufacturers. For an export-dependent economy like Germany or South Korea, a strong currency can seriously damage economic output. There is no unambiguously 'better' exchange rate level."

- question: "Why do economists focus on the real exchange rate rather than the nominal exchange rate when analyzing a country's international trade competitiveness?"
  type: short-answer
  answer: "The nominal exchange rate is the quoted market price of one currency in terms of another, but it does not account for differences in price levels between countries. What matters for trade competitiveness is whether a country's goods are actually cheap or expensive for foreign buyers after adjusting for inflation. The real exchange rate makes this adjustment: Real rate = (Nominal rate × Domestic price level) / Foreign price level. A country with 10% higher inflation than its trading partner becomes less competitive even if the nominal rate is unchanged, because its goods now cost more in real terms."
  explanation: "The key insight is that trade flows respond to relative prices in real terms, not the nominal currency price. PPP theory formalizes this: in the long run, exchange rates should equalize the purchasing power of currencies across countries. This also explains why economists use PPP-adjusted GDP comparisons rather than nominal GDP when comparing living standards across countries with different price levels."
```

## Explainer

You've studied comparative advantage and know that countries benefit from specializing and trading. Exchange rates are the mechanism that makes this work in practice — they determine the relative prices of goods across national borders. The **nominal exchange rate** is simply the market price of one currency in terms of another: if 1 USD = 0.93 EUR, the dollar has a nominal exchange rate of 0.93 against the euro. Like any price, this is determined by supply and demand — the demand for dollars comes from foreigners buying US goods, services, and assets; the supply comes from Americans buying foreign goods, services, and assets.

The **real exchange rate** goes one step deeper: it adjusts the nominal rate for relative price levels. Real exchange rate = (Nominal rate × Domestic price level) / Foreign price level. This measures actual international competitiveness — whether your goods are genuinely cheap or expensive to foreign buyers after accounting for inflation differences. If US inflation is 5% while European inflation is 2%, the dollar will buy fewer euros in real terms even if the nominal rate is unchanged, because US goods have become relatively more expensive. This is why economists focus on real exchange rates when analyzing trade flows: a nominal appreciation that merely reflects higher domestic inflation doesn't hurt competitiveness, but a real appreciation does.

**Purchasing power parity (PPP)** is the long-run anchor for exchange rates. The Big Mac Index — comparing McDonald's burger prices across countries — is a famous illustration: if a Big Mac costs $5 in the US and €4 in Germany, PPP implies the exchange rate should be 0.80 €/$ in the long run. If the dollar is currently stronger, it's "overvalued" relative to PPP. The logic is arbitrage: if identical goods are cheaper in one country, demand for that country's currency should rise until prices equalize. In practice, PPP holds poorly in the short run — financial flows, speculation, and sticky prices dominate exchange rate movements over months or even years. But over decades, currencies tend to drift toward PPP levels, making it useful for long-run forecasting and for comparing living standards across countries.

Short-run exchange rate determination is driven by **interest rate differentials** and **expectations**. Higher interest rates attract capital inflows — foreign investors sell their currency to buy yours in order to invest in your higher-yielding assets. This increased demand appreciates your currency. The **uncovered interest parity** condition formalizes this: the expected return on domestic and foreign assets should be equal, implying that a country with higher interest rates should expect its currency to depreciate — otherwise there would be riskless profit opportunities. In practice, exchange rates are among the hardest financial variables to forecast, and the policy tradeoffs are genuine: a strong currency benefits import-reliant industries and reduces inflation via cheaper imports, while hurting exporters and domestic manufacturers.
