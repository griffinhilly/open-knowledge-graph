---
id: strong-eventual-consistency
title: Strong Eventual Consistency
domain: computer-science
course: distributed-systems
prerequisites:
- id: eventual-consistency
  type: hard
- id: causal-consistency
  type: hard
builds-toward:
- crdts-convergent-replicated-types
tags:
- consistency
- eventual-consistency
- convergence
stage: advanced
status: draft
---

# Strong Eventual Consistency

## Core Idea
Strong eventual consistency (SEC) strengthens eventual consistency by requiring that if all nodes have received the same set of updates (regardless of order), they converge to an identical state. This prevents pathological cases where nodes permanently diverge. SEC is achieved through deterministic conflict resolution (CRDTs) or commutative operations.
