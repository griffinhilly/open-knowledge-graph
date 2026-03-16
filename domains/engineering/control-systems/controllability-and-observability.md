---
id: controllability-and-observability
title: Controllability and Observability
domain: engineering
course: control-systems
prerequisites:
- id: state-space-representation-control
  type: hard
- id: linear-independence
  type: hard
- id: matrix-operations
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
- id: rank-and-nullity-theorem
  type: soft
- id: state-transition-matrix
  type: soft
builds-toward:
- state-feedback-pole-placement
- luenberger-observer
tags:
- controllability
- observability
- Kalman-rank
- PBH-test
- structural-properties
stage: advanced
status: validated
---
# Controllability and Observability

## Core Idea
Controllability determines whether any initial state can be driven to any final state in finite time using the input. The Kalman rank condition states that system (A, B) is controllable if and only if the controllability matrix C = [B AB A²B ⋯ Aⁿ⁻¹B] has full row rank n. Observability determines whether the initial state can be uniquely inferred from the output history; system (A, C) is observable if and only if O = [C; CA; CA²; ⋯; CAⁿ⁻¹] has full column rank n. These properties are dual to each other and can also be tested via the PBH eigenvector test. Controllability is a prerequisite for arbitrary pole placement; observability is required for state estimation.

## How It's Best Learned
Construct controllability and observability matrices for 2nd and 3rd order systems and check rank numerically. Practice the PBH test as an alternative verification. Show that changing actuator or sensor location can destroy these properties on the same plant.

## Common Misconceptions
- An uncontrollable mode is not necessarily unstable — it simply cannot be influenced by the input. An uncontrollable unstable mode is the dangerous case that cannot be stabilized by feedback.
- Controllability and observability depend on the placement of actuators and sensors (B and C matrices), not only on the plant dynamics (A matrix).
- The rank of the controllability matrix can be misleading near the threshold for numerically ill-conditioned systems; condition number analysis provides more reliable insight.

## Explainer

In state-space representation, the system dynamics are encoded in two objects: the **A matrix** (how states evolve autonomously) and the **B matrix** (how inputs influence states). A reasonable assumption might be that since we can pick any input signal, we have complete freedom to push the system anywhere. But this is wrong — certain state variables may be completely hidden from the input, forming "decoupled modes" that evolve independently no matter what we do. **Controllability** is the formal test for whether this problem exists.

The **Kalman controllability matrix** 𝒞 = [B, AB, A²B, …, Aⁿ⁻¹B] stacks together all the directions in state space that the input can reach, directly or after 1, 2, up to n−1 steps of propagation through the dynamics. If these columns span all of ℝⁿ — i.e., the matrix has full row rank n — then you can steer the state to any point in finite time using the right input sequence. If the rank is less than n, there exists at least one state-space direction that the input cannot affect, no matter how cleverly you design the control law. The matrix runs up to Aⁿ⁻¹B rather than longer because the Cayley-Hamilton theorem guarantees that Aⁿ and higher powers of A can be expressed as combinations of I, A, …, Aⁿ⁻¹, so no new directions appear beyond n−1 multiplications.

**Observability** asks the dual question: given the output history y(t) from an unknown initial state, can you uniquely deduce what x(0) was? The **observability matrix** 𝒪 = [C; CA; CA²; …; CAⁿ⁻¹]ᵀ stacks the output maps after 0, 1, …, n−1 time steps. Full column rank means every distinct initial state produces a distinct output trajectory — they are distinguishable. A rank deficiency means two different initial states produce identical outputs forever, so no observer can tell them apart. The duality is exact: system (A, B) is controllable if and only if (Aᵀ, Bᵀ) is observable. This means any test or design method for one property can be mechanically translated to the other by transposing.

The practical stakes are high. **Pole placement** — assigning closed-loop eigenvalues via state feedback u = −Kx — requires full controllability. If a mode is uncontrollable, no choice of K can move its eigenvalue; if that mode is also unstable, the system cannot be stabilized by feedback at all. Conversely, building a **state observer** (estimating x from y) requires full observability: unobservable modes cannot be estimated because they leave no trace in the output. An uncontrollable but stable mode is benign — it decays on its own. An unobservable but stable mode is also manageable — it cannot be estimated but it also doesn't grow. The dangerous pathological case is an **uncontrollable unstable mode** (cannot be moved by input) or an **unobservable unstable mode** (grows invisibly in the output without being detected). Good design practice is to verify both properties early, because they depend on actuator and sensor *placement* — not just the dynamics — and a poor placement choice can be impossible to overcome by clever algorithm design.
