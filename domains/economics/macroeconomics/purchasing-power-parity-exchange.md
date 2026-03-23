---
id: purchasing-power-parity-exchange
title: Purchasing Power Parity and Exchange Rates
domain: economics
course: macroeconomics
prerequisites:
- id: inflation-and-price-level
  type: hard
- id: exchange-rates-macroeconomics
  type: hard
builds-toward:
- interest-rate-parity-international
tags:
- exchange-rates
- parity
- international
stage: formal-systems
status: validated
---

# Purchasing Power Parity and Exchange Rates

## Core Idea
Purchasing power parity (PPP) states that the exchange rate between two currencies equals the ratio of their price levels—a basket of goods should cost the same in both countries after currency conversion. Absolute PPP rarely holds due to trade costs, tariffs, and non-traded goods; relative PPP holds better, predicting exchange rate changes equal inflation differentials. PPP provides a long-run benchmark, though deviations can persist for years.

## Questions

```yaml
- question: "Country A has 8% annual inflation; Country B has 2% annual inflation. What does relative PPP predict about their exchange rate over time?"
  type: multiple-choice
  options:
    - "Country A's currency will appreciate by 6% annually because higher prices signal a stronger economy"
    - "Country A's currency will depreciate by approximately 6% annually — equal to the inflation differential"
    - "The exchange rate will remain stable because relative PPP holds in equilibrium"
    - "Country A's currency will depreciate by 8% annually — equal to its own inflation rate"
  answer: 1
  explanation: "Relative PPP states that exchange rate change ≈ inflation differential between the two countries. Country A's higher inflation erodes its purchasing power faster, so its currency must weaken to keep real prices equivalent. The predicted depreciation is 8% − 2% = 6%, not 8% (option D), because Country B's own 2% inflation partially offsets the differential. Option A reverses the direction — higher inflation weakens, not strengthens, a currency."

- question: "The Big Mac Index shows a Big Mac costs $5 in the US and the equivalent of $3 (after conversion) in Brazil. Why does absolute PPP predict this gap should close, yet it persists in practice?"
  type: multiple-choice
  options:
    - "The Brazilian currency must appreciate significantly before traders can act on the price difference"
    - "Absolute PPP only applies to manufactured goods, not food products"
    - "Restaurant meals cannot be traded across borders, so the arbitrage mechanism that drives price convergence cannot operate"
    - "The gap will close rapidly once financial markets recognize the opportunity"
  answer: 2
  explanation: "Absolute PPP's arbitrage mechanism — buy cheap, sell expensive until prices equalize — only works for tradeable goods. You cannot buy cheap hamburgers in Brazil and ship them to the US for profit. Restaurant meals are a non-traded service. Non-traded goods (haircuts, real estate, restaurant meals) are the main reason absolute PPP fails empirically: the prices that drive exchange rate arbitrage are precisely the prices that can't be arbitraged. This is why the Big Mac Index systematically shows persistent deviations."

- question: "PPP-adjusted GDP figures give a more accurate picture of comparative living standards than market-exchange-rate GDP because they account for differences in price levels across countries."
  type: true-false
  answer: true
  explanation: "A dollar of income buys far more goods in a low-income country than in the US, where prices are higher. Market-rate GDP conversion underestimates the real purchasing power of lower-income country residents. PPP adjustment corrects for this by asking: how much could this income buy at domestic prices? International institutions like the IMF use PPP-adjusted GDP for welfare comparisons precisely because market rates can be highly misleading about actual living standards."

- question: "Under relative PPP, a country with lower inflation than its trading partner should expect its currency to depreciate."
  type: true-false
  answer: false
  explanation: "Relative PPP predicts depreciation for the high-inflation country, not the low-inflation one. Higher inflation means a currency's purchasing power erodes faster — so the currency must weaken to maintain equivalent real prices across borders. Lower inflation means relatively slower erosion of purchasing power, so the currency should appreciate (or depreciate less) relative to the high-inflation partner. Confusing the direction here is the most common error in applying relative PPP."

- question: "Why does relative PPP hold better over long time horizons (5–10 years) than short ones (months), and what forces cause short-run exchange rates to deviate substantially from PPP?"
  type: short-answer
  answer: "Over long horizons, the cumulative effect of inflation differentials dominates, gradually driving exchange rates toward PPP values. In the short run, exchange rates are moved primarily by capital flows, interest rate differentials, risk sentiment, and monetary policy shocks — forces unrelated to price level differences. These short-run drivers can push exchange rates far from PPP and keep them there for years before the underlying inflation differential reasserts itself."
  explanation: "PPP is a long-run anchor, not a short-run predictor. The mechanisms that push exchange rates toward PPP (trade flows, relative purchasing power) work slowly compared to the speed of capital markets. A sudden risk-off episode can move an exchange rate by 10% in a day, overwhelming any PPP signal. This is why currency investors who trade on PPP misvaluation typically work with multi-year time horizons."
```

## Explainer

From your study of inflation and price levels, you know that a rising price level means each unit of currency buys less goods and services — purchasing power erodes. From your study of exchange rates, you know that the exchange rate converts prices between currencies. **Purchasing power parity** connects these two ideas with a simple arbitrage argument: if the same good costs different amounts in two countries after currency conversion, traders should buy it where it's cheap and sell it where it's expensive, driving prices toward equality. PPP is essentially the law of one price applied to entire economies.

**Absolute PPP** states that the exchange rate should equal the ratio of price levels: E = P_domestic / P_foreign. If a basket of goods costs $100 in the US and €80 in Europe, the exchange rate should be $1.25/€. This is intuitively appealing but empirically weak for a clear reason: many goods cannot be freely traded across borders. Haircuts, restaurant meals, and real estate are non-traded goods — you cannot buy them in one country and ship them to another to profit from price differences. Trade costs, tariffs, and regulatory differences also drive persistent price gaps for goods that technically could be traded. The famous **Big Mac Index** (The Economist) illustrates absolute PPP playfully: it tracks how McDonald's burger prices around the world compare after conversion, and the persistent gaps reveal how far exchange rates deviate from parity in practice.

**Relative PPP** is the more empirically useful form. It doesn't claim prices are equalized; it claims that exchange rate changes should equal inflation differentials. If Country A has 6% inflation and Country B has 2%, the exchange rate should depreciate by approximately 4% per year (Country A's currency weakens). The intuition is symmetric: high inflation erodes purchasing power, so the currency should weaken to maintain equivalent real prices over time. Relative PPP holds much better than absolute PPP over long horizons — it is a decent predictor of exchange rate trends over 5–10 year periods — but it can fail dramatically in the short run when capital flows, risk appetite, and monetary shocks dominate exchange rate dynamics.

PPP serves two practical roles. First, it is the standard benchmark for **long-run exchange rate forecasting**: if a currency is substantially undervalued relative to PPP (as estimated by the IMF or World Bank price level comparisons), the expectation is that it will appreciate toward parity over years, not months. Second, PPP-adjusted GDP figures — used extensively by international institutions — convert countries' incomes into comparable units by adjusting for price level differences rather than just using market exchange rates. This matters because a dollar buys far more in a low-income country than in the US, making market-rate GDP comparisons misleading about actual living standards. The gap between a country's market exchange rate and its PPP exchange rate tends to close as the country develops and its price level converges toward rich-country levels — this is the **Balassa-Samuelson effect**, which you'll encounter in international economics.
