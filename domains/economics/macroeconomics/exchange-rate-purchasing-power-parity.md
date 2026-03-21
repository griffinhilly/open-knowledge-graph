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

## Questions

```yaml
- question: "The Big Mac Index shows that a Big Mac costs $6 in the US and the equivalent of $8 in Norway. According to PPP theory, what does this imply about the Norwegian krone?"
  type: multiple-choice
  options:
    - "The krone is undervalued and should appreciate to bring prices into line"
    - "The krone appears overvalued — a dollar buys less in Norway than PPP would predict"
    - "Norwegian food production is less efficient than in the US, explaining the higher price"
    - "Norwegian inflation must be lower than US inflation, which caused this gap"
  answer: 1
  explanation: "If PPP held perfectly, the same good would cost the same in both countries after currency conversion. A Big Mac costing more in Norway (in dollar terms) implies the krone is 'overvalued' relative to PPP — your dollar buys less there than the exchange rate suggests it should. However, the Balassa-Samuelson effect explains this isn't simply a correctable mispricing: Norway's high productivity raises wages economy-wide, pushing up non-tradable prices like restaurant labor, making the overall price level genuinely high."

- question: "The US has 6% annual inflation while the Eurozone has 2%. According to relative PPP, what should happen to the dollar/euro exchange rate?"
  type: multiple-choice
  options:
    - "The dollar should appreciate by about 4% against the euro"
    - "The dollar should depreciate by about 4% against the euro"
    - "The exchange rate should not change because both countries still have positive inflation"
    - "The euro should depreciate because the Eurozone has lower economic growth"
  answer: 1
  explanation: "Relative PPP states that exchange rate changes track inflation differentials: %Δe ≈ π − π*. If US inflation exceeds Eurozone inflation by 4 percentage points, the dollar's purchasing power erodes faster, so it should depreciate by roughly 4% against the euro. It is the differential that drives the direction — even with both rates positive, the country with higher inflation sees its currency weaken."

- question: "According to relative PPP, a country with consistently higher inflation than its trading partners should see its currency depreciate over time."
  type: true-false
  answer: true
  explanation: "This is the core prediction of relative PPP. If a country's prices rise faster than its trading partners', its goods become relatively more expensive abroad, eroding export competitiveness and putting downward pressure on the exchange rate. Over long horizons — especially when inflation differentials are large, as between developed and emerging-market economies — this relationship holds empirically."

- question: "If the Big Mac Index identifies a currency as 'overvalued,' arbitrage should quickly correct the gap, just as with overpriced tradable goods."
  type: true-false
  answer: false
  explanation: "PPP-based mispricings in the Big Mac Index cannot be arbitraged away. A Big Mac cannot be shipped from a cheap country to an expensive one. More importantly, much of the 'overvaluation' in rich countries reflects the Balassa-Samuelson effect: high wages push up non-tradable prices (restaurant labor, services), making overall price levels genuinely high — not a temporary misalignment waiting to be corrected. Only tradable goods face arbitrage pressure; services do not."

- question: "Explain why PPP comparisons systematically show rich countries as having 'overvalued' currencies, using the concept of non-tradable goods."
  type: short-answer
  answer: "Rich countries have high productivity in tradable goods, which raises wages economy-wide — including for non-tradable services like haircuts, restaurant meals, and housing. These services can't be imported to arbitrage away the price difference. So the overall price level in rich countries is genuinely higher than in poor countries — not because their currencies are mispriced, but because local services cost more. PPP comparisons register this as 'overvaluation' when it is actually a real structural difference (the Balassa-Samuelson effect)."
  explanation: "PPP assumes the same basket of goods should cost the same everywhere after currency conversion. But non-tradable goods make up a large share of that basket, and their prices reflect local wages and productivity rather than international arbitrage. A dollar genuinely buys more in Vietnam than Norway because services are cheaper there — and no currency adjustment can change that real structural difference."
```

## Explainer

From your understanding of exchange rates, you know that e (the nominal exchange rate) tells you how many units of foreign currency one unit of domestic currency buys. From your study of inflation, you know that price levels differ across countries and change over time. **Purchasing Power Parity** connects these two concepts through a simple arbitrage argument: if the same good costs $10 in the US and €8 in Europe, the exchange rate should be 0.8 €/$. If it weren't, traders could buy in one market and sell in the other for a risk-free profit — **arbitrage** would push the exchange rate toward the PPP level.

This is the **law of one price**, and when applied to a *basket* of goods rather than a single commodity, it becomes absolute PPP: e = P/P*. The **Big Mac index**, published by The Economist since 1986, is the most famous illustration — it compares the dollar price of a Big Mac in different countries and asks whether currencies are over- or undervalued relative to what PPP would predict. A country where a Big Mac costs $2 when it costs $6 in the US has a currency that is "undervalued" by 67% according to this crude measure. The intuition is real even if the implementation is imprecise: countries with very cheap tradable goods tend to have undervalued currencies.

**Relative PPP** is the more empirically useful version. Rather than claiming that price levels determine exchange rate levels, it claims that *changes* in exchange rates track *differences* in inflation rates: %Δe ≈ π − π* (domestic inflation minus foreign inflation). If the US has 5% inflation and the Eurozone has 2%, the dollar should depreciate by roughly 3% relative to the euro over that period. This preserves real purchasing power across borders. Relative PPP performs reasonably well over long horizons — decades — when inflation differentials are large, as between developed and emerging market economies. It fails badly in the short run because exchange rates are driven by financial flows, interest rate differentials, risk sentiment, and speculation, none of which have direct links to current inflation.

Why does PPP fail in the short to medium run? The most important reason is **non-tradable goods**. Haircuts, restaurant meals, and real estate cannot be arbitraged across borders. A dollar stretches much further in Vietnam than in Norway not because of currency mispricing but because local services are genuinely cheaper. This is the **Balassa-Samuelson effect**: countries with high productivity in tradable goods have high wages across the economy, pushing up the prices of non-tradables and making the overall price level high relative to PPP. As a result, PPP exchange rates — widely used by the IMF and World Bank to compare GDP across countries — systematically show rich countries as having overvalued currencies and poor countries as undervalued. The gap reflects real differences in purchasing power over non-tradables, not a correctable currency misalignment.
