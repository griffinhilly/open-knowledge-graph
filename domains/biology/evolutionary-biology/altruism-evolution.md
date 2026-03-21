---
id: altruism-evolution
title: Evolution of Altruism
domain: biology
course: evolutionary-biology
prerequisites:
- id: hamilton-rule
  type: hard
builds-toward:
- reciprocal-altruism
- cooperation-evolution
tags:
- selection
- sociobiology
- behavior
stage: advanced
status: draft
---

# Evolution of Altruism

## Core Idea
Altruistic behavior—costly acts benefiting others—can evolve through kin selection when helping relatives shares genes identical-by-descent. Kin selection is the primary explanation for eusocial insect colonies and family cooperation in vertebrates, though reciprocal altruism and group selection offer alternative mechanisms.

## Questions

```yaml
- question: "A prairie dog gives an alarm call when it spots a predator, attracting attention to itself and increasing its own predation risk. Under what condition does Hamilton's rule predict this behavior will be favored by natural selection?"
  type: multiple-choice
  options:
    - "When the prairie dog is the dominant individual in the group and can afford the risk"
    - "When the relatedness to recipients (r) times the benefit to them (B) exceeds the cost to the alarm-caller (C): rB > C"
    - "When the group is large enough that one individual's loss is statistically negligible"
    - "When the predator is likely to fail regardless, making the actual risk to the caller low"
  answer: 1
  explanation: "Hamilton's rule states that an altruistic act is favored when rB > C — relatedness to recipients times benefit to them exceeds cost to the actor. Prairie dog colonies are typically family groups (high r). The benefit B is the increased survival probability of multiple relatives. If this weighted benefit exceeds the cost C (increased predation risk to the caller), the alarm-calling gene spreads. Natural selection is operating on gene copies across all individuals, not just on the caller's individual survival."

- question: "Worker bees in a hive are infertile females who spend their lives raising sisters rather than reproducing. In hymenoptera (bees, ants, wasps), females are diploid and males are haploid. How does this haplodiploidy system help explain why extreme worker altruism could evolve?"
  type: multiple-choice
  options:
    - "It makes queen bees genetically more valuable, so workers are selected to protect them at any cost"
    - "Due to haplodiploidy, a female worker shares 75% of her genes with sisters — more than with her own offspring (50%) — so raising sisters propagates more gene copies than reproducing directly"
    - "Haplodiploidy causes developmental sterility in workers, so eusociality is a byproduct, not an adaptation"
    - "It maximizes colony genetic diversity, which benefits resistance to disease rather than individual altruism"
  answer: 1
  explanation: "Under haplodiploidy, the father contributes identical genes to all daughters (he's haploid, so has only one set to give). This makes sisters share r = 0.75 — more than the r = 0.5 relatedness between a mother and her offspring. By Hamilton's rule, if rB > C, helping produce sisters can be more efficient at spreading gene copies than direct reproduction. This provided a genetic pre-condition that may have facilitated eusociality evolving multiple times in hymenoptera."

- question: "From the perspective of gene-level selection, a worker bee that forgoes reproduction to help raise 10 sisters may propagate more copies of its genes than if it had raised 4 of its own offspring."
  type: true-false
  answer: true
  explanation: "Under haplodiploidy, relatedness to sisters = 0.75 vs. relatedness to own offspring = 0.5. Helping raise 10 sisters yields 10 × 0.75 = 7.5 gene-copy-equivalents; raising 4 own offspring yields 4 × 0.5 = 2.0. The gene-level calculus strongly favors helping sisters in this case. This is the core insight: what appears to be individual sacrifice is, from the gene's perspective, a profitable investment in alternative carriers of the same gene."

- question: "Kin selection explains altruism by showing that individuals benefit directly from helping relatives, since relatives tend to reciprocate the help."
  type: true-false
  answer: false
  explanation: "This confuses kin selection with reciprocal altruism, which is a distinct mechanism. Kin selection does not require reciprocation or any direct benefit to the actor. The benefit is indirect — the actor's genes propagate through the relatives it helps. A ground squirrel that gives an alarm call and is killed immediately has received no direct benefit, yet the behavior can be favored by kin selection if relatives share enough gene copies. Reciprocal altruism operates among non-relatives through repeated interactions with the expectation of future returns."

- question: "What does Haldane's quip 'I would lay down my life for two brothers or eight cousins' reveal about the logic of kin selection?"
  type: short-answer
  answer: "It encodes Hamilton's rule in arithmetic. A full sibling shares r = 0.5 genes by descent; two brothers together carry on average 2 × 0.5 = 1.0 gene-copy-equivalents — the same as the actor surviving. Eight first cousins each share r = 0.125; together they represent 8 × 0.125 = 1.0. In both cases, the gene copies propagated through relatives equal those lost by the actor's death, making the sacrifice gene-level break-even. The quip reveals that 'altruism' from the gene's perspective is a calculation about where to locate copies of itself — in the actor's body or in relatives' bodies."
  explanation: "This gene-centered view resolves the apparent paradox of altruism without invoking group benefit or conscious motivation. The 'selfish gene' can produce selfless behavior whenever rB > C. It also predicts where altruism should be common (close kin, high benefit-to-cost ratios) and where it should be absent or weak (distant relatives, low relatedness, high cost), generating testable predictions confirmed across many animal taxa."
```

## Explainer

At first glance, altruism seems like a paradox for evolutionary theory. If natural selection favors traits that increase an individual's reproductive success, why would any organism sacrifice its own fitness to help another? A ground squirrel that gives an alarm call attracts predator attention to itself; a worker bee that stings an intruder dies in the process. These behaviors reduce the actor's fitness while benefiting others. From your understanding of Hamilton's rule, you already have the key to resolving this puzzle.

**Kin selection** explains altruism by shifting the unit of accounting from the individual to the gene. Hamilton's rule states that an altruistic act is favored when *rB > C* — when the **relatedness** (r) between actor and recipient, multiplied by the **benefit** (B) to the recipient, exceeds the **cost** (C) to the actor. A worker bee shares 75% of her genes with her sisters (due to haplodiploidy), so helping her mother queen produce more sisters can propagate more copies of the worker's genes than reproducing directly would. The alarm-calling squirrel is surrounded by close relatives who share its genes; by warning them, it increases the survival of gene copies even as it risks its own life. J.B.S. Haldane captured the logic with his famous quip: "I would lay down my life for two brothers or eight cousins" — the math of shared genes.

Kin selection is most powerful in explaining **eusociality**, the extreme form of cooperation seen in ants, bees, termites, and naked mole-rats, where some individuals forgo reproduction entirely to help relatives breed. But altruism also occurs between non-relatives, which kin selection alone cannot explain. **Reciprocal altruism** accounts for some of these cases: individuals help unrelated partners with the expectation of future return favors, as seen in vampire bats that regurgitate blood meals for roost-mates who failed to feed. This requires repeated interactions and the ability to recognize and punish cheaters — conditions met in many social species.

The broader lesson is that "selfish genes" can produce selfless behavior. What looks like individual sacrifice is, from the gene's perspective, a profitable investment in copies of itself carried by relatives or future reciprocators. This gene-centered view does not diminish the reality of cooperative behavior — it explains why it evolves and predicts where we should expect to find it: among close kin, in species with repeated social interactions, and in contexts where the benefit-to-cost ratio is high enough to satisfy Hamilton's inequality.
