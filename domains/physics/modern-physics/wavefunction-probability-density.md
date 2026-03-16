---
id: wavefunction-probability-density
title: Wavefunctions and Probability Density Interpretation
domain: physics
course: modern-physics
prerequisites:
- id: electron-diffraction-matter
  type: hard
- id: wave-equation-one-dimensional
  type: hard
builds-toward:
- quantum-superposition-states
tags:
- quantum
- wavefunctions
- probability
stage: abstract-reasoning
status: draft
---

# Wavefunctions and Probability Density Interpretation

## Core Idea
The quantum wavefunction ψ(x,t) describes the state of a particle; its squared magnitude |ψ|² gives the probability density for finding the particle at position x. Born's interpretation: |ψ|² is fundamentally probabilistic, not deterministic. The wavefunction itself is complex-valued and its phase carries quantum information about coherence and interference.

## How It's Best Learned
Examine simple wavefunctions (particle in a box, free particle) and plot |ψ|² to see probability distributions. Calculate probabilities by integrating |ψ|² over regions. Recognize that measuring the particle collapses the wavefunction to a definite state.

## Explainer

You already know from studying electron diffraction that matter behaves like a wave — electrons fired at a double slit produce an interference pattern, not two bright spots. The **wavefunction** ψ(x,t) is the mathematical object that makes this precise. It is a complex-valued function: at every point in space and time, ψ has a magnitude and a phase. The magnitude tells you about probability; the phase carries information about interference and coherence.

The central interpretive rule is **Born's rule**: the probability of finding the particle in a small interval dx around position x is |ψ(x,t)|² dx. The squared magnitude |ψ|² is the **probability density** — it behaves exactly like any probability density you know from statistics. It is always real and non-negative. Its integral over all space must equal 1: ∫|ψ|² dx = 1. This **normalization condition** is not optional — it enforces the certainty that the particle exists somewhere. If you know the 1D wave equation from classical physics, think of ψ as a generalization: it satisfies the Schrödinger equation instead of the classical wave equation, and its amplitude carries probabilistic meaning rather than physical displacement.

The complex nature of ψ is not a technicality to be ignored — it is the source of quantum interference. When two wavefunctions overlap, their amplitudes add first: ψ_total = ψ₁ + ψ₂, and then you square. This gives |ψ₁ + ψ₂|² = |ψ₁|² + |ψ₂|² + 2Re(ψ₁*ψ₂). The cross term — the interference term — can be positive (constructive) or negative (destructive), depending on the relative phase. This is precisely what causes the bright and dark fringes in the electron diffraction pattern you studied. Classical probability distributions cannot produce interference; only wavefunctions can. The phase of ψ is physically real, even though ψ itself is never directly measured.

A particle with a sharply peaked |ψ|² has a well-defined position but uncertain momentum; a particle with a broad, spread-out |ψ|² has uncertain position. When you measure the particle's position, the wavefunction collapses: the broad probability distribution instantly becomes a narrow spike at the observed location. Before measurement, the particle doesn't have a hidden definite position — the probability is all there is. This is the conceptual break from classical physics. The wavefunction is not our ignorance about where the particle "really" is; it is the complete description of the particle's state.
