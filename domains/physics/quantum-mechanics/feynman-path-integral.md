---
id: feynman-path-integral
title: Feynman Diagrams and Perturbative Expansion
domain: physics
course: quantum-mechanics
prerequisites:
- id: path-integral-formulation
  type: hard
tags:
- feynman-diagrams
- path-integrals
stage: advanced
status: draft
---

# Feynman Diagrams and Perturbative Expansion

## Core Idea
Path integrals expand perturbatively as Feynman diagrams in quantum field theory. Each diagram represents a contribution to the amplitude (virtual particles, interactions, loops). Feynman rules translate diagrams into cross sections and decay rates.

## Explainer

From the path-integral formulation you already know, the quantum amplitude for a process is a sum over all field configurations (all "histories"), weighted by exp(iS/ħ) where S is the action. In quantum field theory, the action contains a free part — describing non-interacting particles — and an interaction part that couples fields together, typically with a small coupling constant λ (like the electron charge e in QED). When λ is small, you can expand exp(iS_interaction/ħ) as a Taylor series: 1 + iS_int/ħ + (iS_int/ħ)²/2! + … Each term in this **perturbative expansion** contributes a specific correction to the amplitude. Feynman's genius was realizing that each term in this series could be represented as a picture — a **Feynman diagram**.

Think of a Feynman diagram as a bookkeeping device, not a literal depiction of particles. External lines represent real, measurable particles entering or leaving the interaction. Internal lines represent **virtual particles** — field excitations that propagate between interaction points (vertices) but are never directly observed. The key constraint is that all energy and momentum must be conserved at every vertex, but virtual particles are allowed to be "off-shell" — meaning they do not satisfy the usual E² = p²c² + m²c⁴ relation of real particles. A photon mediating the repulsion between two electrons, for example, carries momentum but can have any energy, including zero. It is the path-integral's way of encoding the quantum superposition of all possible intermediary field configurations.

The real power of this machinery is the **Feynman rules**: a precise dictionary that translates each diagram element into a mathematical factor. External lines contribute polarization vectors or spinors. Internal propagator lines contribute factors of i/(p² - m² + iε). Each vertex contributes a coupling constant (−ie for QED). To compute the amplitude for a process, you draw every topologically distinct diagram allowed by the theory, write down the factors from the rules, integrate over unmeasured momenta, and sum. The result is a number whose modulus squared gives the cross section — directly comparable to experiment.

**Loop diagrams** are where the theory becomes subtle. A diagram with no loops is called a **tree-level** diagram; it corresponds to the leading term in the λ expansion. Diagrams with one or more closed loops require integrating over all momenta flowing around the loop, and these integrals often diverge — the famous **ultraviolet divergences** of quantum field theory. Renormalization absorbs these infinities into redefinitions of physical parameters (mass, charge). The remarkable fact of QED is that after renormalization, the perturbative series agrees with experiment to extraordinary precision: the electron's anomalous magnetic moment is predicted to 12 significant figures. Feynman diagrams are thus not merely pictorial conveniences — they are the calculational backbone of modern particle physics.
