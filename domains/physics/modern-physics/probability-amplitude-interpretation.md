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
status: draft
---

# Probability Amplitude and Born Interpretation

## Core Idea
The wavefunction ψ itself is not directly observable; the Born rule states that |ψ(r,t)|² is the probability density for finding the particle at position r at time t. Integration of |ψ|² over a region gives the probability of finding the particle there—wavefunctions are probability amplitudes. The complex phase of ψ carries physical information (interference, coherence) even though |ψ|² alone determines single-particle probabilities.

## Explainer

From studying wavefunctions and boundary conditions you know that quantum states are described by complex-valued functions ψ(r,t) that satisfy the Schrödinger equation. But what does ψ *mean*? The equation produces solutions that are complex numbers — they cannot be directly measured. Max Born's 1926 proposal provided the answer now called the **Born rule**: |ψ(r,t)|² gives the **probability density** for finding the particle at position r at time t. To find the probability of locating the particle within a small volume element dV, you compute |ψ|² dV. The wavefunction ψ itself is called a **probability amplitude** — a complex number whose squared magnitude gives a probability.

The Born rule immediately imposes a constraint: since the particle must be somewhere, integrating |ψ|² over all space must equal 1. This **normalization condition** ∫|ψ(r,t)|² d³r = 1 restricts which functions can represent physical quantum states. Not all solutions to the Schrödinger equation are acceptable — a function that diverges at infinity or is not square-integrable cannot be normalized and therefore cannot represent a physically realizable particle. This is precisely the condition that forced quantization of energy in the hydrogen atom: only certain discrete wavefunctions are normalizable.

The complex nature of ψ might seem to make its phase irrelevant, since |ψ|² = ψ*ψ discards phase information. But this is only true for a *single* wavefunction in isolation. When two amplitudes are *added* — as happens in superposition — their phases profoundly affect the result. If ψ = ψ₁ + ψ₂, then |ψ|² = |ψ₁|² + |ψ₂|² + 2Re(ψ₁*ψ₂). The last term is the **interference term**: it can be positive (constructive) or negative (destructive) depending on the relative phase of ψ₁ and ψ₂. This is why electrons passing through a double slit form an interference pattern — each electron traverses both slits as a superposition, and the two amplitudes interfere. If you tried to describe electrons as classical probability-carrying particles, no interference would be possible.

The Born interpretation forces a radical departure from classical intuition. In classical mechanics, probability describes our *ignorance* of a definite state — the electron is definitely somewhere, and the probability just reflects our uncertainty. In quantum mechanics, the Born rule makes a stronger claim: before measurement, the electron does not have a definite position. The wavefunction is the complete description of the particle's state, not a summary of our ignorance about some underlying definite trajectory. The act of measurement projects the particle to a definite position, and after that the wavefunction "collapses" — but the distribution of outcomes over many measurements is given by |ψ|². This irreducible probabilism, which Born recognized immediately, is what so disturbed Einstein and motivates ongoing debate about the interpretation of quantum mechanics.
