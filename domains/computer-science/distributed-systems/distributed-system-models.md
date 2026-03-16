---
id: distributed-system-models
title: Models of Distributed Computation
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-systems-overview
  type: hard
builds-toward:
- synchronous-asynchronous-systems
- failure-models-distributed
tags:
- models
- computation
- theory
stage: advanced
status: draft
---

# Models of Distributed Computation

## Core Idea
Distributed computation models formalize assumptions about timing, communication, and failures. Synchronous models assume bounded message delays and clock synchronization; asynchronous models make no timing guarantees. The choice of model fundamentally affects which problems are solvable and determines which algorithms can guarantee correctness.

## Explainer

From your distributed systems overview, you understand the basic challenge: multiple computers communicating over a network, with no shared memory and no guarantee that messages arrive quickly or at all. A **model of distributed computation** is a set of formal assumptions about this environment — how fast messages travel, how reliable processes are, and what kinds of failures can occur. These assumptions are not descriptions of any particular real system; they are simplifications that let you prove what is and is not possible.

The **synchronous model** makes the strongest assumptions. It says there exists a known upper bound on message delivery time, a known upper bound on the time each process takes to execute a step, and clocks that are synchronized within a known drift. Under these assumptions, many problems become straightforward. For instance, a process can detect that another process has crashed simply by waiting for the maximum message delay — if no response arrives within that bound, the other process must be down. Consensus algorithms in the synchronous model are relatively simple because timeout-based failure detection is reliable.

The **asynchronous model** makes no timing assumptions at all. Messages can take arbitrarily long to arrive. Processes can pause for arbitrary periods before executing the next step. There is no upper bound you can rely on. This is a much harder world to design for because you cannot distinguish a slow process from a crashed one — a message that has not arrived might still be in transit. The asynchronous model is closer to the reality of the internet, where network congestion, garbage collection pauses, and load spikes can cause unpredictable delays.

Between these extremes lies the **partially synchronous model**, which assumes that timing bounds exist but are unknown, or that the system behaves asynchronously for some period but eventually becomes synchronous. This model captures the practical reality of most distributed systems: most of the time, messages arrive within a few milliseconds, but occasionally there are bursts of delay. Most practical consensus algorithms (like Paxos and Raft) are designed for partial synchrony — they guarantee safety always, but only guarantee progress (liveness) when the system is behaving synchronously enough for timeouts to work.

The choice of model is not a matter of preference — it determines what you can prove. The same problem that is solvable in the synchronous model may be provably impossible in the asynchronous model. Understanding these models is essential before studying impossibility results and consensus algorithms, because every theorem and every algorithm comes with a model attached. When someone says "consensus is impossible," the first question is always: in which model?
