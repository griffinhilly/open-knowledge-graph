---
id: frequency-dependent-selection-polymorphism
title: Frequency-Dependent Selection and Polymorphism
domain: biology
course: ecology-and-evolution
prerequisites:
- id: natural-selection
  type: hard
- id: population-genetics-intro
  type: hard
- id: probability-mass-functions
  type: soft
builds-toward:
- evolutionary-stable-strategy
- sexual-selection
tags:
- selection
- polymorphism
- frequency-dependent
stage: formal-systems
status: draft
---

# Frequency-Dependent Selection and Polymorphism

## Core Idea
Frequency-dependent selection occurs when the fitness of a phenotype depends on its frequency in the population, maintaining polymorphism through negative frequency dependence. Common examples include predators searching for rare prey types and mating preferences that favor rare phenotypes. This mechanism prevents directional selection from fixing alleles, maintaining genetic variation indefinitely.

## How It's Best Learned
Examine classic examples like the peppered moth and predator search images. Model population dynamics with simple Lotka-Volterra equations where rare phenotypes have fitness advantage.

## Common Misconceptions
- Thinking frequency-dependent selection always maintains polymorphism in large populations.
- Assuming it requires conscious preference for rarity; it emerges from ecological processes.

## Questions

```yaml
- question: "In a prey population, blue morphs are at 80% frequency and green morphs at 20%. Predators have formed a strong search image for blue prey. What will happen to morph frequencies in the next generation?"
  type: multiple-choice
  options:
    - "Blue morphs will increase further because they are more numerous and better adapted to the environment"
    - "Green morphs will increase because their rarity makes them harder for predators to detect, giving them a survival advantage"
    - "Both morphs will decline sharply as predators eliminate prey from the population"
    - "The population will fix on blue morphs because the majority phenotype always prevails under natural selection"
  answer: 1
  explanation: "This is the core mechanism of negative frequency-dependent selection: rare phenotypes have a fitness advantage precisely because they are rare. Predators with a search image for blue prey hunt blue morphs efficiently while overlooking green morphs. As green morphs survive and reproduce more, they become more common — at which point the advantage shifts, and predators begin to form a search image for green. This oscillation maintains both morphs indefinitely. Options A and D reflect the misconception that common phenotypes are always favored — true under directional selection but false under negative frequency dependence."

- question: "Warning coloration in toxic species (Müllerian mimicry), where multiple toxic species converge on the same color pattern, is an example of:"
  type: multiple-choice
  options:
    - "Negative frequency-dependent selection, because rare warning patterns are harder for predators to learn and avoid"
    - "Positive frequency-dependent selection, because the most common warning pattern provides the best predator education and protection"
    - "Balancing selection through heterozygote advantage, because individuals heterozygous for color alleles survive best"
    - "Directional selection driving one color pattern to extinction while another fixes"
  answer: 1
  explanation: "In Müllerian mimicry, predators learn to avoid the most common warning pattern most efficiently — the more individuals share a pattern, the stronger the learned avoidance response. This means common patterns are favored: positive frequency-dependent selection. Crucially, positive FDS does the opposite of maintaining polymorphism — it pushes the population toward fixation on one common form. This is why positive FDS cannot be invoked to explain long-term polymorphism; that explanation requires negative FDS."

- question: "Negative frequency-dependent selection can maintain two or more phenotypes in a population indefinitely without any individual organism consciously preferring or choosing rarity."
  type: true-false
  answer: true
  explanation: "The mechanism is entirely ecological, not intentional. Predator search images emerge from statistical regularities in predator learning — predators encounter common prey more often and form stronger recognition templates for them. No organism chooses to be rare, and no organism 'prefers' novelty. The rare-advantage emerges from the interaction between predator cognition and prey frequency, not from any preference within the prey population."

- question: "Positive frequency-dependent selection is the primary mechanism responsible for maintaining genetic polymorphism in natural populations."
  type: true-false
  answer: false
  explanation: "Positive frequency-dependent selection does the opposite — it favors common phenotypes and tends to reduce or eliminate polymorphism by driving the population toward fixation on a single form. The mechanism that maintains polymorphism is NEGATIVE frequency-dependent selection, where rare phenotypes are favored. When population geneticists invoke frequency-dependent selection to explain sustained genetic variation, they almost always mean the negative form."

- question: "Explain why negative frequency-dependent selection prevents directional selection from fixing a single allele in the population."
  type: short-answer
  answer: "Under directional selection, the fittest allele increases in frequency monotonically until it reaches fixation. Negative frequency-dependent selection breaks this monotonic increase by changing the fitness landscape as frequencies change: as a phenotype becomes more common, its fitness advantage declines (and may reverse), while the rarer phenotype gains a fitness advantage. This creates a stable equilibrium frequency for each phenotype — the frequency at which neither has a net advantage. Any perturbation away from equilibrium is self-correcting: if the common phenotype becomes too common, selection favors the rare one; if the rare phenotype becomes too common, selection shifts back. The result is indefinite coexistence of multiple phenotypes."
  explanation: "The contrast with directional selection is the key insight: under directional selection, fitness is fixed and the fittest wins; under negative FDS, fitness is dynamic and depends on frequency, so no single phenotype can achieve permanent dominance."
```

## Explainer

Standard natural selection, as you already understand it, tends to push populations toward fixation — the fittest allele increases in frequency until it dominates. But many natural populations maintain multiple forms of a trait indefinitely. **Frequency-dependent selection** explains how: instead of one phenotype always being fittest, fitness depends on how common or rare the phenotype is. This creates a built-in balancing mechanism that prevents any single form from taking over.

The most important form is **negative frequency-dependent selection**, where rare phenotypes have a fitness advantage precisely because they are rare. The classic example involves predator **search images**. When blue morphs of a prey species are common and green morphs are rare, predators learn to recognize blue and hunt it efficiently, giving the overlooked green morphs higher survival. As green morphs become more common due to their advantage, predators shift their search image, and now blue morphs benefit from rarity. The result is an oscillation that maintains both morphs in the population. No conscious preference for novelty is needed — the mechanism emerges from the statistics of predator attention.

The same logic extends to host-parasite interactions and mating systems. Parasites tend to evolve to exploit the most common host genotype, giving rare genotypes a survival advantage — a key driver of the evolution of sexual reproduction itself, which constantly produces new genetic combinations. In some mating systems, rare male phenotypes have higher reproductive success because females preferentially mate with unfamiliar types, or because common males face more intense competition. In the side-blotched lizard, three male throat-color morphs cycle in frequency over years through a rock-paper-scissors dynamic: each type beats one and loses to another.

**Positive frequency-dependent selection** works in the opposite direction — common phenotypes are favored — and tends to reduce rather than maintain polymorphism. Warning coloration in toxic species (Müllerian mimicry) is an example: the more individuals share the same warning pattern, the better predators learn to avoid it. However, positive frequency dependence eventually drives the population toward a single dominant form, so it does not maintain polymorphism. When population geneticists invoke frequency-dependent selection as a mechanism for sustaining genetic variation, they almost always mean the negative form — the rare-advantage dynamic that creates a stable equilibrium with multiple coexisting phenotypes.
