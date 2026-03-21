---
id: core-of-an-economy
title: The Core of an Economy
domain: economics
course: advanced-microeconomics
prerequisites:
- id: edgeworth-box-exchange
  type: hard
- id: walrasian-equilibrium
  type: hard
tags:
- general-equilibrium
- coalition-formation
stage: advanced
status: draft
---

# The Core of an Economy

## Core Idea
The core is the set of allocations from which no coalition of traders can profitably deviate by trading only among themselves. Competitive equilibrium allocations lie in the core. In large economies, the core shrinks toward the competitive equilibrium, showing that competition eliminates profitable deviations even without explicit equilibration mechanism.

## Questions

```yaml
- question: "In a two-person exchange economy, the core contains many allocations — the entire segment of the contract curve between the two agents' indifference curves through the endowment. What happens as you replicate this economy by adding more agents with identical preferences and endowments?"
  type: multiple-choice
  options:
    - "The core expands, because more agents means more possible mutually beneficial trades"
    - "The core remains the same size, because adding identical agents doesn't change the fundamental tradeoff"
    - "The core shrinks, because each agent now has better outside options and can block more allocations"
    - "The core disappears entirely once a third agent is added"
  answer: 2
  explanation: "As the economy is replicated, each agent has more potential trading partners and therefore better outside options. A coalition of, say, half the buyers and half the sellers can now arrange a better deal internally, blocking allocations that would have survived in the two-person case. In the limit of infinitely many agents, the core converges exactly to the competitive equilibrium allocations — this is the core equivalence theorem."

- question: "An allocation is proposed in a 10-agent economy. A coalition of 4 agents realizes that by redistributing their own endowments among themselves, all 4 can be made strictly better off than under the proposed allocation. What can we conclude?"
  type: multiple-choice
  options:
    - "The allocation is Pareto efficient but not individually rational"
    - "The allocation is blocked by this coalition and therefore not in the core"
    - "The allocation is in the core, because the other 6 agents are unaffected"
    - "The allocation is a competitive equilibrium, since no outside agent is harmed"
  answer: 1
  explanation: "An allocation is blocked if any coalition can redistribute its own endowments to make all members at least as well off and at least one strictly better off. The proposed allocation fails this test — the 4-agent coalition can do better. That means the allocation is not in the core, regardless of what happens to the other 6 agents. The core only contains allocations that no coalition — of any size — can profitably deviate from."

- question: "In a large replicated economy, the core converges to the set of competitive equilibrium allocations."
  type: true-false
  answer: true
  explanation: "This is the core equivalence theorem (Edgeworth's conjecture, proven by Debreu and Scarf). As the economy grows, each agent's outside options improve because there are more potential coalition partners. More and more non-competitive allocations become blockable by some coalition. In the limit, only the competitive equilibrium allocations survive — no coalition can profitably deviate from them. This result provides a game-theoretic foundation for competitive equilibrium without assuming price-taking behavior."

- question: "In a two-person Edgeworth box economy, the core is identical to the entire Pareto frontier (the full contract curve)."
  type: true-false
  answer: false
  explanation: "The core in a two-person economy is only the segment of the contract curve that lies between the two agents' indifference curves through the initial endowment point. Allocations on the contract curve outside this segment are Pareto efficient but not individually rational — at least one agent would be worse off than at their endowment, so that individual can block the allocation by simply refusing to trade. The core requires both Pareto efficiency and individual rationality."

- question: "Why does the core shrink as the economy is replicated, and what does this convergence imply about the relationship between competitive equilibrium and cooperative game theory?"
  type: short-answer
  answer: "As the economy is replicated, each agent gains more potential trading partners, which improves their outside options. Any allocation that deviates from competitive prices can be blocked by a coalition: for example, if a seller is receiving below the competitive price, a coalition of sellers and buyers can form and trade at a better price, leaving the deviating allocation blocked. In the limit, only competitive equilibrium allocations survive because no coalition can do better by breaking away. This implies that competitive equilibrium is not merely an artifact of assuming price-taking behavior — it is the outcome that emerges from free coalition formation in large economies, bridging cooperative game theory and the Walrasian tradition."
  explanation: "The core equivalence result is profound because it shows two very different analytical frameworks — cooperative game theory (which asks what coalitions can enforce) and Walrasian equilibrium theory (which asks what prices clear markets) — converge on the same answer when markets are thick. Competition 'disciplines' agents not because they are forced to take prices as given, but because in a large economy, any group that tries to deviate can be undercut by a competing coalition."
```

## Explainer

From the Edgeworth box and Walrasian equilibrium, you know that competitive markets can produce efficient allocations and that the contract curve represents all Pareto efficient trades between two agents. But a nagging question remains: why should we believe that agents would actually accept a competitive equilibrium allocation? What if a subset of traders could do better by breaking away and trading only among themselves? The **core** of an economy provides the answer by identifying exactly which allocations are immune to such defections.

An allocation is in the core if no **coalition** — any subset of agents, from a single individual to the entire group — can **block** it. A coalition blocks an allocation when its members can redistribute their own endowments among themselves and make every member at least as well off, with at least one member strictly better off, compared to the proposed allocation. Think of it as a stability test: if you announced a particular division of goods, would any group have both the incentive and the ability to walk away and arrange a better deal internally? If no such group exists, the allocation is in the core. The individual rationality constraint (no one is worse off than at their endowment) is a special case where the coalition is a single person.

In a two-person Edgeworth box economy, the core corresponds to the segment of the contract curve between the two agents' indifference curves through the initial endowment point. Every point on this segment is Pareto efficient and individually rational — neither agent would refuse to trade. But notice how large this set can be: many allocations survive the stability test when there are only two traders, because with just one potential trading partner, your outside options are limited. This is where the most powerful result about the core emerges. As you **replicate** the economy — adding more agents with identical preferences and endowments — the core shrinks. With more potential trading partners, each agent's outside options improve, and more allocations can be blocked by some coalition. In the limit, as the economy becomes infinitely large, the core converges exactly to the set of **competitive equilibrium allocations**. This is the **core equivalence theorem** (Edgeworth's conjecture, proven rigorously by Debreu and Scarf).

The core equivalence result is profound because it provides a game-theoretic foundation for competitive equilibrium that does not rely on the fiction of an auctioneer calling out prices. Instead of assuming a price-taking mechanism, it shows that the discipline of free coalition formation — the threat that any group can walk away — is sufficient to drive outcomes toward competitive equilibrium in large economies. Competitive prices emerge not because agents are told to take them as given, but because in a large economy, no group can profitably deviate from the competitive allocation. This bridges cooperative game theory (which the core belongs to) with the Walrasian tradition, demonstrating that these very different analytical frameworks converge on the same prediction when markets are thick.
