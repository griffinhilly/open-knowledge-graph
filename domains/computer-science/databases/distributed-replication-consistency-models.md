---
id: distributed-replication-consistency-models
title: 'Distributed Databases: Replication Models and Consistency'
domain: computer-science
course: databases
prerequisites:
- id: distributed-systems-introduction
  type: hard
- id: cap-theorem
  type: hard
builds-toward:
- nosql-data-models-scalability
tags:
- replication
- consistency
- distributed
- sync
- async
stage: formal-systems
status: draft
---

# Distributed Databases: Replication Models and Consistency

## Core Idea
Distributed databases replicate data across sites for fault tolerance and scalability. Synchronous replication waits for replica acknowledgment before committing, ensuring strong consistency but reducing throughput. Asynchronous replication commits locally and updates replicas later, allowing higher throughput but risking inconsistency. Quorum replication requires acknowledgment from a majority, balancing consistency and availability. Understanding replication models is essential for choosing appropriate consistency levels.

## Explainer

From the CAP theorem, you know that a distributed system cannot simultaneously guarantee consistency, availability, and partition tolerance — it must sacrifice at least one during a network partition. **Replication** is the mechanism that forces this tradeoff into concrete engineering decisions. When you copy data across multiple nodes, you must decide: does a write need to reach all copies before it is considered complete, or can it succeed on one node and propagate to the others later? The answer determines where your system falls on the consistency-availability spectrum.

**Synchronous replication** takes the conservative approach: a write is not acknowledged to the client until every replica has confirmed it received and stored the data. This gives you **strong consistency** — any read from any replica returns the most recent write. The cost is latency and reduced availability. If any replica is slow or unreachable, the write blocks or fails. This model works well when correctness is paramount and replicas are geographically close (e.g., within a single data center), but it becomes impractical across continents where network round-trips add hundreds of milliseconds to every write.

**Asynchronous replication** is the opposite extreme: the write succeeds as soon as the primary node stores it, and replicas receive updates later in the background. This maximizes write throughput and availability — the system keeps working even if replicas lag behind. The tradeoff is **eventual consistency**: a read from a lagging replica might return stale data. If the primary fails before replicating a write, that write can be permanently lost. Many consumer-facing applications accept this tradeoff because a user seeing a slightly stale news feed or follower count is far less costly than the system being unavailable.

**Quorum replication** finds a middle ground by requiring acknowledgment from a **majority** of replicas rather than all of them. With N replicas, a write succeeds when W replicas acknowledge it, and a read succeeds when R replicas respond — as long as W + R > N, the read and write quorums must overlap, guaranteeing that at least one node in any read quorum has the latest write. For example, with 3 replicas, writing to 2 and reading from 2 ensures consistency without requiring all 3 to be available. Tuning W and R lets you shift the tradeoff: higher W strengthens write durability at the cost of availability; higher R strengthens read consistency. This flexibility is why quorum-based systems like Cassandra and DynamoDB expose these knobs to application developers — the right consistency level depends on the specific operation, not a one-size-fits-all system setting.
