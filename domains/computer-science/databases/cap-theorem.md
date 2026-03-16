---
id: cap-theorem
title: CAP Theorem
domain: computer-science
course: databases
prerequisites:
- id: nosql-concepts
  type: hard
- id: acid-properties
  type: soft
- id: key-value-stores
  type: soft
tags:
- CAP theorem
- consistency
- availability
- partition tolerance
- distributed systems
- CP
- AP
stage: formal-systems
status: validated
---
# CAP Theorem

## Core Idea
The CAP theorem states that a distributed data system can guarantee at most two of three properties: Consistency (every read receives the most recent write or an error), Availability (every request receives a non-error response, possibly stale), and Partition tolerance (the system continues operating despite network partitions). Since partitions are unavoidable in real distributed systems, the practical tradeoff is CP (consistency during partitions, possibly refusing requests) vs. AP (availability during partitions, possibly returning stale data). Most real systems allow tunable consistency rather than a strict binary choice.

## How It's Best Learned
Study the behavior of real systems: how does ZooKeeper (CP) behave during a partition vs. Cassandra (AP)? Understand that CAP describes worst-case partition scenarios, not normal steady-state operation.

## Common Misconceptions
- CAP consistency (linearizability — always reading the latest write) is not the same as ACID consistency (preserving application invariants) — these are different properties with the same word.
- CA systems (sacrificing partition tolerance) do not exist in practical distributed systems — partitions always happen eventually.
- The theorem is a theoretical impossibility result, not a design prescription; PACELC and other models better capture the latency-consistency tradeoffs of real systems.

## Explainer

You are familiar with ACID properties for single-database transactions and with the idea that NoSQL systems distribute data across multiple nodes. The **CAP theorem**, proven by Eric Brewer and formalized by Gilbert and Lynch, states a fundamental constraint on any distributed data store: when a network partition occurs, you must choose between consistency and availability — you cannot have both.

To understand why, imagine a simple distributed system with two database nodes, A and B, each holding a copy of some data. Under normal operation, when you write to node A, the update is replicated to node B, and any read from either node returns the latest value. Now suppose the network link between A and B fails — a **partition**. A client writes a new value to node A, but that update cannot reach node B. A different client reads from node B. What should happen? There are exactly two choices. First, node B could return the old (stale) value — it stays **available** (it responds) but sacrifices **consistency** (the read doesn't reflect the latest write). Second, node B could refuse to answer until it can confirm the latest state — it maintains **consistency** but sacrifices **availability**. There is no third option. The partition makes it impossible to both guarantee the latest data and guarantee a response.

This gives rise to two practical system categories. **CP systems** (like ZooKeeper, HBase, or MongoDB with majority-write concern) prioritize consistency: during a partition, nodes that cannot confirm they have the latest data will reject requests or become read-only. You always get correct answers, but sometimes you get no answer at all. **AP systems** (like Cassandra, DynamoDB, or CouchDB) prioritize availability: every node always responds, but during a partition some responses may be stale. AP systems typically offer **eventual consistency** — once the partition heals, replicas converge to the same state through conflict resolution mechanisms.

A critical subtlety: CAP consistency (called **linearizability** — every read returns the most recent write as if there were a single copy of the data) is not the same as ACID consistency (application-level invariants like "account balances cannot go negative"). These are entirely different properties that unfortunately share a name. A system can be AP in the CAP sense while still enforcing some ACID-like application constraints. In practice, most modern distributed databases do not make a hard binary CAP choice. Instead, they offer **tunable consistency** — you can configure per-query how many replicas must acknowledge a write or agree on a read. With Cassandra, for example, writing and reading at quorum (majority) gives you strong consistency during normal operation while remaining partition-tolerant. The CAP theorem tells you about the worst case during a partition; the PACELC extension adds that even without partitions, there is a tradeoff between latency and consistency — stronger consistency requires more coordination between nodes, which takes more time.
