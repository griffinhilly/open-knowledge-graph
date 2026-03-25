---
id: paxos-algorithm
title: Paxos Consensus Algorithm
domain: computer-science
course: distributed-systems
prerequisites:
- id: consensus-problem
  type: hard
- id: logical-clocks
  type: soft
- id: mathematical-induction-intro
  type: soft
builds-toward:
- state-machine-replication
tags:
- paxos
- consensus
- fault-tolerance
stage: advanced
status: validated
---

# Paxos Consensus Algorithm

## Core Idea
Paxos is a consensus algorithm tolerating crash failures in asynchronous systems through multiple rounds: proposers prepare proposals with increasing ballot numbers, acceptors promise not to accept lower-numbered proposals, and learners track accepted values. A value is decided when a majority of acceptors accepts it, ensuring agreement and termination under normal conditions.

## How It's Best Learned
Implement single-decree Paxos from scratch, tracing through scenarios with message loss and node crashes.

## Common Misconceptions
Paxos requires synchrony; Paxos is simple to implement; Paxos provides strong leader guarantees.

## Questions

```yaml
- question: "A proposer sends Prepare(5) to a majority of acceptors. Two reply with promises; one reports it previously accepted value 'blue' at ballot 3, the other reports no previous acceptance. What value must the proposer use in its Phase 2 Accept message?"
  type: multiple-choice
  options:
    - "Any value the proposer chooses, since ballot 5 supersedes ballot 3"
    - "'blue', because it must use the value from the highest-numbered previously accepted proposal it discovered"
    - "The value that the majority of acceptors accepted, but only one reported 'blue' so it cannot be determined"
    - "The proposer's own preferred value, since it has not yet been committed by a majority"
  answer: 1
  explanation: "This is the heart of Paxos's safety guarantee. The proposer must adopt 'blue' in Phase 2. The reason: if 'blue' was accepted by some acceptor at ballot 3, it may have already been decided by a majority in that earlier round. By forcing any new proposer to re-propose the highest-ballot value it discovers, Paxos ensures that a decided value can never be superseded by a different one. If the proposer were free to use its own value, two different values could be decided in different rounds — violating the consensus invariant."

- question: "A Paxos cluster of 5 nodes has 3 nodes simultaneously crash. The remaining 2 nodes attempt to run a new Paxos round. What happens?"
  type: multiple-choice
  options:
    - "Progress continues because 2 nodes can still communicate and agree"
    - "The 2 remaining nodes can decide a value since they still form a quorum for a 3-node subset"
    - "Progress is impossible because a majority (at least 3 out of 5) of acceptors cannot be reached, so neither Phase 1 nor Phase 2 can collect enough promises or acceptances"
    - "Paxos automatically reconfigures to treat the 2 remaining nodes as a complete cluster"
  answer: 2
  explanation: "Paxos requires a majority (quorum) of acceptors to respond in both phases. With 5 nodes, a majority is at least 3. With only 2 nodes reachable, no quorum can be formed, so no proposal can collect enough promises (Phase 1) or acceptances (Phase 2). The system is stuck — it cannot make progress until at least one more node recovers. This is the liveness cost of Paxos: it tolerates up to ⌊(n-1)/2⌋ failures for a cluster of n nodes. With 5 nodes, it tolerates 2 failures, not 3."

- question: "Paxos guarantees that if a value is decided (accepted by a majority), no future round can decide a different value, even if messages are lost or delayed."
  type: true-false
  answer: true
  explanation: "This is Paxos's safety guarantee, and it is unconditional — it holds regardless of timing, message loss, or how many proposers are competing. The mechanism is Phase 1: any proposer with a higher ballot number must first poll a majority of acceptors. If a value was previously decided by a majority, at least one acceptor in any future quorum must have accepted it and will report it in Phase 1. The new proposer is then forced to re-propose that value. Safety is preserved even in the worst asynchronous scenarios that violate liveness."

- question: "A Paxos system with a single designated proposer (leader) is guaranteed to always make progress, because competing proposers can no longer issue conflicting Prepare messages."
  type: true-false
  answer: false
  explanation: "Leader election improves liveness in practice, but it does not guarantee progress. In an asynchronous network, no algorithm can guarantee both safety and liveness (the FLP impossibility result). A leader can crash or become network-partitioned, and detecting this reliably requires eventually correct failure detectors — which themselves cannot be perfectly guaranteed in asynchronous systems. Paxos guarantees safety always; it guarantees liveness only under favorable conditions (bounded message delays, correct failure detection). A leader helps by eliminating dueling proposers, but it does not solve the fundamental asynchrony problem."

- question: "In Phase 2 of Paxos, why must a proposer use the value from the highest-numbered previously accepted proposal it discovered in Phase 1, rather than proposing its own preferred value?"
  type: short-answer
  answer: "Because that value may have already been decided in a prior round. If an earlier round reached a majority acceptance, the decided value must propagate forward — any future decision must agree with it. By requiring the proposer to adopt and re-propose the highest-ballot previously-accepted value it discovers in Phase 1, Paxos ensures that if any value was decided before this round started, it will be the value decided again. This is the invariant that prevents two different values from ever being decided. If the proposer could freely use its own value, a second decision on a different value would be possible, violating consensus."
  explanation: "The safety proof relies entirely on this constraint. Phase 1 acts as a 'survey': what, if anything, has already been committed? If ballot n is the highest previously accepted ballot, then a majority of acceptors accepted that value at ballot n. Any quorum used in Phase 2 of the new proposal will overlap with that majority by at least one acceptor, who will always report the previously accepted value. The proposer's adoption rule then guarantees continuity."
```

## Explainer

You already know from the consensus problem that getting distributed nodes to agree on a single value is deceptively hard — any protocol must handle crashes, message loss, and reordering. Paxos solves this by splitting nodes into three roles: **proposers** (who suggest values), **acceptors** (who vote on proposals), and **learners** (who observe the outcome). A single node can play multiple roles, but the separation clarifies the protocol's logic. The key insight is that agreement emerges not from a single round of voting, but from a two-phase protocol that prevents conflicting decisions even when messages are lost or delayed.

In **Phase 1 (Prepare)**, a proposer picks a unique, monotonically increasing **ballot number** and sends a Prepare(n) message to a majority of acceptors. Each acceptor compares n to the highest ballot it has seen. If n is higher, the acceptor promises not to accept any proposal with a lower ballot number and replies with whatever value it has already accepted (if any). Think of this like calling ahead to reserve a meeting slot — you are not yet proposing an agenda, just securing the right to propose one. If a majority of acceptors respond with promises, the proposer knows it has a "lock" that no lower-numbered proposal can break.

In **Phase 2 (Accept)**, the proposer sends an Accept(n, v) message to the same majority, where v is either the value from the highest-numbered previously accepted proposal (if any acceptor reported one) or the proposer's own chosen value. This constraint is the heart of Paxos's safety: if a value was already accepted by some majority in an earlier round, every future proposer will discover it during Phase 1 and re-propose it, ensuring the system converges rather than oscillating. An acceptor accepts the proposal if it has not since promised a higher ballot number. Once a majority of acceptors accept, the value is **decided** and learners can be notified.

The elegance of Paxos is that safety — no two nodes decide different values — holds regardless of timing, crashes, or message loss. However, **liveness** (eventually deciding) requires that proposers do not endlessly compete with increasing ballot numbers, each invalidating the other's Phase 1. In practice, systems use a **distinguished proposer** (leader) to avoid dueling proposals, but this is an optimization, not a requirement of the protocol. Understanding this distinction matters: Paxos the algorithm guarantees safety always and progress eventually, while real implementations layer leader election on top to make progress practical. The leap from single-decree Paxos (agreeing on one value) to Multi-Paxos (agreeing on a sequence of values for state machine replication) is where the protocol moves from elegant theory to complex engineering.
