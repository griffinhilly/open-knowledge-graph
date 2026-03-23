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
status: validated
---

# Kin Selection and Hamilton's Rule

## Core Idea
Kin selection explains evolution of altruistic behaviors through inclusive fitness: genes increase in frequency if they promote survival and reproduction of relatives who share them by descent. Hamilton's rule (rB > C) quantifies when altruism is favored: the inclusive benefit (relatedness × beneficiary benefit) must exceed the actor's cost. This principle explains eusociality and cooperation.

## How It's Best Learned
Work through classic examples: alarm calls, worker sterility in social insects, sibling cooperation. Calculate coefficients of relatedness (r) for different kin relationships.

## Common Misconceptions
- Organisms behave altruistically for the good of the species; altruism evolves when it benefits relatives who carry the altruist's genes.
- Kin selection only applies to animals; it applies to all organisms with kin-structured populations.

## Questions

```yaml
- question: "A ground squirrel gives an alarm call when it spots a predator. The call attracts the predator's attention, reducing the caller's survival probability by 10%, while increasing the survival of 4 full siblings by 8% each. Does the alarm call gene spread?"
  type: multiple-choice
  options:
    - "No — the individual squirrel's fitness decreases, so natural selection eliminates the gene"
    - "No — natural selection only favors behaviors that benefit the whole population, which this does not"
    - "Yes — because rB (0.5 × 32%) exceeds C (10%), so the gene increases in frequency through relatives"
    - "Yes — but only because the squirrel consciously calculates the benefit to its relatives"
  answer: 2
  explanation: "Applying Hamilton's rule: r = 0.5 (full siblings), B = 4 × 8% = 32% total benefit to beneficiaries, C = 10% cost to actor. rB = 0.5 × 32% = 16% > C = 10%, so the alarm call gene spreads. The gene's copies in the caller's siblings benefit more than the gene's copy in the caller itself loses — the gene increases in frequency overall even though the individual pays a cost. No conscious calculation is required; the gene spreads statistically through kin-structured populations."

- question: "In haplodiploid insects like bees and ants, full sisters share a relatedness coefficient of r = 0.75 rather than the 0.5 expected for diploid siblings. What explains this?"
  type: multiple-choice
  options:
    - "Sisters share both parents, while brothers share only the mother, raising the sisters' relatedness"
    - "Haplodiploid females have twice as many chromosomes as males, increasing shared genetic material"
    - "All sisters inherit an identical haploid genome from their haploid father, making them share all paternal alleles with certainty"
    - "Worker bees suppress recombination during meiosis, preventing allele shuffling among sisters"
  answer: 2
  explanation: "In haplodiploid systems, males (drones) are haploid — they have only one copy of each chromosome. Every egg a drone produces is genetically identical (no meiotic recombination can occur in a haploid). Therefore, all daughters of the same father share 100% of their paternal alleles (r = 1 for the paternal contribution) and share 50% of their maternal alleles on average (r = 0.5). The weighted average: (1 × 0.5) + (0.5 × 0.5) = 0.75. This elevated relatedness helps explain why worker sterility — an extreme form of altruism — evolved repeatedly in haplodiploid Hymenoptera."

- question: "According to Hamilton's rule, an altruistic behavior can be favored by natural selection even if the actor's direct reproductive success decreases, provided that rB exceeds C."
  type: true-false
  answer: true
  explanation: "This is the central insight of kin selection theory. Natural selection does not maximize individual reproductive success — it maximizes the spread of genes. If an altruistic act reduces the actor's own reproduction (cost C) but increases a relative's reproduction by B, and the relative shares the altruism gene with probability r, then the gene increases in frequency whenever rB > C. The actor's personal fitness declines, but the gene's overall representation in the population increases via the relative. Inclusive fitness, which sums the actor's direct fitness and the indirect fitness gained through relatives, is the quantity being maximized."

- question: "Kin selection requires that organisms consciously recognize and deliberately favor their genetic relatives — it cannot operate in species without social cognition or memory."
  type: true-false
  answer: false
  explanation: "Kin selection is a population-genetic process, not a psychological one. It operates whenever genes promoting kin-directed behavior increase in frequency because those genes are statistically more likely to be present in relatives. Organisms need not recognize kin consciously — spatial proximity to relatives, imprinting on nestmates, or simply living in kin-structured populations can all create the conditions for kin selection to work. Cellular slime molds and bacteria, which have no nervous systems, show kin-selected cooperation: cells sacrifice themselves to form spore-bearing stalks that benefit nearby clone-mates carrying the same genes."

- question: "What does 'inclusive fitness' mean, and why does it provide a better account of altruism's evolution than classical individual fitness alone?"
  type: short-answer
  answer: "Classical individual fitness counts only the offspring an organism produces directly. Inclusive fitness expands this accounting to include the extra offspring produced by relatives because of the organism's help, weighted by the coefficient of relatedness r. An organism's inclusive fitness = direct fitness + sum of (r × benefit conferred on each relative). This expanded accounting resolves the altruism paradox: a behavior that reduces direct reproduction but substantially boosts reproduction in close relatives can increase the frequency of the altruism-promoting gene in the population. The gene spreads not through the actor's own offspring but through copies of itself carried by the relatives the actor helped."
  explanation: "The key conceptual shift is to the gene as the unit of selection rather than the individual. A gene 'cares' (in the evolutionary sense) about all its copies in the population, regardless of which bodies they occupy. A gene that promotes self-sacrifice to save relatives propagates copies of itself via those relatives — the individual may lose, but the gene wins. This perspective, developed by Hamilton and popularized by Dawkins as the 'selfish gene' view, unifies kin selection with classical natural selection."
```

## Explainer

Natural selection, as you already understand it, favors traits that increase an individual's own reproductive success. But this creates a puzzle: why do worker bees sacrifice their own reproduction to help the queen, or why does a ground squirrel give an alarm call that attracts a predator's attention? These behaviors reduce the actor's fitness while boosting someone else's. **Kin selection** resolves this paradox by expanding the unit of accounting from personal reproduction to the spread of shared genes through relatives.

The key insight is **inclusive fitness** — your evolutionary success includes not just your own offspring but also the extra offspring your relatives produce because of your help, discounted by how closely related you are. W.D. Hamilton formalized this with an elegantly simple inequality: **rB > C**, where **r** is the coefficient of relatedness between actor and beneficiary, **B** is the reproductive benefit to the beneficiary, and **C** is the reproductive cost to the actor. When this inequality holds, genes promoting the altruistic behavior spread through the population even though the altruist personally pays a price.

The coefficient of relatedness, **r**, measures the probability that two individuals share a given allele by common descent. Full siblings share r = 0.5, half-siblings r = 0.25, and cousins r = 0.125. This is why J.B.S. Haldane reportedly quipped he would lay down his life for two brothers or eight cousins — the math checks out. In haplodiploid insects like bees and ants, sisters share r = 0.75 because they inherit an identical haploid genome from their father, which helps explain why sterile worker castes evolved repeatedly in these lineages. A worker bee who helps her mother produce more sisters passes on more of her genes than she would by reproducing directly.

Kin selection is not limited to dramatic cases of self-sacrifice. It explains a gradient of cooperative behaviors: birds that help at the nest of a related breeding pair, cellular slime molds where some cells sacrifice themselves to form a stalk that disperses spore-bearing relatives, and even bacteria that release costly toxins benefiting nearby clone-mates. The principle applies wherever organisms interact with relatives and the Hamilton's rule inequality is satisfied. What matters is not conscious calculation but the statistical tendency for genes promoting kin-directed help to increase in frequency — natural selection operating on shared genetic interests rather than individual survival alone.
