---
id: uncertainty-principle-canonical
title: Canonical Uncertainty Relations
domain: physics
course: quantum-mechanics
prerequisites:
- id: commutation-relations
  type: hard
- id: heisenberg-uncertainty-principle
  type: soft
builds-toward:
- quantum-harmonic-oscillator
tags:
- uncertainty
- commutation
- limits
stage: advanced
status: validated
---

# Canonical Uncertainty Relations

## Core Idea
For any two observables with commutator [Â, B̂], the uncertainty product satisfies ΔA ΔB ≥ |⟨[Â, B̂]⟩|/2. The canonical relation ΔxΔp ≥ ℏ/2 shows position and momentum cannot both be arbitrarily precise. These relations are fundamental constraints on what can be simultaneously known about a quantum system.

## Questions

```yaml
- question: "A student argues: 'The uncertainty principle says that measuring a particle's position very precisely disturbs its momentum — the measurement kicks the particle and randomizes its momentum.' This account of the Kennard inequality Δx Δp ≥ ℏ/2 is:"
  type: multiple-choice
  options:
    - "Correct — measurement disturbance is the source of the position-momentum uncertainty"
    - "Partially correct — disturbance explains most cases, but there are some exceptions"
    - "Misleading — the inequality holds for the quantum state itself before any measurement occurs, as a consequence of the Fourier transform relationship between position and momentum representations"
    - "Correct for electrons but not for photons"
  answer: 2
  explanation: "The Kennard inequality Δx Δp ≥ ℏ/2 is a theorem about quantum states, not about measurement procedures. A Gaussian wave packet sitting undisturbed in free space already satisfies it — no measurement has occurred. The uncertainty is a property of the wave function: a narrow (localized) wave packet requires a broad superposition of momentum eigenstates (a wide spread in p-space), by the mathematics of Fourier transforms. Measurement disturbance is a real and separate phenomenon, but it is not the source of the canonical uncertainty relations."

- question: "A Gaussian wave packet is prepared with minimum uncertainty Δx · Δp = ℏ/2. Which statement correctly describes this state?"
  type: multiple-choice
  options:
    - "Both Δx and Δp are zero — the state is as classical as possible"
    - "This is the minimum uncertainty state; narrowing Δx further would require increasing Δp to compensate"
    - "The uncertainty principle is violated at the minimum — this state is quantum mechanically impossible"
    - "The uncertainties are only defined after a measurement is performed on the state"
  answer: 1
  explanation: "Δx · Δp = ℏ/2 is the *minimum* allowed by the Robertson relation — achieved by Gaussian (coherent) states. It is a perfectly valid quantum state, the most 'classical-like' in the sense of simultaneously minimizing both uncertainties. Narrowing the spatial width (decreasing Δx) necessarily broadens the momentum distribution (increasing Δp) to keep the product ≥ ℏ/2. The uncertainties are properties of the state, not of measurements — they are defined as standard deviations over an ensemble of identical preparations."

- question: "The Robertson uncertainty relation ΔA ΔB ≥ ½|⟨[Â, B̂]⟩| is a mathematical theorem proven from the Cauchy-Schwarz inequality applied to Hilbert space vectors, not an empirical generalization."
  type: true-false
  answer: true
  explanation: "The derivation is purely mathematical: define two vectors |u⟩ = (Â − ⟨Â⟩)|ψ⟩ and |v⟩ = (B̂ − ⟨B̂⟩)|ψ⟩, apply the Cauchy-Schwarz inequality ‖u‖·‖v‖ ≥ |⟨u|v⟩|, and separate the result into real and imaginary parts. The imaginary part gives ½|⟨[Â, B̂]⟩|. No experiment is needed; the bound follows from the algebra of Hilbert space and the definition of standard deviation. It holds exactly, not approximately."

- question: "Two observables that commute ([Â, B̂] = 0) cannot both be measured precisely in the same quantum state — there will typically be some uncertainty in at least one of them."
  type: true-false
  answer: false
  explanation: "If [Â, B̂] = 0, the Robertson bound is ΔA · ΔB ≥ 0, which imposes no constraint. Commuting operators share a complete set of simultaneous eigenstates. If the system is in a simultaneous eigenstate of both, then ΔA = ΔB = 0 — both can be measured with perfect precision. Non-zero uncertainty for commuting observables is a property of specific states, not a universal constraint. The canonical uncertainty between position and momentum is irreducible precisely because [x̂, p̂] = iℏ ≠ 0."

- question: "Why is a spatially narrow (highly localized) wave packet necessarily associated with a broad spread of momenta?"
  type: short-answer
  answer: "Because position-space and momentum-space wave functions are related by the Fourier transform. A spatially narrow wave packet ψ(x) is a sharp spike in x-space, and its Fourier transform φ(p) — the momentum-space wave function — must be broad to reproduce that spike. This is a mathematical fact about Fourier transforms: narrow functions and their transforms cannot both be narrow simultaneously. The standard deviation of |ψ(x)|² (which is Δx) and the standard deviation of |φ(p)|² (which is Δp) satisfy Δx · Δp ≥ ℏ/2 as a consequence of this Fourier relationship."
  explanation: "This is the deepest way to see why the uncertainty principle holds: it is the quantum expression of a universal mathematical constraint on conjugate Fourier pairs. The same relationship appears in signal processing — a time-limited signal cannot also be frequency-limited. In quantum mechanics, position and momentum are conjugate Fourier variables, so the constraint is not a mysterious quantum weirdness but a consequence of representing the state as a wave."
```

## Explainer

From commutation relations, you know that two operators commute ([Â, B̂] = 0) if and only if they can be simultaneously diagonalized — that is, they share a complete set of eigenstates, and a state can simultaneously have definite values for both observables. Non-commuting operators cannot share eigenstates, so no quantum state can have simultaneously definite values for both. The canonical uncertainty relations translate this algebraic fact into a quantitative bound on *how much* indefiniteness is required.

The **Robertson uncertainty relation** states: for any two observables Â and B̂ in any state |ψ⟩, the product of their standard deviations satisfies ΔA · ΔB ≥ ½|⟨[Â, B̂]⟩|. This is not an approximation or a statement about measurement clumsiness — it is a theorem, proven by applying the Cauchy-Schwarz inequality to two vectors in Hilbert space. For position and momentum, [x̂, p̂] = iℏ, so ⟨[x̂, p̂]⟩ = iℏ in any state, giving the universal bound Δx · Δp ≥ ℏ/2. The bound is state-independent for this pair: no quantum state, no matter how cleverly prepared, can violate it. The minimum Δx · Δp = ℏ/2 is achieved by **Gaussian wave packets** — **coherent states** that are the quantum states most resembling classical particles.

A crucial distinction: ΔA is the standard deviation of outcomes if the same measurement is repeated on many identically prepared copies of the state. It is *not* about a single measurement disturbing the particle. The older "disturbance" picture — a position measurement kicks the momentum — captures some physical intuition but misidentifies the source of uncertainty. The Kennard inequality Δx · Δp ≥ ℏ/2 holds for a Gaussian wave packet *sitting undisturbed in free space*, before any measurement has been made. The uncertainty is a property of the state, not of the measurement procedure. Preparations that reduce Δx necessarily increase Δp, and vice versa, because the Fourier transform relationship between position-space and momentum-space wave functions is a mathematical fact: a narrow spike in x-space requires a broad superposition in p-space.

The Robertson relation is state-dependent in general. For energy eigenstates, ⟨[Ĥ, Â]⟩ = 0 for any observable Â (since energy eigenstates are stationary), so the uncertainty bound vanishes — you can measure compatible observables with arbitrary precision in a stationary state. For angular momentum: [L̂_x, L̂_y] = iℏL̂_z, giving ΔL_x · ΔL_y ≥ ½ℏ|⟨L̂_z⟩|. A state with definite L_z (an eigenstate of L̂_z with ⟨L̂_z⟩ ≠ 0) necessarily has indefinite L_x and L_y. As you move toward the quantum harmonic oscillator, you will see the Robertson relation give a lower bound on the ground-state energy: the zero-point energy ½ℏω is exactly what the uncertainty principle demands of a particle confined to a potential well.
