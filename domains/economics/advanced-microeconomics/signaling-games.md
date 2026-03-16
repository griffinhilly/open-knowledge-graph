---
id: signaling-games
title: Signaling Games
domain: economics
course: advanced-microeconomics
prerequisites:
- id: perfect-bayesian-equilibrium
  type: hard
- id: adverse-selection
  type: hard
- id: game-theory-basics-microeconomics
  type: hard
- id: bayesian-games-strategy
  type: hard
tags:
- contract-theory
- signaling
- information-revelation
stage: abstract-reasoning
status: draft
---

# Signaling Games

## Core Idea
In a signaling game, the informed player (agent) moves first by choosing an action (signal) that reveals or conceals type. The uninformed player (principal) observes the signal and chooses a response. Separating equilibrium: different types send different signals. Pooling equilibrium: all types send the same signal. Example: education as a signal of ability in the job market.

## How It's Best Learned
Analyze Spence's education signaling model. Draw payoff matrices and solve for equilibria. Identify when separating vs. pooling equilibria arise.

## Explainer

From your work on adverse selection, you know that private information can destroy markets: if buyers cannot distinguish high-quality sellers from low-quality ones, good sellers exit and the market unravels. Signaling games ask the next question — what if the informed party can *do something* to credibly reveal their type before the uninformed party acts? The key insight is that not just any action works as a signal. For a signal to separate types, it must be **differentially costly**: expensive enough for low types that they would not want to mimic, but cheap enough for high types that sending it is worthwhile given the reward.

The canonical example is **Spence's job market signaling model**. Suppose workers are either high-ability or low-ability, and employers cannot observe ability directly. Workers can choose to get a college degree before entering the job market. The critical assumption is that education is *less costly* for high-ability workers — not necessarily in tuition, but in effort, time, or opportunity cost. If this differential cost condition holds, a **separating equilibrium** can emerge: high-ability workers get degrees, low-ability workers do not, and employers rationally offer high wages to degree-holders and low wages to non-degree-holders. Crucially, in this pure signaling model, education need not increase productivity at all — it works purely as a sorting device.

The structure of the game follows directly from your knowledge of Bayesian games and perfect Bayesian equilibrium. Nature moves first, assigning a type to the sender (the informed player). The sender observes their type and chooses a signal. The receiver (the uninformed player) observes the signal, updates beliefs using Bayes' rule, and chooses an action. In a **separating equilibrium**, the receiver's beliefs are pinned down by Bayes' rule because each signal is sent by exactly one type. In a **pooling equilibrium**, all types send the same signal, so the receiver's posterior equals the prior — no information is transmitted. Semi-separating equilibria, where some types randomize, also exist.

The hardest part of solving signaling games is handling **off-equilibrium beliefs** — what the receiver believes when observing a signal that no type is supposed to send. Perfect Bayesian equilibrium alone does not restrict these beliefs, which means many pooling equilibria can be sustained by pessimistic off-path beliefs. Refinements like the **Intuitive Criterion** (Cho and Kreps) eliminate implausible equilibria by asking: if only one type could possibly benefit from deviating to the off-path signal, the receiver should assign probability one to that type. This refinement typically selects the most efficient separating equilibrium and rules out pooling equilibria where the high type would want to deviate.

Signaling games appear throughout economics beyond education: firms issue dividends to signal profitability, entrepreneurs retain equity to signal project quality, nations build military capacity to signal resolve, and warranties signal product durability. The unifying logic is always the same — credible communication requires costly action, and the cost must fall differently on different types. Without differential cost, signals are cheap talk and cannot credibly separate.
