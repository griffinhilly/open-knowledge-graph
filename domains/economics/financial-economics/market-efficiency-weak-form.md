---
id: market-efficiency-weak-form
title: 'Market Efficiency: Weak, Semi-Strong, and Strong Forms'
domain: economics
course: financial-economics
prerequisites:
- id: efficient-market-hypothesis
  type: hard
builds-toward:
- technical-analysis-and-market-efficiency
tags:
- market-efficiency
- market-microstructure
- information
stage: advanced
status: draft
---

# Market Efficiency: Weak, Semi-Strong, and Strong Forms

## Core Idea
Weak-form efficiency: past prices don't predict future returns (rules out technical analysis). Semi-strong: public information is instantly priced (rules out fundamental analysis for excess returns). Strong-form: all information (public and private) is priced (rare empirically). Most evidence supports semi-strong efficiency.

## Questions

```yaml
- question: "An analyst has five years of daily price and volume data for a stock. If markets are weak-form efficient, which of the following strategies is ruled out?"
  type: multiple-choice
  options:
    - "Buying and holding a broad index fund"
    - "Trading based on moving-average crossover patterns in the price history"
    - "Using publicly available earnings reports to identify undervalued stocks"
    - "Trading on a confidential tip about an upcoming merger"
  answer: 1
  explanation: "Weak-form efficiency holds that all information in past prices and volume is already reflected in current prices. A strategy based on historical price patterns (moving averages, chart signals) is exactly what weak-form efficiency rules out. Buy-and-hold (option A) is perfectly consistent with any form of efficiency. Using earnings reports (option C) is ruled out only by semi-strong efficiency. Trading on insider tips (option D) is ruled out only by strong-form efficiency."

- question: "A study finds that stock prices adjust fully to earnings announcements within seconds of release, leaving no exploitable profit opportunity. This finding is most consistent with which form of market efficiency?"
  type: multiple-choice
  options:
    - "Weak-form only — it only concerns past price data"
    - "Semi-strong form, which implies weak-form is also satisfied"
    - "Strong-form only — instantaneous adjustment requires all information to be priced"
    - "No form of efficiency — prices should not move at all if markets are efficient"
  answer: 1
  explanation: "Earnings announcements are publicly available information. Evidence that public information is instantly incorporated supports semi-strong efficiency. Because the forms are nested — semi-strong implies weak-form — this also confirms weak-form efficiency. Strong-form (option C) would require that even private, non-public information is priced, which this study does not address. Option D reflects a misconception: efficient markets react quickly to new information; it's only *predictable* price movements that efficiency rules out."

- question: "A market that is semi-strong efficient is necessarily also weak-form efficient."
  type: true-false
  answer: true
  explanation: "The three forms are nested: weak-form ⊂ semi-strong ⊂ strong. Semi-strong efficiency says prices reflect all publicly available information, which includes historical price data. If public information is already priced in, then certainly the subset of historical price data is priced in — satisfying weak-form. The implication only runs in one direction: weak-form does not imply semi-strong."

- question: "Evidence that corporate insiders consistently earn excess returns by trading on advance knowledge of earnings surprises disproves semi-strong market efficiency."
  type: true-false
  answer: false
  explanation: "Insider trading involves non-public (private) information. Semi-strong efficiency only claims that all *publicly available* information is reflected in prices — it says nothing about private information. Consistent profits from insider trading violate strong-form efficiency, not semi-strong. The existence of insider trading laws is itself a recognition that strong-form efficiency does not hold, while semi-strong efficiency can remain a reasonable description of how public markets function."

- question: "Why would finding a reliable, profitable chart-based trading rule (e.g., 'buy whenever the 50-day moving average crosses above the 200-day moving average') be evidence against weak-form market efficiency?"
  type: short-answer
  answer: "Weak-form efficiency holds that all information in past prices is already incorporated into current prices. A profitable chart rule works by using past price patterns to predict future returns. If such a pattern reliably predicted higher returns, traders would exploit it until prices adjusted, eliminating the profit. The fact that no such pattern should persist is exactly what weak-form efficiency means: the history of prices contains no exploitable predictive content about future price movements."
  explanation: "The key is that past prices are information, and efficiency means information is already priced in. Consistent profits from historical price patterns would mean the market had overlooked freely available information — a contradiction of weak-form efficiency. This is also why technical analysis, which is based entirely on price and volume history, is the specific practice that weak-form efficiency declares unprofitable."
```

## Explainer

From the Efficient Market Hypothesis, you know the core claim: in competitive markets, prices quickly incorporate available information, making it impossible to consistently earn abnormal returns. The three forms of market efficiency — weak, semi-strong, and strong — define three progressively larger information sets, and they are nested: semi-strong efficiency implies weak-form efficiency, and strong-form implies both.

**Weak-form efficiency** says that current prices already reflect all information contained in the history of past prices and trading volume. If this holds, looking at a chart of past prices — the entire enterprise of **technical analysis** — cannot generate systematically better-than-market returns. The price tomorrow is not predictable from the price today because all the predictive content of yesterday's price was already priced in by the market. This form is empirically well-supported: price series in developed markets look close to a **random walk**, and trading rules based on chart patterns (head-and-shoulders, moving average crossovers) generally fail to beat a buy-and-hold strategy after transaction costs.

**Semi-strong efficiency** raises the bar: prices reflect all *publicly available* information, not just price history. This includes earnings announcements, news, analyst reports, economic data — anything anyone can read. If the market is semi-strong efficient, **fundamental analysis** (studying financial statements, forecasting cash flows, and estimating intrinsic value) cannot reliably generate excess returns, because by the time you act on public information, the market has already incorporated it. The evidence here is strong but less decisive: **event studies** show that stock prices react almost instantaneously to earnings surprises and news releases, leaving little room for profit. However, documented anomalies — the value premium, the momentum effect — have been interpreted by some researchers as evidence against semi-strong efficiency and by others as risk factors not captured by standard models.

**Strong-form efficiency** claims that prices reflect all information, including private (inside) information. This is the most extreme version and is clearly violated: insider trading laws exist precisely because traders with material non-public information can profit from it — and enforcement actions confirm that they do. Empirically, strong-form efficiency is rejected. The practical hierarchy, then, is: weak-form efficiency is the baseline that most evidence supports; semi-strong efficiency is the working assumption of well-functioning public markets with some empirical anomalies at the edges; strong-form efficiency is a theoretical extreme that does not hold. The key policy implication is that insider trading regulations are necessary precisely because strong-form efficiency does not automatically police itself.
