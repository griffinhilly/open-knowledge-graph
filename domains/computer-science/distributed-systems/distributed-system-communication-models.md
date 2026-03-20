---
id: distributed-system-communication-models
title: Communication Models in Distributed Systems
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-systems-introduction
  type: hard
builds-toward:
- total-order-broadcast
- byzantine-agreement-algorithms
tags:
- models
- synchrony
- assumptions
stage: advanced
status: draft
---

# Communication Models in Distributed Systems

## Core Idea
Distributed systems operate under different communication assumptions: synchronous (bounded network delays and processing time), asynchronous (no bounds on delays), or partial synchrony (periods of synchrony and asynchrony). The choice of model fundamentally determines what consensus algorithms are possible.

## How It's Best Learned
Compare algorithms in different models: Paxos and Raft tolerate asynchrony; synchronous Byzantine agreement requires fewer messages. Understand why certain impossibility results (like FLP) apply to asynchronous systems but not synchronous ones.

## Common Misconceptions
- All real systems are asynchronous; in practice, they are partially synchronous with occasional partitions.
- Synchronous models are only theoretical; synchronous assumptions are useful for bounded-time guarantees in real systems.

## Explainer

When you begin designing algorithms for distributed systems, the first question is not "what do I want to compute?" but "what can I assume about the network and the clocks?" The **communication model** defines these assumptions, and the choice fundamentally constrains which problems are solvable and how efficiently. From your introduction to distributed systems, you know that nodes communicate by passing messages over a network. The communication model specifies what guarantees — if any — exist about how long those messages take to arrive.

In the **synchronous model**, there is a known upper bound on message delay and processing time. If you send a message, you know it will arrive within, say, 10 milliseconds — and if it does not, you can conclude the recipient has crashed. This makes algorithm design much simpler: you can use timeouts to detect failures reliably, and you can coordinate rounds of communication where everyone acts in lockstep. Classic synchronous algorithms can solve Byzantine agreement with fewer messages and simpler logic. The catch is that real networks rarely provide hard delay bounds — a garbage collection pause, a congested switch, or a route change can violate any fixed timeout.

In the **asynchronous model**, there are no bounds whatsoever on message delay or processing speed. A message might arrive in a millisecond or an hour — you simply cannot tell. This is the hardest model to work in because you can never distinguish a slow node from a crashed one. The famous **FLP impossibility result** proves that in a purely asynchronous system, no deterministic algorithm can guarantee consensus if even one node might crash. This does not mean consensus is impossible in practice — it means any real solution must use randomization, timeouts, or some form of partial synchrony assumption to make progress.

The **partial synchrony model** bridges the gap and reflects how real systems actually behave. It posits that the system is asynchronous most of the time, but there exist periods of synchrony — intervals where message delays are bounded — that last long enough for algorithms to make progress. Paxos and Raft are designed for this model: they are safe (never produce incorrect results) regardless of timing, but they rely on periods of synchrony for **liveness** (actually reaching a decision). In practice, this means these algorithms always give correct answers but may temporarily stall during network partitions or high latency. When the network stabilizes, they resume and complete. This is why partial synchrony dominates real-world distributed systems design: it honestly models the unreliable networks we have while still permitting useful algorithms.
