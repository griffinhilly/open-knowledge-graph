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

## Questions

```yaml
- question: "A software architect proposes a distributed database that guarantees both Consistency and Availability by sacrificing Partition Tolerance. Why does the CAP theorem expose this as an unrealistic design?"
  type: multiple-choice
  options:
    - "You should always prioritize Partition Tolerance and Availability over Consistency in distributed systems"
    - "Network partitions are unavoidable in any real distributed deployment, so a system requiring no partitions cannot be reliably operated"
    - "Consistency and Availability are mutually exclusive and cannot be achieved simultaneously under any conditions"
    - "The CAP theorem requires all three properties to be traded off in equal proportions"
  answer: 1
  explanation: "The 'CA without P' option sounds appealing but is not achievable in practice: hardware fails, network cables are cut, packets are dropped, and data centers lose connectivity. A system that assumes zero partitions is effectively a single-node system — not a distributed system at all. Because partitions will occur, every real distributed system must choose how to behave when they do: either refuse some requests (CP) or return potentially stale data (AP). The practical choice is always between CP and AP, never CA."

- question: "A distributed database advertises 'CAP consistency.' A developer assumes this means it enforces data integrity rules such as preventing bank account balances from going negative. Is this correct?"
  type: multiple-choice
  options:
    - "Yes — CAP consistency is equivalent to ACID consistency and enforces application-level invariants"
    - "No — CAP consistency (linearizability) means every read returns the most recent write; it makes no claim about application-level invariants"
    - "Yes — CP systems automatically implement full ACID compliance as a consequence"
    - "No — CAP systems cannot enforce any form of data consistency whatsoever"
  answer: 1
  explanation: "CAP consistency and ACID consistency are entirely different properties that unfortunately share the same word. CAP consistency (formally, linearizability) means: if I write a value, any subsequent read from any node returns that value or a later one. ACID consistency means: the database enforces application-defined invariants (foreign keys, check constraints, business rules). A system can be AP in the CAP sense while still enforcing strong ACID invariants within a single node, or it can be CP yet lack application-level constraint checking. The conflation of these two meanings is one of the most common mistakes in distributed systems reasoning."

- question: "A CA (Consistency + Availability without Partition Tolerance) distributed database is a viable architecture for production applications where high uptime is critical."
  type: true-false
  answer: false
  explanation: "CA systems do not exist as a meaningful category for distributed deployments. Partition tolerance is not a feature you 'sacrifice by choice' — it is an acknowledgment that partitions will happen whether you want them to or not. Any system that requires zero partitions must either run on a single node (giving up distribution) or will fail unpredictably when the inevitable partition occurs. Modern distributed databases acknowledge this and position themselves as CP (like ZooKeeper) or AP (like Cassandra), never CA."

- question: "An AP distributed system that returns stale data during a network partition can still eventually reach the correct consistent state once the partition heals."
  type: true-false
  answer: true
  explanation: "This is the definition of eventual consistency: during a partition, AP nodes continue serving requests (possibly with stale data), but once network connectivity is restored, conflict resolution mechanisms propagate updates across all replicas until they converge. The trade-off is predictability during the partition vs. liveness. Cassandra, DynamoDB, and CouchDB all implement eventual consistency this way — they choose to remain available during outages and accept a window of potential staleness that resolves automatically."

- question: "Why does the CAP theorem reduce in practice to a choice between CP and AP, rather than a genuine three-way trade-off? What makes the third option (CA — sacrificing partition tolerance) unrealistic?"
  type: short-answer
  answer: "Partitions are not optional. In any distributed system spanning multiple machines, network failures, hardware crashes, and connectivity interruptions will occur. A system that 'sacrifices partition tolerance' is claiming it can guarantee no partition will ever happen — an impossible guarantee in real infrastructure. So the real question is not whether to handle partitions, but how: either maintain consistency by refusing some requests when a partition makes it impossible to confirm the latest state (CP), or maintain availability by continuing to respond even with potentially stale data (AP)."
  explanation: "The PACELC model extends this insight: even without partitions, there is a latency-consistency trade-off. Stronger consistency (requiring all replicas to agree before responding) takes more coordination time. AP systems also must design conflict resolution strategies (last-write-wins, vector clocks, CRDTs) because divergent replicas will accumulate during partitions and must be reconciled. The CAP theorem is a theoretical result about worst-case behavior during partitions; real system design adds latency, replication lag, and operational complexity to the picture."
```

## Explainer

You are familiar with ACID properties for single-database transactions and with the idea that NoSQL systems distribute data across multiple nodes. The **CAP theorem**, proven by Eric Brewer and formalized by Gilbert and Lynch, states a fundamental constraint on any distributed data store: when a network partition occurs, you must choose between consistency and availability — you cannot have both.

To understand why, imagine a simple distributed system with two database nodes, A and B, each holding a copy of some data. Under normal operation, when you write to node A, the update is replicated to node B, and any read from either node returns the latest value. Now suppose the network link between A and B fails — a **partition**. A client writes a new value to node A, but that update cannot reach node B. A different client reads from node B. What should happen? There are exactly two choices. First, node B could return the old (stale) value — it stays **available** (it responds) but sacrifices **consistency** (the read doesn't reflect the latest write). Second, node B could refuse to answer until it can confirm the latest state — it maintains **consistency** but sacrifices **availability**. There is no third option. The partition makes it impossible to both guarantee the latest data and guarantee a response.

This gives rise to two practical system categories. **CP systems** (like ZooKeeper, HBase, or MongoDB with majority-write concern) prioritize consistency: during a partition, nodes that cannot confirm they have the latest data will reject requests or become read-only. You always get correct answers, but sometimes you get no answer at all. **AP systems** (like Cassandra, DynamoDB, or CouchDB) prioritize availability: every node always responds, but during a partition some responses may be stale. AP systems typically offer **eventual consistency** — once the partition heals, replicas converge to the same state through conflict resolution mechanisms.

A critical subtlety: CAP consistency (called **linearizability** — every read returns the most recent write as if there were a single copy of the data) is not the same as ACID consistency (application-level invariants like "account balances cannot go negative"). These are entirely different properties that unfortunately share a name. A system can be AP in the CAP sense while still enforcing some ACID-like application constraints. In practice, most modern distributed databases do not make a hard binary CAP choice. Instead, they offer **tunable consistency** — you can configure per-query how many replicas must acknowledge a write or agree on a read. With Cassandra, for example, writing and reading at quorum (majority) gives you strong consistency during normal operation while remaining partition-tolerant. The CAP theorem tells you about the worst case during a partition; the PACELC extension adds that even without partitions, there is a tradeoff between latency and consistency — stronger consistency requires more coordination between nodes, which takes more time.
