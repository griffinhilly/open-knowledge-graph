---
id: efficient-market-hypothesis
title: Efficient Market Hypothesis (EMH)
domain: economics
course: financial-economics
prerequisites:
- id: stock-valuation-fundamentals
  type: hard
- id: capital-asset-pricing-model
  type: soft
- id: price-earnings-valuation
  type: soft
builds-toward:
- market-anomalies-and-puzzles
- behavioral-finance-intro
tags:
- emh
- market-efficiency
- weak-form
- semi-strong
- active-vs-passive
stage: advanced
status: validated
---
# Efficient Market Hypothesis (EMH)

## Core Idea
The Efficient Market Hypothesis (EMH), developed by Eugene Fama, asserts that asset prices fully and immediately reflect all available information, leaving no room for consistent risk-adjusted excess returns. Three forms represent different information sets: weak-form efficiency (prices reflect all past prices; technical analysis cannot generate alpha), semi-strong efficiency (prices reflect all public information; fundamental analysis cannot beat the market), and strong-form efficiency (prices reflect even private information; even insiders cannot consistently profit). A crucial methodological point — the joint hypothesis problem — is that testing EMH always requires specifying an asset pricing model, making it impossible to test EMH alone.

## How It's Best Learned
Examine evidence for each form: autocorrelation tests for weak form, event studies for semi-strong, mutual fund performance for strong form. Study the long-run evidence that actively managed funds underperform index funds after fees — the most compelling practical argument for efficiency.

## Common Misconceptions
- EMH does not claim prices are always correct or that bubbles are impossible — it claims prices reflect available information, not that information itself is correct or complete.
- Market crashes and high volatility do not disprove EMH — prices can be volatile and information-efficient simultaneously.

## Explainer

Your prerequisite work on stock valuation established that a stock's price should reflect the present value of its future cash flows. The Efficient Market Hypothesis asks a related but distinct question: how quickly and fully does the market incorporate information into those prices? The answer shapes everything from investment strategy to policy — if markets are efficient, active management is futile; if they are not, persistent profit opportunities exist.

The three forms of EMH define efficiency by the **information set** that prices are assumed to reflect. **Weak-form efficiency** holds that prices already incorporate all past price history — meaning technical analysis (charting patterns to predict future moves) cannot generate risk-adjusted excess returns. If past prices were predictive, traders would exploit the pattern until it disappeared. **Semi-strong efficiency** goes further: prices reflect all publicly available information — earnings reports, analyst forecasts, macro data. Fundamental analysis (identifying undervalued stocks from public financials) cannot persistently beat the market. **Strong-form efficiency** holds that even private information is already reflected in prices, which implies that even corporate insiders cannot consistently profit from nonpublic knowledge.

From your prerequisite knowledge of stock valuation using P/E multiples and discounted cash flows, the practical implication is striking: if semi-strong efficiency holds, no amount of careful analysis of public financial statements will yield above-market returns, because every other sophisticated analyst has already processed the same information. The market price already embeds the consensus interpretation. Evidence largely supports weak and semi-strong efficiency in developed markets — the most compelling single fact is the long-run underperformance of actively managed funds relative to low-cost index funds after fees. If managers with extensive research capabilities cannot beat the market on average, this is consistent with efficiency.

The **joint hypothesis problem** is the deepest challenge in EMH research. To test whether a market is efficient, you must assume a specific model of expected returns (like the CAPM). If you find abnormal returns, you cannot know whether markets are inefficient or your return model is wrong — the two hypotheses are always tested together. This makes EMH fundamentally difficult to falsify cleanly. Apparent anomalies (momentum, value premium, small-cap premium) may reflect genuine inefficiencies, or they may simply be compensation for risks the model has not captured.

The practical takeaway is nuanced: efficiency is not a binary state but a spectrum. Markets are generally quite efficient for widely-followed large-cap stocks with abundant analyst coverage, and less efficient for obscure, illiquid, or complex securities where information costs are high and arbitrage is difficult. Understanding EMH does not tell you markets are perfect — it tells you that beating them consistently requires either an informational edge the market lacks, a willingness to bear risks others avoid, or lower costs than competitors. That is a high bar, which is why passive indexing beats active management for most investors most of the time.
