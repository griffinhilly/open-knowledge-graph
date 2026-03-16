---
id: hamilton-rule
title: Hamilton's Rule
domain: biology
course: evolutionary-biology
prerequisites:
- id: inclusive-fitness
  type: hard
builds-toward:
- altruism-evolution
- cooperation-evolution
tags:
- selection
- mathematical-biology
- altruism
stage: advanced
status: draft
---

# Hamilton's Rule

## Core Idea
Hamilton's rule (rb > c) predicts that altruistic behavior evolves when the benefit to recipients weighted by relatedness (rb) exceeds the cost to the altruist (c). This quantitative framework explains why sterile castes evolve in eusocial insects and how cooperation can be evolutionarily stable.

## Explainer

From inclusive fitness, you already understand that an organism's evolutionary success is not measured solely by its own offspring but includes the reproduction of relatives who share its genes. Hamilton's rule translates this insight into a precise, testable inequality: **rb > c**. Here, **r** is the coefficient of relatedness between the altruist and the recipient (the probability that they share a given allele by common descent), **b** is the reproductive benefit the recipient gains from the altruistic act, and **c** is the reproductive cost the altruist pays. When the left side exceeds the right, the gene for altruism spreads — even though the altruist personally suffers a fitness cost.

The intuition behind the rule is bookkeeping. Imagine you carry an allele that makes you help your sibling at a cost to yourself. Your sibling shares half your genes (r = 0.5), so any reproductive benefit they gain has a 50% chance of propagating copies of that same allele. If helping your sibling doubles their reproductive output (b = 2 extra offspring) at a cost of one of your own offspring (c = 1), the math works out: 0.5 × 2 = 1 > 1... actually that is exactly equal. The allele breaks even. But if the benefit is slightly larger or the cost slightly lower, the allele spreads. The biologist J.B.S. Haldane reportedly quipped that he would lay down his life for two brothers or eight cousins — a colorful statement of Hamilton's rule, since r = 0.5 for siblings (2 × 0.5 = 1) and r = 0.125 for cousins (8 × 0.125 = 1).

The most dramatic application of Hamilton's rule is explaining **eusociality** in the Hymenoptera (ants, bees, wasps). Due to their **haplodiploid** sex-determination system, female hymenopterans share three-quarters of their genes with their sisters (r = 0.75) but only half with their own daughters (r = 0.5). Hamilton's rule predicts that a female in a haplodiploid species gains more inclusive fitness by helping her mother produce sisters than by reproducing herself — which is exactly the behavior of sterile worker castes. This elegant explanation of one of evolution's greatest puzzles was Hamilton's original motivation for formalizing the rule. However, eusociality has also evolved in diploid species (naked mole-rats, some shrimp), indicating that high relatedness facilitates but does not require haplodiploidy.

Hamilton's rule is powerful because it is general: it applies to any social behavior where costs and benefits can be quantified in fitness terms. It predicts not only when altruism should evolve but when it should *not* — organisms should be less altruistic toward distant relatives and more willing to help when costs are low. Empirical tests across species — from alarm calls in ground squirrels to food sharing in vampire bats — broadly support these predictions. The rule also clarifies the boundary between kin-selected altruism and selfishness: when rb < c, selection favors individuals who refuse to help, even at the expense of relatives. Understanding Hamilton's rule provides the quantitative foundation for all subsequent work on the evolution of cooperation, conflict, and social behavior.
