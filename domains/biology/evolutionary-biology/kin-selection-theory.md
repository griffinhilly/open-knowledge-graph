---
id: kin-selection-theory
title: Kin Selection Theory
domain: biology
course: evolutionary-biology
prerequisites:
- id: natural-selection
  type: hard
builds-toward:
- inclusive-fitness
- hamilton-rule
- altruism-evolution
tags:
- selection
- sociobiology
- genetics
stage: advanced
status: draft
---

# Kin Selection Theory

## Core Idea
Kin selection explains the evolution of altruistic behaviors toward relatives by recognizing that genes promoting helpfulness to kin can spread if the relatedness is high enough. Inclusive fitness extends the concept of reproductive success beyond one's own offspring to include contributions to relatives' offspring.

## Explainer

Natural selection, as you already understand it, favors traits that increase an individual's reproductive success. But this creates a puzzle: why do worker honeybees sacrifice their own reproduction to serve the queen, or why does a ground squirrel give an alarm call that draws a predator's attention? These behaviors reduce the individual's own fitness. **Kin selection** resolves this paradox by shifting the unit of analysis from the individual organism to the gene. What matters is not whether *you* reproduce, but whether copies of *your genes* make it into the next generation — and your relatives carry copies of those same genes.

The key insight is **relatedness** — the probability that two individuals share a particular allele by common descent. You share about 50% of your genes with a sibling, 25% with a half-sibling or grandchild, and 12.5% with a first cousin. This means that helping a relative reproduce can propagate your genes almost as effectively as reproducing yourself, provided the relative is close enough and the help is substantial enough. A gene that causes you to sacrifice some of your own reproductive output to help a sibling can still spread through the population if the sibling's gain, weighted by relatedness, exceeds your loss.

This logic is formalized in **Hamilton's rule**: an altruistic behavior will be favored by selection when *rB > C*, where *r* is the coefficient of relatedness between actor and recipient, *B* is the reproductive benefit to the recipient, and *C* is the reproductive cost to the actor. The rule makes concrete predictions. Altruism should be more common among close relatives than distant ones, and the costlier the act, the closer the relationship must be to justify it. J.B.S. Haldane reportedly quipped that he would lay down his life for two brothers or eight cousins — a rough intuitive version of Hamilton's arithmetic.

**Inclusive fitness** extends the traditional concept of fitness to capture this broader picture. Instead of counting only your own offspring, inclusive fitness adds the extra offspring your relatives produce because of your help, each discounted by the coefficient of relatedness. This framework explains a wide range of otherwise puzzling behaviors: alarm calls in social rodents, cooperative breeding in birds, and the extreme eusociality of Hymenoptera (ants, bees, wasps), where the unusual haplodiploid genetics makes sisters more related to each other (r = 0.75) than they would be to their own daughters (r = 0.5). Kin selection does not require organisms to consciously calculate relatedness — selection simply favors genes that produce helping behavior in contexts where relatives are statistically likely to be nearby.
