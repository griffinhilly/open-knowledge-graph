---
id: probability-amplitude-interpretation
title: Probability Amplitude and Born Interpretation
domain: physics
course: modern-physics
prerequisites:
- id: wavefunctions-boundary-conditions
  type: hard
- id: quantum-postulates
  type: soft
builds-toward:
- quantum-operators-eigenvalues
- measurement-problem-quantum
tags:
- quantum-interpretation
- probability
stage: advanced
status: validated
---

# Probability Amplitude and Born Interpretation

## Core Idea
The wavefunction ψ itself is not directly observable; the Born rule states that |ψ(r,t)|² is the probability density for finding the particle at position r at time t. Integration of |ψ|² over a region gives the probability of finding the particle there—wavefunctions are probability amplitudes. The complex phase of ψ carries physical information (interference, coherence) even though |ψ|² alone determines single-particle probabilities.

## Questions

```yaml
- question: "Two electrons pass through a double slit one at a time. An interference pattern builds up over many electrons. This result is best explained by:"
  type: multiple-choice
  options:
    - "Each electron passes through one definite slit, but we don't know which — the pattern reflects our ignorance"
    - "Electrons repel each other, creating alternating zones of high and low electron density on the screen"
    - "Each electron's wavefunction passes through both slits, and the two probability amplitudes interfere — constructively at bright bands, destructively at dark bands"
    - "The Born rule assigns higher probability to positions near the center, producing the central bright fringe"
  answer: 2
  explanation: "Interference requires superposition of amplitudes, not particles. Each single electron passes through both slits as a quantum superposition ψ = ψ₁ + ψ₂, and the probability density is |ψ₁ + ψ₂|² = |ψ₁|² + |ψ₂|² + 2Re(ψ₁*ψ₂). The last interference term can be positive or negative depending on the relative phase of the two amplitudes, creating bright and dark bands. Option A is the classical interpretation — it predicts no interference pattern, because if each electron went through one slit, there would be no amplitude from the other slit to interfere with. The actual interference pattern rules out option A."

- question: "A student writes ψ(x) = C·e^(−x²) as a proposed wavefunction. Before computing any probabilities from it, they must first:"
  type: multiple-choice
  options:
    - "Verify that ψ is real-valued, since complex wavefunctions cannot represent physically realizable particles"
    - "Confirm that ψ satisfies the time-independent Schrödinger equation everywhere"
    - "Choose C so that ∫|ψ(x)|² dx = 1, ensuring the total probability of finding the particle somewhere equals 1"
    - "Check that ψ(0) = 1 at the most probable position"
  answer: 2
  explanation: "The Born rule gives probabilities from |ψ|², but for these to be genuine probabilities they must sum (integrate) to 1. This normalization condition ∫|ψ|² dx = 1 constrains which functions can represent physical quantum states. For ψ = Ce^(−x²), integrating |ψ|² = C²e^(−2x²) gives C²√(π/2), so C = (2/π)^(1/4). Without normalization, |ψ|² gives a probability density that doesn't integrate to 1 — the output of any probability calculation would be meaningless."

- question: "The complex phase of the wavefunction is physically meaningful in quantum mechanics even though it cannot be directly observed, because it determines interference patterns when amplitudes are superposed."
  type: true-false
  answer: true
  explanation: "For a single wavefunction in isolation, the global phase is unobservable — |e^(iθ)ψ|² = |ψ|². But relative phase between two amplitudes matters crucially. When ψ = ψ₁ + ψ₂, |ψ|² = |ψ₁|² + |ψ₂|² + 2Re(ψ₁*ψ₂). The interference term 2Re(ψ₁*ψ₂) depends on the relative phase of ψ₁ and ψ₂: if they are in phase (relative phase 0), it adds; if out of phase (relative phase π), it cancels. Change the phase of ψ₁ relative to ψ₂ and the entire interference pattern shifts. Phase is physically real even though a single amplitude's absolute phase is not."

- question: "In quantum mechanics, the Born rule's probability distribution describes our ignorance about a particle's definite but unknown position — the particle is somewhere specific before measurement, and measurement merely reveals it."
  type: true-false
  answer: false
  explanation: "This is the classical interpretation of probability, which quantum mechanics rejects. In quantum mechanics, the wavefunction is the complete description of the particle's state — there is no 'hidden' definite position that measurement reveals. Before measurement, the particle does not have a definite position. The Born rule gives the probability distribution for what position will be found upon measurement, but that outcome is not pre-determined — it is genuinely random in a way that has no classical analogue. This irreducible probabilism (not ignorance about a definite state) is what distinguishes quantum probability from classical statistical mechanics."

- question: "Why does the complex phase of the wavefunction matter physically, even though |ψ|² — not ψ — gives the measurable probability density?"
  type: short-answer
  answer: "The phase matters because quantum states can be superposed: when two amplitudes are added, the probability density of the combined state is |ψ₁ + ψ₂|², which contains the interference term 2Re(ψ₁*ψ₂). This term depends on the relative phase between ψ₁ and ψ₂ and can be constructive (adding) or destructive (canceling). A change in relative phase changes the entire interference pattern, even though |ψ₁|² and |ψ₂|² individually are unchanged. The phase encodes which-way information and coherence — it is the reason quantum mechanics can produce phenomena (like the double-slit pattern) that have no classical explanation in terms of particles with definite trajectories."
  explanation: "If quantum states were just probability distributions with no phase, superposition would just be probabilistic mixture, and there would be no interference. The complex structure of the wavefunction is precisely what distinguishes quantum superposition from classical uncertainty."
```

## Explainer

From studying wavefunctions and boundary conditions you know that quantum states are described by complex-valued functions ψ(r,t) that satisfy the Schrödinger equation. But what does ψ *mean*? The equation produces solutions that are complex numbers — they cannot be directly measured. Max Born's 1926 proposal provided the answer now called the **Born rule**: |ψ(r,t)|² gives the **probability density** for finding the particle at position r at time t. To find the probability of locating the particle within a small volume element dV, you compute |ψ|² dV. The wavefunction ψ itself is called a **probability amplitude** — a complex number whose squared magnitude gives a probability.

The Born rule immediately imposes a constraint: since the particle must be somewhere, integrating |ψ|² over all space must equal 1. This **normalization condition** ∫|ψ(r,t)|² d³r = 1 restricts which functions can represent physical quantum states. Not all solutions to the Schrödinger equation are acceptable — a function that diverges at infinity or is not square-integrable cannot be normalized and therefore cannot represent a physically realizable particle. This is precisely the condition that forced quantization of energy in the hydrogen atom: only certain discrete wavefunctions are normalizable.

The complex nature of ψ might seem to make its phase irrelevant, since |ψ|² = ψ*ψ discards phase information. But this is only true for a *single* wavefunction in isolation. When two amplitudes are *added* — as happens in superposition — their phases profoundly affect the result. If ψ = ψ₁ + ψ₂, then |ψ|² = |ψ₁|² + |ψ₂|² + 2Re(ψ₁*ψ₂). The last term is the **interference term**: it can be positive (constructive) or negative (destructive) depending on the relative phase of ψ₁ and ψ₂. This is why electrons passing through a double slit form an interference pattern — each electron traverses both slits as a superposition, and the two amplitudes interfere. If you tried to describe electrons as classical probability-carrying particles, no interference would be possible.

The Born interpretation forces a radical departure from classical intuition. In classical mechanics, probability describes our *ignorance* of a definite state — the electron is definitely somewhere, and the probability just reflects our uncertainty. In quantum mechanics, the Born rule makes a stronger claim: before measurement, the electron does not have a definite position. The wavefunction is the complete description of the particle's state, not a summary of our ignorance about some underlying definite trajectory. The act of measurement projects the particle to a definite position, and after that the wavefunction "collapses" — but the distribution of outcomes over many measurements is given by |ψ|². This irreducible probabilism, which Born recognized immediately, is what so disturbed Einstein and motivates ongoing debate about the interpretation of quantum mechanics.
