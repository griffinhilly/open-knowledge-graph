---
id: failure-models-distributed
title: Failure Models in Distributed Systems
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-system-models
  type: hard
builds-toward:
- byzantine-fault-tolerance
- consensus-problem
tags:
- failures
- faults
- robustness
stage: advanced
status: draft
---

# Failure Models in Distributed Systems

## Core Idea
Distributed systems must account for different failure classes: crash failures (nodes stop), omission failures (lost messages), timing failures (delays exceed bounds), and Byzantine failures (nodes act arbitrarily). More severe failure models require stronger algorithms; Byzantine systems are hardest since even faulty nodes appear responsive.

## Explainer

From your study of distributed system models, you know that the behavior of a distributed system depends on the assumptions you make about the network and the nodes. Failure models refine one specific dimension of those assumptions: **how can things go wrong?** The answer determines how robust your algorithms need to be and how much overhead you must pay for correctness. Failure models form a hierarchy, from the mildest to the most adversarial, and understanding this hierarchy is essential before you can reason about fault tolerance or consensus.

The simplest failure type is the **crash failure** (also called fail-stop): a node is either working correctly or it has stopped entirely and never recovers. Importantly, a crashed node does not send corrupted or misleading messages — it simply goes silent. This is the most common assumption in systems like Raft and Paxos. Detecting crashes is straightforward in synchronous systems (use a timeout) and impossible to distinguish from slowness in asynchronous ones. **Omission failures** are one step worse: a node may be running but silently drops some messages — either ones it should have sent (send omission) or ones it should have received (receive omission). A flaky network interface or a full message queue can cause omission failures even when the node's CPU and memory are fine.

**Timing failures** (or performance failures) occur in synchronous systems when a node or message violates the assumed time bounds — a response arrives too late to be useful, even though it is correct. This matters because many synchronous algorithms rely on timeouts for correctness: if a node responds after the timeout, the algorithm may have already treated it as crashed and made an irreversible decision. In asynchronous models, timing failures do not exist as a distinct category because there are no time bounds to violate.

At the top of the hierarchy sit **Byzantine failures**: a node can behave arbitrarily. It might crash, send conflicting messages to different peers, lie about its state, or actively try to sabotage the protocol. This is the most general and most difficult failure model because you cannot trust anything a faulty node says or does. Tolerating Byzantine failures typically requires at least 3f + 1 total nodes to handle f faulty ones — a significant overhead compared to the 2f + 1 needed for crash failures. The practical implication is that you should always choose the weakest (most benign) failure model that matches your actual threat environment. If you control all the nodes in your data center and trust your hardware, crash failures suffice and you get simpler, faster algorithms. If you are building a system where participants might be malicious — as in blockchain networks or multi-party computation — you need Byzantine fault tolerance and must accept its costs.
