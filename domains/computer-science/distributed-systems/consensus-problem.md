---
id: consensus-problem
title: The Consensus Problem
domain: computer-science
course: distributed-systems
prerequisites:
- id: synchronous-asynchronous-systems
  type: hard
- id: failure-models-distributed
  type: hard
- id: formal-logic-propositions
  type: soft
builds-toward:
- paxos-algorithm
- raft-algorithm
- byzantine-fault-tolerance
tags:
- consensus
- agreement
- agreement-protocols
stage: advanced
status: draft
---

# The Consensus Problem

## Core Idea
Consensus requires all non-faulty processes to decide on a single value, even when some processes fail or propose conflicting values. Consensus must satisfy: agreement (all non-faulty processes decide identically), validity (a decided value was proposed), and termination (all non-faulty processes eventually decide). This foundational problem subsumes many practical coordination challenges.

## Questions

```yaml
- question: "A system satisfies agreement and termination but its consensus algorithm always decides the value 0, regardless of what processes propose. Which property is violated?"
  type: multiple-choice
  options: ["Agreement", "Validity", "Termination", "Liveness"]
  answer: 1
  explanation: "Validity requires that the decided value must have been proposed by some process. If the algorithm always decides 0 but no process proposed 0, validity is violated even though all processes agree. This illustrates why validity is a separate, necessary property — agreement alone would permit nonsense decisions."

- question: "The FLP impossibility result proves that consensus cannot be solved in a purely asynchronous system even if only one process may crash-fail."
  type: true-false
  answer: true
  explanation: "The Fischer-Lynch-Paterson (FLP) result (1985) shows that in a fully asynchronous message-passing system, no deterministic algorithm can guarantee consensus if even a single process might fail by crashing. This is because a slow process is indistinguishable from a crashed one, so the algorithm can never safely decide. Practical systems (Paxos, Raft) escape FLP by using timeouts or randomization."

- question: "What is the key behavioral difference between a crash-fault process and a Byzantine-fault process?"
  type: short-answer
  answer: "A crash-fault process simply stops sending messages; a Byzantine-fault process can behave arbitrarily — sending conflicting values to different peers, lying about its state, or colluding with other faulty processes."
  explanation: "This distinction matters enormously for algorithm design. Crash-fault consensus requires f < n/2 faulty processes; Byzantine consensus requires f < n/3. Byzantine faults model adversarial or hardware-corrupted nodes and demand much stronger guarantees."
```

## Explainer

Imagine a group of generals who must unanimously agree on whether to attack or retreat, communicating only by messenger — and some generals may be traitors sending false orders. This is the essence of the consensus problem in distributed systems. The challenge is not just agreement but guaranteed agreement in the presence of failures, and doing so without any central coordinator.

The three properties of consensus — agreement, validity, and termination — each rules out a different trivial cheat. Without agreement, processes could decide different values. Without validity, an algorithm could satisfy agreement by having everyone decide some hardcoded constant regardless of input. Without termination, an algorithm could satisfy the other two by simply never deciding. All three are required simultaneously, and that turns out to be surprisingly hard.

The landmark FLP impossibility theorem (Fischer, Lynch, Paterson, 1985) shows that in a purely asynchronous system — one where message delays have no upper bound — consensus is impossible even if only one process can crash. The intuitive reason: a slow process looks exactly like a crashed one, so there is always some execution where the algorithm cannot determine whether a process has failed or is just delayed, and committing to a decision risks violating agreement in some scenario. Real-world consensus protocols escape this by adding timing assumptions (synchronous or partially synchronous models) or randomization.

The severity of failures also matters. Crash faults (stop-fail) are the gentlest model: failed processes simply go silent. Byzantine faults are the harshest: a faulty process can send contradictory messages to different peers, actively undermining agreement. Algorithms like Paxos and Raft handle crash faults with f < n/2 failures; Byzantine fault-tolerant algorithms require f < n/3, which is why they are reserved for adversarial settings like blockchains.

Understanding the consensus problem is the key to understanding why distributed coordination is hard in practice. Leader election, distributed transactions, and replicated state machines all reduce to consensus. Every time you interact with a system that promises consistency across multiple servers — a distributed database, a payment processor, a coordination service like ZooKeeper — consensus is the invisible foundation making that promise possible.
