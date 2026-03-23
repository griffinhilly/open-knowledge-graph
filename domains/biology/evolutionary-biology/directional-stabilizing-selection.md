---
id: directional-stabilizing-selection
title: Directional and Stabilizing Selection
domain: biology
course: evolutionary-biology
prerequisites:
- id: selection-coefficients
  type: hard
builds-toward:
- sexual-selection
tags:
- selection
- phenotypic-evolution
- adaptation
- variance
stage: advanced
status: validated
---

# Directional and Stabilizing Selection

## Core Idea
Directional selection favors one phenotypic extreme, shifting the mean phenotype and reducing variation—causing sustained evolution. Stabilizing selection favors intermediate phenotypes, removing variation at both extremes and maintaining the mean—reducing overall variation. These contrasting modes have opposite effects on population variance and rates of phenotypic evolution.

## Questions

```yaml
- question: "A population of deer mice lives in a snowy habitat. Mice with very light fur are easily spotted by predators; mice with very dark fur absorb less heat and suffer in winter cold. Intermediate gray coloration shows the highest survival rates. Which selection mode is operating, and what will happen to the population over generations?"
  type: multiple-choice
  options:
    - "Directional selection: the average color will shift toward darker gray as light mice are eliminated"
    - "Stabilizing selection: the average color will remain approximately constant, but variation will decrease as both extremes are removed"
    - "Directional selection: because both extremes are disadvantaged, the population will become more variable over time"
    - "Disruptive selection: both light and dark mice are disadvantaged, simultaneously favoring both phenotypic extremes"
  answer: 1
  explanation: "When both extremes are penalized and intermediates are favored, stabilizing selection is operating. The mean coloration stays roughly constant (already at the intermediate optimum), while both tails of the distribution are trimmed each generation, reducing overall variation. Option A is wrong because directional selection favors ONE extreme and moves the mean toward it — here, both extremes are penalized equally. Option D confuses stabilizing with disruptive selection: disruptive selection FAVORS both extremes and penalizes the middle, the opposite of the scenario described."

- question: "After a severe drought, a population of finches shows a significant increase in average beak depth over three generations, and beak depth variance also decreases. This pattern is most consistent with:"
  type: multiple-choice
  options:
    - "Stabilizing selection — variance decreases as the population clusters around the pre-existing optimal beak depth"
    - "Directional selection — the mean shifted as shallow-beaked individuals were culled from the disfavored tail, simultaneously reducing variance"
    - "Disruptive selection — both modes reduce variance, so either could explain this pattern"
    - "Genetic drift — small populations lose variation randomly, incidentally shifting the mean"
  answer: 1
  explanation: "Directional selection shifts the mean toward the favored extreme AND reduces variance, because it culls individuals from the disfavored tail. The mean shift (increased average beak depth) and variance reduction together are the characteristic signature of directional selection favoring deep beaks. Stabilizing selection (option A) would maintain the mean while reducing variance — inconsistent with the observed mean shift. Disruptive selection (option C) actually increases variance by favoring both extremes and cannot explain a unimodal mean shift."

- question: "Stabilizing selection causes populations to evolve rapidly toward a new phenotypic optimum."
  type: true-false
  answer: false
  explanation: "Stabilizing selection does not shift the phenotypic mean — it is a force for evolutionary stasis. By penalizing deviations from the current optimum in both directions, it maintains the status quo while reducing variation. Rapid evolution toward a new optimum is the signature of directional selection, which favors one extreme over others. Stabilizing selection explains why many traits appear static over long periods in the fossil record despite ample genetic variation — the trait is already near its local optimum, and any deviation is penalized."

- question: "Both directional and stabilizing selection reduce phenotypic variance within a population, though through different mechanisms and with different effects on the mean."
  type: true-false
  answer: true
  explanation: "This is correct and often overlooked. Directional selection reduces variance by culling the disfavored tail — the population loses that end of the distribution while the mean moves. Stabilizing selection reduces variance more symmetrically, trimming both tails each generation while keeping the mean constant. Both modes reduce variance, but only directional selection moves the mean. This shared effect on variance means variance measurements alone cannot distinguish the two modes — examining whether the mean changes is the key diagnostic."

- question: "Why is stabilizing selection considered the most common mode of selection in nature, despite receiving less attention than directional selection?"
  type: short-answer
  answer: "Most traits in most populations are already close to their local adaptive optimum — the phenotype that maximizes fitness in the current stable environment. Deviations in either direction are typically costly: growing too large exhausts resources, growing too small impairs competition or thermoregulation. Since organisms are generally well-adapted to their environments, selection acts primarily to maintain the current phenotype by removing deviants from both distribution tails. Directional selection requires either an environmental shift that makes the current optimum suboptimal, or colonization of a new environment — events that are less common than ongoing stabilizing pressure in stable environments."
  explanation: "Stabilizing selection explains a key observation in evolutionary biology: despite enormous genetic variation and constant mutation, many traits remain remarkably stable over geological time. This stability is not from lack of variation but from continuous removal of variants that deviate from the optimum. Evolutionary change requires a new selective regime; in its absence, stabilizing selection maintains the existing phenotype."
```

## Explainer

From your study of selection coefficients, you know how to quantify the fitness advantage of one genotype over another. Now consider what happens when selection acts not on discrete genotypes but on a continuous trait — body size, beak depth, running speed — distributed across a population as a bell curve. The **mode of selection** describes which part of that distribution is favored, and it determines both the direction and tempo of evolutionary change.

**Directional selection** occurs when individuals at one extreme of the distribution have the highest fitness. Imagine a drought that kills all but the hardiest seeds — birds with the deepest, strongest beaks crack these seeds and survive, while shallow-beaked birds starve. The next generation's beak depth distribution shifts toward the deep end, because the survivors who reproduced were disproportionately deep-beaked. If the selective pressure persists, the population mean moves steadily in one direction across generations. This is the mode of selection most people picture when they think of evolution in action — the gradual, sustained shift of a trait toward an adaptive optimum. Directional selection also reduces phenotypic variance, because it culls individuals from the disfavored tail.

**Stabilizing selection** does the opposite: it favors the average and penalizes both extremes. Human birth weight is a classic example. Babies that are too small face survival challenges from underdevelopment; babies that are too large risk complications during delivery. The highest survival rates cluster around an intermediate weight. Both tails of the distribution are trimmed each generation, so the population mean stays roughly constant while variance decreases. Stabilizing selection is probably the most common mode in nature — most traits in most populations are already near their local optimum, and deviations in either direction are costly.

The contrast between these modes explains a fundamental pattern in evolution. Directional selection drives rapid change — it is responsible for the dramatic adaptive shifts seen during colonization of new environments, arms races between predators and prey, or responses to sudden environmental change. Stabilizing selection maintains the status quo — it explains why many traits appear static over long periods in the fossil record despite ample genetic variation. A third mode, **disruptive selection**, favors both extremes and disfavors the middle, potentially splitting a population into distinct morphs — but directional and stabilizing selection are the workhorses that account for most observed patterns of trait evolution and stasis across the tree of life.
