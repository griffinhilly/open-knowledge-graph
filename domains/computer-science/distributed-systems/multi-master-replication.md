---
id: multi-master-replication
title: Multi-Master Replication
domain: computer-science
course: distributed-systems
prerequisites:
- id: state-machine-replication
  type: hard
- id: consensus-problem
  type: hard
builds-toward:
- consistency-models
tags:
- replication
- topology
- writes
stage: advanced
status: validated
---

# Multi-Master Replication

## Core Idea
Multi-master replication allows writes to be accepted at any replica. All replicas must synchronize through consensus (Paxos, Raft) or eventual consistency with conflict resolution. This enables high availability and low-latency writes in geographically distributed systems but complicates consistency guarantees and conflict handling.

## Questions

```yaml
- question: "Two users simultaneously update the same database record on different replicas in a multi-master system using last-writer-wins conflict resolution. User A's write has a slightly earlier timestamp than User B's write. What happens to User A's write?"
  type: multiple-choice
  options:
    - "User A's write is preserved and User B's write is rejected with an error"
    - "Both writes are merged using application logic to produce a combined result"
    - "User A's write is silently discarded — last-writer-wins keeps only the write with the later timestamp"
    - "The system enters a conflict state and blocks all reads until an administrator resolves the conflict"
  answer: 2
  explanation: "Last-writer-wins (LWW) resolves conflicts by comparing timestamps and keeping the write with the later timestamp — User B's write wins. User A's write is silently discarded; the user receives no error and may not know their update was lost. This is the core tradeoff of LWW: it is simple and always converges, but it can silently lose data. Systems using LWW accept that concurrent conflicting updates will result in one update being lost, which is acceptable for some applications (shopping cart preferences) but catastrophic for others (financial records)."

- question: "A multi-master system uses a consensus protocol (Raft) on every write to ensure strong consistency. A developer argues this defeats the purpose of multi-master replication. Why is this criticism valid?"
  type: multiple-choice
  options:
    - "Raft consensus only works with at most 3 replicas, limiting geographic distribution"
    - "Raft consensus requires that all write requests go through a single elected leader, eliminating multi-master semantics"
    - "Requiring cross-replica consensus coordination before confirming each write reintroduces latency that multi-master was intended to avoid"
    - "Raft consensus is incompatible with geographically distributed deployments because it requires synchronous communication"
  answer: 2
  explanation: "The primary motivation for multi-master replication is low-latency local writes — a user in Tokyo writes to a Tokyo replica without waiting for coordination with London. When Raft consensus is required for every write, the write cannot be confirmed until replicas agree on its ordering, which requires round-trip communication across geographic distances. A user in Tokyo now waits for a response from London before their write completes. The latency advantage of local writes is largely eliminated. This is the core tension: strong consistency (via consensus) and low-latency local writes cannot both be achieved simultaneously in geographically distributed systems."

- question: "CRDTs (conflict-free replicated data types) are designed so that concurrent operations on different replicas always converge to the same final state, regardless of the order in which updates are applied."
  type: true-false
  answer: true
  explanation: "CRDTs achieve this through careful mathematical design. The data structure and its merge operations are constructed so that concurrent updates commute — applying them in any order produces the same result. For example, a grow-only set CRDT simply takes the union of all elements seen across replicas; adding the same element on two different replicas simultaneously always produces the correct merged result. CRDTs eliminate the need for conflict resolution logic because conflicts are structurally impossible — the data type constrains operations to those that are always safe to merge."

- question: "A multi-master system using eventual consistency provides strong consistency because all replicas will eventually agree on the same value."
  type: true-false
  answer: false
  explanation: "Eventual consistency means replicas converge to the same state *eventually* if no new writes arrive — but during the window before convergence, different replicas may return different values for the same key. This is fundamentally different from strong consistency, which guarantees that all reads reflect the most recent write. A system could return stale or conflicted values to users for seconds, minutes, or longer under eventual consistency. 'Eventually the same' is not the same as 'always the same right now.' The CAP theorem formalizes this: under network partitions, you must choose between consistency (always correct) and availability (always respond), not both."

- question: "Why can't a multi-master replication system simultaneously achieve low-latency local writes, strong consistency, and high availability during network partitions? What tradeoff must be made?"
  type: short-answer
  answer: "Strong consistency requires that all replicas agree on the value before a write is confirmed — which requires cross-replica communication (consensus). This communication introduces latency proportional to network round-trip time between replicas. During a network partition, replicas cannot communicate, so a strongly-consistent system must either refuse writes (sacrificing availability) or accept writes and risk inconsistency. Low-latency local writes require accepting a write immediately on one replica without coordination — which means other replicas are temporarily inconsistent. The CAP theorem captures this: a distributed system can at most provide two of consistency, availability, and partition tolerance. Multi-master systems typically choose between strong consistency with higher latency (consensus-based, like Spanner) or high availability with eventual consistency (like CouchDB), but cannot achieve all three simultaneously."
  explanation: "The tradeoff is not a bug to be engineered away — it is a fundamental property of distributed systems formalized by the CAP theorem. Understanding this forces deliberate design choices: what does your application need most? Financial systems that cannot tolerate inconsistency choose consistency. User-facing applications that cannot tolerate unavailability choose availability. The choice of replication topology and conflict resolution strategy flows directly from this answer."
```

## Explainer

In the replication models you have studied so far — primary-backup and state machine replication — there is a clear distinction between which node accepts writes and which nodes follow. Multi-master replication removes that distinction: **every replica can accept writes independently**. Think of it like a shared document where multiple people can type at the same time in different locations, rather than one person dictating while others copy. This sounds ideal for availability and latency — a user in Tokyo writes to a Tokyo replica, a user in London writes to a London replica — but it introduces a fundamental problem you already understand from the consensus problem: what happens when two replicas accept conflicting writes at the same time?

The answer depends on the consistency model the system chooses. One approach is to run a **consensus protocol** (Paxos or Raft) on every write, so all replicas agree on a single total order of operations before any write is confirmed. This gives you strong consistency — the system behaves as if there were a single copy of the data — but it reintroduces the latency cost of cross-replica coordination, partially defeating the purpose of allowing writes everywhere. The alternative is **eventual consistency with conflict resolution**: each replica accepts writes immediately and propagates them asynchronously, with conflicts detected and resolved after the fact.

Conflict resolution is where multi-master replication gets genuinely hard. Two users might update the same row at the same time on different replicas. Common resolution strategies include **last-writer-wins** (use timestamps to pick a winner, accepting that the "loser" write is silently discarded), **merge functions** (application-specific logic that combines both writes, like a union of set elements), and **conflict-free replicated data types** (CRDTs), which are data structures mathematically designed so that concurrent operations always converge to the same state regardless of the order they are applied. Each strategy trades off simplicity, correctness, and the kinds of operations the system can support.

In practice, most multi-master systems are used when geographic distribution makes single-leader latency unacceptable — global databases like Google Spanner (which uses consensus) or CouchDB (which uses eventual consistency with conflict detection). The design choice between consensus-backed multi-master and eventually-consistent multi-master maps directly to the CAP theorem tradeoff: you can optimize for consistency or availability under network partitions, but not both. Understanding this tradeoff is the key to choosing the right replication topology for a given system.
