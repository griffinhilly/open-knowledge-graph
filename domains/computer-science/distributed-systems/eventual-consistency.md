---
id: eventual-consistency
title: Eventual Consistency
domain: computer-science
course: distributed-systems
prerequisites:
- id: consistency-models
  type: hard
builds-toward:
- crdts-convergent-replicated-types
tags:
- eventual-consistency
- weak-consistency
- availability
stage: advanced
status: validated
---

# Eventual Consistency

## Core Idea
Eventual consistency guarantees that if no new writes occur, all replicas will converge to the same state. Writes succeed on any replica without waiting for others, providing high availability and partition tolerance. Applications must tolerate temporary divergence and resolve concurrent writes (conflict resolution), used widely in systems like Dynamo and Cassandra.

## Questions

```yaml
- question: "Two users in different data centers simultaneously update the same record under an eventually consistent system. User A adds an item; User B removes a different item. A network partition then isolates the two data centers for 30 seconds. What correctly describes what happens?"
  type: multiple-choice
  options:
    - "One of the operations is rejected immediately because the system cannot proceed without consensus"
    - "Both operations succeed locally on their respective replicas; when the partition heals, the system applies a conflict resolution strategy to merge the states — potentially discarding one update"
    - "Both operations are buffered and held pending until the partition heals and both replicas can commit"
    - "The system automatically selects the lower-latency operation as the canonical one"
  answer: 1
  explanation: "The defining property of eventual consistency is that writes succeed on any available replica without waiting for acknowledgment from others. During a partition, both data centers continue operating independently — this is the high-availability guarantee. When the partition heals, the system must reconcile the diverged states using a conflict resolution strategy. Last-writer-wins might discard one of the updates based on timestamps. Vector clocks would detect that both writes are concurrent. CRDTs might be able to merge both (e.g., if using a set that can represent both adds and removes). There is no automatic buffering or rejection — that would sacrifice availability, which is the whole point."

- question: "A distributed system uses last-writer-wins (LWW) conflict resolution with wall-clock timestamps. What is the primary risk of this approach?"
  type: multiple-choice
  options:
    - "LWW requires each node to store all historical versions of every record, creating excessive storage overhead"
    - "LWW is only applicable in systems with two replicas and fails with three or more"
    - "If clocks are not perfectly synchronized across nodes, the 'latest' write by timestamp may not be the causally latest write, silently discarding valid data"
    - "LWW prevents the system from converging because each new write resets the convergence timer"
  answer: 2
  explanation: "Clock synchronization is a hard problem in distributed systems — network delays, clock drift, and hardware variation mean different nodes' clocks can disagree by milliseconds or more. A write that is causally later (a user edited a record after seeing a previous version) might have a slightly earlier timestamp than a concurrent write on another replica. LWW would then discard the causally later update — silently, with no error. Vector clocks avoid this by tracking causal ordering explicitly rather than depending on synchronized time. LWW is simple and fast, but the silent data loss is a serious risk in domains where every write is important."

- question: "An eventually consistent system guarantees that once a network partition heals, most replicas immediately return the same value for most key."
  type: true-false
  answer: false
  explanation: "The 'eventual' in eventual consistency is not instantaneous. The guarantee is that if writes stop and the system is allowed to propagate updates, replicas will converge. But healing a network partition does not instantly synchronize all replicas — the system must still exchange updates, detect conflicts, and apply resolution strategies, which takes time. During that window after healing, different replicas may still return different values. Applications built on eventual consistency must tolerate stale reads, not just during partitions but during the convergence period after them."

- question: "Eventual consistency achieves high availability by allowing replicas to accept writes without waiting for acknowledgment from other replicas, at the cost of allowing temporary divergence between replicas."
  type: true-false
  answer: true
  explanation: "This is the core tradeoff of eventual consistency as an 'AP' choice in the CAP theorem. Strong consistency requires coordination — a write must be acknowledged by a quorum before it is committed, and reads that cannot reach a quorum must be rejected or stale-blocked. This coordination fails or becomes expensive during network partitions. Eventual consistency eliminates the coordination requirement: each replica accepts writes immediately and propagates them asynchronously. The cost is temporary divergence — different replicas may return different values for the same key — which the application must be designed to tolerate."

- question: "Why must eventually consistent systems implement a conflict resolution strategy, and what are the key tradeoffs between last-writer-wins and vector clocks?"
  type: short-answer
  answer: "Eventual consistency allows independent writes on different replicas during partitions, creating the possibility of concurrent conflicting writes to the same key. When the partition heals, the system cannot simply keep both — it must reconcile them into a single state. Last-writer-wins (LWW) uses timestamps to pick the most recent write: it's simple and requires no extra metadata, but it silently discards the 'older' write and depends on clock synchronization. If clocks disagree, causally later writes can be discarded. Vector clocks track causal history per-key, detecting which writes are causally ordered (one happened before the other) and which are truly concurrent (neither caused the other). Concurrent writes are surfaced as genuine conflicts for the application or user to resolve. Vector clocks preserve data but add metadata overhead and application-level complexity."
  explanation: "CRDTs (conflict-free replicated data types) represent a third approach: data structures designed so that all possible merge orders produce identical results, eliminating conflicts by construction. They work for sets, counters, and some other structures but cannot be generalized to arbitrary data. The tradeoff space is fundamentally: simplicity (LWW) vs. data preservation (vector clocks) vs. structural constraints (CRDTs). Real systems like Amazon DynamoDB offer configurable conflict resolution and expose vector clock information to applications, recognizing that no single strategy fits all use cases."
```

## Explainer

From your study of consistency models, you know the spectrum ranges from strong consistency (every read sees the most recent write) to weaker guarantees that trade correctness for performance. **Eventual consistency** sits near the weak end of that spectrum, making a deliberately modest promise: if writes stop, all replicas will *eventually* converge to the same state. It does not say how long convergence takes, and it explicitly allows different replicas to return different values for the same key at the same moment. This sounds alarming, but it is the foundation of many of the most available and scalable systems in production.

The motivation is practical. Strong consistency requires coordination — typically waiting for a majority of replicas to acknowledge a write before considering it committed. That coordination takes time and, critically, fails during network partitions: if a node cannot reach a quorum, it must reject the write. Eventual consistency avoids this by letting any replica accept a write immediately and propagate it to others asynchronously. During a network partition, both sides continue serving reads and writes independently. When the partition heals, replicas exchange their updates and converge. The result is a system that is always available and tolerates partitions — the "AP" choice in the CAP theorem you encountered when studying consistency models.

The hard problem is **conflict resolution**: what happens when two replicas independently accept conflicting writes to the same key during a partition? There are several strategies. **Last-writer-wins** uses timestamps to pick the most recent write, which is simple but discards data and depends on synchronized clocks. **Vector clocks** track causal ordering so the system can detect true conflicts (concurrent writes with no causal relationship) and present them to the application or user for resolution. **CRDTs** (conflict-free replicated data types) design data structures so that all possible merge orders produce the same result, eliminating conflicts by construction. Each strategy trades off simplicity, data preservation, and application complexity.

In practice, eventual consistency works well for use cases where temporary staleness is acceptable: social media feeds, shopping cart contents, DNS, and content delivery networks. A user might see a slightly outdated view of their friend's posts for a few seconds — an acceptable tradeoff for the system remaining available worldwide even during infrastructure failures. The key skill is recognizing which parts of your application can tolerate this divergence and which require stronger guarantees. Most real systems are not purely one or the other — they use eventual consistency for high-throughput paths and stronger consistency selectively where correctness demands it.
