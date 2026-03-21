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

## Questions

```yaml
- question: "Researchers find that value stocks (high book-to-market ratio) have outperformed growth stocks by an average of 4% annually for 50 years. A proponent of market efficiency argues this does not disprove EMH. Which argument is most valid?"
  type: multiple-choice
  options:
    - "The finding must be a statistical artifact — 50 years of data is insufficient to identify a real pattern in markets"
    - "EMH only applies to the average investor; professional portfolio managers are exempt from its predictions"
    - "Value stocks carry higher systematic risk not captured by simple return comparisons; the higher return compensates for risk, which is consistent with efficiency under a correct asset pricing model"
    - "Past performance is random, so a 50-year pattern is simply an unusual sequence of random outcomes"
  answer: 2
  explanation: "This is the joint hypothesis problem in action. Any test of EMH requires assuming a model of expected returns. If value stocks outperform, it could mean (a) markets are inefficient and value stocks are persistently mispriced, or (b) the return model is wrong — value stocks bear risks (distress risk, illiquidity) that the model does not fully capture. You cannot distinguish these hypotheses without an agreed-upon model of risk-adjusted returns, which does not exist. This is why apparent anomalies are so difficult to interpret definitively."

- question: "A financial journalist writes: 'The 40% market crash in 2008 proves that markets are wildly inefficient — if information were fully priced in, prices would not have to fall that much.' What is the strongest EMH counter-argument?"
  type: multiple-choice
  options:
    - "The 2008 crash was caused by government regulation failures, not market behavior, so EMH does not apply"
    - "EMH predicts that prices should never fall more than 10% in a given year"
    - "Large, rapid price declines are consistent with efficiency — they reflect rapid incorporation of new information (collapsing housing prices, frozen credit markets); efficiency requires prices to respond quickly, not to be stable"
    - "Market crashes only disprove strong-form efficiency, not weak or semi-strong efficiency"
  answer: 2
  explanation: "EMH makes no prediction about volatility or price levels — only about the speed and accuracy with which information is incorporated. If new information arrives that fundamentally changes the value of assets (as happened in 2008), prices must fall rapidly and substantially for the market to remain efficient. A crash is not evidence of irrationality; it is what the appropriate response to genuinely bad news looks like. The common misconception is that 'efficient' means 'calm' or 'correct in hindsight.'"

- question: "Under semi-strong form efficiency, even a highly skilled analyst who correctly identifies an undervalued stock using public financial data should not expect to earn consistent risk-adjusted excess returns."
  type: true-false
  answer: true
  explanation: "Semi-strong efficiency holds that all publicly available information — including financial statements, earnings reports, analyst forecasts, and macroeconomic data — is already fully reflected in prices. If a stock looks undervalued based on public data, every other analyst looking at the same public data has already made the same determination and traded on it, eliminating the opportunity. Consistent outperformance would require either private information, lower transaction costs than competitors, or an uncorrected pricing model for risk."

- question: "The joint hypothesis problem means that if researchers discover a persistent market anomaly, they have definitively proven that markets are inefficient."
  type: true-false
  answer: false
  explanation: "Any empirical test of EMH must simultaneously assume a model of expected returns (e.g., CAPM, Fama-French three-factor model). If you observe returns above the model's prediction, you cannot tell whether (a) markets are inefficient, or (b) your risk model is wrong and the 'excess' return is actually compensation for a risk your model missed. The anomaly could be real mispricing, or it could be evidence that your benchmark model is incomplete. This is the joint hypothesis problem: EMH and the return model are tested together, never in isolation."

- question: "Explain the joint hypothesis problem in EMH testing. Why does it make it fundamentally impossible to cleanly prove that markets are inefficient?"
  type: short-answer
  answer: "To test EMH, you must define what 'normal' returns look like — which requires assuming an asset pricing model (like the CAPM). If you observe returns above normal, there are two explanations: (1) markets are inefficient and prices are wrong, or (2) your asset pricing model is wrong and what looks like excess return is actually fair compensation for risk the model doesn't capture. Since any test uses both EMH and a return model simultaneously, rejecting the joint hypothesis only tells you at least one of them is wrong — not which one. Without a universally agreed-upon return model, EMH cannot be tested in isolation."
  explanation: "Fama himself emphasized this problem repeatedly. It is why decades of anomaly research has not produced consensus: every 'proof' of inefficiency is simultaneously a potential indictment of the risk model used as the benchmark. This methodological challenge does not make EMH untestable in practice — it just means every result is always conditional on the assumed model, and researchers must be honest about that conditionality when interpreting evidence."
```

## Explainer

Your prerequisite work on stock valuation established that a stock's price should reflect the present value of its future cash flows. The Efficient Market Hypothesis asks a related but distinct question: how quickly and fully does the market incorporate information into those prices? The answer shapes everything from investment strategy to policy — if markets are efficient, active management is futile; if they are not, persistent profit opportunities exist.

The three forms of EMH define efficiency by the **information set** that prices are assumed to reflect. **Weak-form efficiency** holds that prices already incorporate all past price history — meaning technical analysis (charting patterns to predict future moves) cannot generate risk-adjusted excess returns. If past prices were predictive, traders would exploit the pattern until it disappeared. **Semi-strong efficiency** goes further: prices reflect all publicly available information — earnings reports, analyst forecasts, macro data. Fundamental analysis (identifying undervalued stocks from public financials) cannot persistently beat the market. **Strong-form efficiency** holds that even private information is already reflected in prices, which implies that even corporate insiders cannot consistently profit from nonpublic knowledge.

From your prerequisite knowledge of stock valuation using P/E multiples and discounted cash flows, the practical implication is striking: if semi-strong efficiency holds, no amount of careful analysis of public financial statements will yield above-market returns, because every other sophisticated analyst has already processed the same information. The market price already embeds the consensus interpretation. Evidence largely supports weak and semi-strong efficiency in developed markets — the most compelling single fact is the long-run underperformance of actively managed funds relative to low-cost index funds after fees. If managers with extensive research capabilities cannot beat the market on average, this is consistent with efficiency.

The **joint hypothesis problem** is the deepest challenge in EMH research. To test whether a market is efficient, you must assume a specific model of expected returns (like the CAPM). If you find abnormal returns, you cannot know whether markets are inefficient or your return model is wrong — the two hypotheses are always tested together. This makes EMH fundamentally difficult to falsify cleanly. Apparent anomalies (momentum, value premium, small-cap premium) may reflect genuine inefficiencies, or they may simply be compensation for risks the model has not captured.

The practical takeaway is nuanced: efficiency is not a binary state but a spectrum. Markets are generally quite efficient for widely-followed large-cap stocks with abundant analyst coverage, and less efficient for obscure, illiquid, or complex securities where information costs are high and arbitrage is difficult. Understanding EMH does not tell you markets are perfect — it tells you that beating them consistently requires either an informational edge the market lacks, a willingness to bear risks others avoid, or lower costs than competitors. That is a high bar, which is why passive indexing beats active management for most investors most of the time.
