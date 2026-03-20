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
stage: advanced
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

## Explainer

Standard natural selection, as you already understand it, tends to push populations toward fixation — the fittest allele increases in frequency until it dominates. But many natural populations maintain multiple forms of a trait indefinitely. **Frequency-dependent selection** explains how: instead of one phenotype always being fittest, fitness depends on how common or rare the phenotype is. This creates a built-in balancing mechanism that prevents any single form from taking over.

The most important form is **negative frequency-dependent selection**, where rare phenotypes have a fitness advantage precisely because they are rare. The classic example involves predator **search images**. When blue morphs of a prey species are common and green morphs are rare, predators learn to recognize blue and hunt it efficiently, giving the overlooked green morphs higher survival. As green morphs become more common due to their advantage, predators shift their search image, and now blue morphs benefit from rarity. The result is an oscillation that maintains both morphs in the population. No conscious preference for novelty is needed — the mechanism emerges from the statistics of predator attention.

The same logic extends to host-parasite interactions and mating systems. Parasites tend to evolve to exploit the most common host genotype, giving rare genotypes a survival advantage — a key driver of the evolution of sexual reproduction itself, which constantly produces new genetic combinations. In some mating systems, rare male phenotypes have higher reproductive success because females preferentially mate with unfamiliar types, or because common males face more intense competition. In the side-blotched lizard, three male throat-color morphs cycle in frequency over years through a rock-paper-scissors dynamic: each type beats one and loses to another.

**Positive frequency-dependent selection** works in the opposite direction — common phenotypes are favored — and tends to reduce rather than maintain polymorphism. Warning coloration in toxic species (Müllerian mimicry) is an example: the more individuals share the same warning pattern, the better predators learn to avoid it. However, positive frequency dependence eventually drives the population toward a single dominant form, so it does not maintain polymorphism. When population geneticists invoke frequency-dependent selection as a mechanism for sustaining genetic variation, they almost always mean the negative form — the rare-advantage dynamic that creates a stable equilibrium with multiple coexisting phenotypes.
