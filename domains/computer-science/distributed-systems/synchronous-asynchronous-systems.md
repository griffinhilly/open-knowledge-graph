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
status: validated
---

# Synchronous vs. Asynchronous Distributed Systems

## Core Idea
Synchronous systems guarantee bounded communication rounds and clock rates, enabling deterministic algorithms. Asynchronous systems provide no timing guarantees, reflecting real networks with unbounded delays. Synchrony simplifies reasoning but is unrealistic; asynchrony is realistic but makes some problems provably unsolvable.

## Questions

```yaml
- question: "In a fully asynchronous distributed system, process A sends a message to process B and receives no response after waiting 10 minutes. What can A correctly conclude?"
  type: multiple-choice
  options:
    - "Process B has crashed, since any working process would have responded by now"
    - "The network is partitioned between A and B"
    - "Nothing definitive — B may have crashed or may simply be very slow, since there is no upper bound on message delay or processing time"
    - "B received the message but chose not to respond, indicating a Byzantine fault"
  answer: 2
  explanation: "This is the core hardness of asynchrony: crashed processes and slow processes are indistinguishable. An asynchronous system guarantees only that messages *eventually* arrive and processes *eventually* take steps — there is no upper bound. No matter how long A waits, it cannot rule out that B is merely slow. This indistinguishability is exactly the reason FLP impossibility holds: you can never safely declare a process dead without risking treating a slow-but-alive process as crashed."

- question: "The FLP impossibility result proves that in a fully asynchronous distributed system, consensus is unsolvable. What is the core reason?"
  type: multiple-choice
  options:
    - "Message loss is too frequent in asynchronous networks for any protocol to succeed"
    - "Asynchronous systems cannot elect a leader, and consensus requires a leader"
    - "A crashed process and a slow process look identical, so no algorithm can safely decide without risking being wrong when a 'dead' process is actually alive"
    - "The theorem only applies when more than half of processes can fail"
  answer: 2
  explanation: "FLP holds even when only *one* process can crash. The impossibility comes from indistinguishability: in any protocol, there must be some state where the system is 'balanced' — one more message or step in either direction could produce a 0 or 1 decision. But because you cannot distinguish a crashed process from a slow one, you cannot force the system out of that balanced state without risking a safety violation. Options A and D misstate the theorem; option B is an incorrect reduction (Paxos has no permanent leader requirement)."

- question: "A synchronous distributed system requires that all messages arrive within one second to qualify as synchronous."
  type: true-false
  answer: false
  explanation: "Synchrony requires that timing bounds *exist and are known* — not that they be small. A system where messages are guaranteed to arrive within 10 minutes is synchronous. A system where messages can be delayed for an arbitrarily long but unspecified time is asynchronous. The key property is whether you can set a timeout and trust it: in a synchronous system, a timeout lets you infer failure; in an asynchronous system, no timeout gives you that guarantee."

- question: "Protocols like Paxos and Raft are designed for partial synchrony: they guarantee safety (no incorrect decisions) under fully asynchronous conditions, but only guarantee liveness (making progress) when the network eventually stabilizes."
  type: true-false
  answer: true
  explanation: "This is the correct characterization of partially synchronous protocols. Safety — never committing conflicting values — holds even during network partitions and arbitrary delays. But progress — actually reaching a decision — requires that the system become 'synchronous enough' for a quorum to communicate without timeout interference. This design reflects the FLP result: you cannot guarantee both safety and liveness under full asynchrony, so these protocols sacrifice guaranteed liveness while preserving safety."

- question: "Why does the asynchronous model make consensus provably impossible even if only one process might crash, while the synchronous model allows consensus to be solved?"
  type: short-answer
  answer: "In an asynchronous system, there is no timeout that reliably distinguishes a crashed process from a slow one — both look like silence. Any consensus algorithm must at some point decide, but doing so risks incorrectly treating a slow process as dead, potentially violating agreement or validity. In a synchronous system, known time bounds let you detect failure definitively: if a process doesn't respond within the guaranteed bound, it has crashed. This makes failure detection reliable, which is what consensus algorithms need to safely coordinate."
  explanation: "FLP impossibility (Fischer, Lynch, Paterson 1985) formalizes this: every deterministic consensus protocol has a 'bivalent' state where both outcomes remain possible, and an adversarial scheduler can delay messages indefinitely to keep the system in that state. With synchrony, the scheduler is constrained by known bounds, allowing protocols to escape bivalent states safely."
```

## Explainer

From distributed system models, you know that a model defines the assumptions an algorithm can rely on — what can fail, how processes communicate, and crucially, what timing guarantees exist. The distinction between **synchronous** and **asynchronous** systems is the most fundamental timing assumption in distributed computing, and it determines which problems are even solvable.

A **synchronous system** provides three guarantees: messages arrive within a known bounded delay, each process takes a known bounded time to execute a step, and clocks drift by at most a known bounded rate. These bounds do not need to be small — they just need to exist and be known. With these guarantees, you can use timeouts reliably: if you send a message and get no response within the bound, you know the recipient has crashed (not just been slow). This makes failure detection trivial, which in turn makes consensus, leader election, and coordination algorithms straightforward. The catch is that real networks do not provide these guarantees. Internet links can have arbitrarily long delays due to congestion, routing changes, or buffering. A process can be delayed indefinitely by garbage collection pauses or OS scheduling.

An **asynchronous system** assumes nothing about timing. Messages eventually arrive but with no upper bound on delay. Processes eventually take steps but with no upper bound on speed. This model faithfully represents real networks — and it is brutal to work with. The FLP impossibility result (Fischer, Lynch, Paterson, 1985) proves that in a fully asynchronous system, no deterministic algorithm can solve consensus if even one process can crash. The core problem is indistinguishability: you cannot tell whether a process is dead or merely slow, because both look the same — silence.

In practice, systems use a middle ground called **partial synchrony**: the system is asynchronous most of the time but eventually behaves synchronously for long enough to make progress. Protocols like Paxos and Raft are designed for partial synchrony — they are safe (never produce wrong answers) in fully asynchronous conditions, but they only guarantee liveness (eventually making progress) when the network stabilizes. This is why understanding the synchronous/asynchronous distinction matters: it tells you what is achievable, what is impossible, and what requires careful design to work around the gap between theory and practice.
