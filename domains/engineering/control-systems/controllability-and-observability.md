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
- id: rank-nullity-theorem
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
stage: expert
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

## Questions

```yaml
- question: "You test controllability for a 3rd-order system and find rank(𝒞) = 2. Which statement is most accurate?"
  type: multiple-choice
  options:
    - "The system has one unstable mode that feedback cannot fix"
    - "There exists one direction in state space that the input cannot influence, regardless of the control law applied"
    - "The system cannot be stabilized under any circumstances"
    - "The B matrix must be incorrect since rank should equal n for any physical system"
  answer: 1
  explanation: "A rank deficiency of 1 means one direction in state space lies outside the column span of [B, AB, …, Aⁿ⁻¹B]. The input simply has no effect on that mode. This does not by itself mean the system is unstable — an uncontrollable mode that is also stable (negative eigenvalue) will decay on its own. Only an uncontrollable *unstable* mode is catastrophic. Option A conflates uncontrollability with instability, which is a common and consequential error."

- question: "A control engineer moves an actuator to a different location on the plant, keeping the same A matrix but changing B. The controllability matrix rank drops from n to n−1. What is the most precise explanation?"
  type: multiple-choice
  options:
    - "The plant dynamics changed, making one eigenvalue uncontrollable"
    - "One mode of the system is now uncontrollable because B changed, even though A is identical"
    - "The system is now unstable due to the actuator placement"
    - "The PBH test is no longer valid; the Kalman test must be used instead"
  answer: 1
  explanation: "Controllability depends on the pair (A, B), not on A alone. Moving an actuator changes the B matrix — which directions in state space the input directly enters — without altering the plant's intrinsic dynamics (A). A poor placement can make some modes unreachable from the new actuator position. This is exactly why controllability analysis must be re-run whenever sensor or actuator placement changes, not just when the plant dynamics are modified."

- question: "Moving a sensor to a different location on a plant with the same A matrix can change whether the system is observable, even though the plant dynamics are unchanged."
  type: true-false
  answer: true
  explanation: "Observability depends on the pair (A, C), and C encodes sensor placement — it maps the state to the measured output. Changing the sensor location changes C, which changes the observability matrix 𝒪 = [C; CA; …; CAⁿ⁻¹]. A new sensor position may fail to 'see' certain modes, destroying observability even though the plant's A matrix is identical. This is the observability analogue of the controllability dependence on B."

- question: "An uncontrollable mode in a state-space system is generally unstable and is expected to be addressed before feedback can stabilize the system."
  type: true-false
  answer: false
  explanation: "An uncontrollable mode is simply one the input cannot influence — it evolves according to its own eigenvalue regardless of what control is applied. If that eigenvalue has a negative real part (stable mode), the mode decays to zero on its own; it is benign. Only an uncontrollable *unstable* mode (positive real-part eigenvalue) is catastrophic, because it grows and no feedback can move its eigenvalue. The dangerous distinction is uncontrollable-and-unstable, not merely uncontrollable."

- question: "Why does the Kalman controllability matrix stop at Aⁿ⁻¹B rather than including AⁿB and higher powers, and what theorem justifies this?"
  type: short-answer
  answer: "The Cayley-Hamilton theorem states that every matrix satisfies its own characteristic polynomial, so Aⁿ can be expressed as a linear combination of I, A, …, Aⁿ⁻¹. This means AⁿB lies in the column span of [B, AB, …, Aⁿ⁻¹B], adding no new reachable directions. The same applies to all higher powers. Therefore the first n columns of the infinite power series fully characterize the reachable subspace, and rank([B AB … Aⁿ⁻¹B]) is the complete test."
  explanation: "This result is important because it makes the Kalman rank test finite and computable. Without Cayley-Hamilton, you might worry that longer sequences of input-propagation steps could reach new state-space directions — but the theorem guarantees they cannot. The controllability matrix is exactly as wide as it needs to be."
```

## Explainer

In state-space representation, the system dynamics are encoded in two objects: the **A matrix** (how states evolve autonomously) and the **B matrix** (how inputs influence states). A reasonable assumption might be that since we can pick any input signal, we have complete freedom to push the system anywhere. But this is wrong — certain state variables may be completely hidden from the input, forming "decoupled modes" that evolve independently no matter what we do. **Controllability** is the formal test for whether this problem exists.

The **Kalman controllability matrix** 𝒞 = [B, AB, A²B, …, Aⁿ⁻¹B] stacks together all the directions in state space that the input can reach, directly or after 1, 2, up to n−1 steps of propagation through the dynamics. If these columns span all of ℝⁿ — i.e., the matrix has full row rank n — then you can steer the state to any point in finite time using the right input sequence. If the rank is less than n, there exists at least one state-space direction that the input cannot affect, no matter how cleverly you design the control law. The matrix runs up to Aⁿ⁻¹B rather than longer because the Cayley-Hamilton theorem guarantees that Aⁿ and higher powers of A can be expressed as combinations of I, A, …, Aⁿ⁻¹, so no new directions appear beyond n−1 multiplications.

**Observability** asks the dual question: given the output history y(t) from an unknown initial state, can you uniquely deduce what x(0) was? The **observability matrix** 𝒪 = [C; CA; CA²; …; CAⁿ⁻¹]ᵀ stacks the output maps after 0, 1, …, n−1 time steps. Full column rank means every distinct initial state produces a distinct output trajectory — they are distinguishable. A rank deficiency means two different initial states produce identical outputs forever, so no observer can tell them apart. The duality is exact: system (A, B) is controllable if and only if (Aᵀ, Bᵀ) is observable. This means any test or design method for one property can be mechanically translated to the other by transposing.

The practical stakes are high. **Pole placement** — assigning closed-loop eigenvalues via state feedback u = −Kx — requires full controllability. If a mode is uncontrollable, no choice of K can move its eigenvalue; if that mode is also unstable, the system cannot be stabilized by feedback at all. Conversely, building a **state observer** (estimating x from y) requires full observability: unobservable modes cannot be estimated because they leave no trace in the output. An uncontrollable but stable mode is benign — it decays on its own. An unobservable but stable mode is also manageable — it cannot be estimated but it also doesn't grow. The dangerous pathological case is an **uncontrollable unstable mode** (cannot be moved by input) or an **unobservable unstable mode** (grows invisibly in the output without being detected). Good design practice is to verify both properties early, because they depend on actuator and sensor *placement* — not just the dynamics — and a poor placement choice can be impossible to overcome by clever algorithm design.
