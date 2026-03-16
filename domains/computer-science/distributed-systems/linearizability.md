---
id: linearizability
title: Linearizability
domain: computer-science
course: distributed-systems
prerequisites:
- id: consistency-models
  type: hard
builds-toward:
- distributed-transactions-2pc
- strong-eventual-consistency
tags:
- consistency
- formal-semantics
- correctness
stage: advanced
status: draft
---

# Linearizability

## Core Idea
Linearizability is the strongest consistency model: all operations appear to execute atomically at some point between their invocation and completion, and the execution respects a total order. A linearizable system behaves as if there is a single copy of the data. This model prevents stale reads, causality violations, and ensures a consistent view of shared state across all clients.

## How It's Best Learned
Compare linearizable and non-linearizable execution histories side by side. Understand why linearizability is stricter than sequential consistency and more expensive to implement. Implement a simple linearizable register and test with concurrent operations from multiple clients.

## Common Misconceptions
- Linearizability is the same as serializability (linearizability is stronger and applies to concurrent objects, not just transactions). - Linearizability requires centralized state (distributed linearizable systems exist). - Linearizability solves all consistency problems (availability and latency are separate concerns).

## Explainer

From your study of consistency models, you know that distributed systems must choose how much ordering and freshness to guarantee when multiple nodes hold copies of the same data. **Linearizability** sits at the top of that hierarchy — it is the strongest single-object consistency model, and it makes a distributed system behave as though there is only one copy of the data, accessed by one operation at a time.

The core guarantee is this: every operation appears to take effect **atomically** at some single point in time between when the client issued the request and when the client received the response. This point is called the **linearization point**. If client A's write completes before client B's read begins (in real, wall-clock time), then B is guaranteed to see A's write. There is no window where stale data can leak through. Imagine a shared whiteboard in a room — anyone who walks in sees whatever was most recently written. Linearizability gives you that same property even when the "whiteboard" is replicated across machines in different data centers.

Compare this with **sequential consistency**, which also produces a total order of operations but does not require that order to match real time. Sequential consistency says "there exists some legal ordering," while linearizability says "that ordering must respect the actual wall-clock sequence of non-overlapping operations." The distinction matters when two clients coordinate out of band — for example, if Alice writes a value and then calls Bob on the phone to say "go read it," linearizability guarantees Bob sees the write. Sequential consistency does not.

The cost of linearizability is significant. The CAP theorem tells us that a linearizable system cannot remain both consistent and available during a network partition — it must sacrifice availability by refusing to serve requests from the minority partition. In practice, achieving linearizability requires coordination protocols like consensus (Paxos, Raft) or careful use of a single leader, both of which add latency. This is why many real-world systems offer weaker consistency by default and reserve linearizability for operations that truly need it — like acquiring a distributed lock or performing a compare-and-swap on a configuration value.
