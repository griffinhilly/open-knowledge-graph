---
id: dirac-equation
title: The Dirac Equation
domain: physics
course: quantum-mechanics
prerequisites:
- id: relativistic-quantum-mechanics
  type: hard
- id: pauli-matrices
  type: hard
tags:
- dirac-equation
- relativistic
- spinors
stage: expert
status: validated
---

# The Dirac Equation

## Core Idea
The Dirac equation (iγᵘ∂ᵤψ − mψ = 0) is the relativistic wave equation for spin-½ fermions. It predicts the electron's g-factor and positrons. Solutions are 4-component spinors; spin-½ comes out of the equation's first-order matrix structure rather than being put in by hand.

## How It's Best Learned
Build the Dirac-representation gamma matrices from Pauli matrices in 2×2 blocks and check {γᵘ, γᵛ} = 2ηᵘᵛ by direct multiplication. Next, apply (iγᵘ∂ᵤ + m) to the equation and show that every component obeys the Klein-Gordon equation. Then solve for a particle at rest, where the four solutions separate cleanly into two positive-energy and two negative-energy spinors.

## Common Misconceptions
- The four components stand for four spin directions. (They hold two spin states each for the positive-energy and negative-energy solutions; spin-½ still has only two projections along any axis.)
- Because ψ has four components, it transforms like a spacetime four-vector. (ψ is a spinor and transforms under the spinor representation of the Lorentz group, which differs from the four-vector rule.)
- There is one correct set of gamma matrices. (Any set satisfying the anticommutation relations works; the Dirac and Weyl representations are related by a change of basis and give the same physics.)
- The negative-energy solutions can be thrown away as unphysical. (They are needed for a complete set of solutions and were reinterpreted as antiparticle states.)

## Questions

```yaml
- question: "Why does the Dirac equation require 4-component spinors, while the non-relativistic Pauli theory uses only 2-component spinors?"
  type: multiple-choice
  options:
    - "Four components are needed to represent spin states in a four-dimensional spacetime"
    - "The algebraic requirement for Lorentz-covariant anticommutation relations cannot be satisfied by 2×2 matrices; the minimum is 4×4, which forces the wave function to have 4 components"
    - "Four components are required by the Pauli exclusion principle for pairs of fermions"
    - "The extra two components represent spin projections along two additional orthogonal spatial axes"
  answer: 1
  explanation: "Dirac needed matrices α_i and β satisfying anticommutation relations to write the energy-momentum relation as a first-order linear operator. These relations cannot be satisfied by 2×2 matrices — the minimum matrix size is 4×4. Once a first-order equation is demanded, 4×4 matrices are not a choice; they are forced by the anticommutation algebra. The 4-component spinor is therefore not an assumption about the electron but a mathematical consequence of the equation's requirements."

- question: "A student says: 'The Dirac equation assumes electrons have spin-½ in order to reproduce the experimental value.' What does this miss about Dirac's achievement?"
  type: multiple-choice
  options:
    - "Nothing — the Dirac equation is indeed constructed with spin-½ as an input assumption"
    - "Spin-½ is not an input but an output: demanding a Lorentz-covariant equation that is first-order in time and space forces anticommuting 4×4 matrices and 4-component spinors, and spin-½ structure emerges automatically"
    - "The student is only wrong about chronology — spin-½ was observed after Dirac, not before"
    - "The Dirac equation actually predicts spin-1 particles, not spin-½"
  answer: 1
  explanation: "Within Dirac's equation, spin-½ is not assumed: it emerges from the matrix algebra that a first-order equation requires. The Pauli theory adds spin by hand as a two-component structure; the Dirac equation derives it. Relativity alone does not force spin-½, though: the Klein-Gordon equation (spin 0) and the Proca equation (spin 1) are also relativistic. What produces spin-½ is Dirac's demand for an equation first-order in time and space. The four components split into spin-up/spin-down particle and antiparticle states as a consequence of the equation's structure, not as an input."

- question: "The Dirac equation predicted the existence of the positron before it was experimentally discovered, as a direct consequence of the equation's negative-energy solutions."
  type: true-false
  answer: true
  explanation: "Dirac published the equation in 1928; Carl Anderson discovered the positron in 1932. The negative-energy solutions, initially troubling, were reinterpreted as antiparticles. This made the positron one of the first particles predicted theoretically before experimental confirmation. The prediction that every charged fermion has an antiparticle with opposite charge follows directly from the structure of the Dirac equation and has since been confirmed for every known charged fermion."

- question: "The Klein-Gordon equation solved most of the problems of relativistic quantum mechanics before Dirac, making the Dirac equation redundant."
  type: true-false
  answer: false
  explanation: "The Klein-Gordon equation is Lorentz-invariant (unlike the Schrödinger equation), but it has two critical failures: it admits negative-energy solutions, and its probability density is not positive-definite — it can be negative, which is physically meaningless for a probability. Dirac's first-order approach was designed to cure the second problem, giving a positive-definite probability density. It did not remove negative-energy solutions; the Dirac equation has them too, and they were later reinterpreted as antiparticles. The Klein-Gordon equation correctly describes spin-0 particles but was not an adequate equation for the electron."

- question: "What was Dirac's key mathematical insight in constructing his equation, and why did it force spin to emerge as a consequence rather than an assumption?"
  type: short-answer
  answer: "Dirac required an equation first-order in both time and space, so that the continuity equation would automatically yield a positive-definite probability density. To factorize the relativistic energy-momentum relation E² = p²c² + m²c⁴ as a linear operator, he needed matrices satisfying specific anticommutation relations. These cannot be satisfied by 2×2 matrices — the minimum is 4×4. Introducing 4×4 gamma matrices forces the wave function to be a 4-component spinor, whose components naturally split into spin-up/spin-down particle and antiparticle states. Spin-½ was not assumed; it was the unavoidable algebraic consequence of Lorentz-covariant first-order structure."
  explanation: "The contrast with the Pauli theory is instructive. Pauli added spin by augmenting the Schrödinger equation with 2×2 matrices — an ad hoc addition. Dirac showed that once you impose Lorentz invariance and demand a first-order equation, spin structure is forced on you. This is why the result is considered one of the deepest in theoretical physics: a fundamental property of the electron follows from the first-order requirement rather than from experimental input. Relativity alone does not fix spin, though: the Klein-Gordon (spin 0) and Proca (spin 1) equations are relativistic too."
```

## Explainer

You know the Schrödinger equation and how Pauli matrices represent spin-½ as two-component spinors. The problem Dirac faced was that the Schrödinger equation is not Lorentz-invariant: it is first-order in time but second-order in space, treating time and space asymmetrically. The **Klein-Gordon equation** (∂²ψ/∂t² = ∇²ψ − m²ψ) fixes this by being second-order in both time and space, but it admits negative-energy solutions and a probability density that is not positive-definite — problems that cannot be patched without a fundamentally different approach.

Dirac's insight was to demand an equation that is *first-order in both time and space*, so that the continuity equation automatically gives a positive-definite probability density. To write E = √(p²c² + m²c⁴) as a first-order operator, he needed to "take the square root" of the operator p²c² + m²c⁴ algebraically. He needed matrices α_i and β satisfying anticommutation relations {α_i, α_j} = 2δᵢⱼ and {α_i, β} = 0. Here your knowledge of Pauli matrices becomes essential: these relations cannot be satisfied by 2×2 matrices alone — the minimum size is 4×4. The **gamma matrices** γᵘ are built from Pauli matrices in block form (the Dirac or Weyl representation being two common choices).

The consequence of needing 4×4 matrices is that the wave function must be a **4-component spinor** ψ — this is not an assumption but is forced by the anticommutation algebra. The four components split naturally: two correspond to spin-up and spin-down states of the particle, and two to spin-up and spin-down states of the *antiparticle*. Most remarkably, **spin-½ emerges automatically** from the equation's structure — it is not added by hand as in the non-relativistic Pauli theory. Relativity alone does not force spin-½, though: the Klein-Gordon equation (spin 0) and the Proca equation (spin 1) are also relativistic. Spin-½ follows from Dirac's demand for an equation first-order in time and space.

The Dirac equation made two spectacular predictions at the time of its discovery. First, the **electron's magnetic moment**: the Schrödinger–Pauli theory puts in g = 2 by hand; the Dirac equation *derives* g = 2 from first principles, with no free parameters. (The small deviation g − 2, the electron's anomalous magnetic moment, comes from quantum electrodynamics.) Second, the negative-energy solutions — initially troubling — were reinterpreted as **antiparticles**. Dirac published the equation in 1928 and predicted the anti-electron in 1931, before the positron's experimental discovery in 1932. The original "Dirac sea" picture (negative-energy states are all filled, a hole is a positron) has since been superseded by quantum field theory, where positrons are excitations of the electron field; but the core prediction — that every charged fermion has an antiparticle with opposite charge — follows directly from the structure of the equation and has been confirmed for every known charged fermion.
