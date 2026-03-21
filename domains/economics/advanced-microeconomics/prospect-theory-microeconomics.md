---
id: prospect-theory-microeconomics
title: Prospect Theory and Behavioral Economics
domain: economics
course: advanced-microeconomics
prerequisites:
- id: expected-return-and-variance-of-assets
  type: soft
- id: consumer-theory-utility
  type: soft
tags:
- behavioral-economics
- risk
- decision-making
stage: formal-systems
status: draft
---

# Prospect Theory and Behavioral Economics

## Core Idea
Prospect theory is a descriptive model of decision-making under risk that departs from expected utility theory. Key features: value function (concave for gains, convex for losses; loss-averse), reference dependence (outcomes judged as gains/losses relative to status quo), probability weighting (overweight small probabilities, underweight large ones). Explains phenomena like endowment effect and preference reversals.

## Questions

```yaml
- question: "A person paid $10 for a coffee mug they now own. They refuse to sell it for less than $17, yet they also say they would not pay more than $10 to buy an identical mug they don't own. Which feature of prospect theory best explains this gap?"
  type: multiple-choice
  options:
    - "Probability weighting — they overweight the small chance of regretting the sale"
    - "Loss aversion — giving up the mug is coded as a loss, which hurts more than an equivalent gain feels good"
    - "Diminishing sensitivity to gains — the marginal utility of the 11th dollar of mug value is low"
    - "Reference point adjustment — they have recalibrated to treat the mug as part of their wealth"
  answer: 1
  explanation: "This is the endowment effect, a direct consequence of loss aversion. Once the person owns the mug, the reference point shifts to 'owning it.' Selling the mug is coded as a loss relative to that reference point; not buying the mug is coded as a foregone gain. Because the value function is steeper for losses than for gains (losses hurt roughly twice as much as equal gains feel good), the minimum acceptable sale price exceeds the maximum willingness to pay. Expected utility theory, which tracks final wealth states without reference to how you acquired them, predicts no such gap."

- question: "According to prospect theory's fourfold pattern, which pair of risk preferences is expected for the same individual?"
  type: multiple-choice
  options:
    - "Risk-averse for all gambles, since the value function is globally concave"
    - "Risk-seeking for all gambles, since loss aversion makes people aggressive to recover"
    - "Risk-averse for high-probability gains, but risk-seeking for high-probability losses"
    - "Risk-neutral whenever the expected monetary values of two options are equal"
  answer: 2
  explanation: "The fourfold pattern predicts: (1) risk-averse for high-probability gains — prefer a sure $900 over a 90% chance of $1,000; and (2) risk-seeking for high-probability losses — prefer a 90% chance of losing $1,000 over a sure loss of $900. This asymmetry — opposite risk attitudes depending on whether outcomes are framed as gains or losses — is impossible under a single concave utility function, but follows directly from the S-shaped value function. The loss domain has convex curvature (diminishing sensitivity to larger losses) which generates risk-seeking."

- question: "In prospect theory, losing $100 hurts roughly as much as gaining $100 feels good, since both produce equivalent changes in the value function."
  type: true-false
  answer: false
  explanation: "Loss aversion is one of the central findings of prospect theory: losses hurt more than equivalent gains feel good, typically by a factor of roughly 2. The value function is steeper in the loss domain than the gain domain. This asymmetry explains the endowment effect, the reluctance to realize losses ('riding losers'), and why people demand larger gains to compensate for risks of loss than the size of the risk would justify under expected utility theory."

- question: "Prospect theory predicts that the same person can rationally buy both lottery tickets and insurance, a combination that standard expected utility theory treats as contradictory."
  type: true-false
  answer: true
  explanation: "Expected utility theory requires a single utility function; risk-seeking for lotteries (convex utility) and risk-averse for insurance (concave utility) cannot coexist. Prospect theory resolves this through probability weighting: people overweight small probabilities, making the tiny chance of a jackpot loom large (risk-seeking for lotteries) and the tiny chance of a catastrophe loom large (risk-averse for insurance). Both behaviors stem from the same probability weighting function — no contradiction."

- question: "What is 'reference dependence' in prospect theory, and why does it matter? Give an example where two people receive the same dollar amount but one experiences it as a gain and the other as a loss."
  type: short-answer
  answer: "Reference dependence means people evaluate outcomes as gains or losses relative to a reference point (usually their current status quo or expectation), not as final wealth levels. The same dollar amount can feel like a gain or a loss depending on what the person expected. Example: an employee expecting a $5,000 bonus who receives $3,000 feels a loss of $2,000; an employee expecting no bonus who receives $3,000 feels a gain of $3,000 — though both have $3,000 more than before."
  explanation: "Reference dependence is the foundation of the theory's departures from expected utility. Once you know that people evaluate gains and losses relative to a reference point, and that losses hurt more than gains feel good, many real behaviors become predictable: investors hold losing stocks too long (selling would realize a loss relative to purchase price), marketers frame prices as discounts from a reference price, and negotiators anchor on a reference to make concessions feel like losses. The reference point is the key, and it is contextually determined — not fixed to total wealth."
```

## Explainer

Standard consumer theory and expected utility theory assume that people evaluate outcomes in terms of final wealth levels and weight probabilities linearly. From your study of utility theory and expected returns, you know the framework: a rational agent assigns utility to total wealth states and computes expected utility by multiplying each outcome's utility by its objective probability. This framework is elegant and powerful, but decades of experimental evidence show that real human decisions systematically violate it. **Prospect theory**, developed by Daniel Kahneman and Amos Tversky, replaces the normative model with a descriptive one that matches how people actually behave.

The first departure is **reference dependence**. People do not evaluate outcomes as final wealth levels — they evaluate them as gains or losses relative to a **reference point**, typically the status quo. Receiving $100 when you expected nothing feels like a gain; receiving $100 when you expected $200 feels like a loss. This matters because the **value function** is shaped differently on each side of the reference point. For gains, it is concave (diminishing sensitivity — the difference between $0 and $100 feels larger than between $900 and $1,000). For losses, it is convex (the same diminishing sensitivity applies to increasing losses). Critically, the value function is **steeper for losses than for gains** — a phenomenon called **loss aversion**. Losing $100 hurts roughly twice as much as gaining $100 feels good. This single feature explains the endowment effect (people demand more to give up an object than they would pay to acquire it) and why investors hold losing stocks too long while selling winners too quickly.

The second departure is **probability weighting**. Instead of using objective probabilities directly, people transform them through a weighting function that **overweights small probabilities** and **underweights large ones**. This explains why the same person buys both lottery tickets (overweighting the tiny chance of a jackpot) and insurance (overweighting the tiny chance of a catastrophe). Under expected utility theory, this combination is a contradiction — it requires a utility function that is simultaneously concave (risk-averse for insurance) and convex (risk-seeking for lotteries). Under prospect theory, it is perfectly consistent: the probability weighting function makes unlikely events loom larger than they should.

These features interact to produce a distinctive pattern called the **fourfold pattern of risk attitudes**. For high-probability gains, people are risk-averse (preferring a sure $900 over a 90% chance of $1,000). For low-probability gains, people are risk-seeking (preferring a 1% chance of $10,000 over a sure $100). For high-probability losses, people are risk-seeking (preferring a 90% chance of losing $1,000 over a sure loss of $900). For low-probability losses, people are risk-averse (preferring a sure loss of $100 over a 1% chance of losing $10,000). This fourfold pattern, which expected utility cannot produce, maps closely onto observed behavior in experiments, insurance markets, gambling, and litigation settlement decisions. Prospect theory does not claim people are irrational — it claims that the standard model of rationality misdescribes how people frame and evaluate risky choices.
