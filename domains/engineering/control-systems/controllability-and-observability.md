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
status: draft
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
