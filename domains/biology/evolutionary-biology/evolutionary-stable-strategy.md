---
id: evolutionary-stable-strategy
title: Evolutionary Stable Strategy (ESS)
domain: biology
course: evolutionary-biology
prerequisites:
- id: evolutionary-game-theory
  type: hard
tags:
- game-theory
- strategy
- evolution
stage: advanced
status: draft
---

# Evolutionary Stable Strategy (ESS)

## Core Idea
An evolutionary stable strategy (ESS) is a strategy that, once fixed in a population, cannot be invaded by alternative strategies because invaders do worse against the ESS than the ESS does against itself. ESS concept explains why mixed strategies (probabilistic play of alternatives) can be stable equilibria, such as in hawk-dove conflicts.

## Explainer

From evolutionary game theory, you know that an organism's fitness often depends not just on its own strategy but on what strategies others in the population are playing. An **evolutionarily stable strategy (ESS)** is the central solution concept in this framework: it is a strategy that, once adopted by the entire population, cannot be displaced by any rare mutant strategy. If a population playing the ESS is "invaded" by a small number of individuals using an alternative strategy, the invaders will do worse on average and be eliminated by selection. The ESS is an evolutionary equilibrium — not because nothing changes, but because any departure is self-correcting.

The classic illustration is the **Hawk-Dove game**. Imagine animals competing over a resource. Hawks always fight; Doves always yield. If everyone is a Dove, a single Hawk mutant wins every contest without a fight and spreads rapidly — so pure Dove is not an ESS. If everyone is a Hawk, individuals constantly injure each other in costly fights, and a Dove mutant that avoids injury can do better on average — so pure Hawk is not an ESS either. The ESS turns out to be a **mixed strategy**: each individual plays Hawk with some probability and Dove with the rest, calibrated so that the expected payoff from each pure strategy is equal. At this mixture, no alternative does better against the population, so the mix is stable.

What makes the ESS concept powerful is that it predicts outcomes without requiring that organisms consciously "choose" strategies. Natural selection acts as the optimizer: strategies that yield higher fitness spread, and the population converges on the ESS through differential reproduction. The ESS can be a single pure strategy (if one strategy beats all others when common), a mixed strategy within individuals (probabilistic behavior), or a **polymorphism** — a stable mix of distinct types in the population, each maintained because its fitness increases when it is rare (frequency-dependent selection).

The ESS framework has been applied far beyond animal contests. It explains the evolution of sex ratios (Fisher's principle as an ESS), the persistence of cooperative and cheating strategies in microbial populations, the timing of reproduction in seasonal breeders, and even aspects of plant growth strategies. In each case, the question is the same: given that everyone else is playing strategy X, can a mutant playing strategy Y invade? If no Y can invade, X is the ESS. This invasion criterion gives evolutionary biology a rigorous, game-theoretic tool for predicting which behaviors and life strategies should persist in nature.
