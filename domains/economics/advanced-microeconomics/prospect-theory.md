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
stage: expert
status: validated
---

# Prospect Theory: Loss Aversion and Reference Dependence

## Core Idea
Prospect Theory replaces expected utility with a value function exhibiting loss aversion (losses loom larger than gains) and reference dependence (utility depends on changes from a reference point). Probability weighting overweights small probabilities and underweights large ones. These features explain empirical regularities: reflection effect (risk-seeking for losses, risk-averse for gains), endowment effect (owning increases perceived value), and framing effects (choices depend on how outcomes are framed).

## Questions

```yaml
- question: "You own a stock currently worth $500. You are offered a trade: exchange it for another stock that has equal odds of being worth $400 or $700. According to prospect theory, most people will:"
  type: multiple-choice
  options:
    - "Decline the trade — the potential loss of $100 (relative to the $500 reference point) looms roughly twice as large as the potential gain of $200, making the gamble subjectively unattractive despite its positive expected value"
    - "Accept the trade — rational agents always accept gambles with positive expected value, and prospect theory does not change this"
    - "Be indifferent — prospect theory only applies when the amounts are very large or very small"
    - "Accept the trade — probability weighting overweights the 50% chance of gaining $200, making the gamble attractive"
  answer: 0
  explanation: "Loss aversion, estimated at roughly 2:1, means the pain of a $100 loss is weighted about twice as heavily as the pleasure of a $200 gain. Even though the gamble has a positive expected value of $50 relative to keeping the current stock, the asymmetric value function makes most people prefer the certain $500. This is not irrational within prospect theory's framework — it reflects genuine subjective disutility of losses. The expected-value argument (option B) describes behavior under standard expected utility theory, not prospect theory."

- question: "A participant in a study is offered a choice: (A) a certain gain of $500, or (B) a 50% chance of gaining $1,000. The same participant, given a separate choice between (C) a certain loss of $500 or (D) a 50% chance of losing $1,000, prefers option D. Which pattern of behavior does this illustrate?"
  type: multiple-choice
  options:
    - "The reflection effect — people are risk-averse for gains (preferring A over B) but risk-seeking for losses (preferring D over C), because the value function is concave above the reference point and convex below it"
    - "Loss aversion — the participant is simply avoiding any outcome involving a loss, which is why they prefer the gamble in the loss domain"
    - "Probability weighting — overweighting the 50% probability makes the gamble attractive in both domains equally"
    - "Reference dependence — the participant's reference point shifts between the two problems, making A and D both 'gains' from their subjective perspective"
  answer: 0
  explanation: "The reflection effect is one of prospect theory's key predictions. In the gain domain, the value function is concave — diminishing marginal sensitivity means a certain $500 feels better than a coin flip for $1,000 (risk aversion). In the loss domain, the value function is convex — the certain loss of $500 feels worse than the coin flip for $1,000, because the first $500 of loss hurts more than the next $500 (risk seeking). The two choices are mirror images across the reference point. Loss aversion (option B) is a distinct concept — it concerns the asymmetry between gains and losses at the reference point, not the within-domain curvature."

- question: "According to prospect theory, a person who loses $100 when they have $10,000 in savings experiences approximately the same decrease in subjective value as a person who loses $100 when they have $1,000,000 in savings."
  type: true-false
  answer: true
  explanation: "This follows directly from prospect theory's reference dependence: the value function is defined over changes from the current reference point (typically the status quo), not over final wealth levels. A $100 loss is a $100 loss regardless of initial wealth — the value function responds to the magnitude of the change, not the ending position. This contrasts sharply with standard expected utility theory, where a risk-averse agent with $1,000,000 would suffer less disutility from a $100 loss than a person with $10,000, because the marginal utility of wealth is lower at higher wealth levels."

- question: "Prospect theory's probability weighting function implies that people systematically overweight most probabilities that differ from the extremes of 0 and 1."
  type: true-false
  answer: false
  explanation: "The probability weighting function is not uniformly above the 45-degree line. It overweights small probabilities (transforming, say, 1% into a subjective weight of 5%) but underweights large probabilities (transforming, say, 90% into a subjective weight of 70%). The weighting function typically crosses the 45-degree line at some intermediate probability. This explains why people simultaneously buy lottery tickets (overweighting a tiny chance of a large gain) and purchase insurance (overweighting a tiny chance of a large loss), but also exhibit the certainty effect — strongly preferring a guaranteed outcome over a near-certain one, because moving from, say, 99% to 100% probability receives a large subjective jump."

- question: "Why does prospect theory predict that the same person might both buy a lottery ticket and purchase insurance against a rare disaster? What single feature of the theory explains both behaviors?"
  type: short-answer
  answer: "Both behaviors are driven by the probability weighting function, which overweights small probabilities. A lottery ticket involves a tiny probability of a large gain — overweighting this small probability makes the ticket's subjective expected value seem higher than its objective expected value, making it attractive despite being a bad bet. Insurance involves a tiny probability of a large loss — overweighting this small probability makes the disaster feel more likely subjectively, so the insurance premium seems worthwhile. Standard expected utility with risk aversion predicts insurance but not lottery-buying; prospect theory's probability weighting explains both with a single mechanism."
  explanation: "This is a case where prospect theory is genuinely more parsimonious than standard theory: it resolves an apparent contradiction (the same person being risk-averse and risk-seeking) by showing both behaviors stem from the same distortion in probability perception rather than from inconsistency or irrationality."
```

## Explainer

Standard expected utility theory, which you encountered through expected return and variance analysis, assumes that people evaluate outcomes based on final wealth levels and weight probabilities linearly. **Prospect theory**, developed by Kahneman and Tversky, starts from the observation that real human choices systematically violate these assumptions. People do not evaluate outcomes in terms of final wealth — they evaluate them as gains or losses relative to a **reference point**, typically the status quo. This single shift in framing transforms the entire theory of choice under uncertainty.

The **value function** in prospect theory has three distinctive features. First, it is defined over changes from the reference point, not absolute levels — losing $100 when you have $10,000 feels the same as losing $100 when you have $1,000,000. Second, it is concave for gains (diminishing sensitivity — the difference between gaining $100 and $200 feels larger than between $1,100 and $1,200) and convex for losses (the difference between losing $100 and $200 feels larger than between losing $1,100 and $1,200). Third, and most importantly, it is steeper for losses than for gains — this is **loss aversion**, typically estimated at about 2:1, meaning a loss of $100 feels roughly as bad as a gain of $200 feels good. The value function is therefore kinked at the reference point, creating an asymmetry that standard utility theory cannot capture.

The second major departure is **probability weighting**. Instead of multiplying values by objective probabilities, prospect theory applies a nonlinear weighting function π(p) that overweights small probabilities and underweights large ones. This explains why people simultaneously buy lottery tickets (overweighting the small probability of a large gain) and purchase insurance against rare disasters (overweighting the small probability of a large loss). The weighting function also exhibits a certainty effect: people strongly prefer outcomes that are certain over outcomes that are merely probable, even when the expected values are similar.

These features jointly explain a cluster of empirical puzzles. The **reflection effect** — people are risk-averse over gains but risk-seeking over losses — follows from the shape of the value function: its concavity in gains makes a sure gain attractive, while its convexity in losses makes a sure loss feel particularly painful, driving people to gamble for a chance of avoiding the loss entirely. The **endowment effect** — people demand more to give up an object than they would pay to acquire it — follows from loss aversion: giving up something you own is coded as a loss, which looms larger than the equivalent gain. **Framing effects** arise because the reference point determines whether an outcome is perceived as a gain or a loss, and different framings of the same objective outcome can shift the reference point, producing different choices. Prospect theory does not reject the idea that people respond to incentives — it refines our understanding of what the subjective incentives actually look like.
