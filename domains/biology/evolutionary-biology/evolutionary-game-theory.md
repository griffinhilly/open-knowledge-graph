---
id: evolutionary-game-theory
title: Evolutionary Game Theory
domain: biology
course: evolutionary-biology
prerequisites:
- id: natural-selection
  type: hard
- id: probability-axioms
  type: soft
builds-toward:
- evolutionary-stable-strategy
- arms-race-coevolution
tags:
- game-theory
- behavior
- evolution
stage: advanced
status: draft
---

# Evolutionary Game Theory

## Core Idea
Evolutionary game theory applies game theory to evolution by treating organisms as players with fitness payoffs determined by strategy frequencies in the population. Strategies that perform well against the current population composition can invade, leading to dynamic equilibria. Game theory explains cooperation, conflict, and signaling evolution.

## Explainer

From your understanding of natural selection, you know that traits increasing an organism's fitness tend to spread through populations. But there is a complication that simple fitness calculations miss: the best strategy for an individual often depends on what everyone else is doing. A hawk-like aggressive fighter does well in a population of doves, but poorly when surrounded by other hawks who fight back. **Evolutionary game theory** provides the mathematical framework for analyzing exactly these frequency-dependent situations, where fitness is not a fixed property of a trait but a function of the strategies present in the population.

The foundational concept is the **payoff matrix**, borrowed from classical game theory but reinterpreted in biological terms. Instead of dollars, payoffs are measured in fitness — survival and reproductive success. Consider the classic **Hawk-Dove game**: two individuals compete over a resource. Hawks always fight; Doves always yield. When a Hawk meets a Dove, the Hawk takes everything. When two Doves meet, they share the resource. When two Hawks meet, they fight and both suffer injury costs. You can immediately see that being a Hawk is great when Hawks are rare (you almost always meet Doves and win easily), but terrible when Hawks are common (you constantly fight and get injured). This frequency dependence means neither pure strategy dominates, and the population settles at a **mixed equilibrium** where Hawks and Doves coexist at the ratio where their average fitness is equal.

The key concept that emerges from this analysis is the **evolutionarily stable strategy** (ESS) — a strategy that, once common in the population, cannot be invaded by any rare alternative. If everyone plays the ESS and a mutant with a different strategy appears, that mutant will have lower fitness and be eliminated. The ESS is not necessarily the strategy that maximizes group welfare or even individual payoff in isolation — it is the strategy that is stable against invasion. In the Hawk-Dove game, the ESS is typically a mixed strategy (or a population mix), not pure Hawk or pure Dove. This explains a widespread biological pattern: many animal contests are settled by ritualized displays rather than all-out fights, because the mixed strategy favoring restraint in many encounters is evolutionarily stable.

Evolutionary game theory has been transformative for understanding behaviors that seem to defy simple natural selection. **Cooperation** is a puzzle because cooperators can be exploited by cheaters, yet cooperation is widespread in nature. Game-theoretic models like the iterated Prisoner's Dilemma show that cooperation can be stable when individuals interact repeatedly and can retaliate against defectors — the famous **tit-for-tat** strategy. **Signaling** is another domain: why do male peacocks grow enormous, costly tails? Handicap signaling models show that only genuinely high-quality males can afford the cost, making the signal honest and evolutionarily stable. In each case, the game-theoretic approach reveals that the fitness of a behavior cannot be evaluated in isolation — it depends on the social environment, which is itself evolving. This recursive quality is what makes evolutionary game theory both challenging and indispensable for understanding the evolution of social behavior.
