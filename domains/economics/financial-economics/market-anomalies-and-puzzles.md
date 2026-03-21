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

## Questions

```yaml
- question: "A researcher finds that stocks with high short interest consistently earn negative abnormal returns over the following month, even after adjusting for beta. She concludes this proves financial markets are inefficient. A colleague challenges this conclusion. What is the strongest challenge?"
  type: multiple-choice
  options:
    - "One month is too short a measurement window to draw reliable conclusions about market efficiency"
    - "High short interest might proxy for a priced risk factor that CAPM fails to capture — anomaly tests always simultaneously test market efficiency and the assumed pricing model"
    - "Short sellers are sophisticated insiders and their positions are not exploitable by ordinary investors"
    - "Abnormal returns disappear once the transaction costs of establishing short positions are factored in"
  answer: 1
  explanation: "This is the joint hypothesis problem in action. Any test of market efficiency must specify what 'normal' returns are, which requires an asset pricing model. If short-interest stocks earn excess returns relative to CAPM predictions, there are two interpretations: (1) markets are inefficient and these stocks are mispriced, or (2) CAPM is misspecified and high short interest proxies for a genuine risk factor that commands a premium. Return data alone cannot distinguish these. The colleague's challenge is correct: the finding is anomalous relative to CAPM, but that could reflect model failure rather than market failure."

- question: "The equity premium puzzle is best described as:"
  type: multiple-choice
  options:
    - "The empirical finding that stocks have underperformed bonds over most 30-year horizons, contradicting the prediction that risk-bearing earns a premium"
    - "The difficulty of explaining why the historical equity-bond return gap is so large that it requires implausibly extreme levels of risk aversion within standard expected utility models"
    - "The paradox that small-cap stocks earn higher returns than large-cap stocks despite being easier to diversify"
    - "The observation that investors hold too many equities relative to what portfolio theory prescribes, suggesting they are risk-seeking rather than risk-averse"
  answer: 1
  explanation: "The puzzle is not that equities outperform bonds — that's expected as compensation for bearing systematic risk. The puzzle is the *magnitude* of the premium (~5–8% annually in U.S. data). Under standard consumption-based asset pricing with plausible risk aversion (coefficient 1–10), the model predicts a premium of less than 1%. Matching the observed premium requires a risk aversion coefficient above 30, implying investors would refuse coin flips for trivially small losses — behavior inconsistent with observed economic decisions. The puzzle reveals a deep failure of standard utility models to match asset market data, not a simple question about whether stocks beat bonds."

- question: "The momentum anomaly — past 3-12 month winners outperforming past losers — constitutes definitive evidence that financial markets are informationally inefficient, since no rational risk story can explain it."
  type: true-false
  answer: false
  explanation: "Momentum is among the most persistent and puzzling anomalies, and rational risk-based explanations are strained — but 'strained' is not the same as 'impossible.' The joint hypothesis problem means any anomaly is simultaneously evidence against EMH and against the pricing model. Researchers have proposed risk stories involving time-varying expected returns and momentum crash risk (momentum strategies suffer severe losses during market reversals). The behavioral explanations (underreaction, overconfidence) fit the data better, but behavioral biases should be arbitraged away by rational investors — which is itself a puzzle. 'Definitive evidence' is too strong; the debate remains live."

- question: "Market anomalies typically weaken or disappear after being published in academic journals, because publication allows more capital to exploit the strategy and arbitrage away the mispricing."
  type: true-false
  answer: true
  explanation: "This 'anomaly decay' is well-documented. After a strategy is published, institutional investors incorporate it into their trading, increasing demand for the pattern's winners and selling its losers, which compresses the return differential. This is actually consistent with the EMH — the market becomes more efficient once information about the pattern is publicly available. However, not all anomalies fully disappear; some (like momentum) remain partially intact, suggesting either genuine risk compensation or limits to arbitrage that prevent complete elimination."

- question: "What is the joint hypothesis problem, and why does it make anomalies fundamentally ambiguous evidence about whether financial markets are efficient?"
  type: short-answer
  answer: "Every test of market efficiency requires a model of what 'fair' returns are. When we test whether an anomaly represents a mispricing, we are simultaneously testing two things: (1) the EMH, and (2) the asset pricing model used to compute expected returns. If small stocks earn 'excess' returns, it could mean markets are inefficient and small stocks are underpriced, or it could mean CAPM is wrong and small stocks bear a real risk factor that commands a premium. Return data alone cannot separate these explanations. This is why Fama and French responded to the size and value effects by adding risk factors to CAPM rather than declaring markets inefficient — both responses are consistent with the same data."
  explanation: "The joint hypothesis problem is one of the deepest methodological challenges in empirical finance. It implies that any anomaly finding is only as strong as the asset pricing model it uses as a benchmark. This is why anomaly research has driven the development of multi-factor models (Fama-French 3-factor, Carhart 4-factor, Fama-French 5-factor) — as the benchmark model improves, some anomalies 'disappear' by being reinterpreted as risk factors, while others survive even the more sophisticated models and remain genuine puzzles."
```

## Explainer

The **efficient market hypothesis (EMH)** and the **Capital Asset Pricing Model (CAPM)** are intertwined claims: EMH says prices fully reflect available information; CAPM says the only priced risk is systematic (beta) risk. Together, they predict that no trading strategy based on public information should earn returns above what beta exposure explains. **Market anomalies** are empirical patterns that survive this joint prediction. The most studied are the **size effect** (small-capitalization stocks earn excess returns), the **value effect** (stocks with high book-to-market ratios outperform growth stocks), and **momentum** (stocks with strong past 3–12 month returns continue to outperform). Each of these patterns has been replicated across markets and time periods, making them hard to dismiss as data mining.

The key conceptual problem every anomaly creates is the **joint hypothesis problem**. When you test whether the size effect is real, you are simultaneously testing EMH and CAPM. If small stocks earn high returns, it could mean: (1) markets are inefficient and mispricing persists, or (2) small stocks are riskier in ways CAPM does not capture. You cannot tell from the return data alone. Fama and French responded to size and value by extending CAPM with two additional risk factors — a small-minus-big (SMB) factor and a high-minus-low book-to-market (HML) factor — reframing the anomalies as compensation for priced risks. Whether these factors represent genuine systematic risks or just captured mispricings that rational investors were slow to arbitrage is still debated.

**Momentum** is the most puzzling anomaly from a rational risk perspective. Stocks that performed well over the past 3–12 months continue to outperform over the next 3–12 months — and then frequently crash dramatically (momentum crashes). Rational risk stories for momentum are strained; the reversal pattern at longer horizons (3–5 years) suggests overreaction and correction rather than risk compensation. Behavioral explanations — investor underreaction to new information, overconfidence in prior trends, herding — fit the data better, but behavioral biases should be arbitraged away by rational investors in efficient markets. The persistence of momentum is one of the strongest challenges to pure rational asset pricing.

The **equity premium puzzle** operates at a different level. Over the 20th century, U.S. equities returned roughly 5–8% more annually than short-term government bonds. Using a standard consumption-based asset pricing model with plausible levels of risk aversion (coefficient of 1–10), this premium requires investors to be so risk-averse that they would refuse a coin flip for trivial losses — a level of aversion inconsistent with observed economic behavior. The puzzle is not that stocks earn more than bonds, but that the gap is so large it demands an unrealistic explanation within standard expected utility theory. Proposed resolutions include habit formation utility, rare disaster risk, and market frictions — none fully satisfying. What the equity premium puzzle teaches is that the question "is this return too high given the risk?" is far harder to answer than it appears, because it depends entirely on which model you use to price risk.
