---
id: exchange-rate-purchasing-power-parity
title: Exchange Rates and Purchasing Power Parity
domain: economics
course: macroeconomics
prerequisites:
- id: exchange-rates-macroeconomics
  type: hard
- id: inflation-and-price-level
  type: hard
builds-toward:
  - current-account-and-external-balance
tags:
- exchange-rates
- international
- ppp
stage: abstract-reasoning
status: draft
---
# Exchange Rates and Purchasing Power Parity

## Core Idea
Purchasing Power Parity (PPP) states that the exchange rate between two currencies should equal the ratio of their price levels: e = P / P*. Absolute PPP implies the law of one price holds everywhere; relative PPP states that exchange rate changes equal inflation differentials. PPP holds approximately in the very long run but deviates substantially in the short to medium term due to non-tradable goods, transportation costs, and capital flows.

## Explainer

From your understanding of exchange rates, you know that e (the nominal exchange rate) tells you how many units of foreign currency one unit of domestic currency buys. From your study of inflation, you know that price levels differ across countries and change over time. **Purchasing Power Parity** connects these two concepts through a simple arbitrage argument: if the same good costs $10 in the US and €8 in Europe, the exchange rate should be 0.8 €/$. If it weren't, traders could buy in one market and sell in the other for a risk-free profit — **arbitrage** would push the exchange rate toward the PPP level.

This is the **law of one price**, and when applied to a *basket* of goods rather than a single commodity, it becomes absolute PPP: e = P/P*. The **Big Mac index**, published by The Economist since 1986, is the most famous illustration — it compares the dollar price of a Big Mac in different countries and asks whether currencies are over- or undervalued relative to what PPP would predict. A country where a Big Mac costs $2 when it costs $6 in the US has a currency that is "undervalued" by 67% according to this crude measure. The intuition is real even if the implementation is imprecise: countries with very cheap tradable goods tend to have undervalued currencies.

**Relative PPP** is the more empirically useful version. Rather than claiming that price levels determine exchange rate levels, it claims that *changes* in exchange rates track *differences* in inflation rates: %Δe ≈ π − π* (domestic inflation minus foreign inflation). If the US has 5% inflation and the Eurozone has 2%, the dollar should depreciate by roughly 3% relative to the euro over that period. This preserves real purchasing power across borders. Relative PPP performs reasonably well over long horizons — decades — when inflation differentials are large, as between developed and emerging market economies. It fails badly in the short run because exchange rates are driven by financial flows, interest rate differentials, risk sentiment, and speculation, none of which have direct links to current inflation.

Why does PPP fail in the short to medium run? The most important reason is **non-tradable goods**. Haircuts, restaurant meals, and real estate cannot be arbitraged across borders. A dollar stretches much further in Vietnam than in Norway not because of currency mispricing but because local services are genuinely cheaper. This is the **Balassa-Samuelson effect**: countries with high productivity in tradable goods have high wages across the economy, pushing up the prices of non-tradables and making the overall price level high relative to PPP. As a result, PPP exchange rates — widely used by the IMF and World Bank to compare GDP across countries — systematically show rich countries as having overvalued currencies and poor countries as undervalued. The gap reflects real differences in purchasing power over non-tradables, not a correctable currency misalignment.
