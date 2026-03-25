---
id: consistency-models
title: Consistency Models in Distributed Systems
domain: computer-science
course: distributed-systems
prerequisites:
- id: happened-before-relation-causality
  type: soft
- id: distributed-systems-introduction
  type: hard
builds-toward:
- eventual-consistency
- causal-consistency
- linearizability
tags:
- consistency
- correctness
- models
stage: advanced
status: validated
---

# Consistency Models in Distributed Systems

## Core Idea
Consistency models define what values a read can return after a write in a replicated system. Strong models (linearizability, sequential consistency) provide intuitive semantics but require coordination overhead. Weaker models (eventual consistency, causal consistency) improve availability and latency by tolerating temporary disagreement and concurrent write conflicts.

## Questions

```yaml
- question: "Two consistency models are commonly confused. Which one is strictly stronger: linearizability or sequential consistency?"
  type: multiple-choice
  options: ["Sequential consistency, because it allows more orderings", "Linearizability, because it additionally requires real-time ordering of operations", "They are equivalent — both require a single global order", "Neither; they are incomparable models"]
  answer: 1
  explanation: "Linearizability (also called atomic consistency) requires that operations appear to execute instantaneously at some point between their invocation and completion, preserving real-time order. Sequential consistency only requires that all nodes observe operations in the same order, but that order does not need to match wall-clock time. Linearizability is therefore strictly stronger."

- question: "Under eventual consistency, if a client writes a value to one replica and then immediately reads from a different replica, the read is guaranteed to return the new value."
  type: true-false
  answer: false
  explanation: "Eventual consistency only guarantees that replicas will *eventually* converge to the same value if no new writes occur — it makes no promise about when. A read immediately after a write may return a stale value from a replica that has not yet received the update. This is the fundamental tradeoff: lower latency and higher availability at the cost of temporarily stale reads."

- question: "Why do distributed systems designers often choose eventual consistency over linearizability, even when they would prefer strong consistency semantics?"
  type: short-answer
  answer: "The CAP theorem shows that a distributed system cannot simultaneously guarantee consistency, availability, and partition tolerance. Linearizability requires coordination (e.g., quorum reads/writes) that adds latency and becomes unavailable during network partitions. Eventual consistency allows systems to remain available and low-latency by deferring convergence."
  explanation: "This is the core design tension in distributed systems. Systems like Amazon DynamoDB and Apache Cassandra chose eventual consistency to achieve high availability across data centers. Systems like Google Spanner accept higher latency to provide linearizability. The choice depends on whether the application can tolerate stale reads."
```

## Explainer

From your study of distributed systems, you know that replication — storing the same data on multiple nodes — is fundamental to fault tolerance and scalability. But replication introduces a problem: what happens when a client writes to one replica and reads from another? What value should the read return? Consistency models are the formal answer to this question. They define the contract between the system and its clients about which behaviors are observable.

The strongest commonly-used model is **linearizability** (sometimes called atomic consistency). It requires that every operation appear to execute instantaneously at a single point in time, and that this point respects real-world clock order. If a write completes before a read begins, the read must see the new value. This is the intuition most programmers have about a variable — you write 5, then you read 5. Achieving linearizability across replicas requires coordination: the system must ensure that before a read returns, it has contacted enough replicas to guarantee it has the latest value (typically a quorum).

**Sequential consistency** is slightly weaker. It requires that all clients observe operations in the same global order, but that order does not need to match wall-clock time. Client A's write might appear to happen "before" client B's write in the global sequence even if B's write completed earlier in real time. This relaxation removes the real-time constraint and can allow more efficient implementations, but the semantics are harder to reason about.

**Eventual consistency** is much weaker and much more practical for geographically distributed systems. It guarantees only that, if no new writes occur, all replicas will eventually converge to the same value. There is no bound on *when* — a read may see a stale value for seconds or minutes. This allows replicas to accept writes locally and synchronize asynchronously, yielding very low write latency. Systems like DNS and shopping cart databases often use eventual consistency.

Between these extremes, **causal consistency** offers a useful middle ground: if operation A causally precedes operation B (e.g., you read a message, then reply to it), then any client that sees B must also have seen A. This preserves the logical flow of causally related events without requiring global coordination. The choice of consistency model is ultimately an engineering tradeoff between correctness guarantees, latency, and availability — and it must match the actual requirements of the application.
