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
- id: strong-eventual-consistency
  type: soft
tags:
- crdts
- replicated-data-types
- eventual-consistency
stage: expert
status: validated
---

# CRDTs: Conflict-Free Replicated Data Types

## Core Idea
CRDTs are data structures that converge automatically without coordination: replicas update independently and the merge operation is commutative and idempotent, guaranteeing convergence to the same state. Examples include counters, sets, and sequences. CRDTs enable offline-first applications and peer-to-peer systems where strong consistency is infeasible.

## Questions

```yaml
- question: "A G-Counter allows each of n replicas to increment only its own entry. When two replicas exchange state, what merge operation ensures they converge to the same count, and why?"
  type: multiple-choice
  options:
    - "Element-wise sum — add corresponding entries so no increments are lost"
    - "Element-wise maximum — take the larger value for each entry; because max is commutative and idempotent, replicas converge regardless of message order"
    - "Element-wise minimum — take the smaller value to prevent double-counting"
    - "Last-write-wins — the most recently timestamped entry overwrites the other"
  answer: 1
  explanation: "Element-wise max is the correct merge for a G-Counter. If replica A has [3,1,0] and replica B has [2,2,0], the merge is [3,2,0] — the total is 5 regardless of which replica you merge from (commutative) and merging again produces the same result (idempotent). Element-wise sum would double-count increments that both replicas already have. Last-write-wins requires coordination to determine 'last.' Max requires none of that."

- question: "An application needs to ensure no two users can register the same username — a global uniqueness constraint. Can a CRDT provide this guarantee without any coordination?"
  type: multiple-choice
  options:
    - "Yes — an OR-Set CRDT tags each username with a unique identifier, preventing duplicates"
    - "Yes — a G-Set's union merge naturally ensures each element appears only once"
    - "No — enforcing global uniqueness requires knowing the complete current state across all replicas simultaneously, which requires coordination that CRDTs cannot provide"
    - "No — CRDTs only support numeric data types, not strings like usernames"
  answer: 2
  explanation: "CRDTs guarantee convergence for operations whose semantics fit a join semilattice. A uniqueness constraint is fundamentally different: to accept 'alice' you must know that no other replica has already accepted it, which requires a globally consistent snapshot at the moment of the write. CRDTs let each replica accept writes locally and independently — which is precisely why they cannot enforce global exclusion. This is not an implementation limitation but a logical impossibility without coordination."

- question: "CRDTs achieve conflict-free convergence by having replicas contact a central coordinator before accepting each write operation."
  type: true-false
  answer: false
  explanation: "The entire value of CRDTs is that they require NO coordination. Each replica accepts writes locally and immediately, without contacting any other replica. Convergence is guaranteed not by coordination but by the mathematical properties of the merge operation: commutativity, associativity, and idempotence ensure that no matter in which order replicas exchange updates, they reach the same final state. Requiring a coordinator would make CRDTs equivalent to traditional distributed locks — only fast when the coordinator is reachable."

- question: "If a replica receives the same CRDT update twice due to network retransmission, applying it a second time corrupts the state."
  type: true-false
  answer: false
  explanation: "CRDTs are idempotent: merging the same state twice produces the same result as merging it once. For a G-Counter, taking element-wise max of [3,1,0] with [3,1,0] yields [3,1,0] — unchanged. Idempotence is one of the three required semilattice properties (alongside commutativity and associativity), and it means replicas can receive duplicate messages from at-least-once delivery networks with no ill effects — a critical property for practical deployment."

- question: "Why must a CRDT's merge operation be commutative, associative, AND idempotent? What breaks if any one of these properties is missing?"
  type: short-answer
  answer: "Commutativity ensures merge(A,B) = merge(B,A) — replicas that receive updates in different orders converge to the same state. Associativity ensures that pairwise merges in any sequence produce the same result — important when updates propagate through intermediate nodes. Idempotence ensures that receiving the same update more than once has no effect. If commutativity fails, message ordering matters and replicas diverge. If associativity fails, the propagation path affects the result. If idempotence fails, duplicate delivery corrupts state. All three together make coordination unnecessary."
  explanation: "The three properties define a join semilattice, the mathematical structure that guarantees convergence. Each property eliminates a different class of distributed hazard: ordering dependence, path dependence, and duplicate delivery. A system missing any one of these either reintroduces coordination requirements or produces incorrect results — defeating the purpose of a CRDT entirely."
```

## Explainer

From your study of eventual consistency, you know that replicas in a distributed system can temporarily diverge and must eventually converge to the same state. The hard question is: how do you guarantee convergence without a central coordinator deciding who wins? **CRDTs** (Conflict-Free Replicated Data Types) answer this by building convergence into the data structure itself. The mathematical trick is that the merge operation forms a **join semilattice** — it is commutative (merge(A, B) = merge(B, A)), associative (order of pairwise merges does not matter), and idempotent (merging the same state twice has no effect). These properties mean replicas can receive updates in any order, merge them in any order, and always arrive at the same final state.

The simplest example is a **G-Counter** (grow-only counter). Each of *n* replicas maintains its own counter. To increment, a replica bumps only its own entry. To merge, take the element-wise maximum across all entries. The total count is the sum. Because `max` is commutative and idempotent, all replicas converge regardless of message ordering. A **PN-Counter** extends this to support decrements by pairing two G-Counters — one for increments, one for decrements — and reporting the difference. Sets work similarly: a **G-Set** (grow-only set) merges via union, which is naturally a semilattice operation. An **OR-Set** (observed-remove set) supports both add and remove by tagging each element with a unique identifier so that "add" and "remove" can be distinguished even when they arrive out of order.

The practical value of CRDTs is that they eliminate coordination. In a traditional system, concurrent writes to the same data require either locking (which blocks other replicas and needs network round-trips) or a consensus protocol (which requires a majority of replicas to agree). CRDTs sidestep both: every replica can accept writes locally and immediately, without contacting any other replica. Synchronization happens lazily — replicas exchange state or operations whenever they connect, and the merge function guarantees convergence. This makes CRDTs ideal for **offline-first applications** (collaborative text editors, mobile apps, local-first software) and **peer-to-peer systems** where nodes come and go unpredictably.

The tradeoff is expressiveness. Not every operation naturally fits a semilattice. Counters and sets are straightforward, but ordered sequences (like text in a collaborative document) require sophisticated designs like RGA or Logoot. Some application semantics — like enforcing a global uniqueness constraint — are fundamentally impossible without coordination, and CRDTs cannot help there. The design challenge is finding a CRDT that captures the semantics your application actually needs while accepting the ones it does not. When the fit is right, CRDTs provide strong eventual consistency with zero coordination overhead.
