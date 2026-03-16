---
id: prospect-theory
title: 'Prospect Theory: Loss Aversion and Reference Dependence'
domain: economics
course: advanced-microeconomics
prerequisites:
- id: expected-return-and-variance-of-assets
  type: soft
tags:
- behavioral-economics
- decision-theory
stage: advanced
status: draft
---

# Prospect Theory: Loss Aversion and Reference Dependence

## Core Idea
Prospect Theory replaces expected utility with a value function exhibiting loss aversion (losses loom larger than gains) and reference dependence (utility depends on changes from a reference point). Probability weighting overweights small probabilities and underweights large ones. These features explain empirical regularities: reflection effect (risk-seeking for losses, risk-averse for gains), endowment effect (owning increases perceived value), and framing effects (choices depend on how outcomes are framed).

## Explainer

Standard expected utility theory, which you encountered through expected return and variance analysis, assumes that people evaluate outcomes based on final wealth levels and weight probabilities linearly. **Prospect theory**, developed by Kahneman and Tversky, starts from the observation that real human choices systematically violate these assumptions. People do not evaluate outcomes in terms of final wealth — they evaluate them as gains or losses relative to a **reference point**, typically the status quo. This single shift in framing transforms the entire theory of choice under uncertainty.

The **value function** in prospect theory has three distinctive features. First, it is defined over changes from the reference point, not absolute levels — losing $100 when you have $10,000 feels the same as losing $100 when you have $1,000,000. Second, it is concave for gains (diminishing sensitivity — the difference between gaining $100 and $200 feels larger than between $1,100 and $1,200) and convex for losses (the difference between losing $100 and $200 feels larger than between losing $1,100 and $1,200). Third, and most importantly, it is steeper for losses than for gains — this is **loss aversion**, typically estimated at about 2:1, meaning a loss of $100 feels roughly as bad as a gain of $200 feels good. The value function is therefore kinked at the reference point, creating an asymmetry that standard utility theory cannot capture.

The second major departure is **probability weighting**. Instead of multiplying values by objective probabilities, prospect theory applies a nonlinear weighting function π(p) that overweights small probabilities and underweights large ones. This explains why people simultaneously buy lottery tickets (overweighting the small probability of a large gain) and purchase insurance against rare disasters (overweighting the small probability of a large loss). The weighting function also exhibits a certainty effect: people strongly prefer outcomes that are certain over outcomes that are merely probable, even when the expected values are similar.

These features jointly explain a cluster of empirical puzzles. The **reflection effect** — people are risk-averse over gains but risk-seeking over losses — follows from the shape of the value function: its concavity in gains makes a sure gain attractive, while its convexity in losses makes a sure loss feel particularly painful, driving people to gamble for a chance of avoiding the loss entirely. The **endowment effect** — people demand more to give up an object than they would pay to acquire it — follows from loss aversion: giving up something you own is coded as a loss, which looms larger than the equivalent gain. **Framing effects** arise because the reference point determines whether an outcome is perceived as a gain or a loss, and different framings of the same objective outcome can shift the reference point, producing different choices. Prospect theory does not reject the idea that people respond to incentives — it refines our understanding of what the subjective incentives actually look like.
