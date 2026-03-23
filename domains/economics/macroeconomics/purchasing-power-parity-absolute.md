---
id: purchasing-power-parity-absolute
title: Absolute Purchasing Power Parity
domain: economics
course: macroeconomics
prerequisites:
- id: foreign-exchange-market-mechanics
  type: hard
builds-toward:
- relative-purchasing-power-parity
tags:
- ppp
- exchange-rates
- price-levels
- goods-arbitrage
stage: advanced
status: validated
---

# Absolute Purchasing Power Parity

## Core Idea
Absolute PPP states that the exchange rate should equal the ratio of price levels: identical goods should cost the same in different countries when converted to a common currency.

## How It's Best Learned
Use Big Mac index: compare prices in different countries and calculate implied exchange rate. Compare to actual rate; deviations suggest currency over/undervaluation.

## Common Misconceptions
- Assuming PPP holds in short run; it applies over long horizons (5-10 years).
- Treating PPP as a law.
- Confusing PPP with commodity prices.

## Questions

```yaml
- question: "A Big Mac costs $5.58 in the US and ¥700 in Japan. Absolute PPP implies the exchange rate should be 125 yen per dollar. The actual rate is 150 yen per dollar. What does this suggest?"
  type: multiple-choice
  options:
    - "The yen is overvalued relative to PPP because it buys fewer dollars than PPP predicts"
    - "The yen is undervalued relative to PPP because more yen are needed per dollar than PPP predicts"
    - "The dollar is undervalued because the yen buys more Big Macs per dollar than PPP suggests"
    - "The deviation is meaningless since absolute PPP never holds in practice"
  answer: 1
  explanation: "PPP predicts 125 yen/dollar, but the actual rate is 150 yen/dollar — you need MORE yen than PPP predicts to buy one dollar. This means the yen is UNDERVALUED relative to PPP: the yen has less purchasing power in dollar terms than the goods-price comparison would suggest. Option A confuses direction: an overvalued yen would mean fewer yen are needed per dollar than PPP predicts, not more."

- question: "Absolute PPP fails to hold precisely in the short run primarily because of which mechanism?"
  type: multiple-choice
  options:
    - "Central banks actively prevent exchange rate movements toward PPP"
    - "Non-traded goods like haircuts and housing cannot be arbitraged across borders, allowing persistent price differences"
    - "Goods arbitrage is too fast — exchange rates overshoot PPP and then oscillate"
    - "PPP only applies to developing economies, not advanced economies with flexible exchange rates"
  answer: 1
  explanation: "The key reason absolute PPP fails, especially in the short run, is non-traded goods: services and goods that cannot be physically moved across borders can maintain price differences indefinitely. Countries with low labor costs can sustain systematically lower prices for these services — the Balassa-Samuelson effect. Option B has it backwards — goods arbitrage in reality is SLOW because of trade barriers and transportation costs. Exchange rate overshooting (Option C) is a real phenomenon but is about short-run dynamics, not the reason for persistent long-run deviations."

- question: "Absolute PPP in its strict form applies only to traded goods; it explicitly excludes services and non-traded goods from the price basket."
  type: true-false
  answer: false
  explanation: "Absolute PPP in its strict form applies to a basket of ALL goods, including both traded and non-traded goods. However, it is precisely because non-traded goods are included that PPP fails in practice — non-traded goods cannot be arbitraged, so their prices can diverge across countries without triggering the exchange rate adjustment that the theory predicts. The existence of non-traded goods is a reason why PPP holds poorly, not a feature of its definition."

- question: "Absolute PPP is more useful as a long-run benchmark for assessing currency misalignment than as a short-run exchange rate forecasting tool."
  type: true-false
  answer: true
  explanation: "Empirically, exchange rates show some tendency to revert toward PPP over long horizons (5–10+ years), with half-life deviations of roughly 3–5 years. In the short run, capital flows, monetary policy expectations, and risk sentiment overwhelm goods-market arbitrage, making PPP nearly useless for forecasting next month's spot rate. This is why economists use PPP exchange rates to compare GDP across countries (a structural benchmark question) rather than to predict short-run exchange rate movements."

- question: "Explain why absolute PPP is based on a goods arbitrage argument, and identify the main reasons why this arbitrage is imperfect in practice."
  type: short-answer
  answer: "Absolute PPP rests on the law of one price applied to a basket of goods: if identical goods cost different amounts in two countries when expressed in a common currency, arbitrageurs can buy in the cheap country and sell in the expensive one, earning a profit while simultaneously driving the cheap-country price up, the expensive-country price down, and the exchange rate toward the PPP value. In practice, this arbitrage is imperfect for three reasons: (1) non-traded goods (services, real estate) cannot be physically moved, so price gaps persist indefinitely; (2) trade barriers, tariffs, and transportation costs create a band around PPP within which arbitrage is unprofitable; (3) short-run exchange rate dynamics are dominated by capital flows and monetary factors that can overwhelm goods-market adjustment for years."
  explanation: "The Balassa-Samuelson effect is a systematic consequence of non-traded goods: richer countries have higher productivity in traded goods, which bids up wages across the economy, raising non-traded goods prices — making richer countries systematically more expensive than PPP based on traded goods alone would predict."
```

## Explainer

From your study of foreign exchange market mechanics, you know that exchange rates are prices — the price of one currency in terms of another — determined by supply and demand in foreign exchange markets. **Absolute purchasing power parity** grounds exchange rates in something more tangible: the prices of goods. The core idea is a goods arbitrage argument. If a basket of identical goods costs $100 in the United States and ¥15,000 in Japan, then the exchange rate "should" be 150 yen per dollar. If the rate were 100 yen per dollar, goods would be cheaper in the US in yen terms — traders would buy US goods and sell them in Japan, driving up demand for dollars and the yen price of US goods, until the exchange rate converged to 150. This arbitrage logic, applied to traded goods, is the foundation of absolute PPP.

The **Big Mac index**, published by The Economist since 1986, makes this concrete. A Big Mac costs about $5.58 in the US and, say, £4.19 in the UK. If absolute PPP held, the exchange rate should be 5.58 / 4.19 ≈ 1.33 dollars per pound. The actual exchange rate may differ significantly from this implied rate — the gap is interpreted as over- or undervaluation. If the actual rate is 1.20 dollars per pound, the pound is "undervalued" by about 9% against the dollar relative to PPP. This is a simplification, but it captures the logic: PPP gives you a benchmark exchange rate based on price levels, and deviations from it say something about whether currencies are expensive or cheap relative to their purchasing power.

Why does absolute PPP fail in practice, especially in the short run? Three reasons dominate. First, **non-traded goods**: a haircut, restaurant meal, or housing cannot be arbitraged across borders. Countries with lower labor costs can sustain lower prices for these services indefinitely — this is the Balassa-Samuelson effect. Second, **trade barriers and transportation costs**: tariffs, shipping, and regulations mean that goods arbitrage is imperfect even for traded goods. Third, **short-run exchange rate dynamics**: exchange rates in the short run are driven by capital flows, monetary policy expectations, and risk sentiment — forces that can overwhelm goods-market arbitrage for years. A sudden capital flight can depreciate a currency 30% in months, far faster than any goods-market adjustment.

Over longer horizons — five to ten years or more — absolute PPP has better empirical support. Studies find that exchange rates tend to revert toward PPP, though the half-life of deviations is roughly three to five years. The practical implication is that PPP is most useful as a **long-run benchmark** rather than a short-run prediction tool. It tells you whether currencies appear misaligned over the medium term, which matters for long-run investment returns, policy analysis, and comparing economic size across countries (GDP at PPP exchange rates vs. market exchange rates gives very different pictures of relative economic size, especially for lower-income countries where price levels are systematically lower).
