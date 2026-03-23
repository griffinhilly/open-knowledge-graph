---
id: strong-consistency-models
title: 'Strong Consistency: Linearizability and Sequential Consistency'
domain: computer-science
course: distributed-systems
prerequisites:
- id: consistency-models
  type: hard
builds-toward:
- state-machine-replication
tags:
- linearizability
- sequential-consistency
- strong-consistency
stage: advanced
status: validated
---

# Strong Consistency: Linearizability and Sequential Consistency

## Core Idea
Linearizability is the strongest consistency: the system appears as a single copy and each operation takes effect instantaneously between invocation and response. Sequential consistency is slightly weaker: operations appear in a total order respecting program order on each process. Both prevent anomalies but require coordination, increasing latency and reducing availability.

## Questions

```yaml
- question: "Client A completes a write of value 5. Only after A's response is received does Client B begin and complete a write of value 7. Under sequential consistency (but not linearizability), which outcome is possible for a subsequent read by Client C?"
  type: multiple-choice
  options:
    - "The read always returns 7, since B's write occurred last in wall-clock time"
    - "The read might return 5, because sequential consistency does not require the global ordering to match real-time order across processes"
    - "The read blocks indefinitely until all replicas synchronize"
    - "The read always returns the most recently written value regardless of consistency model"
  answer: 1
  explanation: "Sequential consistency requires a total order consistent with program order *within* each process, but it does not require this total order to match wall-clock time *across* processes. Since A and B are different processes, SC allows the global sequence to place A's write after B's write even though A's write physically completed first. A read that sees this ordering would return 5. Linearizability would rule this out: because A's write *completed* before B's write *began*, linearizability requires A's write to appear before B's in any legal total order, so a read must see 7."

- question: "A distributed system guarantees that once any client reads a newly written value, all subsequent reads by any client will also see that value or a later one. Which consistency model does this describe?"
  type: multiple-choice
  options:
    - "Sequential consistency"
    - "Eventual consistency"
    - "Linearizability"
    - "Causal consistency"
  answer: 2
  explanation: "This is a defining property of linearizability: once a write is 'visible' (any client has seen it), it is visible to all future reads — there is no window where some clients see the new value and others see the old one. Sequential consistency provides a total order consistent with per-process program order, but it does not guarantee real-time visibility propagation across clients. Eventual consistency only guarantees convergence eventually, not immediately after a read. Linearizability is the model that makes a distributed system behave as a single non-replicated copy."

- question: "A linearizable system must pay higher latency than an eventually consistent system because linearizability requires writes to be acknowledged by a majority of replicas before returning to the client."
  type: true-false
  answer: true
  explanation: "Linearizability requires coordination: to ensure a write is globally visible before returning to the client, the system must wait for a quorum of replicas to confirm the write (e.g., via Paxos or Raft). This takes at least one network round-trip to remote replicas, adding latency proportional to the slowest replica in the quorum. Eventual consistency, by contrast, can acknowledge writes locally and propagate them asynchronously, making writes appear much faster. The CAP theorem formalizes this: linearizability (consistency) trades off against availability under network partitions."

- question: "Sequential consistency is a stronger model than linearizability because it adds the constraint that operations must appear in program order within each process."
  type: true-false
  answer: false
  explanation: "This is backwards. Linearizability is strictly stronger than sequential consistency. Both require a total order consistent with per-process program order. The extra constraint that linearizability adds is real-time ordering: if operation A completes (its response is delivered) before operation B begins (its request is sent), then A must appear before B in the global order. Sequential consistency does not require this, allowing wall-clock inversions across processes. Every linearizable execution is sequentially consistent, but not vice versa."

- question: "What is the key difference between linearizability and sequential consistency, and why does it matter for applications like distributed banking or lock services?"
  type: short-answer
  answer: "Linearizability requires that the global ordering of operations respects real-time order across all processes: if one operation's response arrives before another's request is sent, the first must appear earlier in the global order. Sequential consistency only requires the global order to respect program order within each individual process, but allows wall-clock inversions between processes. For banking or lock services, linearizability matters because clients rely on real-time causality: if I see my balance updated (read completes) and then tell you to read it, you must see the same or newer value. Sequential consistency could allow your read to see a stale value because it doesn't guarantee real-time cross-client ordering."
  explanation: "Linearizability is the consistency guarantee that makes a distributed system feel like a single machine: any operation that completes before another begins must be reflected in the later operation's result. Applications like distributed locks (where acquiring the lock must prevent other clients from doing so), leader election, and financial transfers depend on this property. Sequential consistency is sufficient for some use cases (e.g., a single-client sequential workload), but breaks down when multiple clients need to coordinate based on shared real-time observations."
```

## Explainer

You already know from consistency models that a distributed system replicating data across nodes must define rules about which values reads can return and when writes become visible. Strong consistency models impose the strictest rules: they make the distributed system behave as if there were only one copy of the data, eliminating the anomalies (stale reads, reordered writes) that weaker models permit.

**Linearizability** is the gold standard. It requires that every operation appears to take effect at a single instantaneous point in time, somewhere between when the client sends the request and when it receives the response. Imagine a shared register. Client A writes the value 5, then Client B writes 7. If A's write completes (response received) before B's write begins (request sent), then any subsequent read must return 7, never 5. The critical property is that once a write is visible to any client, it is visible to all clients — there is no window where some clients see the old value and others see the new one. This is what "appears as a single copy" means: you could place every operation on a single timeline and the results would be consistent with a single-threaded program operating on one machine.

**Sequential consistency** relaxes this slightly. It still requires a total order of all operations that is consistent with the program order within each individual process — if process P does write(5) then write(7), both of those appear in that order in the global sequence. But sequential consistency does not require the global order to respect real-time ordering across processes. If A's write finishes before B's write starts in wall-clock time, sequential consistency might still place B's write first in the global order, as long as no single process observes a contradiction. This means sequential consistency is easier to implement (less coordination needed) but can produce results that are surprising if you reason about wall-clock time.

The practical cost of both models is coordination. To guarantee linearizability, replicas must agree on the order of operations, typically through consensus protocols like Paxos or Raft. Every write must wait for a majority of replicas to acknowledge it before returning to the client, and reads may need to contact a quorum or go through the leader. This adds latency — often a full network round-trip to remote replicas — and reduces availability, because the system cannot process operations if a majority of nodes are unreachable. The CAP theorem formalizes this tradeoff: a linearizable system must sacrifice availability during network partitions. For applications like bank transfers or distributed locks where correctness depends on seeing the latest value, this cost is worth paying. For applications like social media feeds where slight staleness is acceptable, weaker models trade consistency for speed.
