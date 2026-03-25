---
id: genetic-drift-process
title: 'Genetic Drift: Process and Population Effects'
domain: biology
course: evolutionary-biology
prerequisites:
- id: genetic-drift
  type: hard
- id: allele-frequency-change
  type: hard
- id: probability-axioms
  type: soft
builds-toward:
- effective-population-size
- peripatric-speciation
tags:
- drift
- stochastic-evolution
- population-size
stage: formal-systems
status: validated
---

# Genetic Drift: Process and Population Effects

## Core Idea
Genetic drift is random sampling of alleles in finite populations, causing random fluctuations in allele frequency regardless of selection. The strength of drift (measured by its variance) is inversely proportional to population size: larger populations experience weaker drift. Drift can fix neutral alleles, eliminate beneficial alleles, and preserve deleterious alleles, making it a major driver of molecular evolution.

## How It's Best Learned
Run Monte Carlo simulations of drift in populations of varying sizes. Observe fixation and loss of alleles and note that time to fixation increases with population size.

## Common Misconceptions
- Drift only matters in very small populations; drift affects all populations and is particularly important for neutral evolution.
- Drift causes alleles to predictably increase; drift causes random changes with no directional bias.

## Questions

```yaml
- question: "A beneficial allele that increases fitness by 0.01% (s = 0.0001) arises as a single new mutation in a population of N = 1,000 individuals. What is the most likely fate of this allele?"
  type: multiple-choice
  options:
    - "It will spread to fixation because it is beneficial and natural selection is deterministic"
    - "It will be lost, because when it is rare its fate is dominated by drift (Ns ≈ 0.1 ≪ 1), making it behave nearly neutrally"
    - "It will reach an intermediate stable frequency because selection and drift balance each other"
    - "It will spread to fixation slowly, because selection always wins over drift in the long run"
  answer: 1
  explanation: "Whether selection or drift dominates depends on the product Ns. When Ns ≪ 1 (here Ns = 1000 × 0.0001 = 0.1), the allele behaves as effectively neutral: drift overwhelms the tiny selective advantage. As a single new mutation, it starts at frequency 1/2N = 1/2000. The probability of fixation for a neutral allele is simply 1/2N ≈ 0.05% — nearly certain loss. A selection coefficient of 0.01% cannot overcome the massive sampling variance in a population of only 1,000. Option D is the common misconception: selection does not 'always win in the long run' for mildly beneficial alleles in finite populations."

- question: "In a population of 10,000 individuals, a neutral allele is currently at frequency 5% (p = 0.05). What is its probability of eventually fixing (reaching p = 1.0)?"
  type: multiple-choice
  options:
    - "Essentially zero — neutral alleles are almost always lost because drift is too weak at this population size"
    - "5% — equal to its current frequency, because fixation probability of a neutral allele equals its current frequency"
    - "50% — because drift is symmetric, there is an equal chance of going up or down"
    - "About 1/2N = 0.005% — because the fixation probability equals the initial frequency when the allele first appeared"
  answer: 1
  explanation: "For a neutral allele, the probability of fixation equals its current frequency p. This is a fundamental result of drift theory: if p = 0.05, there is a 5% chance this allele eventually goes to fixation, and a 95% chance it is lost. Importantly, this probability holds regardless of population size — the population size affects *how long* fixation takes (approximately 4N generations), not the probability itself. Option C (50%) is wrong; symmetry of drift means expected frequency change is zero, but fixation probability depends on starting frequency. Option D confuses the initial frequency at first appearance (1/2N) with the current frequency."

- question: "Genetic drift operates in a predictable, directional manner, systematically pushing allele frequencies toward values that enhance population fitness."
  type: true-false
  answer: false
  explanation: "False. Genetic drift is inherently random and undirected — it is sampling error, not a force with direction or tendency. In any given generation, drift is equally likely to increase or decrease an allele's frequency (the expected change is zero). Over time, allele frequencies perform a random walk that must eventually end in fixation or loss, but which outcome occurs for any particular allele is stochastic. Natural selection is the directional force that favors higher-fitness alleles; drift is the random noise around that signal. The misconception that drift has a direction often arises from conflating drift with the Founder Effect, where a small founding population may by chance carry unusual allele frequencies — but this is still a random sampling outcome, not a directed process."

- question: "Genetic drift can cause a beneficial allele to be permanently lost from a population before selection has a chance to spread it."
  type: true-false
  answer: true
  explanation: "True. When a beneficial allele first arises as a mutation, it exists at very low frequency. At low frequencies, the random component of its fate (drift) is large relative to the deterministic component (selection). Even an allele with a 10% fitness advantage has approximately a 20% chance of fixation when it first arises — meaning an ~80% chance of loss, primarily from drift while it is rare. This has important consequences: many beneficial mutations are lost before they spread, evolution is not a reliable optimizer, and the efficacy of selection depends critically on Ne. The neutral theory of molecular evolution partially rests on this observation: most alleles that fix are neutral, fixed by drift, because beneficial alleles are so often lost before they can spread."

- question: "Why does drift become negligible relative to selection as population size increases, and what is the condition that determines whether an allele 'behaves as if neutral'?"
  type: short-answer
  answer: "The variance in allele frequency change per generation due to drift is p(1-p)/2N — it decreases as N increases. Selection causes a deterministic frequency change of approximately sp(1-p) per generation. The ratio of selection to drift scales with Ns: when Ns ≫ 1, selection's deterministic push far exceeds drift's random fluctuations, and alleles behave as their fitness predicts. When Ns ≪ 1, drift's noise swamps selection's signal, and the allele behaves as effectively neutral regardless of its actual s. The boundary condition Ns ≈ 1 (equivalently, s ≈ 1/N) marks when selection and drift are approximately equal in strength."
  explanation: "This is the central quantitative insight of population genetics: it is not s alone, or N alone, but their product Ns that determines which force dominates. This has major implications: the same allele with s = 0.001 behaves as neutral in a population of 100 (Ns = 0.1) but is strongly selected in a population of 10,000 (Ns = 10). Conservation geneticists use this principle to assess the minimum viable population size needed for selection to function effectively."
```

## Explainer

You already know from studying genetic drift that allele frequencies can change by chance alone, and from allele frequency change that populations evolve when allele frequencies shift across generations. This topic deepens your understanding of the **process mechanics** of drift — how and why random sampling in finite populations produces the patterns we observe, and what those patterns mean for evolution.

Think of reproduction as drawing marbles from a jar. A population of diploid organisms has a "jar" of 2N gene copies. The next generation is formed by randomly sampling 2N copies from this jar. If the jar contains 50% red and 50% blue marbles, you would expect the sample to be roughly 50/50 — but "roughly" is the key word. In a jar of 20 marbles, a sample might easily come out 60/40 or 40/60 by chance. In a jar of 20,000, a 51/49 split would be unusual. This is why **drift is inversely proportional to population size**: the sampling error is larger when fewer copies are drawn. The variance in allele frequency change per generation is approximately *p(1-p)/2N*, where p is the current allele frequency and N is the population size.

Over many generations, drift causes allele frequencies to wander unpredictably — a **random walk**. Eventually, every allele either drifts to fixation (frequency = 1.0) or loss (frequency = 0). For a neutral allele, the probability of fixation equals its current frequency, and the average time to fixation is 4N generations. This means drift is both inevitable and slow in large populations but rapid and powerful in small ones. A neutral allele at 10% frequency has a 10% chance of eventually fixing — regardless of population size — but it takes vastly longer in a population of a million than in a population of a hundred.

The evolutionary consequences are profound. Drift can **fix mildly deleterious alleles** that selection alone would eliminate, because in small populations the random noise of drift can overpower weak selective pressures. This happens when the selection coefficient (s) is smaller than roughly 1/2N — the allele behaves as if it were neutral. Drift can also **eliminate beneficial alleles** before they have a chance to spread, especially when they are rare and selection is weak. At the molecular level, the neutral theory of molecular evolution argues that most substitutions between species are neutral alleles fixed by drift, not beneficial alleles fixed by selection. Understanding drift is therefore essential for interpreting DNA sequence divergence, designing conservation strategies for small populations, and recognizing the limits of natural selection's power.
