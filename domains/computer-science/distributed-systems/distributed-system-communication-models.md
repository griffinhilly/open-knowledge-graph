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

## Questions

```yaml
- question: "An engineer argues their production system doesn't need to worry about the FLP impossibility result because 'it always reaches consensus in practice.' Which explanation best accounts for this real-world success?"
  type: multiple-choice
  options:
    - "FLP only applies to systems where more than one node crashes simultaneously"
    - "Their system operates under partial synchrony — during stable periods with bounded delays, consensus completes, even though it may stall during asynchronous intervals"
    - "FLP has been superseded by more recent results that show consensus is achievable in asynchronous systems"
    - "Production networks always provide hard delay bounds, making them truly synchronous"
  answer: 1
  explanation: "FLP proves that no deterministic algorithm can guarantee consensus in a purely asynchronous system if even one node might crash. But real systems don't operate in purely asynchronous conditions — they experience periods of synchrony where message delays are bounded, even if those periods aren't guaranteed to last forever. Algorithms like Paxos and Raft are designed for partial synchrony: they are always correct (safe), and they make progress (liveness) during the synchronous periods. The engineer's system 'always' reaches consensus because asynchronous periods are rare in practice and synchronous windows are long enough."

- question: "In a fully asynchronous distributed system, why can't a timeout be used to reliably detect that a node has crashed?"
  type: multiple-choice
  options:
    - "Asynchronous systems have no mechanism for maintaining clocks or timers"
    - "In an asynchronous system, there are no bounds on message delay or processing speed, so a timed-out node may simply be slow rather than crashed"
    - "Timeouts require synchronized clocks, which asynchronous systems explicitly prohibit by definition"
    - "Crashed nodes continue emitting delayed messages that make timeout-based detection unreliable"
  answer: 1
  explanation: "The defining property of an asynchronous model is the absence of any bound on message delay or processing time. A message could take a millisecond or a year — you cannot tell. If you set a timeout and a node doesn't respond within it, you face a fundamental ambiguity: is the node crashed, or is it slow? A slow-but-alive node and a crashed node are indistinguishable in this model. This indistinguishability is precisely why timeout-based failure detection only works in synchronous or partially synchronous models, where you can set a timeout larger than the known maximum delay."

- question: "Paxos and Raft guarantee safety (never producing incorrect results) under asynchrony, but require periods of synchrony to guarantee liveness (actually completing a consensus decision)."
  type: true-false
  answer: true
  explanation: "This is the core design property of partial-synchrony algorithms. Safety is unconditional: Paxos and Raft never commit two different values for the same slot, regardless of timing or message reordering. Liveness is conditional: they only guarantee that decisions are eventually made when the network is stable enough (bounded delays, a live leader). During a network partition or high-latency period, they may stall indefinitely without producing a wrong answer. This is the right trade-off: a system that stalls is recoverable; a system that produces incorrect results is not."

- question: "The FLP impossibility result proves that consensus is practically unachievable in modern distributed systems, which is why Paxos and Raft require external coordination services like hardware clocks."
  type: true-false
  answer: false
  explanation: "FLP applies to deterministic algorithms in a purely asynchronous model — a theoretical abstraction. It does not claim consensus is practically impossible. Real systems escape FLP by operating under partial synchrony (not pure asynchrony), using randomization (randomized algorithms can achieve consensus with high probability in asynchronous settings), or relying on failure detectors. Paxos and Raft don't need external coordination services — they use leader election and round-trip message timing internally. FLP is a theoretical bound, not a practical barrier."

- question: "What does it mean for a distributed algorithm to be 'safe under asynchrony but require synchrony for liveness,' and why is this the right design goal for real distributed systems?"
  type: short-answer
  answer: "Safety means the algorithm never produces incorrect results — it never commits two different values, allows an unauthorized operation, or violates an invariant — regardless of network timing, message reordering, or delays. Liveness means the algorithm eventually makes progress — completes a decision, responds to a request. Requiring synchrony only for liveness means the algorithm can tolerate arbitrary network chaos without corrupting state; it just pauses. When the network stabilizes, it resumes and completes. This is the right goal because incorrectness is catastrophic (data corruption, split-brain, inconsistency) while unavailability is recoverable. A system that pauses during a network partition and resumes correctly when it heals is far preferable to one that commits conflicting writes to preserve availability."
  explanation: "This safety-liveness separation maps directly to the CAP theorem intuition: under a partition, you must choose between consistency (safety) and availability (liveness). Partial-synchrony algorithms choose consistency, tolerating temporary unavailability. This is why distributed databases like Zookeeper, etcd, and CockroachDB are described as 'CP' systems — they prioritize correctness over availability during partitions."
```

## Explainer

When you begin designing algorithms for distributed systems, the first question is not "what do I want to compute?" but "what can I assume about the network and the clocks?" The **communication model** defines these assumptions, and the choice fundamentally constrains which problems are solvable and how efficiently. From your introduction to distributed systems, you know that nodes communicate by passing messages over a network. The communication model specifies what guarantees — if any — exist about how long those messages take to arrive.

In the **synchronous model**, there is a known upper bound on message delay and processing time. If you send a message, you know it will arrive within, say, 10 milliseconds — and if it does not, you can conclude the recipient has crashed. This makes algorithm design much simpler: you can use timeouts to detect failures reliably, and you can coordinate rounds of communication where everyone acts in lockstep. Classic synchronous algorithms can solve Byzantine agreement with fewer messages and simpler logic. The catch is that real networks rarely provide hard delay bounds — a garbage collection pause, a congested switch, or a route change can violate any fixed timeout.

In the **asynchronous model**, there are no bounds whatsoever on message delay or processing speed. A message might arrive in a millisecond or an hour — you simply cannot tell. This is the hardest model to work in because you can never distinguish a slow node from a crashed one. The famous **FLP impossibility result** proves that in a purely asynchronous system, no deterministic algorithm can guarantee consensus if even one node might crash. This does not mean consensus is impossible in practice — it means any real solution must use randomization, timeouts, or some form of partial synchrony assumption to make progress.

The **partial synchrony model** bridges the gap and reflects how real systems actually behave. It posits that the system is asynchronous most of the time, but there exist periods of synchrony — intervals where message delays are bounded — that last long enough for algorithms to make progress. Paxos and Raft are designed for this model: they are safe (never produce incorrect results) regardless of timing, but they rely on periods of synchrony for **liveness** (actually reaching a decision). In practice, this means these algorithms always give correct answers but may temporarily stall during network partitions or high latency. When the network stabilizes, they resume and complete. This is why partial synchrony dominates real-world distributed systems design: it honestly models the unreliable networks we have while still permitting useful algorithms.
