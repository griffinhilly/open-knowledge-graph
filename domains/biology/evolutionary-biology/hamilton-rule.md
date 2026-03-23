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
status: validated
---

# Hamilton's Rule

## Core Idea
Hamilton's rule (rb > c) predicts that altruistic behavior evolves when the benefit to recipients weighted by relatedness (rb) exceeds the cost to the altruist (c). This quantitative framework explains why sterile castes evolve in eusocial insects and how cooperation can be evolutionarily stable.

## Questions

```yaml
- question: "J.B.S. Haldane reportedly quipped he would lay down his life for eight cousins. Which version of Hamilton's rule correctly captures why eight cousins (but not seven) meets the threshold?"
  type: multiple-choice
  options:
    - "r = 0.5 for cousins, so 8 × 0.5 = 4 > 1, giving a large fitness surplus"
    - "r = 0.125 for first cousins, so 8 × 0.125 = 1.0 ≥ c (=1 life), exactly meeting the rb ≥ c threshold"
    - "r = 0.25 for cousins, so 8 × 0.25 = 2 > 1, well exceeding the threshold"
    - "Haldane's quip doesn't satisfy Hamilton's rule — he was speaking metaphorically"
  answer: 1
  explanation: "First cousins share on average r = 0.125 of their genes by common descent (one of eight possible shared great-grandparent alleles). With eight cousins: rb = 8 × 0.125 = 1.0, which exactly equals the cost c = 1 (one life). This is the break-even point — the allele for this altruism neither spreads nor declines. With even slightly higher benefit (nine cousins) or lower cost, the allele would spread. r = 0.5 applies to full siblings (two brothers is sufficient for Haldane), and r = 0.25 applies to half-siblings or grandchildren."

- question: "Worker bees in a haplodiploid (Hymenoptera) colony are sterile females who help their mother (the queen) produce more sisters rather than reproducing themselves. Hamilton's rule explains this because:"
  type: multiple-choice
  options:
    - "Workers cannot reproduce physiologically, so Hamilton's rule does not apply — this is a case of constraint, not selection"
    - "Due to haplodiploidy, workers share r = 0.75 with their sisters but only r = 0.5 with their own daughters, so helping raise sisters yields more inclusive fitness than personal reproduction"
    - "The queen has higher fitness than workers, so workers defer to her reproductive advantage"
    - "Workers benefit by receiving food and protection from the colony in exchange for their labor"
  answer: 1
  explanation: "In haplodiploid species, females develop from fertilized diploid eggs and males from unfertilized haploid eggs. Because the father is haploid, all daughters share identical paternal genes (r = 0.5 from father) plus an average of 0.25 from the mother — giving r = 0.75 between sisters. But a worker's own daughters would share only r = 0.5 with her. Since rb for sisters (0.75 × b) exceeds the equivalent for daughters (0.5 × b) for the same b, Hamilton's rule predicts workers gain more inclusive fitness by raising sisters than by reproducing directly. This is Hamilton's original explanation for eusociality — one of evolutionary biology's most elegant applications of the rule."

- question: "Hamilton's rule only applies to behaviors that benefit the altruist's direct offspring."
  type: true-false
  answer: false
  explanation: "Hamilton's rule applies to any social behavior where costs and benefits can be quantified in fitness terms and where the recipient is a genetic relative. The 'r' in rb > c is the coefficient of relatedness between the altruist and the recipient — not restricted to offspring (where r = 0.5). The rule predicts altruism toward siblings (r = 0.5), cousins (r = 0.125), and any relatives. It also predicts when altruism should NOT evolve (when rb < c). The rule is a general framework for kin-selected social evolution, covering alarm calls, food sharing, cooperative breeding, and sterile castes."

- question: "Hamilton's rule predicts that, all else being equal, organisms should be more willing to help more distantly related individuals than closely related ones."
  type: true-false
  answer: false
  explanation: "The opposite is true. In Hamilton's rule rb > c, the r term (coefficient of relatedness) weights the benefit b. Higher r means a higher rb, making it easier for the inequality to be satisfied. An altruistic act toward a close relative (high r) propagates more copies of the altruism allele per unit of benefit than the same act toward a distant relative (low r). Hamilton's rule therefore predicts that organisms should be MORE altruistic toward close relatives and LESS altruistic toward distant ones — exactly what is observed in kin-biased helping behavior across species."

- question: "Why can an allele that causes its bearer to pay a personal fitness cost still spread through a population?"
  type: short-answer
  answer: "Natural selection tracks the fate of alleles, not individuals. An allele for altruism can spread if it increases the reproductive success of enough relatives who carry copies of that same allele. Because relatives share genes by common descent, a copy of the altruism allele in the altruist can propagate through the reproductively successful relatives it helped — even if the altruist itself has fewer offspring. Hamilton's rule quantifies when this happens: rb > c means that the expected number of extra copies of the altruism allele transmitted through helped relatives (r × b) exceeds the copies lost because the altruist paid a personal cost (c). Inclusive fitness, not personal reproductive success, is what selection maximizes."
  explanation: "This insight — that the unit of selection is the allele, not the organism — is the core of kin selection theory and resolves what Darwin saw as a major puzzle: how sterile castes evolve in social insects. The sterile worker 'loses' personal reproduction but 'wins' in terms of allele propagation through the fertile relatives it helps. Hamilton's rule makes this intuition precise and testable."
```

## Explainer

From inclusive fitness, you already understand that an organism's evolutionary success is not measured solely by its own offspring but includes the reproduction of relatives who share its genes. Hamilton's rule translates this insight into a precise, testable inequality: **rb > c**. Here, **r** is the coefficient of relatedness between the altruist and the recipient (the probability that they share a given allele by common descent), **b** is the reproductive benefit the recipient gains from the altruistic act, and **c** is the reproductive cost the altruist pays. When the left side exceeds the right, the gene for altruism spreads — even though the altruist personally suffers a fitness cost.

The intuition behind the rule is bookkeeping. Imagine you carry an allele that makes you help your sibling at a cost to yourself. Your sibling shares half your genes (r = 0.5), so any reproductive benefit they gain has a 50% chance of propagating copies of that same allele. If helping your sibling doubles their reproductive output (b = 2 extra offspring) at a cost of one of your own offspring (c = 1), the math works out: 0.5 × 2 = 1 > 1... actually that is exactly equal. The allele breaks even. But if the benefit is slightly larger or the cost slightly lower, the allele spreads. The biologist J.B.S. Haldane reportedly quipped that he would lay down his life for two brothers or eight cousins — a colorful statement of Hamilton's rule, since r = 0.5 for siblings (2 × 0.5 = 1) and r = 0.125 for cousins (8 × 0.125 = 1).

The most dramatic application of Hamilton's rule is explaining **eusociality** in the Hymenoptera (ants, bees, wasps). Due to their **haplodiploid** sex-determination system, female hymenopterans share three-quarters of their genes with their sisters (r = 0.75) but only half with their own daughters (r = 0.5). Hamilton's rule predicts that a female in a haplodiploid species gains more inclusive fitness by helping her mother produce sisters than by reproducing herself — which is exactly the behavior of sterile worker castes. This elegant explanation of one of evolution's greatest puzzles was Hamilton's original motivation for formalizing the rule. However, eusociality has also evolved in diploid species (naked mole-rats, some shrimp), indicating that high relatedness facilitates but does not require haplodiploidy.

Hamilton's rule is powerful because it is general: it applies to any social behavior where costs and benefits can be quantified in fitness terms. It predicts not only when altruism should evolve but when it should *not* — organisms should be less altruistic toward distant relatives and more willing to help when costs are low. Empirical tests across species — from alarm calls in ground squirrels to food sharing in vampire bats — broadly support these predictions. The rule also clarifies the boundary between kin-selected altruism and selfishness: when rb < c, selection favors individuals who refuse to help, even at the expense of relatives. Understanding Hamilton's rule provides the quantitative foundation for all subsequent work on the evolution of cooperation, conflict, and social behavior.
