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

## Questions

```yaml
- question: "In a population playing the Hawk-Dove game, Hawks are currently very rare. Almost every interaction a Hawk has is with a Dove, so Hawks win the resource easily each time. What happens to Hawk frequency over subsequent generations?"
  type: multiple-choice
  options:
    - "Hawks remain rare — they are already at the stable equilibrium frequency"
    - "Hawks increase in frequency because they currently have higher fitness than Doves in this population composition"
    - "Doves increase because cooperation is better for the group's long-term survival"
    - "Frequency stays constant because natural selection does not act on behavioral strategies"
  answer: 1
  explanation: "When Hawks are rare, they almost always encounter Doves and win the resource without injury. Their fitness is therefore high relative to Doves, who must share resources with other Doves. Natural selection favors the high-fitness type, so Hawks increase in frequency. This continues until Hawks become common enough that they frequently encounter each other — suffering injury costs — and their average fitness drops to match Doves' average fitness. The equilibrium is reached not at pure Hawk or pure Dove, but at the frequency where both strategies have equal average fitness. This frequency-dependence is the key insight."

- question: "Which of the following best describes an evolutionarily stable strategy (ESS)?"
  type: multiple-choice
  options:
    - "The strategy that maximizes the average fitness of the entire population"
    - "The strategy that gives the individual the highest possible payoff, regardless of what others do"
    - "A strategy that, once it becomes common in the population, cannot be successfully invaded by a rare mutant using a different strategy"
    - "Any strategy that allows the individual to survive and reproduce at least once"
  answer: 2
  explanation: "An ESS is defined by its stability against invasion, not by optimality. If a population is playing an ESS and a rare mutant with a different strategy appears, the mutant will have lower fitness than the resident strategy and be eliminated by natural selection. Crucially, the ESS need not maximize individual payoff (a lone Dove in a Hawk population does badly) or group welfare (ritualized display is the ESS even though all-out fighting might be better for some individuals). It is the strategy that is self-reinforcing: once common, it resists displacement."

- question: "In evolutionary game theory, the fitness value of a strategy can change as the frequency of that strategy in the population changes."
  type: true-false
  answer: true
  explanation: "This is the defining feature of evolutionary game theory — fitness is frequency-dependent. A Hawk strategy is highly fit when Hawks are rare (easy wins against Doves) but less fit when Hawks are common (frequent costly fights). A Dove strategy has moderate but stable fitness. The payoff to any strategy depends on what strategies it is likely to encounter, which depends on population composition. This is fundamentally different from simple natural selection models where a trait has a fixed fitness advantage or disadvantage independent of its frequency."

- question: "An evolutionarily stable strategy is always the strategy that maximizes the reproductive output of the group as a whole."
  type: true-false
  answer: false
  explanation: "An ESS is stable against invasion, not collectively optimal. Classic examples illustrate the gap: in the Prisoner's Dilemma, mutual defection is evolutionarily stable in a single-interaction context even though mutual cooperation would produce higher fitness for everyone. Male peacock tails are an ESS (honest signaling) that imposes enormous individual costs and serves no group benefit. The tragedy of many ESS outcomes is exactly that individually stable strategies can produce collectively suboptimal results — a key theme in understanding arms races, overexploitation, and the evolution of altruism."

- question: "Why does evolutionary game theory require considering strategy frequencies in the population, rather than simply asking which trait has higher fitness?"
  type: short-answer
  answer: "In evolutionary game theory, the fitness of a strategy is not a fixed property — it depends on what other strategies it encounters, and what it encounters depends on the frequencies of strategies in the population. This is frequency-dependent selection. A Hawks-only population suffers high injury costs; a Doves-only population is vulnerable to invasion by Hawks. Neither pure state is stable. The fitness of each strategy changes as its frequency changes, and the population evolves toward the equilibrium frequency where strategies have equal fitness. Simple fitness comparisons assume payoffs are constant, which fails whenever organisms interact and the outcomes of those interactions determine fitness."
  explanation: "This insight applies far beyond the Hawk-Dove game: it explains why cooperation can evolve (tit-for-tat is stable in iterated games), why costly signals are honest (only high-quality individuals can afford them), and why many biological equilibria involve mixed strategies or polymorphisms rather than the fixation of a single 'optimal' type."
```

## Explainer

From your understanding of natural selection, you know that traits increasing an organism's fitness tend to spread through populations. But there is a complication that simple fitness calculations miss: the best strategy for an individual often depends on what everyone else is doing. A hawk-like aggressive fighter does well in a population of doves, but poorly when surrounded by other hawks who fight back. **Evolutionary game theory** provides the mathematical framework for analyzing exactly these frequency-dependent situations, where fitness is not a fixed property of a trait but a function of the strategies present in the population.

The foundational concept is the **payoff matrix**, borrowed from classical game theory but reinterpreted in biological terms. Instead of dollars, payoffs are measured in fitness — survival and reproductive success. Consider the classic **Hawk-Dove game**: two individuals compete over a resource. Hawks always fight; Doves always yield. When a Hawk meets a Dove, the Hawk takes everything. When two Doves meet, they share the resource. When two Hawks meet, they fight and both suffer injury costs. You can immediately see that being a Hawk is great when Hawks are rare (you almost always meet Doves and win easily), but terrible when Hawks are common (you constantly fight and get injured). This frequency dependence means neither pure strategy dominates, and the population settles at a **mixed equilibrium** where Hawks and Doves coexist at the ratio where their average fitness is equal.

The key concept that emerges from this analysis is the **evolutionarily stable strategy** (ESS) — a strategy that, once common in the population, cannot be invaded by any rare alternative. If everyone plays the ESS and a mutant with a different strategy appears, that mutant will have lower fitness and be eliminated. The ESS is not necessarily the strategy that maximizes group welfare or even individual payoff in isolation — it is the strategy that is stable against invasion. In the Hawk-Dove game, the ESS is typically a mixed strategy (or a population mix), not pure Hawk or pure Dove. This explains a widespread biological pattern: many animal contests are settled by ritualized displays rather than all-out fights, because the mixed strategy favoring restraint in many encounters is evolutionarily stable.

Evolutionary game theory has been transformative for understanding behaviors that seem to defy simple natural selection. **Cooperation** is a puzzle because cooperators can be exploited by cheaters, yet cooperation is widespread in nature. Game-theoretic models like the iterated Prisoner's Dilemma show that cooperation can be stable when individuals interact repeatedly and can retaliate against defectors — the famous **tit-for-tat** strategy. **Signaling** is another domain: why do male peacocks grow enormous, costly tails? Handicap signaling models show that only genuinely high-quality males can afford the cost, making the signal honest and evolutionarily stable. In each case, the game-theoretic approach reveals that the fitness of a behavior cannot be evaluated in isolation — it depends on the social environment, which is itself evolving. This recursive quality is what makes evolutionary game theory both challenging and indispensable for understanding the evolution of social behavior.
