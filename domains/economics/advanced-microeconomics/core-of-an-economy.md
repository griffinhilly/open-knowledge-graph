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

## Explainer

From the Edgeworth box and Walrasian equilibrium, you know that competitive markets can produce efficient allocations and that the contract curve represents all Pareto efficient trades between two agents. But a nagging question remains: why should we believe that agents would actually accept a competitive equilibrium allocation? What if a subset of traders could do better by breaking away and trading only among themselves? The **core** of an economy provides the answer by identifying exactly which allocations are immune to such defections.

An allocation is in the core if no **coalition** — any subset of agents, from a single individual to the entire group — can **block** it. A coalition blocks an allocation when its members can redistribute their own endowments among themselves and make every member at least as well off, with at least one member strictly better off, compared to the proposed allocation. Think of it as a stability test: if you announced a particular division of goods, would any group have both the incentive and the ability to walk away and arrange a better deal internally? If no such group exists, the allocation is in the core. The individual rationality constraint (no one is worse off than at their endowment) is a special case where the coalition is a single person.

In a two-person Edgeworth box economy, the core corresponds to the segment of the contract curve between the two agents' indifference curves through the initial endowment point. Every point on this segment is Pareto efficient and individually rational — neither agent would refuse to trade. But notice how large this set can be: many allocations survive the stability test when there are only two traders, because with just one potential trading partner, your outside options are limited. This is where the most powerful result about the core emerges. As you **replicate** the economy — adding more agents with identical preferences and endowments — the core shrinks. With more potential trading partners, each agent's outside options improve, and more allocations can be blocked by some coalition. In the limit, as the economy becomes infinitely large, the core converges exactly to the set of **competitive equilibrium allocations**. This is the **core equivalence theorem** (Edgeworth's conjecture, proven rigorously by Debreu and Scarf).

The core equivalence result is profound because it provides a game-theoretic foundation for competitive equilibrium that does not rely on the fiction of an auctioneer calling out prices. Instead of assuming a price-taking mechanism, it shows that the discipline of free coalition formation — the threat that any group can walk away — is sufficient to drive outcomes toward competitive equilibrium in large economies. Competitive prices emerge not because agents are told to take them as given, but because in a large economy, no group can profitably deviate from the competitive allocation. This bridges cooperative game theory (which the core belongs to) with the Walrasian tradition, demonstrating that these very different analytical frameworks converge on the same prediction when markets are thick.
