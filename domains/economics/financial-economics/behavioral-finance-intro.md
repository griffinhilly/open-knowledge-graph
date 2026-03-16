---
id: behavioral-finance-intro
title: 'Behavioral Finance: Biases and Bounded Rationality'
domain: economics
course: financial-economics
prerequisites:
- id: efficient-market-hypothesis
  type: hard
- id: consumer-theory-utility
  type: soft
- id: game-theory-basics-microeconomics
  type: soft
builds-toward:
- market-anomalies-and-puzzles
tags:
- behavioral-finance
- prospect-theory
- loss-aversion
- cognitive-bias
- heuristics
stage: abstract-reasoning
status: validated
---

# Behavioral Finance: Biases and Bounded Rationality

## Core Idea
Behavioral finance applies insights from psychology to explain why investors systematically deviate from the rational agent model. Kahneman and Tversky's prospect theory shows that losses feel roughly twice as painful as equivalent gains (loss aversion) and that people evaluate outcomes relative to reference points rather than final wealth. Other key biases include overconfidence (overestimating predictive ability), herding (following the crowd rather than independent analysis), anchoring (over-relying on salient price levels), and the disposition effect (holding losers too long and selling winners too early). These biases can cause asset mispricing that persists because arbitrage is often limited by cost, risk, and capital constraints.

## How It's Best Learned
Study the original Kahneman-Tversky experiments that motivated prospect theory — the questions feel straightforward but elicit systematically irrational responses. Examine real market bubbles and manias (dot-com, housing, crypto) through a behavioral lens to identify which biases amplified the excess. Consider which biases are most relevant for individual vs. institutional investors.

## Common Misconceptions
- Behavioral finance does not prove markets are consistently wrong or exploitable — biases coexist with substantial, if imperfect, market efficiency in many asset classes.
- Not all heuristics are errors — many are effective shortcuts in uncertain environments and only fail systematically in specific, predictable contexts.

## Explainer

The efficient market hypothesis — your prerequisite — holds that asset prices reflect all available information, because rational, self-interested investors would instantly exploit any discrepancy. Behavioral finance doesn't simply reject this; it asks: what happens when real investors, with limited cognitive resources and emotional responses, make decisions? The answer is that actual behavior systematically departs from the rational agent model in predictable directions that can affect prices.

The cornerstone is **prospect theory**, developed by Kahneman and Tversky as a descriptive alternative to expected utility theory. Recall from consumer theory that expected utility treats individuals as maximizing a function of absolute wealth levels — gaining $100 feels as good as losing $100 feels bad if the utility function is symmetric. Prospect theory shows empirically this is wrong in two ways. First, people evaluate outcomes relative to a **reference point** (usually the status quo or purchase price) rather than final wealth. Second, the value function is asymmetric: losses feel roughly twice as painful as equivalent gains feel pleasurable — **loss aversion**. A third property, **diminishing sensitivity**, means the function is concave in gains (each additional gain feels smaller) and convex in losses (each additional loss feels less devastating), producing risk aversion in gains and risk-seeking in losses.

These features generate specific and testable behavioral patterns. The **disposition effect** — the tendency to hold losing positions too long and sell winning ones too quickly — follows directly from prospect theory: investors are reluctant to realize losses because losses loom large relative to reference prices, but they eagerly lock in gains. **Overconfidence** leads investors to trade too frequently, underestimate risk, and concentrate portfolios excessively — empirically, more active traders earn lower risk-adjusted returns on average. **Anchoring** causes investors to over-rely on salient price levels (e.g., a stock's 52-week high) when making decisions, even when those levels are informationally irrelevant. **Herding** reflects social information cascades and career concerns for professional managers: following the crowd is rational if you will be judged relative to the consensus.

The important question is whether these biases generate **persistent** mispricing, or whether rational arbitrageurs quickly eliminate them. The limits-to-arbitrage framework explains why exploitation is harder than it sounds. An arbitrageur who correctly identifies an overpriced asset must short it, which requires borrowing shares (costly), posting collateral (capital-intensive), and accepting the risk that the mispricing widens before it corrects — forcing an early exit at a loss. Keynes's observation that "markets can remain irrational longer than you can remain solvent" captures the core constraint. As a result, behavioral biases can coexist with markets that are efficient in a weak-form sense while still generating anomalies (value premium, momentum, post-earnings announcement drift) that are difficult to explain purely through rational risk-pricing. Understanding behavioral finance tells you less about how to exploit markets than about why they behave as they do — and which investor mistakes to avoid in your own decision-making.
