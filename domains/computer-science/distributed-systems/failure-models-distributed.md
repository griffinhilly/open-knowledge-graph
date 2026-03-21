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

## Questions

```yaml
- question: "A node in your distributed system is responding to messages, but sends conflicting state information to different peers. Which failure model does this exemplify?"
  type: multiple-choice
  options:
    - "Crash failure — the node has stopped and is unresponsive"
    - "Omission failure — the node is silently dropping some messages"
    - "Byzantine failure — the node behaves arbitrarily, including sending inconsistent information to different peers"
    - "Timing failure — the node's responses are arriving after the deadline"
  answer: 2
  explanation: "Byzantine failure is the only model in which a faulty node remains active yet can send incorrect or conflicting messages to different peers. Crash failures produce silence; omission failures drop messages but do not fabricate them; timing failures concern latency, not content. A node that actively lies or sends conflicting data is the defining case of Byzantine behavior."

- question: "A system must tolerate f faulty nodes. How many total nodes are required for Byzantine fault tolerance compared to crash fault tolerance?"
  type: multiple-choice
  options:
    - "The same — both require 2f + 1 nodes, since faulty nodes must be outvoted"
    - "More — Byzantine tolerance requires 3f + 1 nodes, while crash tolerance requires only 2f + 1"
    - "Fewer — crash failures are harder to detect and therefore require greater redundancy"
    - "More — Byzantine tolerance requires 4f + 1 nodes, while crash tolerance requires 2f + 1"
  answer: 1
  explanation: "Crash fault tolerance requires 2f + 1 nodes so a majority of honest nodes can outvote crashed ones. Byzantine fault tolerance requires 3f + 1 because a Byzantine node can send conflicting votes to different peers — you need enough honest nodes to reach agreement even when f nodes collude and misrepresent. The extra overhead is the direct cost of the more adversarial failure model."

- question: "In an asynchronous distributed system, timing failures are the most dangerous failure category because the network provides no delay bounds."
  type: true-false
  answer: false
  explanation: "Timing failures are only defined for synchronous systems — those that specify upper bounds on message delivery and processing time. Asynchronous systems make no timing assumptions, so there are no bounds to violate and timing failures do not exist as a category. Byzantine failures remain the most adversarial type in any model. In asynchronous systems, the inability to distinguish a crashed node from a slow one is a fundamental detectability problem, but it belongs to crash-failure reasoning, not a separate failure class."

- question: "A system designed to tolerate Byzantine failures can also correctly handle crash and omission failures, since those are strictly weaker failure modes."
  type: true-false
  answer: true
  explanation: "The failure hierarchy is nested: crash ⊂ omission ⊂ Byzantine. An algorithm that survives Byzantine behavior handles all weaker modes as special cases — a crashed node is simply a Byzantine node that goes permanently silent, and an omission failure is a Byzantine node that drops messages without fabricating them. The reverse is not true: crash-tolerant algorithms can fail completely if Byzantine faults occur, since they assume faulty nodes are silent, not deceptive."

- question: "Why should a distributed system designer choose the weakest failure model that accurately reflects their threat environment, rather than always designing for Byzantine fault tolerance?"
  type: short-answer
  answer: "Because more adversarial failure models require substantially more expensive algorithms. Byzantine fault tolerance demands 3f + 1 nodes (vs. 2f + 1 for crash), extra message rounds, and higher computational cost. If all nodes are in a trusted data center where hardware failures are the only realistic threat, crash-failure assumptions yield simpler, faster protocols with equivalent real-world correctness. Over-engineering for Byzantine threats that cannot occur wastes resources and adds complexity without benefit."
  explanation: "The principle is threat-model alignment: the failure model should match the actual adversarial environment. Byzantine tolerance is essential when participants may be actively malicious (blockchain, multi-party computation with untrusted parties). It is unnecessary and costly when you control all nodes and trust the hardware. Choosing the weakest sufficient model minimizes overhead while maintaining correctness guarantees for the realistic threat surface."
```

## Explainer

From your study of distributed system models, you know that the behavior of a distributed system depends on the assumptions you make about the network and the nodes. Failure models refine one specific dimension of those assumptions: **how can things go wrong?** The answer determines how robust your algorithms need to be and how much overhead you must pay for correctness. Failure models form a hierarchy, from the mildest to the most adversarial, and understanding this hierarchy is essential before you can reason about fault tolerance or consensus.

The simplest failure type is the **crash failure** (also called fail-stop): a node is either working correctly or it has stopped entirely and never recovers. Importantly, a crashed node does not send corrupted or misleading messages — it simply goes silent. This is the most common assumption in systems like Raft and Paxos. Detecting crashes is straightforward in synchronous systems (use a timeout) and impossible to distinguish from slowness in asynchronous ones. **Omission failures** are one step worse: a node may be running but silently drops some messages — either ones it should have sent (send omission) or ones it should have received (receive omission). A flaky network interface or a full message queue can cause omission failures even when the node's CPU and memory are fine.

**Timing failures** (or performance failures) occur in synchronous systems when a node or message violates the assumed time bounds — a response arrives too late to be useful, even though it is correct. This matters because many synchronous algorithms rely on timeouts for correctness: if a node responds after the timeout, the algorithm may have already treated it as crashed and made an irreversible decision. In asynchronous models, timing failures do not exist as a distinct category because there are no time bounds to violate.

At the top of the hierarchy sit **Byzantine failures**: a node can behave arbitrarily. It might crash, send conflicting messages to different peers, lie about its state, or actively try to sabotage the protocol. This is the most general and most difficult failure model because you cannot trust anything a faulty node says or does. Tolerating Byzantine failures typically requires at least 3f + 1 total nodes to handle f faulty ones — a significant overhead compared to the 2f + 1 needed for crash failures. The practical implication is that you should always choose the weakest (most benign) failure model that matches your actual threat environment. If you control all the nodes in your data center and trust your hardware, crash failures suffice and you get simpler, faster algorithms. If you are building a system where participants might be malicious — as in blockchain networks or multi-party computation — you need Byzantine fault tolerance and must accept its costs.
