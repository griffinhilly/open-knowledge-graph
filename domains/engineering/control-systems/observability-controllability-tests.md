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
stage: advanced
status: draft
---

# Tests for Controllability and Observability

## Core Idea
Controllability matrix Qc = [B AB A²B ... A^(n-1)B] has full rank iff system is controllable (all states reachable). Observability matrix Qo = [C; CA; ... CA^(n-1)]ᵀ has full rank iff system is observable (all states detectable). Loss of controllability/observability creates hidden modes that cannot be controlled or observed, limiting achievable performance.

## Explainer

The state-space model ẋ = Ax + Bu, y = Cx captures everything a system can do — but not everything the system *allows you to do with it*. Two fundamental questions arise before you attempt any controller or observer design: can you actually steer the system to arbitrary states using the input, and can you actually infer what the states are from the output? Controllability and observability answer these questions, and the matrix rank tests give you a definitive yes/no without any simulation or trial-and-error.

**Controllability** asks: starting from any initial state, can the input u(t) drive the system to any desired state in finite time? The **controllability matrix** Qc = [B | AB | A²B | ... | A^(n-1)B] stacks together B and all the products of A with B up to n-1 times. Each column of B represents the directions in state space that the input can directly push the state in one step. Multiplying by A gives the directions reachable after one step of system dynamics plus one more input step. Building up through A^(n-1)B captures the accumulating influence of the input over n steps. The Cayley-Hamilton theorem guarantees that nothing new is added beyond n-1 powers — any further influence is a linear combination of what's already in Qc. If these columns span all of ℝⁿ (full rank = n), the input can reach every direction; if they don't (rank deficient), there's a subspace of states the input can never reach, no matter how cleverly u(t) is chosen.

**Observability** is the dual question: given that you can only measure y(t) = Cx(t), can you reconstruct the initial state x(0)? The **observability matrix** Qo = [C; CA; CA²; ...; CA^(n-1)] is built by stacking C with all the products of C with A. The first row block C tells you what combinations of states directly appear in the output. The row CA tells you what combinations appear in the output one step later (after the dynamics have propagated the state forward). Building up through CA^(n-1) captures how the output reflects state information over n time steps. If these row blocks span all of ℝⁿ (full rank), every component of the state eventually shows up in the output in some distinguishable way — you can invert the relationship and deduce x(0). If rank is deficient, there exist distinct initial conditions that produce identical output trajectories — no measurement can tell them apart.

The consequence of uncontrollable or unobservable modes is directly practical. A state similarity transform (which you've studied) can convert any linear system into **Kalman decomposition form**, revealing which state components are controllable, observable, both, or neither. The only transfer function visible from input to output corresponds to modes that are **both** controllable and observable — the rest are **hidden modes**. If a hidden mode is unstable, the system will diverge internally even if the output and input look well-behaved; no controller or observer can fix this without redesigning the hardware (changing B or C). This is why checking these rank tests is always the first step before pole placement, LQR design, or Luenberger observer design — if the rank condition fails, the design methods will either fail numerically or produce a controller that silently leaves dangerous hidden dynamics untouched.
