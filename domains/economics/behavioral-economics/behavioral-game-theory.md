---
id: behavioral-game-theory
title: Behavioral Game Theory
domain: economics
course: behavioral-economics
prerequisites:
- id: bounded-rationality
  type: hard
- id: game-theory-basics-microeconomics
  type: hard
- id: nash-equilibrium-microeconomics
  type: hard
- id: experimental-economics-methods
  type: soft
tags:
- level-k
- cognitive-hierarchy
- quantal-response-equilibrium
- Camerer
- strategic-cognition
stage: advanced
status: validated
---

# Behavioral Game Theory

## Core Idea
Behavioral game theory studies how people actually make strategic decisions, documenting systematic departures from Nash equilibrium and developing formal models that incorporate bounded rationality into strategic interaction. Three major frameworks have emerged: level-k thinking models, where players differ in how many steps of strategic reasoning they perform (level-0 randomizes, level-1 best-responds to level-0, level-2 best-responds to level-1, etc.); cognitive hierarchy models (Camerer, Ho, and Chong, 2004), which generalize level-k by allowing players to best-respond to a Poisson-distributed mixture of lower levels; and quantal response equilibrium (McKelvey and Palfrey, 1995), where players choose better strategies more often but make errors proportional to a noise parameter, converging to Nash as noise vanishes. These models explain canonical anomalies — overbidding in auctions, under-contribution in public goods games, and non-equilibrium play in beauty contest games — that standard game theory cannot.

## Questions

```yaml
- question: "In a beauty contest game where players choose numbers from 0 to 100 and the winner is closest to 2/3 of the average, the Nash equilibrium is 0. In experiments, the average choice is typically around..."
  type: multiple-choice
  options:
    - "0, confirming Nash equilibrium predictions"
    - "33, consistent with one step of strategic reasoning (level-1 thinking: best-respond to uniform random play at 50)"
    - "50, because players choose randomly"
    - "67, because players multiply the maximum by 2/3"
  answer: 1
  explanation: "The typical experimental result clusters around 33, with a secondary cluster near 22 (level-2 thinking: best-respond to level-1 at 33). A level-0 player randomizes (mean 50), a level-1 player best-responds to level-0 by choosing 2/3 * 50 = 33, a level-2 player chooses 2/3 * 33 = 22, and so on converging to 0. The data suggest most players perform 1-2 steps of strategic reasoning, not the infinite recursion required for Nash equilibrium. With experience (repeated play), choices converge toward the Nash prediction, but initial play is well-described by level-k with low k."

- question: "Quantal response equilibrium assumes that players always best-respond to their beliefs about other players' strategies."
  type: true-false
  answer: false
  explanation: "QRE assumes players choose better strategies more often than worse ones, but with noise — they do not perfectly best-respond. The probability of choosing a strategy increases with its expected payoff according to a logistic (or similar) response function governed by a precision parameter lambda. When lambda is infinite, QRE collapses to Nash equilibrium (perfect best response). When lambda is zero, players randomize uniformly. QRE is an equilibrium concept because players' noisy strategies are mutually consistent — each player's choice probabilities are a quantal (noisy) best response to the other players' choice probabilities. This captures the intuition that people are roughly strategic but make mistakes, with costlier mistakes being rarer."

- question: "What distinguishes level-k models from cognitive hierarchy models, and why does the distinction matter empirically?"
  type: short-answer
  answer: "In level-k models, each player believes all other players are exactly one level below them — a level-2 player assumes everyone else is level-1. In cognitive hierarchy models, each level-k player best-responds to a mixture of all lower types (0 through k-1), weighted by a frequency distribution (typically Poisson). The distinction matters because level-k predicts sharp, level-specific behavior (a level-2 player ignores the existence of level-0 players), while cognitive hierarchy produces smoother predictions by averaging over the lower-level population. Cognitive hierarchy generally fits experimental data better because it accounts for the heterogeneity of opponents a player might face."
  explanation: "The Poisson distribution in the cognitive hierarchy model is governed by a single parameter tau (the average number of thinking steps), making it parsimonious. Camerer, Ho, and Chong found tau around 1.5 fits a wide range of experimental games — suggesting people average about 1.5 steps of strategic reasoning. This parameter is remarkably stable across different game forms, giving the model predictive power for new games rather than just post-hoc fit."
```

## Explainer

Standard game theory assumes that players are perfectly rational, have correct beliefs about others' rationality, and reason through infinite levels of "I think that you think that I think..." until reaching Nash equilibrium. Behavioral game theory starts from the empirical observation that this assumption fails systematically: in experiments, people rarely play Nash strategies in one-shot games, they overbid in auctions, they contribute to public goods when free-riding is dominant, and they reject unfair offers when acceptance is strategically optimal. The question is not whether Nash fails descriptively — that is clear — but what formal model better predicts actual strategic behavior.

The level-k framework provides one answer. Instead of assuming all players perform infinite strategic reasoning, it assigns each player a discrete "level" of thinking. A level-0 player does not reason strategically at all — they might randomize uniformly or follow a salient focal point. A level-1 player assumes everyone else is level-0 and best-responds accordingly. A level-2 player assumes everyone else is level-1 and best-responds to that. The beauty contest game illustrates this cleanly: with a target of 2/3 of the average and a range of 0-100, level-0 averages 50, level-1 chooses 33, level-2 chooses 22, level-3 chooses 15, and the Nash equilibrium of 0 requires infinite levels. Experimental data cluster around 33 and 22, suggesting most people are level-1 or level-2 thinkers in novel strategic situations.

Cognitive hierarchy (CH) refines level-k in an important way. In level-k models, a level-2 player assumes everyone is level-1 — ignoring level-0 players entirely. In the cognitive hierarchy model, a level-2 player best-responds to a mixture of level-0 and level-1 players, weighted by their estimated frequencies in the population. The distribution of types follows a Poisson distribution with a single parameter tau representing the average number of thinking steps. This produces smoother and generally more accurate predictions. Camerer, Ho, and Chong (2004) estimated tau around 1.5 across dozens of experimental games — a stable parameter that gives the model genuine out-of-sample predictive power.

Quantal response equilibrium takes a different approach entirely. Rather than modeling discrete levels of reasoning, QRE assumes all players are noisy optimizers: they choose better strategies more often than worse ones, but with error. The key innovation is that the noise is endogenous to the equilibrium — each player's noisy strategy is a quantal best response to the other players' noisy strategies. When the precision parameter lambda is high, choices are nearly optimal and QRE approximates Nash. When lambda is low, choices are nearly random. QRE explains several puzzles simultaneously: the tendency to play dominated strategies at low rates (not zero, as Nash predicts), the sensitivity of behavior to payoff magnitudes (people play closer to Nash when stakes are higher, because the cost of errors is higher), and the persistent but declining deviations from equilibrium with experience.

These three frameworks are not mutually exclusive — they capture different aspects of bounded rationality in strategic settings. Level-k and cognitive hierarchy model limited depth of strategic reasoning (people do not think far enough ahead). QRE models imprecise execution of strategic reasoning (people think roughly correctly but implement noisily). Empirically, level-k/CH models fit initial play in novel games better, while QRE fits experienced play and games with continuous strategy spaces better. Together, they constitute the theoretical core of behavioral game theory and have been applied to auctions, mechanism design, political competition, and bargaining, producing both better predictions and better-designed institutions.
