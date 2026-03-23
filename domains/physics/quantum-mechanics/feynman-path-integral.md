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
status: validated
---

# Feynman Diagrams and Perturbative Expansion

## Core Idea
Path integrals expand perturbatively as Feynman diagrams in quantum field theory. Each diagram represents a contribution to the amplitude (virtual particles, interactions, loops). Feynman rules translate diagrams into cross sections and decay rates.

## Questions

```yaml
- question: "A virtual photon appears as an internal line in a Feynman diagram for electron-electron scattering. Which statement about this virtual photon is correct?"
  type: multiple-choice
  options:
    - "It is a real photon that briefly exists during the interaction and then annihilates"
    - "It is a field excitation that may carry any energy, including values that violate E² = p²c² + m²c⁴, because it is never directly observed"
    - "It must satisfy the photon dispersion relation E = pc, because all photons are massless"
    - "It represents the average over all possible photon trajectories between the two electrons"
  answer: 1
  explanation: "Virtual particles are 'off-shell': they are internal lines in Feynman diagrams representing intermediate field excitations that need not satisfy the on-shell relation E² = p²c² + m²c⁴. This is possible because they are never directly measured — only the external lines (real, observable particles) are required to be on-shell. Energy and momentum are conserved at every vertex, but the propagator for an internal line allows all values of p², which is why integrating over unmeasured loop momenta can give divergent results. Options A and D mischaracterize what internal lines mean; option C incorrectly imposes the on-shell condition."

- question: "In the perturbative expansion of a quantum field theory amplitude, what does a 'tree-level' diagram represent?"
  type: multiple-choice
  options:
    - "A diagram drawn on paper (as opposed to a computer-generated diagram)"
    - "The leading-order term in the expansion — a diagram with no closed loops, corresponding to the lowest power of the coupling constant"
    - "A diagram that only involves photons, not electrons or other fermions"
    - "An approximation valid only for strong coupling constants where higher-order terms are negligible"
  answer: 1
  explanation: "Tree-level diagrams are those with no closed loops. In the perturbative expansion in powers of the coupling constant λ, the tree-level diagrams give the lowest-order (leading) contributions. Each additional loop adds a factor of λ (or λ²), so loop diagrams are higher-order corrections. Tree-level amplitudes correspond to the classical field theory limit and are finite; loop diagrams introduce integrals over unconstrained momenta that can diverge. The term 'tree' refers to the topological structure (graph with no cycles), not to the physical medium or the content of the diagram."

- question: "Virtual particles in Feynman diagrams are field excitations that need not satisfy the energy-momentum relation required of real, observable particles."
  type: true-false
  answer: true
  explanation: "True. Internal lines in Feynman diagrams represent propagators — mathematical factors encoding the quantum amplitude for a field excitation to carry a given four-momentum. These excitations are 'off-shell': the four-momentum squared p² need not equal m². Because they are never directly measured (only external, observable particles enter detectors), there is no physical requirement that they be on-shell. This off-shell freedom is what makes the integration over internal momenta in loop diagrams possible — and is also why those integrals diverge at large momenta."

- question: "A Feynman diagram represents the literal spacetime path taken by particles during a quantum interaction."
  type: true-false
  answer: false
  explanation: "False. Feynman diagrams are bookkeeping devices for terms in a perturbative expansion of the path integral — they encode specific mathematical contributions to a quantum amplitude, not literal particle trajectories. In quantum mechanics, there is no single definite path; the path integral sums over all possible histories. Each diagram represents one term in a power-series expansion of that sum. Internal lines (virtual particles) do not correspond to real particles with definite trajectories; they represent the quantum superposition of all possible intermediary field configurations at that order in the expansion."

- question: "Why do loop diagrams in quantum field theory produce divergent integrals, and what does renormalization do to handle them?"
  type: short-answer
  answer: "Loop diagrams require integrating over all momenta flowing around the loop — there is no kinematic constraint fixing the loop momentum, because energy-momentum conservation at vertices still leaves one free integration variable per loop. As the loop momentum goes to infinity (the ultraviolet limit), the integrand typically does not decay fast enough, producing a divergent result. Renormalization absorbs these infinities into redefinitions of physical parameters (mass, charge, field strength), which are then measured experimentally rather than computed from the bare theory. After renormalization, predictions for observable quantities are finite and in remarkable agreement with experiment."
  explanation: "The key insight is that the bare parameters in the Lagrangian are not the measurable physical parameters — renormalization establishes the relationship between them by requiring that loop-corrected quantities equal observed values. For QED, this procedure yields predictions (like the electron's anomalous magnetic moment) accurate to 12 significant figures, making it one of the most precisely tested theories in physics."
```

## Explainer

From the path-integral formulation you already know, the quantum amplitude for a process is a sum over all field configurations (all "histories"), weighted by exp(iS/ħ) where S is the action. In quantum field theory, the action contains a free part — describing non-interacting particles — and an interaction part that couples fields together, typically with a small coupling constant λ (like the electron charge e in QED). When λ is small, you can expand exp(iS_interaction/ħ) as a Taylor series: 1 + iS_int/ħ + (iS_int/ħ)²/2! + … Each term in this **perturbative expansion** contributes a specific correction to the amplitude. Feynman's genius was realizing that each term in this series could be represented as a picture — a **Feynman diagram**.

Think of a Feynman diagram as a bookkeeping device, not a literal depiction of particles. External lines represent real, measurable particles entering or leaving the interaction. Internal lines represent **virtual particles** — field excitations that propagate between interaction points (vertices) but are never directly observed. The key constraint is that all energy and momentum must be conserved at every vertex, but virtual particles are allowed to be "off-shell" — meaning they do not satisfy the usual E² = p²c² + m²c⁴ relation of real particles. A photon mediating the repulsion between two electrons, for example, carries momentum but can have any energy, including zero. It is the path-integral's way of encoding the quantum superposition of all possible intermediary field configurations.

The real power of this machinery is the **Feynman rules**: a precise dictionary that translates each diagram element into a mathematical factor. External lines contribute polarization vectors or spinors. Internal propagator lines contribute factors of i/(p² - m² + iε). Each vertex contributes a coupling constant (−ie for QED). To compute the amplitude for a process, you draw every topologically distinct diagram allowed by the theory, write down the factors from the rules, integrate over unmeasured momenta, and sum. The result is a number whose modulus squared gives the cross section — directly comparable to experiment.

**Loop diagrams** are where the theory becomes subtle. A diagram with no loops is called a **tree-level** diagram; it corresponds to the leading term in the λ expansion. Diagrams with one or more closed loops require integrating over all momenta flowing around the loop, and these integrals often diverge — the famous **ultraviolet divergences** of quantum field theory. Renormalization absorbs these infinities into redefinitions of physical parameters (mass, charge). The remarkable fact of QED is that after renormalization, the perturbative series agrees with experiment to extraordinary precision: the electron's anomalous magnetic moment is predicted to 12 significant figures. Feynman diagrams are thus not merely pictorial conveniences — they are the calculational backbone of modern particle physics.
