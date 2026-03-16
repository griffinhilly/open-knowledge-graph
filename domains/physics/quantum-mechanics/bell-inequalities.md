---
id: bell-inequalities
title: Bell Inequalities and Their Violation
domain: physics
course: quantum-mechanics
prerequisites:
- id: bell-theorem
  type: hard
tags:
- bell-inequalities
- quantum-nonlocality
stage: abstract-reasoning
status: draft
---

# Bell Inequalities and Their Violation

## Core Idea
CHSH inequality: |⟨AB⟩ + ⟨AB'⟩ + ⟨A'B⟩ − ⟨A'B'⟩| ≤ 2 in local hidden-variable theories. Quantum mechanics allows ≤ 2√2 for entangled states.

## Explainer

Bell's theorem, which you have already studied, establishes that no local hidden-variable (LHV) theory can reproduce all predictions of quantum mechanics. But a theorem is only as strong as what you can test. The **Bell inequalities** — and in particular the **CHSH inequality** (named for Clauser, Horne, Shimony, and Holt) — translate Bell's abstract argument into a precise, experimentally measurable bound. They give you a number: if nature obeys local realism, certain correlation measurements must stay within a hard limit. Quantum mechanics predicts that entangled states can violate that limit. Experiments have confirmed the violation. The inequalities are the instrument that turned a philosophical debate into a laboratory result.

To understand the CHSH inequality, imagine two distant parties, Alice and Bob, each receiving one particle from an entangled pair. Alice can choose between two measurement settings, call them A and A′, each returning outcome ±1. Bob can choose between B and B′, also returning ±1. They repeat the experiment many times and compute the four correlation values ⟨AB⟩, ⟨AB′⟩, ⟨A′B⟩, and ⟨A′B′⟩ — each is the average of the product of their outcomes when that pair of settings is used. In any local hidden-variable theory, each particle carries pre-determined instructions for how to respond to each measurement. A simple algebraic argument (the CHSH derivation) then shows that the combination |⟨AB⟩ + ⟨AB′⟩ + ⟨A′B⟩ − ⟨A′B′⟩| cannot exceed 2. This is the **CHSH bound** for classical local realism.

Quantum mechanics breaks through this bound. For two qubits in a maximally entangled (singlet) state and optimally chosen measurement angles, quantum theory predicts the combination reaches 2√2 ≈ 2.83 — the **Tsirelson bound**, which is the maximum any quantum state can achieve. The reason is that quantum correlations are not carried by hidden variables pre-assigned at emission; they arise from the entangled state itself, which does not factor into independent particle states. When Alice measures, her outcome is genuinely random — but it is **correlated** with Bob's outcome in a way that cannot be explained by any shared classical information. The correlations are "spookier" than any classical mechanism can produce.

Experiments by Aspect (1982), and more recently loophole-free experiments by groups in Delft, Vienna, and NIST (2015), have measured CHSH values above 2 with high statistical confidence, closing detector and locality loopholes simultaneously. These results rule out all local hidden-variable theories as complete descriptions of nature. What they do *not* do is require a particular interpretation of quantum mechanics — they are silent on whether collapse is real, whether many-worlds is correct, or what the wavefunction "is." But they firmly establish that if a deeper theory underlies quantum mechanics, it cannot be both local and deterministic in the classical sense. The CHSH inequality is the quantitative scar left by Bell's theorem on the surface of experimental physics.
