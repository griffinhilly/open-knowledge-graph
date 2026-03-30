---
id: feynman-diagrams-systematic
title: Feynman Diagrams (Systematic Rules)
domain: physics
course: quantum-field-theory
prerequisites:
- id: wicks-theorem
  type: hard
- id: propagators-greens-functions
  type: hard
tags:
- feynman-diagrams
- feynman-rules
- perturbation-theory
stage: expert
status: validated
---

# Feynman Diagrams (Systematic Rules)

## Core Idea
Feynman diagrams are a systematic graphical representation of terms in the perturbative expansion of scattering amplitudes. Each diagram encodes a precise mathematical expression: external lines represent incoming/outgoing particles, internal lines are propagators, and vertices carry coupling constants. The Feynman rules translate any diagram into an integral.

## Questions

```yaml
- question: "A student draws all possible Feynman diagrams for a process at a given order but gets the wrong amplitude. They used the correct propagators and vertex factors. What is the most likely systematic error?"
  type: multiple-choice
  options:
    - "They forgot to include the symmetry factor, which accounts for the number of ways the diagram can be drawn from the same set of contractions"
    - "They forgot to include the phase factor from Lorentz transformations"
    - "They used the wrong metric signature"
    - "They forgot to sum over all possible orderings of the external particles"
  answer: 0
  explanation: "Symmetry factors are the most common source of error in Feynman diagram calculations. A symmetry factor S arises when a diagram has internal symmetries — permutations of internal lines and vertices that leave the diagram unchanged. The amplitude must be divided by S to avoid overcounting. For example, a self-energy loop with two identical propagators has S = 2. The vacuum bubble diagram in phi^4 theory (a single vertex with two loops) has S = 8. Forgetting symmetry factors gives amplitudes that are too large by a factor of S."

- question: "In QED, the vertex factor is -ie gamma^mu. Each QED Feynman diagram with n vertices therefore contains a factor of e^n = (sqrt{4 pi alpha})^n. Why does this mean higher-order diagrams give smaller corrections?"
  type: multiple-choice
  options:
    - "Because gamma matrices become smaller at higher powers"
    - "Because alpha = e^2/(4 pi) is approximately 1/137, so each additional vertex introduces a suppression factor of roughly 1/137"
    - "Because momentum conservation at each vertex reduces the available phase space"
    - "Because higher-order diagrams have more internal lines which suppress the amplitude"
  answer: 1
  explanation: "Each QED vertex contributes a factor of e, and each loop introduces an additional factor of alpha = e^2/(4 pi) approximately equal to 1/137. A diagram with L loops is suppressed by alpha^L relative to the tree-level diagram. This is why perturbation theory works so well for QED: each successive order in alpha gives a correction roughly 137 times smaller than the previous one. The spectacular agreement between QED predictions and experiment (the electron g-2 is verified to 12 significant figures) is a direct consequence of alpha being small."

- question: "Disconnected Feynman diagrams (diagrams with pieces not connected to any external line) contribute to physical scattering amplitudes."
  type: true-false
  answer: false
  explanation: "Disconnected diagrams factorize into a connected part (involving the external particles) times vacuum bubble diagrams (closed loops with no external lines). The vacuum bubbles contribute an overall phase factor e^{iW} to the S-matrix, where W is the sum of all vacuum diagrams. This phase cancels when you compute physical quantities like cross sections and decay rates, which depend on |S-matrix element|^2. The linked cluster theorem guarantees that only connected diagrams contribute to the physically relevant connected S-matrix elements."

- question: "State the complete set of Feynman rules for scalar QED (a complex scalar field coupled to the electromagnetic field) at tree level, and explain what each rule represents physically."
  type: short-answer
  answer: "External lines: each incoming/outgoing scalar contributes a factor of 1 (for the standard normalization); each external photon contributes a polarization vector epsilon^mu(k). Internal lines (propagators): scalar propagator i/(p^2 - m^2 + i epsilon) for each internal scalar line; photon propagator -i g_{mu nu}/(k^2 + i epsilon) in Feynman gauge for each internal photon line. Vertices: the scalar-scalar-photon vertex gives -ie(p + p')^mu where p and p' are the momenta of the two scalar lines; the scalar-scalar-photon-photon (seagull) vertex gives 2ie^2 g^{mu nu}. At each vertex, impose momentum conservation. For each internal momentum not fixed by conservation, integrate d^4p/(2pi)^4. Divide by the symmetry factor."
  explanation: "Each rule has a direct physical origin. Propagators describe free-particle propagation between interactions. Vertex factors encode the strength and structure of the interaction — they come from the interaction terms in the Lagrangian. Momentum conservation at vertices reflects translational invariance. The integration over undetermined momenta sums over all possible virtual particle momenta. The Feynman rules are a precise algorithm for turning the physical content of the Lagrangian into numerical predictions."
```

## Explainer

Feynman diagrams are not merely illustrations -- they are a precise computational tool. Each diagram corresponds to a specific term in the perturbative expansion of a scattering amplitude, and the **Feynman rules** translate the diagram into a mathematical expression that can be evaluated. The rules are derived rigorously from Wick's theorem and the interaction Lagrangian, but once derived, they can be applied mechanically without re-deriving them each time.

The rules for any theory are: (1) draw all topologically distinct diagrams with the correct external particles at the desired order in the coupling constant; (2) for each external line, write the appropriate wave function factor (spinor, polarization vector, or 1 for scalars); (3) for each internal line, write the propagator for that field type; (4) for each vertex, write the vertex factor derived from the interaction Lagrangian; (5) impose four-momentum conservation at each vertex; (6) integrate over each undetermined internal momentum with d^4p/(2pi)^4; (7) include a factor of (-1) for each closed fermion loop; (8) divide by the symmetry factor of the diagram.

The **symmetry factor** accounts for the fact that different contractions in Wick's theorem can produce the same diagram. If a diagram has S internal symmetries (permutations of internal lines and vertices that leave the topology unchanged), the amplitude must be divided by S to avoid overcounting. For simple diagrams the symmetry factor is 1, but loops with identical propagators or vertices with multiple identical fields can have larger symmetry factors.

The organizing principle is the coupling constant. In QED, each vertex contributes a factor of e (the electron charge), and each loop introduces an additional power of alpha = e^2/(4pi) approximately 1/137. Tree-level diagrams (no loops) give the leading contribution. One-loop diagrams are suppressed by alpha, two-loop diagrams by alpha^2, and so on. This is why perturbation theory converges rapidly for QED -- higher-order corrections are systematically smaller. The same structure applies to any weakly coupled theory, though for strongly coupled theories (like QCD at low energies), the perturbative expansion breaks down and non-perturbative methods are needed.
