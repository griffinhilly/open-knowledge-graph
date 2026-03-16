---
id: flp-impossibility
title: FLP Impossibility Theorem
domain: computer-science
course: distributed-systems
prerequisites:
- id: consensus-problem
  type: hard
- id: synchronous-asynchronous-systems
  type: hard
builds-toward:
- raft-algorithm
- paxos-algorithm
tags:
- impossibility
- bounds
- theory
- flp
stage: advanced
status: draft
---

# FLP Impossibility Theorem

## Core Idea
The FLP impossibility theorem proves that in asynchronous systems with even one crash failure, no algorithm can guarantee both safety (never violate agreement) and liveness (all processes terminate) for consensus. This foundational result shows that real systems must assume synchrony, use randomization, or sacrifice liveness (e.g., timeouts) to solve consensus.

## Explainer

You understand the consensus problem: a set of processes must agree on a single value, and once they decide, the decision is final. You also know the distinction between synchronous and asynchronous system models — in particular, that asynchronous systems provide no upper bound on message delivery time or processing speed. The **FLP impossibility theorem** (named after Fischer, Lynch, and Paterson, 1985) connects these two concepts with a surprising result: in a purely asynchronous system where even one process can crash, no deterministic algorithm can guarantee consensus.

To understand why, consider what makes asynchronous systems so difficult. If a process has not responded, you cannot tell whether it has crashed or is merely slow. Any algorithm that waits for all processes to respond risks waiting forever if one has crashed — violating **liveness** (the guarantee that a decision is eventually reached). But any algorithm that proceeds without hearing from all processes risks making a decision that a slow (not crashed) process would have disagreed with — potentially violating **safety** (the guarantee that all processes agree on the same value). The FLP result proves that this is not a shortcoming of existing algorithms; it is a fundamental property of the model itself.

The proof works by showing that any deterministic consensus algorithm in an asynchronous system must have a **bivalent** initial configuration — a starting state from which both decision values (0 and 1) are still reachable depending on the order of message deliveries. The proof then demonstrates that from any bivalent state, there always exists a sequence of message delivery orderings that keeps the system bivalent indefinitely, never forcing a decision. Because the asynchronous model allows messages to be delayed arbitrarily, this adversarial scheduling is a valid execution of the system. The algorithm is perpetually one step away from deciding but never commits.

What makes FLP profound is not that it says consensus is hard — it says consensus is *impossible* under these specific conditions. But notice the conditions are very precise: deterministic algorithm, fully asynchronous model, even one crash failure. Real systems escape the impossibility by relaxing one of these assumptions. **Paxos and Raft** relax the asynchrony assumption — they assume partial synchrony where timeouts eventually work, sacrificing liveness during periods of asynchrony but guaranteeing safety always. **Randomized algorithms** relax determinism — by flipping coins, processes can break the adversarial scheduling that keeps the system bivalent. Understanding FLP is essential because it explains *why* every practical consensus algorithm makes the tradeoffs it does — not by choice, but by mathematical necessity.
