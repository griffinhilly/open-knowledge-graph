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

## Explainer

From your study of eventual consistency, you know that replicas in a distributed system can temporarily diverge and must eventually converge to the same state. The hard question is: how do you guarantee convergence without a central coordinator deciding who wins? **CRDTs** (Conflict-Free Replicated Data Types) answer this by building convergence into the data structure itself. The mathematical trick is that the merge operation forms a **join semilattice** — it is commutative (merge(A, B) = merge(B, A)), associative (order of pairwise merges does not matter), and idempotent (merging the same state twice has no effect). These properties mean replicas can receive updates in any order, merge them in any order, and always arrive at the same final state.

The simplest example is a **G-Counter** (grow-only counter). Each of *n* replicas maintains its own counter. To increment, a replica bumps only its own entry. To merge, take the element-wise maximum across all entries. The total count is the sum. Because `max` is commutative and idempotent, all replicas converge regardless of message ordering. A **PN-Counter** extends this to support decrements by pairing two G-Counters — one for increments, one for decrements — and reporting the difference. Sets work similarly: a **G-Set** (grow-only set) merges via union, which is naturally a semilattice operation. An **OR-Set** (observed-remove set) supports both add and remove by tagging each element with a unique identifier so that "add" and "remove" can be distinguished even when they arrive out of order.

The practical value of CRDTs is that they eliminate coordination. In a traditional system, concurrent writes to the same data require either locking (which blocks other replicas and needs network round-trips) or a consensus protocol (which requires a majority of replicas to agree). CRDTs sidestep both: every replica can accept writes locally and immediately, without contacting any other replica. Synchronization happens lazily — replicas exchange state or operations whenever they connect, and the merge function guarantees convergence. This makes CRDTs ideal for **offline-first applications** (collaborative text editors, mobile apps, local-first software) and **peer-to-peer systems** where nodes come and go unpredictably.

The tradeoff is expressiveness. Not every operation naturally fits a semilattice. Counters and sets are straightforward, but ordered sequences (like text in a collaborative document) require sophisticated designs like RGA or Logoot. Some application semantics — like enforcing a global uniqueness constraint — are fundamentally impossible without coordination, and CRDTs cannot help there. The design challenge is finding a CRDT that captures the semantics your application actually needs while accepting the ones it does not. When the fit is right, CRDTs provide strong eventual consistency with zero coordination overhead.
