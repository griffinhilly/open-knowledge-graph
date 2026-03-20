---
id: market-anomalies-and-puzzles
title: Market Anomalies and Asset Pricing Puzzles
domain: economics
course: financial-economics
prerequisites:
- id: efficient-market-hypothesis
  type: hard
- id: capital-asset-pricing-model
  type: hard
- id: behavioral-finance-intro
  type: soft
- id: price-earnings-valuation
  type: soft
builds-toward:
- risk-adjusted-performance-measures
tags:
- anomalies
- value-effect
- momentum
- size-effect
- equity-premium-puzzle
stage: advanced
status: validated
---
# Market Anomalies and Asset Pricing Puzzles

## Core Idea
Market anomalies are empirical return patterns that standard asset pricing models — particularly CAPM — cannot explain without invoking additional factors or market frictions. The most studied anomalies include the size effect (small-cap stocks earn returns exceeding their beta-predicted level), the value effect (high book-to-market stocks outperform growth stocks), and momentum (past 3-12 month winners outperform past losers). The equity premium puzzle asks why the historical equity risk premium (roughly 5-8% annually) is so large that it implies implausibly high levels of risk aversion under standard utility models. Debate continues on whether anomalies represent genuine mispricings (behavioral view) or compensation for risks the models have not captured (rational view).

## How It's Best Learned
Read the original Fama-French (1992) paper documenting size and value effects. Examine the 'anomaly decay' phenomenon — many anomalies have weakened after publication as more capital attempts to exploit them. Discuss whether momentum is a behavioral phenomenon or a risk factor, given its persistence and crash risk.

## Common Misconceptions
- Anomalies are not necessarily free money — transaction costs, capacity limits, and the risk of sudden reversals (especially for momentum) often prevent profitable exploitation at scale.
- Any anomaly is ambiguous evidence against EMH due to the joint hypothesis problem: it could indicate model misspecification rather than true market inefficiency.

## Explainer

The **efficient market hypothesis (EMH)** and the **Capital Asset Pricing Model (CAPM)** are intertwined claims: EMH says prices fully reflect available information; CAPM says the only priced risk is systematic (beta) risk. Together, they predict that no trading strategy based on public information should earn returns above what beta exposure explains. **Market anomalies** are empirical patterns that survive this joint prediction. The most studied are the **size effect** (small-capitalization stocks earn excess returns), the **value effect** (stocks with high book-to-market ratios outperform growth stocks), and **momentum** (stocks with strong past 3–12 month returns continue to outperform). Each of these patterns has been replicated across markets and time periods, making them hard to dismiss as data mining.

The key conceptual problem every anomaly creates is the **joint hypothesis problem**. When you test whether the size effect is real, you are simultaneously testing EMH and CAPM. If small stocks earn high returns, it could mean: (1) markets are inefficient and mispricing persists, or (2) small stocks are riskier in ways CAPM does not capture. You cannot tell from the return data alone. Fama and French responded to size and value by extending CAPM with two additional risk factors — a small-minus-big (SMB) factor and a high-minus-low book-to-market (HML) factor — reframing the anomalies as compensation for priced risks. Whether these factors represent genuine systematic risks or just captured mispricings that rational investors were slow to arbitrage is still debated.

**Momentum** is the most puzzling anomaly from a rational risk perspective. Stocks that performed well over the past 3–12 months continue to outperform over the next 3–12 months — and then frequently crash dramatically (momentum crashes). Rational risk stories for momentum are strained; the reversal pattern at longer horizons (3–5 years) suggests overreaction and correction rather than risk compensation. Behavioral explanations — investor underreaction to new information, overconfidence in prior trends, herding — fit the data better, but behavioral biases should be arbitraged away by rational investors in efficient markets. The persistence of momentum is one of the strongest challenges to pure rational asset pricing.

The **equity premium puzzle** operates at a different level. Over the 20th century, U.S. equities returned roughly 5–8% more annually than short-term government bonds. Using a standard consumption-based asset pricing model with plausible levels of risk aversion (coefficient of 1–10), this premium requires investors to be so risk-averse that they would refuse a coin flip for trivial losses — a level of aversion inconsistent with observed economic behavior. The puzzle is not that stocks earn more than bonds, but that the gap is so large it demands an unrealistic explanation within standard expected utility theory. Proposed resolutions include habit formation utility, rare disaster risk, and market frictions — none fully satisfying. What the equity premium puzzle teaches is that the question "is this return too high given the risk?" is far harder to answer than it appears, because it depends entirely on which model you use to price risk.
