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

## Explainer

You already understand eventual consistency: if updates stop arriving, all replicas will *eventually* converge to the same state. And from causal consistency, you know how to ensure that causally related operations are seen in the right order. **Strong eventual consistency** (SEC) addresses a gap that neither of these guarantees fills: what happens when two replicas have received exactly the same set of updates, but in different orders? Under plain eventual consistency, there is no guarantee they will agree — they might need additional reconciliation, manual conflict resolution, or even rollback. SEC closes this gap with a stronger promise: same updates in, same state out, regardless of delivery order.

The key insight is that SEC is not about *when* replicas converge but about *whether* they converge deterministically. Consider two replicas of a shared document. User A inserts "hello" at position 5, while User B simultaneously inserts "world" at position 5. Replica 1 sees A's edit first, then B's. Replica 2 sees them in the opposite order. Under eventual consistency, these replicas might end up with "helloworld" and "worldhello" respectively — technically they received the same updates, but the result depends on ordering. SEC requires that both replicas reach the *same* final state, which means the system must have a deterministic rule for resolving this conflict that produces the same answer regardless of which order the operations arrive.

This is where **conflict-free replicated data types** (CRDTs) enter the picture. CRDTs are data structures whose operations are designed to be commutative (order doesn't matter), associative (grouping doesn't matter), and idempotent (applying the same update twice has no additional effect). A simple example is a **grow-only counter**: each node maintains its own counter, and the merged state is the sum of all counters. No matter what order you receive the individual increments, the sum is the same. More sophisticated CRDTs handle sets (add/remove), registers (last-writer-wins with timestamps), and even text editing (using techniques from the operational transformation family). The mathematical properties of these data structures *guarantee* convergence, removing the need for consensus protocols or central coordination.

The practical significance of SEC is that it enables systems that are both highly available and convergent. Under the CAP theorem, you learned that during a network partition you must choose between consistency and availability. SEC-based systems choose availability — every replica can accept writes during a partition — while still guaranteeing that once the partition heals and updates propagate, all replicas will automatically converge to an identical state without human intervention. This makes SEC the foundation for collaborative editing tools, distributed caches, and eventually consistent databases that need stronger guarantees than "it'll probably work out."
