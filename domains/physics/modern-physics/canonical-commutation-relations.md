---
id: canonical-commutation-relations
title: Canonical Commutation Relations and Uncertainty
domain: physics
course: modern-physics
prerequisites:
- id: quantum-operators-observables
  type: hard
- id: commutation-relations
  type: hard
builds-toward:
- uncertainty-principle-derivation
tags:
- quantum
- commutation
- operators
stage: advanced
status: draft
---

# Canonical Commutation Relations and Uncertainty

## Core Idea
The canonical commutation relation [x̂,p̂] = iℏ states that position and momentum operators do not commute. This non-commutativity reflects the fundamental structure of quantum mechanics and directly implies that position and momentum cannot be simultaneously diagonalized (measured with arbitrary precision).

## Questions

```yaml
- question: "An experimenter argues: 'The Heisenberg uncertainty principle just means our measuring devices disturb particles. A sufficiently gentle measurement could in principle determine both position and momentum precisely.' What is fundamentally wrong with this claim?"
  type: multiple-choice
  options:
    - "Nothing — the uncertainty principle is indeed about measurement disturbance"
    - "The principle only applies to subatomic particles, not macroscopic measuring devices"
    - "The principle reflects that no quantum state can simultaneously have definite position and definite momentum — it is not about measurement clumsiness"
    - "The principle only applies when the particle is not in an energy eigenstate"
  answer: 2
  explanation: "The Heisenberg uncertainty principle ΔxΔp ≥ ℏ/2 is a statement about the spread of outcomes in repeated measurements on identically prepared systems — it is a property of quantum *states*, not of measurement technology. A state that is a sharp position eigenstate (Dirac delta in position space) must be a superposition of all momentum eigenstates with equal amplitude — it literally has no definite momentum to be 'disturbed.' No matter how gentle the measurement, you cannot extract precise momentum information that isn't there. The 'disturbance' picture is a popular but incorrect gloss; the principle was rigorously established by Kennard (1927) as a statement about state preparation."

- question: "Which mathematical property of the relation [x̂, p̂] = iℏ directly implies that position and momentum cannot be simultaneously measured with arbitrary precision?"
  type: multiple-choice
  options:
    - "That iℏ is imaginary, which means their eigenvalues cannot both be real"
    - "That the commutator is nonzero, meaning x̂ and p̂ cannot be simultaneously diagonalized in the same basis"
    - "That ℏ is very small, so the uncertainty is negligible for macroscopic objects"
    - "That p̂ contains a derivative operator, making it unbounded and unphysical"
  answer: 1
  explanation: "Two Hermitian operators share a complete set of simultaneous eigenstates — and can therefore be simultaneously measured with precision — if and only if their commutator is zero. Since [x̂,p̂] = iℏ ≠ 0, they cannot be simultaneously diagonalized. Any position eigenstate spreads across infinitely many momentum eigenstates, and vice versa. The smallness of ℏ (option C) determines the *size* of the minimum uncertainty product but does not affect whether simultaneous precision is possible in principle. Option A is wrong because Hermitian operators always have real eigenvalues regardless of whether i appears in their commutator."

- question: "The canonical commutation relation [x̂, p̂] = iℏ can be verified in the position representation by showing that applying x̂ then p̂ differs from applying p̂ then x̂ by a term equal to iℏ times the wavefunction — an extra term that emerges from the product rule of differentiation."
  type: true-false
  answer: true
  explanation: "With x̂ψ = xψ and p̂ψ = (ℏ/i)∂ψ/∂x, computing [x̂,p̂]ψ = x̂(p̂ψ) − p̂(x̂ψ) = x·(ℏ/i)∂ψ/∂x − (ℏ/i)∂(xψ)/∂x. Applying the product rule to the second term: ∂(xψ)/∂x = ψ + x∂ψ/∂x. Substituting: x·(ℏ/i)∂ψ/∂x − (ℏ/i)(ψ + x∂ψ/∂x) = −(ℏ/i)ψ = iℏψ. The extra ψ term is precisely the product rule contribution, and it equals iℏψ for any ψ, confirming [x̂,p̂] = iℏ as an operator identity."

- question: "The Heisenberg uncertainty principle is violated by classical objects like a baseball, which simultaneously have a definite position and a definite momentum."
  type: true-false
  answer: false
  explanation: "Classical objects do not violate the uncertainty principle — they trivially satisfy it. For a 0.1 kg baseball, even a position uncertainty of 10⁻³⁰ m (far below any measurable scale, far smaller than an atomic nucleus) gives a momentum uncertainty of only ~10⁻⁵ kg·m/s via ΔxΔp ≥ ℏ/2 ≈ 5.3×10⁻³⁵ J·s. The principle holds for all physical objects; it just has no detectable consequence at macroscopic scales because ℏ is so tiny. Quantum mechanics does not break down for classical objects — it reduces to classical behavior in the appropriate limit."

- question: "Explain why the canonical commutation relation [x̂, p̂] = iℏ is considered the defining postulate that distinguishes quantum mechanics from classical mechanics, and what would follow if the commutator were zero instead."
  type: short-answer
  answer: "In classical mechanics, position and momentum are ordinary numbers (not operators), and their product always commutes: xp = px. The canonical commutation relation [x̂,p̂] = iℏ ≠ 0 is the precise mathematical statement that position and momentum are incompatible observables in quantum theory — their operators do not share eigenstates, so no quantum state can have simultaneously definite values for both. If [x̂,p̂] = 0, the uncertainty principle ΔxΔp ≥ ℏ/2 would collapse to ΔxΔp ≥ 0 — trivially satisfied — and position and momentum could be simultaneously sharp. Wavefunctions would be unnecessary; particles could have definite trajectories; and the theory would reduce to classical mechanics. The nonzero commutator is what forces the probabilistic structure of quantum mechanics and the wave-particle duality it entails."
```

## Explainer

From your study of quantum operators and observables, you learned that physical quantities in quantum mechanics are represented by **operators** acting on wavefunctions, and that measurements correspond to eigenvalues of these operators. You also learned about **commutators**: the commutator [Â,B̂] = ÂB̂ − B̂Â measures how much the order of applying two operators matters. For classical variables, multiplication commutes: position times momentum equals momentum times position, always. In quantum mechanics this is not the case, and the deviation from commutativity is not a technicality — it is the heart of the theory.

The **canonical commutation relation** [x̂, p̂] = iℏ is the defining postulate that distinguishes quantum mechanics from classical mechanics. To see what it means concretely, work in the position representation where x̂ acts by multiplying by x and p̂ acts by (ℏ/i)∂/∂x. Apply [x̂, p̂] to an arbitrary wavefunction ψ(x): x̂(p̂ψ) − p̂(x̂ψ) = x·(ℏ/i)∂ψ/∂x − (ℏ/i)∂(xψ)/∂x = x·(ℏ/i)∂ψ/∂x − (ℏ/i)[ψ + x∂ψ/∂x] = −(ℏ/i)ψ = iℏψ. So [x̂, p̂]ψ = iℏψ for any ψ, confirming the relation. The extra term ψ comes from the product rule — differentiation knows about x in a way that simple multiplication does not. This is why position and momentum are fundamentally incompatible observables.

The consequence is the **Heisenberg uncertainty principle**: ΔxΔp ≥ ℏ/2. This follows from a general theorem: if two Hermitian operators A and B have commutator [A,B] = iC, then ΔAΔ B ≥ |⟨C⟩|/2. The canonical commutation relation [x̂,p̂] = iℏ gives C = ℏ (a constant), so ΔxΔp ≥ ℏ/2 regardless of the state. This is not a statement about measurement disturbance (a common misconception) — it is a statement about the spread of outcomes in repeated measurements on identically prepared systems. A state with perfectly definite position (a Dirac delta in position space) has completely indefinite momentum — it would be a superposition of all momentum eigenstates with equal amplitude. Nature does not allow sharp simultaneous position and momentum, not because our measuring devices are clumsy, but because position and momentum eigenstates are mutually exclusive bases.

The canonical commutation relations generalize across quantum mechanics. For each generalized coordinate qᵢ and its conjugate momentum pⱼ, [q̂ᵢ, p̂ⱼ] = iℏδᵢⱼ, while coordinates commute with each other and momenta commute with each other. This canonical structure, inherited from the Poisson bracket structure of Hamiltonian classical mechanics (where {q,p} = 1 becomes [q̂,p̂] = iℏ), is the bridge between classical and quantum theory. The same commutation algebra underlies angular momentum quantization, bosonic field quantization, and the ladder operator approach to the harmonic oscillator — the algebraic backbone of all of quantum mechanics.
