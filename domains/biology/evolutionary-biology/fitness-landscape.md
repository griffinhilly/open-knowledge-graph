---
id: fitness-landscape
title: Fitness Landscapes
domain: biology
course: evolutionary-biology
prerequisites:
- id: natural-selection
  type: hard
- id: adaptation-and-fitness
  type: hard
builds-toward:
- directional-selection
- balancing-selection
tags:
- selection
- adaptation
- visualization
stage: advanced
status: draft
---

# Fitness Landscapes

## Core Idea
A fitness landscape is a multidimensional surface where each point represents a genotype and its height represents fitness. Populations evolve by climbing peaks (local optima) or navigating valleys due to mutation and selection. Real landscapes are complex with multiple peaks, epistasis, and changing surfaces.

## Explainer

From natural selection you know that individuals with higher fitness — greater survival and reproductive success — leave more offspring, and from adaptation and fitness you understand that populations tend to become better matched to their environments over time. The **fitness landscape** is a powerful visual metaphor that makes this process spatial and intuitive. Imagine a topographic map where every possible genotype occupies a specific location on the map, and the elevation at that point represents the fitness of that genotype. Natural selection pushes populations uphill — toward genotypes with higher fitness — just as a ball rolling on a hilly surface tends to settle into valleys (though in fitness landscapes, we invert the metaphor: populations climb *toward* peaks rather than rolling into valleys).

The simplest fitness landscape has a single smooth peak — one optimal genotype that selection drives the population toward. But Sewall Wright, who originated the concept, emphasized that real landscapes are **rugged**: they have multiple peaks of different heights separated by valleys of low fitness. This ruggedness arises from **epistasis** — the fitness effect of a mutation at one gene depends on the alleles present at other genes. When gene interactions are complex, nearby genotypes in sequence space can have very different fitnesses, creating a corrugated surface. A population climbing by natural selection alone will reach the nearest peak and get stuck there, even if a much higher peak exists elsewhere, because reaching it would require passing through a fitness valley — a sequence of deleterious intermediate steps that selection opposes.

This is the **local optimum problem**, and it explains why evolution does not always produce the "best" possible solution. How do populations escape local peaks? Several mechanisms help. **Genetic drift** — random fluctuation in allele frequencies — can push small populations off a local peak and into the basin of attraction of a higher one, especially when the valley is shallow. **Mutation** continually introduces new variation that explores neighboring genotype space. **Recombination** can generate novel genotype combinations that jump across the landscape rather than traversing it step by step. And **environmental change** reshapes the landscape itself: a peak under one set of conditions becomes a valley under another, forcing the population to move whether it has reached an optimum or not.

The fitness landscape concept has important limitations to keep in mind. Real genotype spaces are astronomically high-dimensional — even a modest genome offers more possible genotypes than atoms in the universe — so the two-dimensional hill metaphor dramatically understates the complexity. In high dimensions, populations have far more mutational neighbors and more possible routes between peaks, which means local optima may be less "sticky" than the simple 2D picture suggests. Additionally, fitness landscapes are not fixed — they change as the environment shifts, as other species coevolve, and as the population's own allele frequencies alter the selective pressures (frequency-dependent selection). Despite these caveats, the landscape metaphor remains one of evolutionary biology's most useful conceptual tools for reasoning about how selection, drift, mutation, and epistasis interact to shape the trajectory of adaptation.
