---
id: wicks-theorem
title: Wick's Theorem
domain: physics
course: quantum-field-theory
prerequisites:
- id: propagators-greens-functions
  type: hard
- id: fock-space-particle-interpretation
  type: hard
tags:
- wick-theorem
- normal-ordering
- contractions
stage: expert
status: validated
---

# Wick's Theorem

## Core Idea
Wick's theorem expresses a time-ordered product of field operators as a sum of normal-ordered products with all possible contractions. Each contraction equals a Feynman propagator. This theorem is the bridge between the abstract operator formalism and the practical Feynman diagram rules.

## Questions

```yaml
- question: "Wick's theorem states that T{phi(x1)phi(x2)...phi(xn)} equals the sum of all possible ways to contract pairs of fields, with each contraction replaced by a propagator. What does a 'fully contracted' term correspond to physically?"
  type: multiple-choice
  options:
    - "A term where all fields are contracted into propagator pairs — this gives a vacuum-to-vacuum amplitude (vacuum bubble) with no external particles"
    - "A term with the maximum number of vertices"
    - "A term that vanishes due to normal ordering"
    - "A term representing the classical field configuration"
  answer: 0
  explanation: "In a fully contracted term, every field operator is paired with another in a propagator. Since normal-ordered operators give zero when sandwiched between vacuum states, only fully contracted terms survive in vacuum expectation values. In scattering amplitude calculations, some fields are contracted with external states (representing incoming and outgoing particles) and the remaining internal contractions form the propagators of internal lines. Fully contracted terms with no external fields are vacuum bubbles — they contribute to the vacuum energy but cancel in physical S-matrix elements."

- question: "Normal ordering places all creation operators to the left of all annihilation operators. Why does this ensure that <0|:phi(x1)...phi(xn):|0> = 0 for n >= 1?"
  type: multiple-choice
  options:
    - "Because creation operators acting to the left on <0| give zero"
    - "Because annihilation operators acting to the right on |0> give zero — and in a normal-ordered product, there is always at least one annihilation operator on the right"
    - "Because the vacuum state is normalized to zero"
    - "Because normal-ordered products are always Hermitian"
  answer: 1
  explanation: "In a normal-ordered product, all annihilation operators stand to the right. When such a product acts on the vacuum |0>, the rightmost annihilation operator immediately gives zero (a_p|0> = 0), so the entire expression vanishes. Similarly, creation operators on the far left act to the left on <0|, but in a vacuum expectation value the key is that annihilation on the right kills |0>. This is precisely why Wick's theorem is useful: the normal-ordered pieces vanish in vacuum expectation values, and only the contraction terms (propagators) survive."

- question: "For four field operators, Wick's theorem gives T{phi_1 phi_2 phi_3 phi_4} = :phi_1 phi_2 phi_3 phi_4: + (sum of single contractions times normal-ordered pairs) + (sum of double contractions). The number of fully contracted (double contraction) terms is three."
  type: true-false
  answer: true
  explanation: "With four fields, the possible complete pairings are: (12)(34), (13)(24), and (14)(23), where (ij) denotes the contraction of phi_i with phi_j. Each contraction gives a Feynman propagator D_F(x_i - x_j). There are 4!/(2^2 * 2!) = 3 ways to pair four objects into two pairs, which matches. For a vacuum expectation value of the time-ordered product, only these three fully contracted terms survive, since the normal-ordered terms vanish between vacuum states."

- question: "Explain why Wick's theorem is essential for deriving Feynman diagram rules from the operator formalism of QFT."
  type: short-answer
  answer: "The S-matrix for scattering processes is expressed as a time-ordered exponential of the interaction Hamiltonian, which involves products of field operators. Computing these matrix elements directly in the operator formalism is impractical for anything beyond the simplest cases. Wick's theorem systematically converts these time-ordered products into sums of Feynman propagators (contractions) multiplied by normal-ordered remainders. For vacuum expectation values, only fully contracted terms survive. Each contraction pattern maps directly to a Feynman diagram: external contractions are external lines, internal contractions are propagators, and the vertices come from the interaction. Wick's theorem therefore provides the rigorous derivation of the Feynman rules from first principles."
  explanation: "Without Wick's theorem, you would have to evaluate operator products by commuting creation and annihilation operators through each other — a combinatorial nightmare. Wick's theorem organizes this into a systematic enumeration of contraction patterns, each of which is a Feynman diagram drawn according to fixed rules. The theorem is what makes perturbation theory practical."
```

## Explainer

When computing scattering amplitudes in quantum field theory, you encounter time-ordered products of many field operators -- for instance, <0|T{phi(x1) phi(x2) phi(x3) phi(x4)}|0> in a phi^4 theory. Evaluating this directly would require commuting operators through each other, tracking the ordering, and handling the combinatorics of which creation operators pair with which annihilation operators. **Wick's theorem** reduces this to a systematic bookkeeping exercise.

The theorem states that any time-ordered product can be written as a sum over all possible **contractions**. A contraction of two fields is defined as the difference between the time-ordered and normal-ordered product: phi(x) phi(y) (contracted) = T{phi(x)phi(y)} - :phi(x)phi(y): = D_F(x - y), which is exactly the Feynman propagator. Wick's theorem says: T{phi_1 phi_2 ... phi_n} = :phi_1 phi_2 ... phi_n: + (all terms with one contraction) + (all terms with two contractions) + ... + (all fully contracted terms). Each contraction replaces a pair of fields with the propagator D_F and removes those fields from the normal-ordered product.

The power of the theorem becomes clear when you take vacuum expectation values. Since <0|:anything:|0> = 0, only **fully contracted terms survive**. For the four-point function <0|T{phi_1 phi_2 phi_3 phi_4}|0> of a free field, only the three complete pairings contribute: D_F(x1-x2)D_F(x3-x4) + D_F(x1-x3)D_F(x2-x4) + D_F(x1-x4)D_F(x2-x3). Each term is a product of two propagators, and each corresponds to a Feynman diagram with two internal lines connecting four points in different patterns.

When interactions are present, the S-matrix expansion generates time-ordered products with additional field operators from the interaction vertices. Wick's theorem applied to these products produces all possible Feynman diagrams at a given order of perturbation theory. The contraction rules translate directly into Feynman rules: each contraction is an internal propagator, the uncontracted fields connect to external states, and each vertex contributes a coupling constant factor. This is how the intuitive picture of particles exchanging virtual quanta is rigorously derived from the quantum field theory formalism.
