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
status: draft
---

# Eventual Consistency

## Core Idea
Eventual consistency guarantees that if no new writes occur, all replicas will converge to the same state. Writes succeed on any replica without waiting for others, providing high availability and partition tolerance. Applications must tolerate temporary divergence and resolve concurrent writes (conflict resolution), used widely in systems like Dynamo and Cassandra.

## Explainer

From your study of consistency models, you know the spectrum ranges from strong consistency (every read sees the most recent write) to weaker guarantees that trade correctness for performance. **Eventual consistency** sits near the weak end of that spectrum, making a deliberately modest promise: if writes stop, all replicas will *eventually* converge to the same state. It does not say how long convergence takes, and it explicitly allows different replicas to return different values for the same key at the same moment. This sounds alarming, but it is the foundation of many of the most available and scalable systems in production.

The motivation is practical. Strong consistency requires coordination — typically waiting for a majority of replicas to acknowledge a write before considering it committed. That coordination takes time and, critically, fails during network partitions: if a node cannot reach a quorum, it must reject the write. Eventual consistency avoids this by letting any replica accept a write immediately and propagate it to others asynchronously. During a network partition, both sides continue serving reads and writes independently. When the partition heals, replicas exchange their updates and converge. The result is a system that is always available and tolerates partitions — the "AP" choice in the CAP theorem you encountered when studying consistency models.

The hard problem is **conflict resolution**: what happens when two replicas independently accept conflicting writes to the same key during a partition? There are several strategies. **Last-writer-wins** uses timestamps to pick the most recent write, which is simple but discards data and depends on synchronized clocks. **Vector clocks** track causal ordering so the system can detect true conflicts (concurrent writes with no causal relationship) and present them to the application or user for resolution. **CRDTs** (conflict-free replicated data types) design data structures so that all possible merge orders produce the same result, eliminating conflicts by construction. Each strategy trades off simplicity, data preservation, and application complexity.

In practice, eventual consistency works well for use cases where temporary staleness is acceptable: social media feeds, shopping cart contents, DNS, and content delivery networks. A user might see a slightly outdated view of their friend's posts for a few seconds — an acceptable tradeoff for the system remaining available worldwide even during infrastructure failures. The key skill is recognizing which parts of your application can tolerate this divergence and which require stronger guarantees. Most real systems are not purely one or the other — they use eventual consistency for high-throughput paths and stronger consistency selectively where correctness demands it.
