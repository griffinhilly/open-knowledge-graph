---
id: sexual-selection
title: Sexual Selection
domain: biology
course: evolutionary-biology
prerequisites:
- id: natural-selection
  type: hard
- id: adaptation-and-fitness
  type: soft
builds-toward:
- evolution-of-sex
- signal-evolution
tags:
- selection
- mating
- reproduction
stage: advanced
status: validated
---

# Sexual Selection

## Core Idea
Sexual selection arises from competition for mates (intrasexual) or mate choice (intersexual) and can drive rapid evolution of secondary sexual traits. Traits costly for survival can increase in frequency if they improve mating success sufficiently. Sexual selection explains elaborate ornaments like peacock tails and complex courtship behaviors.

## Questions

```yaml
- question: "A peacock's tail is metabolically expensive to grow, makes the bird conspicuous to predators, and reduces escape speed. Yet peacocks with larger, more elaborate tails mate more frequently, and the trait has become more extreme over generations. What does this tell us about sexual selection's relationship to natural selection?"
  type: multiple-choice
  options:
    - "Sexual selection operates against natural selection; the tail would eventually disappear if natural selection were the dominant force"
    - "The tail must provide hidden survival benefits — perhaps camouflage or thermoregulation — that compensate for its apparent costs"
    - "Sexual selection is a form of natural selection acting through mating success; a trait spreads if reproductive gains sufficiently outweigh survival costs"
    - "This is an evolutionary paradox: costly traits cannot increase in frequency under Darwinian theory"
  answer: 2
  explanation: "The key insight is that natural selection acts on total reproductive fitness, not survival alone. Fitness includes both survival probability and mating success. If a tail increases a peacock's matings enough to more than compensate for its survival costs, the net effect on gene transmission is positive, and the trait spreads. Sexual selection is not opposed to natural selection — it is a subset of natural selection, specifically the component acting through differential mating success. Darwin was right to identify it as a distinct mechanism because it can drive traits in the opposite direction from survival-only selection, but the underlying logic is identical: genes that increase representation in the next generation spread."

- question: "What is the key distinction between the 'good genes' hypothesis and the 'runaway selection' hypothesis as explanations for why females prefer costly male ornaments?"
  type: multiple-choice
  options:
    - "Good genes: females are instinctively attracted to bright colors; runaway: females make deliberate mate assessments"
    - "Good genes: ornaments reliably signal heritable genetic quality, giving choosy females offspring with better fitness; runaway: a preference and the preferred trait coevolve in a self-reinforcing feedback loop that can escalate beyond any indicator value"
    - "Good genes: applies only to birds; runaway: applies only to insects and fish"
    - "Good genes: predicts sexual dimorphism; runaway: predicts sexual monomorphism"
  answer: 1
  explanation: "Both hypotheses explain female preference for costly ornaments, but through different mechanisms. Under the good genes (indicator) hypothesis, a costly ornament is an honest signal: only genuinely healthy, well-nourished males can afford to produce a brilliant tail, so the tail reveals underlying quality. Females who choose ornamented males get better genes for their offspring. Under runaway selection (Fisherian), the process starts with an arbitrary preference: females who prefer some male trait (for any reason) have sons who inherit the trait and daughters who inherit the preference, so preference and trait coevolve and escalate together. The ornament can become extreme even if it no longer signals any real quality — the preference itself sustains the selection."

- question: "Because sexually selected traits often reduce survival, sexual selection works in the opposite direction from natural selection."
  type: true-false
  answer: false
  explanation: "Sexual selection is a component of natural selection, not its opposite. Natural selection encompasses all processes that cause differential reproduction — including survival and mating success. A peacock's tail reduces survival but increases mating success; whether the trait spreads depends on the net effect on total reproductive fitness. Sexual selection can drive traits that harm survival, but only when the mating gain more than compensates for the survival cost. The two components of fitness are not opposing forces; they are additive influences on gene transmission."

- question: "Species with more intense sexual selection tend to show greater sexual dimorphism — larger differences in appearance between males and females of the same species."
  type: true-false
  answer: true
  explanation: "Sexual dimorphism is a direct readout of sexual selection intensity. When one sex (typically males) is subject to strong competition for mates or strong female choice, selection drives the divergence of male and female appearance. Elephant seals, where dominant males monopolize harems, show extreme body-size dimorphism. Birds of paradise, with intense female mate choice, show extreme plumage dimorphism. Monogamous species where both sexes choose show minimal dimorphism. This pattern across species is one of the strongest pieces of evidence that sexual selection, not other forces, drives the evolution of sex differences."

- question: "Why can sexually selected traits that reduce survival (like a peacock's tail or elk antlers) still increase in frequency and become more elaborate over evolutionary time? What two conditions must be met?"
  type: short-answer
  answer: "A costly sexually selected trait can spread when: (1) the increase in mating success it provides more than compensates for the reduction in survival — so overall reproductive fitness is positive — and (2) the trait is heritable, so that the mating advantage translates into more offspring that inherit the trait. The net effect on gene transmission across a lifetime must be positive. Traits can escalate over time through intersexual selection (female preferences driving ever-more-elaborate ornaments via runaway selection) or through intrasexual competition (males with larger weapons winning more contests and passing on those traits). The trait stabilizes only when the fitness costs of further elaboration balance the mating gains."
  explanation: "The key to understanding sexual selection is that 'fitness' is not the same as 'survival.' Fitness is the expected number of surviving offspring an individual leaves. A peacock that dies slightly younger but mates four times as often may leave more offspring overall than a survival-optimized peacock that rarely mates. Darwin's insight was that this logic can drive traits in a direction that seems paradoxical from a survival-only perspective — but is perfectly coherent from a total reproductive fitness perspective."
```

## Explainer

Natural selection, as you already know, favors traits that increase survival and reproduction. But Darwin noticed a puzzle: many animals possess traits that seem to actively harm survival. A peacock's enormous tail makes it slower, more conspicuous to predators, and more metabolically expensive to grow. Elk antlers are so heavy they can become tangled in branches. These traits persist and even become more elaborate over generations because they increase **mating success** enough to more than compensate for their survival costs. This is **sexual selection** — a subset of natural selection that acts specifically through differential mating success rather than differential survival.

Sexual selection operates through two distinct mechanisms. **Intrasexual selection** involves direct competition between members of the same sex — typically males fighting, displaying, or otherwise contesting access to mates. The result is weaponry: antlers, tusks, large body size, and aggressive behavior. The winners mate more often and pass on the traits that helped them win. **Intersexual selection** involves mate choice — typically females evaluating males and preferring those with particular traits. The result is ornamentation: bright plumage, elaborate songs, complex dances, and costly displays. The key insight is that the choosing sex exerts a selection pressure on the chosen sex, and the traits that are preferred become more extreme over generations.

Why would females prefer costly, seemingly useless ornaments? Two major hypotheses address this. The **good genes** (or indicator) hypothesis proposes that elaborate ornaments are honest signals of genetic quality — only genuinely healthy, well-nourished males can afford to produce a brilliant tail or sustain an energetically expensive display. By choosing ornamented males, females obtain better genes for their offspring. The **runaway selection** (Fisherian) hypothesis proposes a feedback loop: if females have a slight initial preference for some male trait, males with more of that trait mate more, and their sons inherit the trait while their daughters inherit the preference. The preference and the trait then coevolve in an escalating spiral, potentially driving the ornament to extreme levels that are far beyond any indicator value.

Sexual selection explains some of the most striking patterns in biology. **Sexual dimorphism** — the difference in appearance between males and females of the same species — is directly predicted by its intensity. Species with strong male-male competition (like elephant seals, where dominant males monopolize harems) show extreme size dimorphism. Species with strong female choice (like birds of paradise) show extreme plumage dimorphism. Species where both sexes choose and compete (like many monogamous songbirds) show minimal dimorphism. Sexual selection can also drive **rapid speciation** because mating preferences can diverge quickly between populations, creating reproductive isolation even without geographic barriers.
