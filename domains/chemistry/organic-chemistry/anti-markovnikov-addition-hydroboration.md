---
id: anti-markovnikov-addition-hydroboration
title: Anti-Markovnikov Addition and Hydroboration
domain: chemistry
course: organic-chemistry
prerequisites:
- id: markovnikov-rule-and-mechanism
  type: hard
tags:
- regioselectivity
- hydroboration
- concerted
- borane
- oxidation
stage: advanced
status: draft
---

# Anti-Markovnikov Addition and Hydroboration

## Core Idea
Hydroboration (R₂BH addition to alkenes) gives anti-Markovnikov products: BH adds to the less substituted carbon and H adds to the more substituted carbon. This occurs because hydroboration has no carbocation intermediate; instead, it proceeds via a concerted mechanism and a boron-carbon bond forms to the more accessible (less hindered) carbon. Subsequent oxidation converts B to OH, yielding primary or secondary alcohols with opposite regioselectivity to HX addition.

## How It's Best Learned
Compare Markovnikov (HBr + alkene) with anti-Markovnikov (BH₃/H₂O₂ + alkene) products for the same substrate. Draw the concerted cyclic transition state for hydroboration. Follow oxidation step using a detailed mechanism.

## Explainer

From Markovnikov's rule, you learned that when HBr adds to an unsymmetrical alkene, the hydrogen goes to the less substituted carbon and the bromine goes to the more substituted carbon — because the reaction proceeds through the more stable (more substituted) carbocation intermediate. **Hydroboration-oxidation** gives you the opposite regiochemistry, and understanding why requires appreciating a fundamentally different mechanism: one with no carbocation at all.

In **hydroboration**, borane (BH₃, which exists as B₂H₆ in practice) adds across the double bond in a single concerted step — both the B–H bond breaking and the new B–C and C–H bonds forming happen simultaneously through a four-centered transition state. There is no intermediate, no charged species, and therefore no opportunity for carbocation rearrangement. The boron, being electron-deficient with an empty p orbital, acts as a mild electrophile and attaches to the less sterically hindered carbon of the double bond (the less substituted end). The hydrogen from B–H simultaneously delivers to the adjacent carbon. Because both atoms add to the same face of the double bond in one step, hydroboration is **syn addition** — a stereochemical detail that matters when the alkene has substituents that create distinct faces.

After hydroboration, you have an alkylborane (C–B bond) that is not yet useful as a final product. The second step, **oxidation** with hydrogen peroxide (H₂O₂) in base (NaOH), replaces the boron with a hydroxyl group (–OH) while retaining the configuration — the OH ends up exactly where the boron was. The net result of the two-step sequence is addition of water across the double bond with anti-Markovnikov regiochemistry: the OH is on the less substituted carbon. For a terminal alkene like 1-butene, Markovnikov hydration (acid-catalyzed) gives 2-butanol, but hydroboration-oxidation gives 1-butanol — a primary alcohol that is otherwise difficult to access from simple alkene addition reactions.

This reaction illustrates a broader principle in organic chemistry: **mechanism determines regiochemistry**. Markovnikov selectivity arises because a cationic intermediate favors greater substitution. Anti-Markovnikov selectivity in hydroboration arises because a concerted, steric-controlled mechanism favors the less hindered position. Whenever you encounter a new addition reaction, asking "does this go through a carbocation?" immediately tells you whether to expect Markovnikov or anti-Markovnikov products. Hydroboration-oxidation is the classic example of how changing the mechanism — not just the reagent — flips the regiochemical outcome.
