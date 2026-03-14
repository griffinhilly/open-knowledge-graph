---
id: crdts-convergent-replicated-types
title: 'CRDTs: Conflict-Free Replicated Data Types'
domain: computer-science
course: distributed-systems
prerequisites:
- id: eventual-consistency
  type: hard
- id: causal-consistency
  type: soft
tags:
- crdts
- replicated-data-types
- eventual-consistency
stage: advanced
status: draft
---

# CRDTs: Conflict-Free Replicated Data Types

## Core Idea
CRDTs are data structures that converge automatically without coordination: replicas update independently and the merge operation is commutative and idempotent, guaranteeing convergence to the same state. Examples include counters, sets, and sequences. CRDTs enable offline-first applications and peer-to-peer systems where strong consistency is infeasible.
