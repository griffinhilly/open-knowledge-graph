---
id: expectation-values
title: Expectation Values and Averages
domain: physics
course: quantum-mechanics
prerequisites:
- id: operators-and-observables
  type: hard
- id: born-rule-and-measurement
  type: hard
builds-toward:
- variational-method
- time-independent-perturbation-theory
tags:
- observables
- averages
stage: advanced
status: draft
---

# Expectation Values and Averages

## Core Idea
The expectation value ⟨A⟩ = ⟨ψ|A|ψ⟩ gives the average result of measuring observable A. Higher moments characterize the full probability distribution. Expectation values connect quantum mechanics to classical observables.

## Explainer

You already know from the Born rule that measuring observable A on state |ψ⟩ yields eigenvalue aₙ with probability |⟨φₙ|ψ⟩|², where {|φₙ⟩} are the eigenstates of the operator Â. The **expectation value** ⟨A⟩ is simply the statistical average over all possible measurement outcomes: ⟨A⟩ = Σ aₙ |⟨φₙ|ψ⟩|². It answers the question: if you prepare many identical copies of |ψ⟩ and measure A on each one, what is the mean of your results? It does not tell you what any single measurement will give — only the long-run average.

The compact formula ⟨A⟩ = ⟨ψ|Â|ψ⟩ packages this average elegantly. For position, it becomes ⟨x⟩ = ∫ ψ*(x) · x · ψ(x) dx, which is just the probability-density-weighted average of position — a continuous version of E[X] from probability theory. For momentum, the operator is Âₚ = −iℏ ∂/∂x, so ⟨p⟩ = ∫ ψ*(x) (−iℏ ∂ψ/∂x) dx. The operator acts on the ket before the inner product is evaluated; the order matters whenever the operator involves derivatives. For an eigenstate |φₙ⟩ with eigenvalue aₙ, the expectation value is simply aₙ — no surprise, since every measurement returns the same value.

**Higher moments** extend this: ⟨A²⟩ = ⟨ψ|Â²|ψ⟩ gives the mean-square value, and the **variance** is ⟨(ΔA)²⟩ = ⟨A²⟩ − ⟨A⟩². The standard deviation ΔA = √⟨(ΔA)²⟩ is the **uncertainty** in observable A, the quantity that appears in the Heisenberg uncertainty principle: ΔxΔp ≥ ℏ/2. An eigenstate of A has zero variance in A (ΔA = 0), while a superposition of different eigenstates has nonzero uncertainty. The uncertainty is not a measurement imprecision — it is a property of the state itself.

The deepest connection is to classical mechanics via **Ehrenfest's theorem**: d⟨x⟩/dt = ⟨p⟩/m and d⟨p⟩/dt = −⟨∂V/∂x⟩. The expectation values of position and momentum obey Newton's second law, but with the force evaluated as an expectation value of the gradient of the potential. When the wavepacket is narrow enough that ∂V/∂x is approximately constant across it, the quantum equations reduce to the classical equations of motion. This is why macroscopic objects follow classical trajectories even though they are quantum mechanically: their wavefunctions are so sharply peaked that expectation values track the classical path precisely.
