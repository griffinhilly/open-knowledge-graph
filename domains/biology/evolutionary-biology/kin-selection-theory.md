---
id: kin-selection-theory
title: Kin Selection Theory
domain: biology
course: evolutionary-biology
prerequisites:
- id: natural-selection
  type: hard
- id: codon-bias-and-selection
  type: soft
builds-toward:
- inclusive-fitness
- hamilton-rule
- altruism-evolution
tags:
- selection
- sociobiology
- genetics
stage: advanced
status: validated
---
# Kin Selection Theory

## Core Idea
Kin selection explains the evolution of altruistic behaviors toward relatives by recognizing that genes promoting helpfulness to kin can spread if the relatedness is high enough. Inclusive fitness extends the concept of reproductive success beyond one's own offspring to include contributions to relatives' offspring.

## Questions

```yaml
- question: "A ground squirrel gives an alarm call when it spots a predator, increasing the survival of nearby squirrels but drawing the predator's attention to itself. Hamilton's rule predicts this altruism is most likely to evolve when:"
  type: multiple-choice
  options:
    - "The alarm call benefits the group as a whole, regardless of the genetic relationship between caller and beneficiaries"
    - "The caller is the dominant individual, since dominant animals can afford to take greater risks"
    - "The recipients of the alarm call are close relatives, so that the coefficient of relatedness r is high enough that rB > C"
    - "The caller has already reproduced, since fitness costs are lower for individuals who have passed on their genes"
  answer: 2
  explanation: "Hamilton's rule states that altruism evolves when rB > C — the cost to the actor must be outweighed by the benefit to the recipient, scaled by their relatedness. For the alarm call, C is the increased predation risk to the caller, B is the survival benefit to hearers, and r is the genetic relatedness. If the squirrels nearby are unrelated (r ≈ 0), rB is trivially small and the altruism should not evolve even if B is large. The behavior evolves specifically when the beneficiaries are close relatives. Group benefit (option A) is the common misconception: natural selection acts on genes, not groups — the mechanism is relatedness, not group membership."

- question: "In Hymenoptera (bees, ants, wasps), female workers are more closely related to their sisters (r = 0.75, due to haplodiploidy) than they would be to their own daughters (r = 0.5). Kin selection predicts:"
  type: multiple-choice
  options:
    - "Workers should preferentially invest in their own offspring rather than the queen's, since direct reproduction always maximizes fitness"
    - "Workers should be indifferent between helping sisters and producing daughters, since both are offspring of the same colony"
    - "Workers may gain higher inclusive fitness by rearing sisters than by producing their own daughters, because the relatedness asymmetry makes sibling-rearing genetically more productive"
    - "Haplodiploidy should cause eusociality to collapse, since workers are exploited by the queen who has higher fitness"
  answer: 2
  explanation: "This is Hamilton's original explanation for the extreme eusociality of Hymenoptera. Since r(sister) = 0.75 > r(daughter) = 0.5, a worker can propagate her genes more efficiently per offspring-equivalent by rearing sisters than by producing her own offspring — provided the other conditions of Hamilton's rule are met. This is why worker bees forego direct reproduction: inclusive fitness through sibling-rearing can exceed inclusive fitness through own reproduction when relatedness is high enough. Option A reflects individual-selection thinking (maximize own reproduction) without accounting for inclusive fitness."

- question: "Kin selection requires that organisms consciously recognize and calculate their genetic relatedness to potential recipients before deciding whether to help."
  type: true-false
  answer: false
  explanation: "Kin selection operates through natural selection on genes — no cognitive calculation is required. Selection simply favors genes that produce helping behavior in contexts where relatives are statistically likely to be nearby. A ground squirrel doesn't calculate r; it just has inherited tendencies that correlate with directing alarm calls toward relatives (often because relatives live nearby). The Explainer explicitly states: 'Kin selection does not require organisms to consciously recognize and calculate their relatedness — selection simply favors genes that produce helping behavior in contexts where relatives are statistically likely to be nearby.'"

- question: "According to Hamilton's rule, an altruistic act that is too costly to evolve between distant relatives might still be favored by selection between close relatives."
  type: true-false
  answer: true
  explanation: "This follows directly from rB > C. For a given benefit B and cost C, whether the inequality holds depends on r. If r is small (distant relatives), rB may fall below C and the act is disfavored. If r is large (close relatives), rB may exceed C and the act is favored. Haldane's quip about 'two brothers or eight cousins' captures this: with r = 0.5 for siblings and r = 0.125 for first cousins, the same amount of gene copying requires different numbers of relatives, making some altruistic acts selectively neutral or negative for distant kin but clearly beneficial for close kin."

- question: "Kin selection theory resolves a puzzle that standard natural selection cannot explain. What is that puzzle, and why does shifting the unit of selection from the individual to the gene resolve it?"
  type: short-answer
  answer: "The puzzle is the evolution of altruism: behaviors that reduce an individual's own reproductive success but increase others'. Standard natural selection, focused on individual reproductive success, predicts such behaviors should be eliminated — individuals who help at personal cost should be outcompeted by those who don't. The resolution requires shifting to gene-level thinking: what matters is not whether the individual reproduces, but whether copies of its genes reach the next generation. An altruistic individual shares a fraction r of its genes with each relative. Helping a relative reproduce is therefore equivalent — at the genetic level — to partially reproducing oneself. A gene that programs altruism toward relatives can spread if the indirect genetic benefits (rB) exceed the direct cost (C), because the gene propagates itself through relatives' reproductive success rather than (or in addition to) the actor's own."
  explanation: "This reframing — from organism fitness to gene propagation — is what makes kin selection theoretically coherent. The gene 'for' altruism is present in the relatives being helped; by helping them reproduce, the altruist is helping copies of that very gene spread. Selection acts on genes across multiple bodies, not just on the individual carrying a trait. This is why W.D. Hamilton defined inclusive fitness to capture effects both through the actor's own offspring and through the extra reproduction of relatives weighted by relatedness."
```

## Explainer

Natural selection, as you already understand it, favors traits that increase an individual's reproductive success. But this creates a puzzle: why do worker honeybees sacrifice their own reproduction to serve the queen, or why does a ground squirrel give an alarm call that draws a predator's attention? These behaviors reduce the individual's own fitness. **Kin selection** resolves this paradox by shifting the unit of analysis from the individual organism to the gene. What matters is not whether *you* reproduce, but whether copies of *your genes* make it into the next generation — and your relatives carry copies of those same genes.

The key insight is **relatedness** — the probability that two individuals share a particular allele by common descent. You share about 50% of your genes with a sibling, 25% with a half-sibling or grandchild, and 12.5% with a first cousin. This means that helping a relative reproduce can propagate your genes almost as effectively as reproducing yourself, provided the relative is close enough and the help is substantial enough. A gene that causes you to sacrifice some of your own reproductive output to help a sibling can still spread through the population if the sibling's gain, weighted by relatedness, exceeds your loss.

This logic is formalized in **Hamilton's rule**: an altruistic behavior will be favored by selection when *rB > C*, where *r* is the coefficient of relatedness between actor and recipient, *B* is the reproductive benefit to the recipient, and *C* is the reproductive cost to the actor. The rule makes concrete predictions. Altruism should be more common among close relatives than distant ones, and the costlier the act, the closer the relationship must be to justify it. J.B.S. Haldane reportedly quipped that he would lay down his life for two brothers or eight cousins — a rough intuitive version of Hamilton's arithmetic.

**Inclusive fitness** extends the traditional concept of fitness to capture this broader picture. Instead of counting only your own offspring, inclusive fitness adds the extra offspring your relatives produce because of your help, each discounted by the coefficient of relatedness. This framework explains a wide range of otherwise puzzling behaviors: alarm calls in social rodents, cooperative breeding in birds, and the extreme eusociality of Hymenoptera (ants, bees, wasps), where the unusual haplodiploid genetics makes sisters more related to each other (r = 0.75) than they would be to their own daughters (r = 0.5). Kin selection does not require organisms to consciously calculate relatedness — selection simply favors genes that produce helping behavior in contexts where relatives are statistically likely to be nearby.
