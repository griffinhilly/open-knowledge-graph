---
id: heisenberg-and-interaction-pictures
title: The Schrödinger, Heisenberg, and Interaction Pictures
domain: physics
course: quantum-mechanics
prerequisites:
- id: schrodinger-equation-time-dependent
  type: hard
- id: commutation-relations
  type: hard
- id: hilbert-space-formalism
  type: hard
- id: expectation-values
  type: soft
- id: quantum-harmonic-oscillator
  type: soft
builds-toward:
- time-dependent-perturbation-theory
- s-matrix-scattering-amplitudes
- klein-gordon-field-quantization
tags:
- time-evolution
- operators
- heisenberg-picture
- interaction-picture
stage: advanced
status: validated
---

# The Schrödinger, Heisenberg, and Interaction Pictures

## Core Idea
Quantum time evolution is carried by the unitary operator U(t) = exp(−iHt/ħ) for a time-independent Hamiltonian. In the Schrödinger picture states evolve as |ψ(t)⟩ = U(t)|ψ(0)⟩ and operators stay fixed; in the Heisenberg picture states stay fixed and operators evolve as A_H(t) = U†AU, obeying dA_H/dt = (i/ħ)[H, A_H]. Both pictures give the same expectation values, so they are equivalent descriptions. The interaction picture splits H = H₀ + V, lets operators evolve with H₀ and states evolve with V alone, and is the starting point for time-dependent perturbation theory and quantum field theory.

## How It's Best Learned
Show that ⟨ψ(t)|A|ψ(t)⟩ equals ⟨ψ(0)|U†AU|ψ(0)⟩, which is the whole idea of the change of picture. Derive the Heisenberg equation of motion and apply it to x and p for a free particle and for the harmonic oscillator; compare with the classical equations. Then introduce the interaction picture for a two-level system with a weak drive. Point out the parallel between [A, H] and the classical Poisson bracket {A, H}.

## Common Misconceptions
- The pictures make different physical predictions. (They differ only in how time dependence is assigned; all probabilities and expectation values agree.)
- In the Heisenberg picture nothing changes with time. (The state vector is fixed, but the operators for observables change, and they carry all the dynamics.)
- The interaction picture is a separate theory with its own Hamiltonian. (It is a bookkeeping choice that removes the known, solvable part H₀ so that the effect of V can be studied by itself.)

## Questions

```yaml
- question: "The Schrödinger and Heisenberg pictures predict the same expectation value for every observable at every time."
  type: true-false
  answer: true
  explanation: "⟨ψ(t)|A|ψ(t)⟩ = ⟨ψ(0)|U†AU|ψ(0)⟩ = ⟨ψ_H|A_H(t)|ψ_H⟩. Moving U from the state to the operator does not change the number."
- question: "An operator A has no explicit time dependence and commutes with the Hamiltonian. What happens to A_H(t) in the Heisenberg picture?"
  type: multiple-choice
  options: ["It grows linearly in time", "It oscillates at frequency H/ħ", "It stays constant, so its expectation value is conserved", "It becomes zero"]
  answer: 2
  explanation: "dA_H/dt = (i/ħ)[H, A_H] = 0. The operator does not change, so A is a constant of the motion."
- question: "For a harmonic oscillator, which is the Heisenberg-picture position operator?"
  type: multiple-choice
  options: ["x_H(t) = x(0) + (p(0)/m)t", "x_H(t) = x(0) cos ωt + (p(0)/mω) sin ωt", "x_H(t) = x(0)e^(−iωt)", "x_H(t) = x(0)"]
  answer: 1
  explanation: "The Heisenberg equations give dx_H/dt = p_H/m and dp_H/dt = −mω²x_H. Their solution has the same form as the classical solution, with operators in place of numbers."
- question: "In the interaction picture with H = H₀ + V, what governs the time evolution of the state vector?"
  type: short-answer
  answer: "The interaction alone, in the form V_I(t) = e^(iH₀t/ħ) V e^(−iH₀t/ħ), through iħ d|ψ_I⟩/dt = V_I(t)|ψ_I⟩."
  explanation: "The free evolution under H₀ is moved onto the operators. If V = 0, the interaction-picture state does not change at all, which makes the effect of V easy to isolate."
```

## Explainer
Everything measurable in quantum mechanics comes from quantities like ⟨ψ|A|ψ⟩ and |⟨φ|ψ⟩|². For a time-independent Hamiltonian, the Schrödinger equation is solved formally by |ψ(t)⟩ = U(t)|ψ(0)⟩ with U(t) = exp(−iHt/ħ). Because U is unitary, U†U = 1. This gives freedom in where to place the time dependence.

In the Schrödinger picture, the usual starting point, the state carries the time dependence and observables such as x and p are fixed operators. But the expectation value can be regrouped:

⟨ψ(t)|A|ψ(t)⟩ = ⟨ψ(0)| U†AU |ψ(0)⟩.

Define A_H(t) = U†(t) A U(t) and keep the state fixed at |ψ(0)⟩. This is the Heisenberg picture. Differentiating A_H gives the Heisenberg equation of motion,

dA_H/dt = (i/ħ)[H, A_H] + (∂A/∂t)_H.

For a particle with H = p²/2m + V(x), the Heisenberg equations are dx_H/dt = p_H/m and dp_H/dt = −V′(x_H). These look like Newton's laws written in operators. Taking expectation values gives Ehrenfest's theorem. For the harmonic oscillator they can be solved exactly: x_H(t) = x(0) cos ωt + (p(0)/mω) sin ωt. Any operator that commutes with H is constant in time, which gives a direct test for conserved quantities. The structure parallels classical mechanics, where df/dt = {f, H}; the commutator divided by iħ takes the place of the Poisson bracket.

Werner Heisenberg's 1925 matrix mechanics was built in this form, with time-dependent matrices for position and momentum. Erwin Schrödinger's wave mechanics of 1926 put the time dependence in the wavefunction. The two were soon shown to be equivalent.

The interaction picture sits between the two. Split the Hamiltonian into a part H₀ that can be solved exactly and a part V that is small or interesting. Let operators evolve with H₀ alone, A_I(t) = e^(iH₀t/ħ) A e^(−iH₀t/ħ), and define |ψ_I(t)⟩ = e^(iH₀t/ħ)|ψ(t)⟩. Then the state obeys

iħ d|ψ_I⟩/dt = V_I(t)|ψ_I⟩.

If V were zero, |ψ_I⟩ would not change, so any change it shows is due to the interaction. Solving this equation by iteration gives the Dyson series, a power series in V. Its first term is ordinary first-order time-dependent perturbation theory. In quantum field theory, the same construction, with free fields evolving under H₀, is the basis for the S-matrix and for Feynman diagrams.
