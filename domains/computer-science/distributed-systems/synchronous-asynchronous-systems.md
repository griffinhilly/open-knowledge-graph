---
id: synchronous-asynchronous-systems
title: Synchronous vs. Asynchronous Distributed Systems
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-system-models
  type: hard
builds-toward:
- failure-models-distributed
- consensus-problem
tags:
- timing
- models
- asynchrony
stage: advanced
status: draft
---

# Synchronous vs. Asynchronous Distributed Systems

## Core Idea
Synchronous systems guarantee bounded communication rounds and clock rates, enabling deterministic algorithms. Asynchronous systems provide no timing guarantees, reflecting real networks with unbounded delays. Synchrony simplifies reasoning but is unrealistic; asynchrony is realistic but makes some problems provably unsolvable.

## Explainer

From distributed system models, you know that a model defines the assumptions an algorithm can rely on — what can fail, how processes communicate, and crucially, what timing guarantees exist. The distinction between **synchronous** and **asynchronous** systems is the most fundamental timing assumption in distributed computing, and it determines which problems are even solvable.

A **synchronous system** provides three guarantees: messages arrive within a known bounded delay, each process takes a known bounded time to execute a step, and clocks drift by at most a known bounded rate. These bounds do not need to be small — they just need to exist and be known. With these guarantees, you can use timeouts reliably: if you send a message and get no response within the bound, you know the recipient has crashed (not just been slow). This makes failure detection trivial, which in turn makes consensus, leader election, and coordination algorithms straightforward. The catch is that real networks do not provide these guarantees. Internet links can have arbitrarily long delays due to congestion, routing changes, or buffering. A process can be delayed indefinitely by garbage collection pauses or OS scheduling.

An **asynchronous system** assumes nothing about timing. Messages eventually arrive but with no upper bound on delay. Processes eventually take steps but with no upper bound on speed. This model faithfully represents real networks — and it is brutal to work with. The FLP impossibility result (Fischer, Lynch, Paterson, 1985) proves that in a fully asynchronous system, no deterministic algorithm can solve consensus if even one process can crash. The core problem is indistinguishability: you cannot tell whether a process is dead or merely slow, because both look the same — silence.

In practice, systems use a middle ground called **partial synchrony**: the system is asynchronous most of the time but eventually behaves synchronously for long enough to make progress. Protocols like Paxos and Raft are designed for partial synchrony — they are safe (never produce wrong answers) in fully asynchronous conditions, but they only guarantee liveness (eventually making progress) when the network stabilizes. This is why understanding the synchronous/asynchronous distinction matters: it tells you what is achievable, what is impossible, and what requires careful design to work around the gap between theory and practice.
