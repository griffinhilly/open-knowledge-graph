---
id: multipole-static-fields
title: Multipole Expansion for Static Fields
domain: physics
course: electrodynamics
prerequisites:
- id: electric-potential-and-potential-energy
  type: hard
- id: multivariable-calculus
  type: hard
builds-toward:
- multipole-expansion-radiation
tags:
- multipole
- expansion
- static
stage: abstract-reasoning
status: draft
---

# Multipole Expansion for Static Fields

## Core Idea
Multipole expansion approximates far-field potentials of localized charge and current distributions. The monopole (total charge) provides the leading 1/r term. The dipole moment p provides the next 1/r² term. This systematic expansion clarifies which properties of sources dominate at different distances.

## Explainer

Suppose you have a localized collection of charges — an atom, a molecule, a small cluster — and you want to know the electric potential at a distant point r >> (size of distribution). You could sum the Coulomb potential from every individual charge, but this is both computationally expensive and physically uninformative. The **multipole expansion** provides an alternative: it rewrites the potential as a series of terms, each corresponding to a progressively more detailed description of the source. At large distances, only the first few terms matter — and each tells you something concrete about the charge distribution.

The first term is the **monopole**: V_monopole = kQ/r, where Q is the total net charge. If Q ≠ 0, this term dominates at large r, and the entire charge distribution looks, from far away, like a single point charge Q. This falls off as 1/r. If Q = 0 (equal amounts of positive and negative charge — as in a neutral atom), the monopole term vanishes entirely, and you must look at the next term.

The second term is the **dipole**: V_dipole ~ k(p · r̂)/r², where **p** = Σ q_i **r_i** is the **dipole moment** — a vector pointing from the center of negative charge toward the center of positive charge. The dipole potential falls off as 1/r², faster than the monopole. A neutral water molecule has a nonzero dipole moment because its oxygen end pulls electron density away from the hydrogen atoms, creating a permanent separation of charge. At distances large compared to the molecule but small enough that 1/r² still dominates over 1/r³, water-water interactions are primarily dipole-dipole. If p = 0 (as in a perfectly symmetric neutral atom), you must look to the **quadrupole** term (~1/r³), and so on.

The physical insight is a hierarchy of distance scales. Very far from any source, only the monopole matters — everything looks like a point charge. Somewhat closer, dipole structure becomes resolvable. Closer still, quadrupole shape effects emerge. This is why nuclear physicists measure the **quadrupole moment** of atomic nuclei: a nonzero quadrupole moment reveals that the nucleus is not perfectly spherical but elongated or flattened. From your study of electric potential, you know that potentials from multiple charges superpose as scalars — the multipole expansion is simply the most efficient organization of that superposition when the source is compact. It transforms a messy integral over distributed charge into a clean series of well-defined moments, each with a clear physical meaning and a definite distance dependence.
