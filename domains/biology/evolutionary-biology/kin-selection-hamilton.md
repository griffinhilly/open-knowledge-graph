---
id: kin-selection-hamilton
title: Kin Selection and Hamilton's Rule
domain: biology
course: evolutionary-biology
prerequisites:
- id: natural-selection
  type: hard
builds-toward:
- evolutionary-game-theory
tags:
- kin-selection
- altruism
- inclusive-fitness
- relatedness
stage: advanced
status: draft
---

# Kin Selection and Hamilton's Rule

## Core Idea
Kin selection explains evolution of altruistic behaviors through inclusive fitness: genes increase in frequency if they promote survival and reproduction of relatives who share them by descent. Hamilton's rule (rB > C) quantifies when altruism is favored: the inclusive benefit (relatedness × beneficiary benefit) must exceed the actor's cost. This principle explains eusociality and cooperation.

## How It's Best Learned
Work through classic examples: alarm calls, worker sterility in social insects, sibling cooperation. Calculate coefficients of relatedness (r) for different kin relationships.

## Common Misconceptions
- Organisms behave altruistically for the good of the species; altruism evolves when it benefits relatives who carry the altruist's genes.
- Kin selection only applies to animals; it applies to all organisms with kin-structured populations.

## Explainer

Natural selection, as you already understand it, favors traits that increase an individual's own reproductive success. But this creates a puzzle: why do worker bees sacrifice their own reproduction to help the queen, or why does a ground squirrel give an alarm call that attracts a predator's attention? These behaviors reduce the actor's fitness while boosting someone else's. **Kin selection** resolves this paradox by expanding the unit of accounting from personal reproduction to the spread of shared genes through relatives.

The key insight is **inclusive fitness** — your evolutionary success includes not just your own offspring but also the extra offspring your relatives produce because of your help, discounted by how closely related you are. W.D. Hamilton formalized this with an elegantly simple inequality: **rB > C**, where **r** is the coefficient of relatedness between actor and beneficiary, **B** is the reproductive benefit to the beneficiary, and **C** is the reproductive cost to the actor. When this inequality holds, genes promoting the altruistic behavior spread through the population even though the altruist personally pays a price.

The coefficient of relatedness, **r**, measures the probability that two individuals share a given allele by common descent. Full siblings share r = 0.5, half-siblings r = 0.25, and cousins r = 0.125. This is why J.B.S. Haldane reportedly quipped he would lay down his life for two brothers or eight cousins — the math checks out. In haplodiploid insects like bees and ants, sisters share r = 0.75 because they inherit an identical haploid genome from their father, which helps explain why sterile worker castes evolved repeatedly in these lineages. A worker bee who helps her mother produce more sisters passes on more of her genes than she would by reproducing directly.

Kin selection is not limited to dramatic cases of self-sacrifice. It explains a gradient of cooperative behaviors: birds that help at the nest of a related breeding pair, cellular slime molds where some cells sacrifice themselves to form a stalk that disperses spore-bearing relatives, and even bacteria that release costly toxins benefiting nearby clone-mates. The principle applies wherever organisms interact with relatives and the Hamilton's rule inequality is satisfied. What matters is not conscious calculation but the statistical tendency for genes promoting kin-directed help to increase in frequency — natural selection operating on shared genetic interests rather than individual survival alone.
