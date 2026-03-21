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

## Questions

```yaml
- question: "In a population consisting entirely of Doves, a single Hawk mutant appears. What happens, and what does this reveal about the stability of the all-Dove strategy?"
  type: multiple-choice
  options:
    - "The Hawk is outcompeted because cooperative Dove populations are more productive overall"
    - "The Hawk invades successfully — it wins every contest, getting V instead of V/2, so pure Dove is not an ESS"
    - "The Hawk is neutral — it gets the same fitness as Doves when it is rare because it rarely meets other Hawks"
    - "The Hawk invades only if V > C; otherwise it does no better than Doves"
  answer: 1
  explanation: "In an all-Dove population, every contest ends in display and resource sharing — each Dove gets V/2. A rare Hawk wins every contest because Doves retreat immediately, so the Hawk always gets V > V/2. This positive fitness advantage means the Hawk can invade and spread. The all-Dove state is therefore not an evolutionarily stable strategy (ESS) regardless of the values of V and C. Option D conflates the condition for a mixed ESS with the condition for Hawk to invade an all-Dove population — those are different questions."

- question: "Under what condition is a pure Hawk strategy itself evolutionarily stable (resistant to invasion by Dove mutants)?"
  type: multiple-choice
  options:
    - "When C > V — injury cost exceeds resource value, making fighting too risky for pure Hawks"
    - "When V > C — resource value exceeds injury cost, so Hawks in an all-Hawk population still earn positive expected payoffs that exceed what a rare Dove earns"
    - "Never — Hawk is always invaded by Doves regardless of V and C"
    - "When V = C — the costs and benefits exactly balance, making Hawk neutral"
  answer: 1
  explanation: "In an all-Hawk population, each individual earns (V − C)/2 on average. A rare Dove earns 0 (it always retreats against Hawks). If V > C, then (V − C)/2 > 0 > 0... wait, the Dove earns exactly 0 regardless, and Hawks earn (V−C)/2. When V > C, (V−C)/2 > 0 > Dove's payoff? No — Dove earns 0, which equals Dove's payoff. Actually when V > C, Hawks get (V-C)/2 which is positive, and a rare Dove gets 0. Since 0 < (V-C)/2, Doves cannot invade — pure Hawk is an ESS. When C > V, (V-C)/2 is negative, so rare Doves get 0 which is better, and Dove can invade. This is why C > V is the condition for a mixed equilibrium."

- question: "At the mixed ESS in the Hawk-Dove game (with C > V), the average fitness of Hawks exactly equals the average fitness of Doves, so neither strategy has a selective advantage."
  type: true-false
  answer: true
  explanation: "The mixed equilibrium frequency V/C is defined by the condition that fitness is equalized across strategies. At this frequency, the payoff for playing Hawk (averaged over encounters with Hawks and Doves in proportion V/C and 1−V/C) equals the payoff for playing Dove. This equality is precisely what makes the equilibrium stable: if Hawks become too common, their average fitness drops below Doves' (because they encounter costly Hawk-Hawk fights more often), reducing their frequency back toward V/C. Conversely, if Doves become too common, Hawks do better, restoring the ratio."

- question: "Natural selection consistently favors the most aggressive strategy in any population, because aggression provides direct access to resources."
  type: true-false
  answer: false
  explanation: "The Hawk-Dove game demonstrates the opposite: fitness is frequency-dependent, not absolute. When Hawks are rare, aggression is highly profitable (they mostly meet Doves and win). As Hawks become common, they increasingly encounter each other, paying injury costs that erode fitness. At frequency V/C, Hawk fitness falls to equal Dove fitness and further spread stops. Natural selection does not maximize aggression — it produces a stable balance point where the costs and benefits of fighting exactly counterbalance each other. Species with dangerous weapons (snakes, deer) often show ritualized rather than lethal conflict, consistent with high C relative to V."

- question: "Explain why neither pure Hawk nor pure Dove is an evolutionarily stable strategy when the cost of injury (C) exceeds the resource value (V), and describe the equilibrium that evolves instead."
  type: short-answer
  answer: "Pure Dove is unstable because a rare Hawk mutant always outcompetes Doves — it wins every contest (getting V vs. Dove's V/2) and can invade. Pure Hawk is unstable when C > V because in an all-Hawk population each individual earns (V−C)/2, which is negative; a rare Dove mutant earns 0 by retreating, which is better than a negative payoff, so Doves can invade. Since each pure strategy can be invaded by the other, neither is an ESS. The stable outcome is a mixed equilibrium: the proportion of Hawks in the population (or the probability any individual plays Hawk) settles at V/C, the frequency at which the average fitness of Hawks equals the average fitness of Doves, so neither strategy has a net selective advantage."
  explanation: "This illustrates frequency-dependent selection: the fitness of a strategy depends on how common it is. The equilibrium is self-correcting — any deviation from V/C creates a selective pressure that returns the population to that ratio."
```

## Explainer

From your study of evolutionary game theory, you know that an organism's fitness depends not just on its own strategy but on what strategies others in the population are playing. The Hawk-Dove game is the simplest and most foundational model in this framework, and it answers a question that puzzled early ethologists: if fighting ability determines access to resources, why don't animals always fight to the death?

The setup is deliberately minimal. Two individuals contest a resource worth **V** fitness units. Each plays one of two strategies: **Hawk** (escalate and fight until you win or are injured) or **Dove** (display but retreat if the opponent escalates). When two Hawks meet, they fight — each has a 50% chance of winning the resource and a 50% chance of sustaining an injury costing **C** fitness units. The average Hawk-vs-Hawk payoff is therefore (V − C)/2. When a Hawk meets a Dove, the Dove retreats immediately, so the Hawk gets V and the Dove gets 0. When two Doves meet, they share the resource through display, each getting V/2. You can arrange these payoffs in a 2×2 matrix, and the dynamics follow directly.

The critical insight emerges from asking: can either strategy take over the population? If everyone is a Dove, a rare Hawk mutant wins every encounter (getting V instead of V/2), so it invades — Dove is not stable. If everyone is a Hawk and the cost of fighting exceeds the resource value (C > V), each Hawk-vs-Hawk encounter yields a negative expected payoff of (V − C)/2, while a rare Dove mutant gets 0 against Hawks, which is better than a negative number. So Hawk is not stable either. Neither pure strategy is an **evolutionarily stable strategy** (ESS) when C > V. Instead, the population settles at a **mixed equilibrium** where the proportion of Hawks equals V/C. At this frequency, the average fitness of Hawks and Doves is exactly equal, so neither strategy has an advantage — any deviation from this ratio is self-correcting.

This equilibrium can be interpreted in two equivalent ways. In a **mixed-strategy** interpretation, each individual probabilistically plays Hawk with probability V/C and Dove with probability 1 − V/C. In a **polymorphism** interpretation, V/C of the population are pure Hawks and 1 − V/C are pure Doves. Both produce the same population-level outcome. The biological prediction is concrete: when the cost of injury is high relative to the resource value (C >> V), aggressive encounters should be rare and most contests should be settled by ritualized display — exactly what we observe in species with dangerous weapons (venomous snakes rarely bite each other in territorial disputes; they wrestle). When resources are extremely valuable relative to injury cost (V ≈ C), fighting should be common — as seen in male elephant seals, where access to a harem justifies the risk of severe injury.

The Hawk-Dove game is the starting point for richer models. Adding a third strategy — **Bourgeois** (play Hawk if you are the territory holder, Dove if you are the interloper) — explains why "ownership conventions" are so common in nature: the Bourgeois strategy is an ESS because it avoids costly symmetric fights. Adding asymmetries in fighting ability, resource value, or information produces models that better match the complexity of real animal conflicts. But the core lesson of the basic Hawk-Dove game remains: **natural selection does not maximize aggression — it balances the costs and benefits of fighting in a frequency-dependent way**, producing populations where restraint and escalation coexist in predictable proportions.
