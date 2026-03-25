---
id: multipole-static-fields
title: Multipole Expansion for Static Fields
domain: physics
course: electrodynamics
prerequisites:
- id: electric-potential-and-potential-energy
  type: hard
- id: partial-derivatives
  type: hard
builds-toward:
- multipole-expansion-radiation
tags:
- multipole
- expansion
- static
stage: expert
status: validated
---

# Multipole Expansion for Static Fields

## Core Idea
Multipole expansion approximates far-field potentials of localized charge and current distributions. The monopole (total charge) provides the leading 1/r term. The dipole moment p provides the next 1/r² term. This systematic expansion clarifies which properties of sources dominate at different distances.

## Questions

```yaml
- question: "A neutral atom has perfectly symmetric electron distribution so its center of positive charge exactly coincides with its center of negative charge. Far from this atom, which term in the multipole expansion dominates the electric potential?"
  type: multiple-choice
  options:
    - "Monopole (1/r) — it always dominates at large distances regardless of net charge"
    - "Dipole (1/r²) — neutral atoms always have some residual charge separation"
    - "Quadrupole (1/r³) — because both the monopole and dipole terms vanish for this distribution"
    - "None — a perfectly neutral, symmetric atom produces zero electric potential at any distance"
  answer: 2
  explanation: "The monopole term requires Q ≠ 0 (nonzero net charge) — it vanishes here because the atom is neutral. The dipole term requires p ≠ 0 (nonzero dipole moment, meaning separated centers of charge) — it vanishes here because the distribution is perfectly symmetric, so the centers of positive and negative charge coincide. The first nonzero contribution is therefore the quadrupole term (~1/r³), which responds to the shape of the charge distribution even when it is neutral and symmetric. This hierarchical logic — check monopole, then dipole, then quadrupole — is the operational procedure of multipole expansion."

- question: "Why does the dipole potential fall off as 1/r² (faster than the monopole's 1/r) at large distances?"
  type: multiple-choice
  options:
    - "Because the dipole moment vector p is always numerically smaller than the net charge Q"
    - "Because the positive and negative charges of the dipole partially cancel each other's potentials, producing a progressively weaker net effect as distance increases"
    - "Because the dipole is a mathematical approximation that underestimates the true potential at large r"
    - "Because dipoles only occur in polar molecules, which are less common than charged objects"
  answer: 1
  explanation: "A dipole consists of equal and opposite charges separated by a small distance. From far away, their individual Coulomb potentials (each falling as 1/r) nearly cancel — the positive charge attracts from one direction, the negative charge attracts from almost the same direction. The residual potential from this near-cancellation falls off faster than either charge alone would, specifically as 1/r². This faster falloff is a general principle: higher multipole terms represent increasingly complete cancellations, which is why each successive term falls off one additional power of r faster."

- question: "If a charge distribution has zero net charge (Q=0) but a nonzero dipole moment p, the dominant far-field electric potential falls off as 1/r²."
  type: true-false
  answer: true
  explanation: "With Q=0, the monopole term vanishes. With p≠0, the dipole term is the leading surviving term, and it falls off as 1/r². This is precisely the situation for polar molecules like water: the molecule is electrically neutral overall (Q=0), but the oxygen end pulls electron density from the hydrogens, creating a permanent charge separation and a nonzero dipole moment. At distances large compared to the molecule, water-water interactions are therefore primarily dipole-dipole in character."

- question: "The monopole term in the multipole expansion always provides the best approximation to a charge distribution's far-field potential, regardless of the distribution's properties."
  type: true-false
  answer: false
  explanation: "The monopole term only dominates when Q ≠ 0. If the total charge is zero, the monopole term vanishes entirely, and the dipole term becomes the leading contribution. If both Q=0 and p=0, the quadrupole leads. 'Best approximation' depends entirely on which terms survive — the monopole is only 'best' when it is nonzero, and even then the dipole correction becomes important at shorter distances. The hierarchy of terms is the whole point of the expansion: different terms dominate at different conditions."

- question: "Explain why measuring a nucleus's quadrupole moment tells a physicist something about the shape of the nucleus. What does a nonzero quadrupole moment imply?"
  type: short-answer
  answer: "The quadrupole moment measures how much the charge distribution deviates from spherical symmetry — it is sensitive to whether the distribution is elongated (prolate, like a football) or flattened (oblate, like a discus). A perfectly spherical charge distribution has zero quadrupole moment. A nonzero quadrupole moment therefore reveals that the nucleus is not perfectly spherical: positive quadrupole moments indicate a prolate (elongated) nucleus, negative indicate oblate (flattened). This shape information comes purely from the far-field potential behavior, without directly imaging the nucleus."
  explanation: "This is the power of the multipole hierarchy: each term reveals a different physical property of the source. Monopole → total charge. Dipole → charge separation / polarity. Quadrupole → shape / asphericity. By measuring how the far-field potential falls off and fits the various terms, physicists extract structural information about sources too small to image directly. Nuclear quadrupole moments are measured through their effect on atomic spectra, not by looking at the nucleus."
```

## Explainer

Suppose you have a localized collection of charges — an atom, a molecule, a small cluster — and you want to know the electric potential at a distant point r >> (size of distribution). You could sum the Coulomb potential from every individual charge, but this is both computationally expensive and physically uninformative. The **multipole expansion** provides an alternative: it rewrites the potential as a series of terms, each corresponding to a progressively more detailed description of the source. At large distances, only the first few terms matter — and each tells you something concrete about the charge distribution.

The first term is the **monopole**: V_monopole = kQ/r, where Q is the total net charge. If Q ≠ 0, this term dominates at large r, and the entire charge distribution looks, from far away, like a single point charge Q. This falls off as 1/r. If Q = 0 (equal amounts of positive and negative charge — as in a neutral atom), the monopole term vanishes entirely, and you must look at the next term.

The second term is the **dipole**: V_dipole ~ k(p · r̂)/r², where **p** = Σ q_i **r_i** is the **dipole moment** — a vector pointing from the center of negative charge toward the center of positive charge. The dipole potential falls off as 1/r², faster than the monopole. A neutral water molecule has a nonzero dipole moment because its oxygen end pulls electron density away from the hydrogen atoms, creating a permanent separation of charge. At distances large compared to the molecule but small enough that 1/r² still dominates over 1/r³, water-water interactions are primarily dipole-dipole. If p = 0 (as in a perfectly symmetric neutral atom), you must look to the **quadrupole** term (~1/r³), and so on.

The physical insight is a hierarchy of distance scales. Very far from any source, only the monopole matters — everything looks like a point charge. Somewhat closer, dipole structure becomes resolvable. Closer still, quadrupole shape effects emerge. This is why nuclear physicists measure the **quadrupole moment** of atomic nuclei: a nonzero quadrupole moment reveals that the nucleus is not perfectly spherical but elongated or flattened. From your study of electric potential, you know that potentials from multiple charges superpose as scalars — the multipole expansion is simply the most efficient organization of that superposition when the source is compact. It transforms a messy integral over distributed charge into a clean series of well-defined moments, each with a clear physical meaning and a definite distance dependence.
