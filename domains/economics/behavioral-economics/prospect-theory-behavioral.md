---
id: prospect-theory-behavioral
title: Prospect Theory
domain: economics
course: behavioral-economics
prerequisites:
- id: bounded-rationality
  type: hard
- id: expected-value
  type: soft
- id: consumer-theory-utility
  type: soft
tags:
- Kahneman
- Tversky
- reference-dependence
- probability-weighting
- value-function
stage: advanced
status: validated
---

# Prospect Theory

## Core Idea
Prospect theory (Kahneman & Tversky, 1979) is the most influential alternative to expected utility theory for modeling decision-making under risk. It introduces three key departures from standard theory: (1) outcomes are evaluated as gains or losses relative to a reference point rather than as final wealth states; (2) the value function is concave for gains (risk aversion) but convex for losses (risk seeking), with losses looming larger than equivalent gains (loss aversion); and (3) people overweight small probabilities and underweight large probabilities (probability weighting function). Prospect theory explains a wide range of anomalies that expected utility theory cannot — including the simultaneous purchase of insurance and lottery tickets, the endowment effect, and the disposition effect in financial markets.

## Questions

```yaml
- question: "According to prospect theory, a person who has just gained $1,000 and faces a choice between a certain gain of $500 and a 50% chance of gaining $1,000 (or nothing) will most likely..."
  type: multiple-choice
  options:
    - "Choose the gamble because they are in the domain of gains and are risk-seeking"
    - "Choose the certain $500 because the value function is concave in the domain of gains, producing risk aversion"
    - "Be indifferent between the two options because the expected values are identical"
    - "Refuse both options due to loss aversion"
  answer: 1
  explanation: "In the domain of gains, the prospect theory value function is concave — diminishing sensitivity means that the certain $500 is valued more than a 50% chance of $1,000 because the psychological difference between $0 and $500 is larger than between $500 and $1,000. This produces risk aversion for gains — the certainty of $500 is preferred. The mirror pattern holds for losses: in the loss domain, the convex value function produces risk seeking, which is why people gamble to avoid certain losses."

- question: "Expected utility theory and prospect theory make identical predictions about how people evaluate risky choices."
  type: true-false
  answer: false
  explanation: "The theories make systematically different predictions. Expected utility evaluates outcomes as final wealth states, is linear in probabilities, and predicts consistent risk attitudes. Prospect theory evaluates outcomes relative to a reference point, uses a nonlinear value function (concave for gains, convex for losses, with loss aversion), and applies a probability weighting function that overweights small probabilities and underweights large ones. These differences produce divergent predictions: prospect theory predicts the reflection effect (risk aversion for gains, risk seeking for losses), the certainty effect, and loss aversion — all of which violate expected utility."

- question: "What is the reference point in prospect theory, and why does it matter so much for decision-making?"
  type: short-answer
  answer: "The reference point is the baseline against which outcomes are evaluated as gains or losses. It is typically the status quo, but can be an expectation, aspiration level, or social comparison. It matters because the same objective outcome can be perceived as a gain or a loss depending on the reference point, and the value function treats gains and losses asymmetrically — losses loom roughly twice as large as equivalent gains. Shifting the reference point can reverse preferences even when the objective options are identical."
  explanation: "Reference-dependence is what makes prospect theory fundamentally different from expected utility theory, which evaluates outcomes as final wealth states independent of any starting point. A person with $100,000 who gained $10,000 is in a very different psychological state from a person with $100,000 who lost $10,000 — even though their current wealth is identical. The reference point introduces context-sensitivity into evaluation, which standard theory deliberately excludes but which profoundly affects real behavior."
```

## Explainer

Expected utility theory, the standard framework for decision-making under risk since von Neumann and Morgenstern (1944), treats people as evaluating options based on their final wealth states, with consistent risk attitudes and linear probability assessment. It is elegant and powerful, but it fails to explain a large and systematic set of observed behaviors. Prospect theory was developed to account for these failures — not by tweaking expected utility at the margins but by proposing a fundamentally different model of how people evaluate risky outcomes.

The first key innovation is reference-dependence. Standard theory says that a person evaluating a gamble considers how each possible outcome would affect their total wealth. Prospect theory says people evaluate outcomes relative to a reference point — typically the status quo — and code them as gains or losses from that reference. This seemingly subtle shift has profound consequences because the value function is not symmetric around the reference point. Gains and losses of the same magnitude do not have equal psychological impact.

The value function has three defining features. First, it is concave in the domain of gains: the subjective difference between gaining $0 and $100 is larger than between gaining $900 and $1,000 (diminishing sensitivity to gains). This produces risk aversion for gains — people prefer a certain $100 to a 50/50 chance of $200. Second, it is convex in the domain of losses: the subjective difference between losing $0 and $100 is larger than between losing $900 and $1,000 (diminishing sensitivity to losses). This produces risk seeking for losses — people prefer a 50/50 gamble between losing $200 and losing nothing to a certain loss of $100. Third, the value function is steeper for losses than for gains — loss aversion, estimated at roughly 2:1. Losing $100 feels about twice as bad as gaining $100 feels good. This single feature explains why people reject gambles with positive expected value (like a coin flip for +$110 or -$100), why they hold losing stocks too long, and why they demand much more to sell a good they own than they would pay to acquire it.

The probability weighting function is the second major innovation. Standard theory assumes that people weight outcomes by their objective probabilities. Prospect theory proposes a nonlinear weighting function: small probabilities are overweighted (making both lottery tickets and insurance attractive) and large probabilities are underweighted (reducing the subjective certainty of very likely outcomes). This probability distortion explains why people simultaneously insure against rare catastrophes (overweighting small probabilities of loss) and buy lottery tickets (overweighting small probabilities of gain) — a pattern that expected utility theory cannot reconcile.

Prospect theory's impact extends far beyond the laboratory. In finance, it explains the disposition effect (selling winners too early and holding losers too long), the equity premium puzzle (the surprisingly large premium demanded for holding risky stocks), and loss-averse investor behavior. In labor economics, it explains why taxi drivers work fewer hours on high-wage days (they have a daily income target — a reference point — and quit once they reach it). In public policy, it explains why framing a policy as preventing a loss is more persuasive than framing the same policy as achieving a gain. The theory earned Kahneman the 2002 Nobel Prize in Economics — the first psychologist to receive the economics prize — and remains the cornerstone of behavioral economics.
