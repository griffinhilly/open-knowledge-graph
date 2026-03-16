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
status: draft
---

# Strong Consistency: Linearizability and Sequential Consistency

## Core Idea
Linearizability is the strongest consistency: the system appears as a single copy and each operation takes effect instantaneously between invocation and response. Sequential consistency is slightly weaker: operations appear in a total order respecting program order on each process. Both prevent anomalies but require coordination, increasing latency and reducing availability.

## Explainer

You already know from consistency models that a distributed system replicating data across nodes must define rules about which values reads can return and when writes become visible. Strong consistency models impose the strictest rules: they make the distributed system behave as if there were only one copy of the data, eliminating the anomalies (stale reads, reordered writes) that weaker models permit.

**Linearizability** is the gold standard. It requires that every operation appears to take effect at a single instantaneous point in time, somewhere between when the client sends the request and when it receives the response. Imagine a shared register. Client A writes the value 5, then Client B writes 7. If A's write completes (response received) before B's write begins (request sent), then any subsequent read must return 7, never 5. The critical property is that once a write is visible to any client, it is visible to all clients — there is no window where some clients see the old value and others see the new one. This is what "appears as a single copy" means: you could place every operation on a single timeline and the results would be consistent with a single-threaded program operating on one machine.

**Sequential consistency** relaxes this slightly. It still requires a total order of all operations that is consistent with the program order within each individual process — if process P does write(5) then write(7), both of those appear in that order in the global sequence. But sequential consistency does not require the global order to respect real-time ordering across processes. If A's write finishes before B's write starts in wall-clock time, sequential consistency might still place B's write first in the global order, as long as no single process observes a contradiction. This means sequential consistency is easier to implement (less coordination needed) but can produce results that are surprising if you reason about wall-clock time.

The practical cost of both models is coordination. To guarantee linearizability, replicas must agree on the order of operations, typically through consensus protocols like Paxos or Raft. Every write must wait for a majority of replicas to acknowledge it before returning to the client, and reads may need to contact a quorum or go through the leader. This adds latency — often a full network round-trip to remote replicas — and reduces availability, because the system cannot process operations if a majority of nodes are unreachable. The CAP theorem formalizes this tradeoff: a linearizable system must sacrifice availability during network partitions. For applications like bank transfers or distributed locks where correctness depends on seeing the latest value, this cost is worth paying. For applications like social media feeds where slight staleness is acceptable, weaker models trade consistency for speed.
