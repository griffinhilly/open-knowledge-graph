---
id: percolation-critical-phenomena
title: Percolation and Critical Phenomena
domain: physics
course: statistical-mechanics
prerequisites:
- id: phase-transitions
  type: hard
- id: critical-exponents
  type: soft
builds-toward:
- universality-classes-critical
tags:
- percolation
- networks
- phase-transitions
stage: advanced
status: draft
---

# Percolation and Critical Phenomena

## Core Idea
Percolation theory studies connectivity in random networks. At a critical density p_c, a spanning connected path first forms, marking a phase transition. The order parameter (cluster size) exhibits critical exponents that match those of equilibrium phase transitions, revealing universal behavior independent of microscopic details.

## Explainer

Percolation is one of the simplest models that exhibits a genuine phase transition, and it requires no Hamiltonian, no temperature, and no thermodynamics. Consider a square lattice where each site is independently **occupied** with probability p and **empty** with probability 1 − p. Occupied sites are connected to their neighbors, forming clusters. At small p, you get only isolated occupied sites and tiny clusters. At large p, almost every site is occupied and one enormous connected cluster spans the entire lattice. The question is: at what value of p does a **spanning cluster** (one that connects opposite edges of the lattice) first appear?

The answer is the **critical probability** p_c. For the square lattice, p_c ≈ 0.5928. Below p_c, only finite clusters exist; no path crosses the system. Above p_c, a single **infinite cluster** (in the thermodynamic limit) exists and spans the system. This is a genuine phase transition, with p playing the role of temperature (or its inverse) and the probability of belonging to the infinite cluster playing the role of the **order parameter**. From your study of phase transitions, you know that the order parameter goes from zero to nonzero as you cross the transition — here it goes from zero below p_c to a nonzero percolation probability P_∞ above p_c.

The transition has a **critical exponent** structure that mirrors equilibrium statistical mechanics. The percolation probability P_∞ ~ (p − p_c)^β for p just above p_c, where β ≈ 0.14 in 2D. The mean finite cluster size diverges as ξ ~ |p − p_c|^{−γ}. The correlation length — roughly the typical size of clusters — diverges as |p − p_c|^{−ν} as you approach p_c from either side. These power laws are the hallmark of a continuous phase transition. Exactly at p_c, clusters of all sizes exist simultaneously, and the system is **scale-invariant**: there is no characteristic length, and the cluster size distribution follows a pure power law.

What makes percolation particularly important in the context of phase transitions is that it is a *geometric* transition, not a thermodynamic one, yet it obeys the same critical scaling framework. This is the first hint of a deep universality: systems as different as bond percolation, site percolation, random graphs (Erdős–Rényi networks), and polymer gelation all share the same critical exponents when they have the same spatial dimension and symmetry. Percolation thus serves as a bridge between combinatorics and statistical physics, and as a clean testing ground for the concepts of critical exponents and scaling that you will carry forward into universality classes and the renormalization group.
