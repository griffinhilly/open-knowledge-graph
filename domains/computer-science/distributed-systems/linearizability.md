---
id: linearizability
title: Linearizability
domain: computer-science
course: distributed-systems
prerequisites:
- id: consistency-models
  type: hard
builds-toward:
- two-phase-commit-protocol
- strong-eventual-consistency
tags:
- consistency
- formal-semantics
- correctness
stage: advanced
status: validated
---

# Linearizability

## Core Idea
Linearizability is the strongest consistency model: all operations appear to execute atomically at some point between their invocation and completion, and the execution respects a total order. A linearizable system behaves as if there is a single copy of the data. This model prevents stale reads, causality violations, and ensures a consistent view of shared state across all clients.

## How It's Best Learned
Compare linearizable and non-linearizable execution histories side by side. Understand why linearizability is stricter than sequential consistency and more expensive to implement. Implement a simple linearizable register and test with concurrent operations from multiple clients.

## Common Misconceptions
- Linearizability is the same as serializability (linearizability is stronger and applies to concurrent objects, not just transactions). - Linearizability requires centralized state (distributed linearizable systems exist). - Linearizability solves all consistency problems (availability and latency are separate concerns).

## Questions

```yaml
- question: "Alice writes value X to a linearizable key-value store and the write completes. She calls Bob and tells him to read the key. Bob issues a read. What does linearizability guarantee?"
  type: multiple-choice
  options:
    - "Nothing — linearizability only applies to operations from the same client"
    - "Bob will see value X, because Alice's write completed before Bob's read began, and linearizability ensures reads reflect all prior completed writes"
    - "Bob may or may not see X — linearizability only guarantees eventual consistency"
    - "Bob will see X only if Alice and Bob contact the same server replica"
  answer: 1
  explanation: "This is the defining scenario for linearizability. Alice's write completed (in real wall-clock time) before Bob's read began. Linearizability requires that Bob's read must observe Alice's write, because the write's linearization point precedes the start of the read. Sequential consistency would not guarantee this — it only requires some legal ordering, not one that respects actual real-time causality across clients."

- question: "A distributed lock service requires that if client A releases a lock and client B then acquires it, B is guaranteed to see all state written by A before the release. Which consistency model is required?"
  type: multiple-choice
  options:
    - "Eventual consistency — the data will propagate to B eventually"
    - "Sequential consistency — any total ordering is sufficient for lock correctness"
    - "Linearizability — real-time ordering must be preserved so B is guaranteed to see A's writes"
    - "Causal consistency — tracking causally related operations is sufficient"
  answer: 2
  explanation: "Lock release and acquisition are real-time-ordered events from different clients. Linearizability guarantees that B's read after acquiring the lock reflects everything completed before B's operation began. Eventual consistency provides no timing guarantee. Sequential consistency does not require respecting real wall-clock time, so B might read stale data even after properly acquiring the lock. Only linearizability provides the required guarantee."

- question: "A linearizable distributed system must use a single physical server to maintain its 'single copy' behavioral guarantee."
  type: true-false
  answer: false
  explanation: "Linearizability is a property of observable behavior, not implementation. Distributed systems achieve linearizability using consensus protocols like Raft or Paxos, which coordinate among multiple physical replicas to ensure every operation appears atomic at a single point in time. The 'single copy' semantics is an illusion maintained by the protocol — the physical implementation always involves multiple nodes."

- question: "Sequential consistency and linearizability both produce a total order of operations, so they provide identical guarantees to distributed system clients."
  type: true-false
  answer: false
  explanation: "Both produce a total order, but linearizability adds a critical constraint: that total order must respect real wall-clock time for non-overlapping operations. Sequential consistency only requires that some legal total order exists. The Alice-calls-Bob scenario illustrates the gap: sequential consistency does not guarantee Bob sees Alice's completed write; linearizability does, because it respects the actual real-time ordering."

- question: "Why does achieving linearizability in a distributed system require consensus protocols like Paxos or Raft, and what does this cost?"
  type: short-answer
  answer: "To ensure every operation appears atomic at a single point in time across all replicas, replicas must agree on a total order of operations — which requires consensus. Consensus requires multiple network round-trips between replicas, adding latency. More critically, the CAP theorem forces a tradeoff: during a network partition, a linearizable system must refuse requests from the isolated partition (sacrificing availability) to preserve consistency."
  explanation: "Every write must be confirmed by a quorum of replicas before being considered complete. This eliminates stale reads but means any replica outage or network partition can cause writes to stall. Systems like ZooKeeper and etcd accept this tradeoff for coordination tasks where correctness is paramount; they sacrifice availability to preserve linearizable semantics."
```

## Explainer

From your study of consistency models, you know that distributed systems must choose how much ordering and freshness to guarantee when multiple nodes hold copies of the same data. **Linearizability** sits at the top of that hierarchy — it is the strongest single-object consistency model, and it makes a distributed system behave as though there is only one copy of the data, accessed by one operation at a time.

The core guarantee is this: every operation appears to take effect **atomically** at some single point in time between when the client issued the request and when the client received the response. This point is called the **linearization point**. If client A's write completes before client B's read begins (in real, wall-clock time), then B is guaranteed to see A's write. There is no window where stale data can leak through. Imagine a shared whiteboard in a room — anyone who walks in sees whatever was most recently written. Linearizability gives you that same property even when the "whiteboard" is replicated across machines in different data centers.

Compare this with **sequential consistency**, which also produces a total order of operations but does not require that order to match real time. Sequential consistency says "there exists some legal ordering," while linearizability says "that ordering must respect the actual wall-clock sequence of non-overlapping operations." The distinction matters when two clients coordinate out of band — for example, if Alice writes a value and then calls Bob on the phone to say "go read it," linearizability guarantees Bob sees the write. Sequential consistency does not.

The cost of linearizability is significant. The CAP theorem tells us that a linearizable system cannot remain both consistent and available during a network partition — it must sacrifice availability by refusing to serve requests from the minority partition. In practice, achieving linearizability requires coordination protocols like consensus (Paxos, Raft) or careful use of a single leader, both of which add latency. This is why many real-world systems offer weaker consistency by default and reserve linearizability for operations that truly need it — like acquiring a distributed lock or performing a compare-and-swap on a configuration value.
