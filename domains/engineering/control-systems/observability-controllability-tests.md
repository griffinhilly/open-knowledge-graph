---
id: observability-controllability-tests
title: Tests for Controllability and Observability
domain: engineering
course: control-systems
prerequisites:
- id: state-transformation-similarity-transform
  type: hard
- id: matrix-operations
  type: soft
builds-toward:
- pole-placement-observer-design
tags:
- controllability
- observability
- rank-test
- gramian
stage: expert
status: validated
---

# Tests for Controllability and Observability

## Core Idea
Controllability matrix Qc = [B AB A²B ... A^(n-1)B] has full rank iff system is controllable (all states reachable). Observability matrix Qo = [C; CA; ... CA^(n-1)]ᵀ has full rank iff system is observable (all states detectable). Loss of controllability/observability creates hidden modes that cannot be controlled or observed, limiting achievable performance.

## Questions

```yaml
- question: "A 4th-order system (n=4) has a controllability matrix Qc with rank 3. What can you conclude?"
  type: multiple-choice
  options:
    - "The system is controllable — rank 3 out of 4 is close enough for practical purposes"
    - "There is a 1-dimensional subspace of state space that the input can never reach, regardless of the control signal applied"
    - "The system has one unstable pole that the controller cannot stabilize"
    - "The system's transfer function has a pole-zero cancellation that reduces its effective order to 3"
  answer: 1
  explanation: "Controllability requires Qc to have full rank (rank = n = 4). A rank of 3 means the columns of Qc span only a 3-dimensional subspace of the 4-dimensional state space. There exists a direction in state space that no input can push the state toward — no matter how the control signal is chosen, the state can never reach that direction from the origin. Option A is wrong: rank deficiency is binary in its consequences, not a matter of degree. Option C is a different issue (stability without controllability). Option D is partially related (pole-zero cancellations can cause uncontrollability) but is not the direct conclusion from the rank test."

- question: "A system is fully controllable but its observability matrix Qo has rank less than n. What is the consequence for observer and feedback design?"
  type: multiple-choice
  options:
    - "No consequence — controllability is sufficient for full feedback design, observability only matters for open-loop systems"
    - "You can design a state-feedback controller, but you cannot build an observer to estimate unmeasurable states — some state components are indistinguishable from the output"
    - "The system will be unstable regardless of the feedback gain chosen"
    - "The transfer function from input to output will be unstable"
  answer: 1
  explanation: "Controllability and observability are independent properties. A system can be controllable (all states reachable via input) without being observable (all states detectable from output). If Qo is rank-deficient, there exist distinct initial state vectors x₁(0) ≠ x₂(0) that produce identical output trajectories y(t). No measurement can distinguish them — the observer is blind to those state components. You can still design state feedback if you have full state access, but you cannot build a Luenberger observer (or Kalman filter) to reconstruct the unmeasurable states. Option A is wrong because modern control design (LQG, observer-based feedback) requires both properties."

- question: "If a system's controllability matrix has full rank, the system is also guaranteed to be observable."
  type: true-false
  answer: false
  explanation: "Controllability and observability are dual but entirely independent structural properties. A system can have any combination: controllable and observable, controllable but not observable, observable but not controllable, or neither. Controllability depends on the pair (A, B) — whether the input matrix B, through powers of A, can reach all of state space. Observability depends on the pair (A, C) — whether the output matrix C, through powers of A, can distinguish all initial states. Changing B (adding or removing actuators) affects controllability but not observability, and vice versa for changing C. There is no implication between the two rank conditions."

- question: "An unstable hidden mode — a mode that is neither controllable nor observable — cannot be stabilized by any feedback controller that uses the system's existing inputs and outputs."
  type: true-false
  answer: true
  explanation: "A hidden mode appears in neither the input-to-state reachable subspace nor the state-to-output observable subspace. This means no control signal can affect it (uncontrollable) and no measurement reveals its behavior (unobservable). A controller can only affect modes it can reach and observe; a hidden mode evolves freely under the autonomous dynamics ẋ = Ax. If this mode is unstable (the corresponding eigenvalue has positive real part), it will diverge without any possibility of correction. Kalman decomposition makes this explicit: the transfer function only reflects the controllable-and-observable subsystem, so an unstable hidden mode is completely invisible in the transfer function yet physically present and growing. The only remedies are hardware changes: adding actuators to make it controllable, or adding sensors to make it observable."

- question: "What is a 'hidden mode' in a linear system, and why is an unstable hidden mode especially dangerous from a control engineering perspective?"
  type: short-answer
  answer: "A hidden mode is an eigenmode of the system matrix A that is neither controllable (the input cannot excite it) nor observable (the output cannot reveal it). It corresponds to a subspace of state space that is decoupled from both the input and the output. In Kalman decomposition, the transfer function from input to output only captures modes that are both controllable and observable — hidden modes do not appear in the transfer function at all. An unstable hidden mode is especially dangerous because its divergence is invisible: the output looks well-behaved while the state is growing unboundedly. A controller acting only on the outputs sees no problem to correct, and even if it applies input, the input cannot reach the uncontrollable hidden mode. The system can catastrophically fail internally while appearing stable from the input-output perspective."
  explanation: "This is why rank tests are the first step in control design — not an optional mathematical formality. Discovering an unstable hidden mode after designing a controller means the controller is fundamentally flawed in a way that cannot be patched without redesigning the physical system (changing sensor or actuator placement)."
```

## Explainer

The state-space model ẋ = Ax + Bu, y = Cx captures everything a system can do — but not everything the system *allows you to do with it*. Two fundamental questions arise before you attempt any controller or observer design: can you actually steer the system to arbitrary states using the input, and can you actually infer what the states are from the output? Controllability and observability answer these questions, and the matrix rank tests give you a definitive yes/no without any simulation or trial-and-error.

**Controllability** asks: starting from any initial state, can the input u(t) drive the system to any desired state in finite time? The **controllability matrix** Qc = [B | AB | A²B | ... | A^(n-1)B] stacks together B and all the products of A with B up to n-1 times. Each column of B represents the directions in state space that the input can directly push the state in one step. Multiplying by A gives the directions reachable after one step of system dynamics plus one more input step. Building up through A^(n-1)B captures the accumulating influence of the input over n steps. The Cayley-Hamilton theorem guarantees that nothing new is added beyond n-1 powers — any further influence is a linear combination of what's already in Qc. If these columns span all of ℝⁿ (full rank = n), the input can reach every direction; if they don't (rank deficient), there's a subspace of states the input can never reach, no matter how cleverly u(t) is chosen.

**Observability** is the dual question: given that you can only measure y(t) = Cx(t), can you reconstruct the initial state x(0)? The **observability matrix** Qo = [C; CA; CA²; ...; CA^(n-1)] is built by stacking C with all the products of C with A. The first row block C tells you what combinations of states directly appear in the output. The row CA tells you what combinations appear in the output one step later (after the dynamics have propagated the state forward). Building up through CA^(n-1) captures how the output reflects state information over n time steps. If these row blocks span all of ℝⁿ (full rank), every component of the state eventually shows up in the output in some distinguishable way — you can invert the relationship and deduce x(0). If rank is deficient, there exist distinct initial conditions that produce identical output trajectories — no measurement can tell them apart.

The consequence of uncontrollable or unobservable modes is directly practical. A state similarity transform (which you've studied) can convert any linear system into **Kalman decomposition form**, revealing which state components are controllable, observable, both, or neither. The only transfer function visible from input to output corresponds to modes that are **both** controllable and observable — the rest are **hidden modes**. If a hidden mode is unstable, the system will diverge internally even if the output and input look well-behaved; no controller or observer can fix this without redesigning the hardware (changing B or C). This is why checking these rank tests is always the first step before pole placement, LQR design, or Luenberger observer design — if the rank condition fails, the design methods will either fail numerically or produce a controller that silently leaves dangerous hidden dynamics untouched.
