---
id: time-dependent-perturbation-theory
title: Time-Dependent Perturbation Theory
domain: physics
course: quantum-mechanics
prerequisites:
- id: time-independent-perturbation-theory
  type: hard
- id: differential-equations
  type: hard
builds-toward:
- fermi-golden-rule
tags:
- perturbation-theory
- time-dependent
stage: mathematical-application
status: draft
---

# Time-Dependent Perturbation Theory

## Core Idea
Time-varying perturbations H'(t) cause state evolution; coefficients expand as c_n(t) ≈ c_n⁽⁰⟩ − (i/ℏ) ∫₀ᵗ dt' ⟨n|H'(t')|m⟩ e^{iω_{nm}t'} c_m⁽⁰⟩.
