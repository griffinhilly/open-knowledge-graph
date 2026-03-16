---
id: adaptive-landscape-crossing
title: Traversing Adaptive Landscapes
domain: biology
course: evolutionary-biology
prerequisites:
- id: fitness-landscape
  type: hard
- id: natural-selection
  type: hard
- id: genetic-drift
  type: soft
builds-toward:
- evolvability
- major-evolutionary-innovations
tags:
- fitness-landscape
- evolution
- selection
- drift
stage: advanced
status: draft
---

# Traversing Adaptive Landscapes

## Core Idea
Evolution navigates fitness landscapes by moving uphill via selection and occasionally crossing fitness valleys via drift-assisted mutations or environmental change. Population size and landscape topology determine probability of crossing valleys and exploring distant adaptive peaks.

## Explainer

From your study of fitness landscapes, you can picture evolution as a population moving across a rugged terrain where elevation represents fitness. Natural selection pushes populations uphill toward local fitness peaks — genotype combinations that are fitter than their immediate neighbors. But here is the central problem: **what happens when a population reaches a local peak that is not the global optimum?** Selection alone cannot move a population downhill through a fitness valley to reach a higher peak, because every step downhill is disfavored. This is the valley-crossing problem, and solving it is essential for understanding how evolution produces major innovations.

**Genetic drift** provides the primary mechanism for valley crossing. In small populations, random fluctuations in allele frequencies can push a population off its current peak and into a fitness valley, purely by chance. Once in the valley, the population may drift to the slope of a different, potentially higher peak, where selection can then take over and drive it uphill. This is Sewall Wright's **shifting balance theory** in essence: drift explores, selection exploits. The probability of crossing a valley depends on both the population size and the depth of the valley. Shallow valleys are crossed readily even in moderately sized populations; deep valleys require very small populations where drift is strong enough to overpower selection against the valley genotypes.

Population size creates a fundamental tension. Large populations are efficient at climbing peaks because selection is strong relative to drift — beneficial mutations spread quickly and deleterious ones are purged. But large populations are also trapped on their current peak because drift is too weak to push them into a valley. Small populations can explore the landscape more freely through drift, but they are also vulnerable to extinction and accumulate deleterious mutations. This tradeoff means that **population structure** — a species divided into many small, semi-isolated subpopulations connected by occasional migration — may be the ideal configuration for landscape traversal. Small subpopulations can drift across valleys independently, and if one finds a higher peak, migration can spread its superior genotype to other subpopulations.

Environmental change offers another route across valleys by **reshaping the landscape itself**. A fitness valley under one set of conditions may become a ridge under different conditions — what was once a maladaptive intermediate genotype becomes favored when the environment shifts. Mass extinctions, climate changes, and ecological upheavals can flatten existing peaks and raise new ones, releasing populations from local optima and opening paths to novel adaptations. This means that the adaptive landscape is not static but dynamic, and the history of life reflects populations navigating a constantly shifting terrain where both stochastic drift and deterministic environmental change open doors that selection alone cannot.
