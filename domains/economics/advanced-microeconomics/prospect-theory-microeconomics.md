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

## Explainer

Standard consumer theory and expected utility theory assume that people evaluate outcomes in terms of final wealth levels and weight probabilities linearly. From your study of utility theory and expected returns, you know the framework: a rational agent assigns utility to total wealth states and computes expected utility by multiplying each outcome's utility by its objective probability. This framework is elegant and powerful, but decades of experimental evidence show that real human decisions systematically violate it. **Prospect theory**, developed by Daniel Kahneman and Amos Tversky, replaces the normative model with a descriptive one that matches how people actually behave.

The first departure is **reference dependence**. People do not evaluate outcomes as final wealth levels — they evaluate them as gains or losses relative to a **reference point**, typically the status quo. Receiving $100 when you expected nothing feels like a gain; receiving $100 when you expected $200 feels like a loss. This matters because the **value function** is shaped differently on each side of the reference point. For gains, it is concave (diminishing sensitivity — the difference between $0 and $100 feels larger than between $900 and $1,000). For losses, it is convex (the same diminishing sensitivity applies to increasing losses). Critically, the value function is **steeper for losses than for gains** — a phenomenon called **loss aversion**. Losing $100 hurts roughly twice as much as gaining $100 feels good. This single feature explains the endowment effect (people demand more to give up an object than they would pay to acquire it) and why investors hold losing stocks too long while selling winners too quickly.

The second departure is **probability weighting**. Instead of using objective probabilities directly, people transform them through a weighting function that **overweights small probabilities** and **underweights large ones**. This explains why the same person buys both lottery tickets (overweighting the tiny chance of a jackpot) and insurance (overweighting the tiny chance of a catastrophe). Under expected utility theory, this combination is a contradiction — it requires a utility function that is simultaneously concave (risk-averse for insurance) and convex (risk-seeking for lotteries). Under prospect theory, it is perfectly consistent: the probability weighting function makes unlikely events loom larger than they should.

These features interact to produce a distinctive pattern called the **fourfold pattern of risk attitudes**. For high-probability gains, people are risk-averse (preferring a sure $900 over a 90% chance of $1,000). For low-probability gains, people are risk-seeking (preferring a 1% chance of $10,000 over a sure $100). For high-probability losses, people are risk-seeking (preferring a 90% chance of losing $1,000 over a sure loss of $900). For low-probability losses, people are risk-averse (preferring a sure loss of $100 over a 1% chance of losing $10,000). This fourfold pattern, which expected utility cannot produce, maps closely onto observed behavior in experiments, insurance markets, gambling, and litigation settlement decisions. Prospect theory does not claim people are irrational — it claims that the standard model of rationality misdescribes how people frame and evaluate risky choices.
