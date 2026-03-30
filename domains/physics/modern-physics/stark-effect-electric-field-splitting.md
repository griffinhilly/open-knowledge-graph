---
id: stark-effect-electric-field-splitting
title: 'Stark Effect: Energy Level Splitting in Electric Fields'
domain: physics
course: modern-physics
prerequisites:
- id: zeeman-effect-magnetic-splitting
  type: soft
- id: hydrogen-atom-schrodinger-solution
  type: soft
- id: franck-hertz-discrete-energy-levels
  type: soft
tags:
- electric-field
- energy-levels
- atomic-physics
stage: expert
status: validated
---
# Stark Effect: Energy Level Splitting in Electric Fields

## Core Idea
An external electric field E induces an electric dipole moment in atoms and shifts energy levels by ΔE ∝ E (linear Stark effect, rare) or ΔE ∝ E² (quadratic Stark effect, more common). The effect arises from mixing of nearby levels by the field. In hydrogen's 2s and 2p levels, the degeneracy is lifted—the 2s and 2p are split by the field.

## How It's Best Learned
Compare Stark and Zeeman effects: both are perturbations of atomic energy levels. For hydrogen, calculate the perturbation matrix and find the shifted energy levels. Observe Stark shifts spectroscopically.

## Common Misconceptions
Not all atoms show a linear Stark effect (hydrogen is special due to accidental degeneracy). The shift is not always proportional to the applied field (higher-order terms can dominate).

## Questions

```yaml
- question: "A spectroscopy experiment measures the energy shift of the ground state of a helium atom as an external electric field is varied. The shift is found to scale as E² rather than linearly with E. The correct explanation is:"
  type: multiple-choice
  options:
    - "The helium ground state has a permanent electric dipole moment that saturates at high field strengths, producing the E² dependence"
    - "The linear Stark effect is suppressed in helium by spin-orbit coupling, leaving only the quadratic term"
    - "The ground state has no permanent electric dipole moment — the field must first induce one by distorting the electron cloud, and the resulting energy shift is second-order in the field"
    - "The quadratic dependence occurs only in multi-electron atoms; hydrogen would show a linear shift at the same energy level"
  answer: 2
  explanation: "Most atoms in their ground states have spherically symmetric electron distributions and no permanent electric dipole moment. The electric field must first polarize the atom — distort the cloud asymmetrically — before there is a dipole to interact with. This makes the energy shift second-order in E: the induced dipole is proportional to E, and the interaction energy of that dipole with the field is proportional to E again, giving ΔE ∝ E². Option D is wrong: hydrogen's ground state (1s) also shows only a quadratic Stark effect for the same reason — it is the n=2 accidental degeneracy that enables the linear case, not the number of electrons."

- question: "Why does hydrogen exhibit a linear Stark effect for its n=2 energy levels, unlike most atoms at the same level?"
  type: multiple-choice
  options:
    - "Hydrogen's single electron has a permanent dipole moment in the n=2 state due to its elongated orbital shape"
    - "The Bohr radius at n=2 is large enough that the linear approximation holds exactly"
    - "The 2s and 2p levels are accidentally degenerate in hydrogen, so even a tiny electric field perturbation mixes them strongly, producing energy shifts linear in the field"
    - "Linear Stark effect is found in all atoms at n=2 — hydrogen is not special in this respect"
  answer: 2
  explanation: "Accidental degeneracy is the key. In bare hydrogen, the 2s (ℓ=0) and 2p (ℓ=1) states are exactly degenerate — the Schrödinger equation gives them the same energy. The electric field perturbation H′ = eEz connects states with Δℓ = ±1, so it couples 2s directly to 2p. When two levels are degenerate, even an infinitesimal coupling produces a first-order energy shift proportional to the perturbation (and hence to E). The off-diagonal matrix element is nonzero from the start, so the result is ΔE = ±3eEa₀ — linear in E. In non-degenerate atoms, the coupling to nearby levels is small and the quadratic term dominates."

- question: "The quadratic Stark effect in most atoms arises because those atoms have no permanent electric dipole moment in the ground state — the applied field must first induce a dipole by polarizing the electron cloud."
  type: true-false
  answer: true
  explanation: "This is the physical mechanism behind the quadratic case. A spherically symmetric electron cloud has zero net dipole moment. The electric field distorts the cloud, inducing a dipole proportional to E (the proportionality constant is the polarizability). The energy of this induced dipole in the field is -½αE², giving ΔE ∝ E². This two-step process — first create a dipole, then interact with the field — is what makes the shift second-order rather than first-order."

- question: "The linear Stark effect in hydrogen's n=2 states occurs because the 2p orbital has an inherently asymmetric (non-spherical) shape that gives it a permanent electric dipole moment."
  type: true-false
  answer: false
  explanation: "The linear Stark effect in hydrogen's n=2 level does not arise from a permanent dipole of the 2p orbital. Individual energy eigenstates (2s, 2p with definite m_ℓ) are parity eigenstates and have zero expectation value of the dipole operator. The linear effect arises because the 2s and 2p states are accidentally degenerate, allowing the electric field to mix them into new eigenstates — superpositions that are not parity eigenstates. These mixed states have non-zero dipole moments and energies that shift linearly with E. The mechanism is level mixing, not intrinsic asymmetry."

- question: "Why do most atoms show only a quadratic Stark effect, while hydrogen shows a linear effect in its n=2 states? What physical mechanism enables the linear case?"
  type: short-answer
  answer: "Most atoms show a quadratic Stark effect because they have no permanent electric dipole moment: their ground states are spherically symmetric, so the field must first induce a dipole (proportional to E), and the resulting energy shift is second-order in E. The linear Stark effect in hydrogen's n=2 states arises from accidental degeneracy: the 2s (ℓ=0) and 2p (ℓ=1) states have identical energies in bare hydrogen. The electric field perturbation couples these degenerate states (since H′ = eEz connects states with Δℓ = ±1). Degenerate perturbation theory then gives energy shifts that are first-order in the perturbation — linear in E. The mixed eigenstates are superpositions of 2s and 2p with electron densities shifted toward or away from the positive electrode."
  explanation: "The contrast is between first-order and second-order perturbation theory. When levels are degenerate, the perturbation matrix must be diagonalized at first order — the energy shift is proportional to the off-diagonal matrix element, hence linear in E. When levels are non-degenerate, the first-order shift vanishes (for states with definite parity) and the leading correction is second-order, going as E²."
```

## Explainer

The Stark effect is the electric analogue of the Zeeman effect you've already encountered. Where a magnetic field couples to the magnetic dipole moment of an electron, an electric field couples to the electric dipole moment. The key difference is that most atoms in their ground state don't have a permanent electric dipole moment — the electron cloud is spherically symmetric. So the field first has to *create* a dipole by distorting the cloud, and the energy shift is proportional to E² (the **quadratic Stark effect**). This is the normal case for most atoms and for most levels of hydrogen.

Hydrogen in its first excited state is special because the 2s and 2p levels are **accidentally degenerate** — they share the same energy at the level of the Schrödinger equation for bare hydrogen. When two levels are degenerate, even a tiny perturbation can mix them strongly. The electric field perturbation operator is H′ = eEz, which connects states that differ by Δℓ = ±1. This couples the 2s (ℓ = 0) state directly to the 2p (ℓ = 1) states; the perturbation matrix has off-diagonal elements proportional to E. Diagonalizing it yields energy eigenvalues that are *linear* in the field: ΔE = ±3eEa₀, where a₀ is the Bohr radius. This is the **linear Stark effect** — the exception enabled by accidental degeneracy.

The physical picture is intuitive: the field polarizes the atom, creating a dipole oriented along the field direction. The two mixed eigenstates correspond to electron distributions shifted toward or away from the positive electrode — one state is stabilized and the other destabilized. The spectral lines that were degenerate split into distinct components, and the splitting grows linearly with field strength rather than quadratically.

More generally, the Stark effect is one of the most direct experimental probes of atomic structure. The magnitude of the quadratic shift measures the **polarizability** of the atom — how easily its charge distribution deforms in a field — which is directly tied to the matrix elements of the dipole operator between the ground and excited states. Measuring Stark shifts spectroscopically therefore yields detailed quantitative information about the geometry and scale of the electron cloud that complements what you can extract from the zero-field spectrum alone.
