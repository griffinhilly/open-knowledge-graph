---
id: precautionary-saving
title: Precautionary Saving and Prudence
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: euler-equation-consumption
  type: hard
- id: expected-utility-and-risk-aversion
  type: hard
- id: hall-random-walk-consumption
  type: soft
- id: consumption-smoothing-intertemporal
  type: soft
builds-toward: []
tags:
- consumption
- saving
- uncertainty
- prudence
- buffer-stock saving
- certainty equivalence
stage: expert
status: validated
---

# Precautionary Saving and Prudence

## Core Idea
Precautionary saving is extra saving caused by uncertainty about future income. In the Euler equation, saving depends on expected future marginal utility. If marginal utility is convex, which holds when the third derivative of utility is positive (u‴ > 0), then more uncertainty raises expected marginal utility of future consumption, and the consumer saves more today. Quadratic utility has u‴ = 0, which is why Hall's random-walk model shows no precautionary motive; common utility functions such as log and constant relative risk aversion (CRRA) have u‴ > 0. Miles Kimball called this property prudence and measured it by −u‴/u″.

## How It's Best Learned
Work a two-period example with log utility. Compare a consumer whose second-period consumption is certain with one facing a fifty-fifty spread around the same mean, and compute expected marginal utility in each case. Then draw the convex marginal-utility curve and the chord between the two outcomes, so the role of convexity is visible.

## Common Misconceptions
- Precautionary saving is the same thing as risk aversion. (Risk aversion depends on concave utility, u″ < 0; precautionary saving depends on convex marginal utility, u‴ > 0. Quadratic utility is risk averse but has no precautionary motive.)
- Uncertainty affects saving only if people expect income to fall on average. (A mean-preserving increase in risk, with no change in expected income, raises saving for a prudent consumer.)
- Precautionary savers keep accumulating wealth without limit. (In buffer-stock models with impatient consumers, saving targets a modest wealth buffer and stops growing once it is reached.)

## Questions

```yaml
- question: "A consumer has log utility, so u′(C) = 1/C. Next period's consumption will be 100 for sure, or else 50 or 150 with equal probability. Compare expected marginal utility of next-period consumption in the two cases."
  type: multiple-choice
  options: ["It is 0.01 in both cases", "It is 0.01 when certain and about 0.0133 when risky", "It is higher when certain", "It cannot be computed without knowing the interest rate"]
  answer: 1
  explanation: "Certain case: 1/100 = 0.01. Risky case: 0.5 × (1/50) + 0.5 × (1/150) = 0.5 × (0.02 + 0.00667) ≈ 0.0133. Higher expected future marginal utility makes saving more valuable, so the consumer saves more today."
- question: "With quadratic utility, an increase in future income uncertainty that leaves expected income unchanged has no effect on current consumption."
  type: true-false
  answer: true
  explanation: "Quadratic utility has linear marginal utility, so expected marginal utility depends only on expected consumption. This is called certainty equivalence. Without convex marginal utility there is no precautionary motive."
- question: "Which condition on the utility function produces a precautionary saving motive?"
  type: multiple-choice
  options: ["u′ > 0", "u″ < 0", "u‴ > 0", "u″ = 0"]
  answer: 2
  explanation: "A positive third derivative makes marginal utility convex. By Jensen's inequality, spreading out future consumption then raises expected marginal utility, which raises desired saving. Concavity alone (u″ < 0) gives risk aversion but not prudence."
- question: "Why might precautionary saving help explain why young households with uncertain earnings hold liquid savings even when they expect higher income later?"
  type: short-answer
  answer: "The permanent income hypothesis with certainty would have them borrow against future income. But with prudent preferences, uncertainty about earnings raises the value of a cash buffer against bad outcomes, especially if borrowing is limited. They therefore hold a small stock of savings and consume less than a certainty model predicts."
  explanation: "Buffer-stock models by Angus Deaton and Christopher Carroll combine impatience, income risk, and borrowing limits to produce this pattern."
```

## Explainer
Hall's random-walk result rests on quadratic utility. That assumption is convenient, but it hides one channel through which uncertainty affects saving. Once we drop it, the consumer facing risky future income generally saves more than one facing certain income with the same mean. That extra saving is **precautionary saving**.

Begin with the Euler equation with r equal to the discount rate: u′(C_t) = E_t[u′(C_{t+1})]. The consumer saves until the marginal utility of consuming today equals the expected marginal utility of consuming tomorrow. Now ask how uncertainty about C_{t+1} affects the right-hand side. If u′ is a straight line, as with quadratic utility, the expectation of u′(C_{t+1}) equals u′ of the expected value. Spreading out outcomes changes nothing. This is called **certainty equivalence**.

If u′ is convex, Jensen's inequality gives E[u′(C_{t+1})] > u′(E[C_{t+1}]). Uncertainty raises expected future marginal utility. To restore the Euler equation, the consumer must raise u′(C_t), which means lowering current consumption, which means saving more. Convex marginal utility is the same as a positive third derivative, u‴ > 0. Log utility and CRRA utility both have this property. A numerical check with log utility: if next-period consumption is a sure 100, expected marginal utility is 0.01; if it is 50 or 150 with equal chance, it is about 0.0133.

Miles Kimball, in a 1990 paper, named this property **prudence** and proposed −u‴/u″ as its measure, by analogy with the Arrow-Pratt measure of risk aversion, −u″/u′. The two concepts differ. Risk aversion concerns dislike of risk; prudence concerns how risk changes the desire to save. Quadratic utility is risk averse and not prudent.

Precautionary saving matters for several reasons. It helps explain why households hold liquid wealth well before retirement. Combined with impatience and borrowing limits, it yields **buffer-stock** behavior, studied by Angus Deaton and Christopher Carroll: households build a modest cushion, spend from it in bad years, and rebuild it in good years. It also implies that consumption grows faster when income is more uncertain, because people consume less now and more later. Finally, it gives a reason why social insurance, which reduces income risk, can lower private saving.
