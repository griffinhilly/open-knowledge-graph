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
stage: advanced
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

## Questions

```yaml
- question: "An investor bought a stock at $100. It has fallen to $60 and continues declining. She holds it, unwilling to sell, telling herself it will recover. Which behavioral concept best explains this?"
  type: multiple-choice
  options:
    - "Overconfidence — she overestimates her ability to predict the stock's recovery"
    - "Loss aversion — selling at $60 would realize a loss that feels approximately twice as painful as an equivalent gain would feel pleasurable, so she avoids locking it in"
    - "Anchoring — she is over-relying on the irrelevant $100 purchase price as a reference for current value"
    - "Herding — other investors in similar situations also hold rather than sell"
  answer: 1
  explanation: "This is the classic disposition effect, driven directly by loss aversion. Prospect theory shows that losses loom approximately twice as large as equivalent gains in the value function. Selling at $60 when you paid $100 crystallizes a $40 loss — a highly painful outcome relative to the reference point. By holding, the investor avoids the psychological pain of realizing the loss, even at the cost of rational portfolio management. Option C (anchoring) is also partially present — the $100 reference point matters — but loss aversion is the primary mechanism that prevents selling. Option A (overconfidence) would predict excessive trading, not paralysis."

- question: "Prospect theory holds that people evaluate outcomes relative to a reference point rather than in terms of final wealth. Why does this matter for investor behavior?"
  type: multiple-choice
  options:
    - "It means investors use historical price data to forecast future returns, anchoring to past performance"
    - "It means whether an outcome feels like a gain or a loss depends on where you started — not on absolute wealth — which determines how much emotional weight the outcome carries"
    - "It means investors care only about relative performance compared to benchmarks, not absolute returns"
    - "It means rational investors always set their reference point at zero to avoid bias"
  answer: 1
  explanation: "The reference point — typically the purchase price, status quo, or expected outcome — determines whether any particular result registers as a gain or a loss. The same $50,000 portfolio value feels different to someone who invested $40,000 (a gain) versus $60,000 (a loss), even though final wealth is identical. Because the loss side of the value function is steeper than the gain side, the framing as gain or loss dramatically affects behavior: people take more risk to avoid a loss than to secure an equivalent gain. This reference-point dependence is empirically robust and violates classical expected utility theory's prediction that only final wealth states matter."

- question: "Behavioral finance demonstrates that financial markets are consistently mispriced and therefore easily exploitable by rational investors who recognize common cognitive biases."
  type: true-false
  answer: false
  explanation: "This is the key misconception the topic's common misconceptions section addresses directly. Behavioral biases can coexist with substantial market efficiency because of limits to arbitrage. Even when a rational investor correctly identifies a mispriced asset, exploiting it requires shorting (costly), posting collateral (capital-intensive), and bearing the risk that the mispricing worsens before it corrects — potentially forcing an early exit at a loss. As Keynes noted, markets can remain irrational longer than you can remain solvent. Behavioral finance primarily explains *why* markets behave as they do and which investor mistakes to avoid — not a reliable road map for profitable exploitation."

- question: "According to prospect theory, a person who just won $500 will typically feel less pleasure from the gain than the pain they would feel from a $500 loss — even though the dollar amounts are identical."
  type: true-false
  answer: true
  explanation: "This is the core empirical finding of loss aversion: the disutility of a loss is roughly twice the utility of an equivalent gain. Kahneman and Tversky's experiments consistently showed that people require approximately $200–$250 in potential gain to be willing to accept a 50/50 bet with a $100 potential loss — far more than expected value calculations would predict. This asymmetry is not a cognitive error in the sense of being irrational given the values people hold; it is a descriptive fact about how human psychology weights gains and losses. It violates symmetric expected utility theory but accurately predicts a wide range of real financial behaviors including the disposition effect, equity premium puzzle components, and insurance demand."

- question: "What is the disposition effect, and why does prospect theory predict it? Explain specifically how loss aversion and reference points together produce the tendency to hold losing positions too long while selling winning ones too quickly."
  type: short-answer
  answer: "The disposition effect is the empirically documented tendency of investors to sell assets that have increased in value (winners) too quickly while holding assets that have decreased in value (losers) too long. Prospect theory predicts it through two features: First, loss aversion — losses feel approximately twice as painful as equivalent gains feel pleasurable. Selling a losing position crystallizes the loss, making it psychologically real and intensely painful relative to the reference point (purchase price). Continuing to hold leaves the loss 'on paper' and psychologically avoidable. Second, the value function is concave in gains and convex in losses (diminishing sensitivity) — investors are risk-averse in the gain domain (they prefer to lock in a sure gain rather than gamble for more) but risk-seeking in the loss domain (they prefer to gamble on recovery rather than accept a certain loss). Together, these produce systematic asymmetry: sell winners early to pocket the gain, hold losers in hopes of recovery."
  explanation: "The disposition effect is irrational from a tax perspective (holding winners longer would defer capital gains taxes) and from a performance perspective (stocks that have fallen often continue falling; momentum suggests selling losers and holding winners). Yet it is pervasive in both retail and professional investors. Behavioral finance's power is explaining not just that this happens but *why*, with a mathematically specific model of the value function."
```

## Explainer

The efficient market hypothesis — your prerequisite — holds that asset prices reflect all available information, because rational, self-interested investors would instantly exploit any discrepancy. Behavioral finance doesn't simply reject this; it asks: what happens when real investors, with limited cognitive resources and emotional responses, make decisions? The answer is that actual behavior systematically departs from the rational agent model in predictable directions that can affect prices.

The cornerstone is **prospect theory**, developed by Kahneman and Tversky as a descriptive alternative to expected utility theory. Recall from consumer theory that expected utility treats individuals as maximizing a function of absolute wealth levels — gaining $100 feels as good as losing $100 feels bad if the utility function is symmetric. Prospect theory shows empirically this is wrong in two ways. First, people evaluate outcomes relative to a **reference point** (usually the status quo or purchase price) rather than final wealth. Second, the value function is asymmetric: losses feel roughly twice as painful as equivalent gains feel pleasurable — **loss aversion**. A third property, **diminishing sensitivity**, means the function is concave in gains (each additional gain feels smaller) and convex in losses (each additional loss feels less devastating), producing risk aversion in gains and risk-seeking in losses.

These features generate specific and testable behavioral patterns. The **disposition effect** — the tendency to hold losing positions too long and sell winning ones too quickly — follows directly from prospect theory: investors are reluctant to realize losses because losses loom large relative to reference prices, but they eagerly lock in gains. **Overconfidence** leads investors to trade too frequently, underestimate risk, and concentrate portfolios excessively — empirically, more active traders earn lower risk-adjusted returns on average. **Anchoring** causes investors to over-rely on salient price levels (e.g., a stock's 52-week high) when making decisions, even when those levels are informationally irrelevant. **Herding** reflects social information cascades and career concerns for professional managers: following the crowd is rational if you will be judged relative to the consensus.

The important question is whether these biases generate **persistent** mispricing, or whether rational arbitrageurs quickly eliminate them. The limits-to-arbitrage framework explains why exploitation is harder than it sounds. An arbitrageur who correctly identifies an overpriced asset must short it, which requires borrowing shares (costly), posting collateral (capital-intensive), and accepting the risk that the mispricing widens before it corrects — forcing an early exit at a loss. Keynes's observation that "markets can remain irrational longer than you can remain solvent" captures the core constraint. As a result, behavioral biases can coexist with markets that are efficient in a weak-form sense while still generating anomalies (value premium, momentum, post-earnings announcement drift) that are difficult to explain purely through rational risk-pricing. Understanding behavioral finance tells you less about how to exploit markets than about why they behave as they do — and which investor mistakes to avoid in your own decision-making.
