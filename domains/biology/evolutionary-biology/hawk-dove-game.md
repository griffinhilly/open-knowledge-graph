---
id: hawk-dove-game
title: The Hawk-Dove Game
domain: biology
course: evolutionary-biology
prerequisites:
- id: evolutionary-game-theory
  type: hard
builds-toward:
- evolutionary-stable-strategy
tags:
- game-theory
- conflict
- mixed-strategy
- behavior
stage: advanced
status: draft
---

# The Hawk-Dove Game

## Core Idea
The Hawk-Dove game models conflict over a resource: Hawks fight (winning or losing) while Doves retreat, avoiding injury. At equilibrium, neither pure strategy is stable; instead, a mixed strategy evolves where the frequency of Hawks is determined by fitness equality. This game explains why animals sometimes fight fiercely and sometimes retreat, depending on population composition.

## Explainer

From your study of evolutionary game theory, you know that an organism's fitness depends not just on its own strategy but on what strategies others in the population are playing. The Hawk-Dove game is the simplest and most foundational model in this framework, and it answers a question that puzzled early ethologists: if fighting ability determines access to resources, why don't animals always fight to the death?

The setup is deliberately minimal. Two individuals contest a resource worth **V** fitness units. Each plays one of two strategies: **Hawk** (escalate and fight until you win or are injured) or **Dove** (display but retreat if the opponent escalates). When two Hawks meet, they fight — each has a 50% chance of winning the resource and a 50% chance of sustaining an injury costing **C** fitness units. The average Hawk-vs-Hawk payoff is therefore (V − C)/2. When a Hawk meets a Dove, the Dove retreats immediately, so the Hawk gets V and the Dove gets 0. When two Doves meet, they share the resource through display, each getting V/2. You can arrange these payoffs in a 2×2 matrix, and the dynamics follow directly.

The critical insight emerges from asking: can either strategy take over the population? If everyone is a Dove, a rare Hawk mutant wins every encounter (getting V instead of V/2), so it invades — Dove is not stable. If everyone is a Hawk and the cost of fighting exceeds the resource value (C > V), each Hawk-vs-Hawk encounter yields a negative expected payoff of (V − C)/2, while a rare Dove mutant gets 0 against Hawks, which is better than a negative number. So Hawk is not stable either. Neither pure strategy is an **evolutionarily stable strategy** (ESS) when C > V. Instead, the population settles at a **mixed equilibrium** where the proportion of Hawks equals V/C. At this frequency, the average fitness of Hawks and Doves is exactly equal, so neither strategy has an advantage — any deviation from this ratio is self-correcting.

This equilibrium can be interpreted in two equivalent ways. In a **mixed-strategy** interpretation, each individual probabilistically plays Hawk with probability V/C and Dove with probability 1 − V/C. In a **polymorphism** interpretation, V/C of the population are pure Hawks and 1 − V/C are pure Doves. Both produce the same population-level outcome. The biological prediction is concrete: when the cost of injury is high relative to the resource value (C >> V), aggressive encounters should be rare and most contests should be settled by ritualized display — exactly what we observe in species with dangerous weapons (venomous snakes rarely bite each other in territorial disputes; they wrestle). When resources are extremely valuable relative to injury cost (V ≈ C), fighting should be common — as seen in male elephant seals, where access to a harem justifies the risk of severe injury.

The Hawk-Dove game is the starting point for richer models. Adding a third strategy — **Bourgeois** (play Hawk if you are the territory holder, Dove if you are the interloper) — explains why "ownership conventions" are so common in nature: the Bourgeois strategy is an ESS because it avoids costly symmetric fights. Adding asymmetries in fighting ability, resource value, or information produces models that better match the complexity of real animal conflicts. But the core lesson of the basic Hawk-Dove game remains: **natural selection does not maximize aggression — it balances the costs and benefits of fighting in a frequency-dependent way**, producing populations where restraint and escalation coexist in predictable proportions.
