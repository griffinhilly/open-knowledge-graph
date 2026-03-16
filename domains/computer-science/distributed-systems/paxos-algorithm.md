---
id: paxos-algorithm
title: Paxos Consensus Algorithm
domain: computer-science
course: distributed-systems
prerequisites:
- id: consensus-problem
  type: hard
- id: lamport-timestamps
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
status: draft
---

# Paxos Consensus Algorithm

## Core Idea
Paxos is a consensus algorithm tolerating crash failures in asynchronous systems through multiple rounds: proposers prepare proposals with increasing ballot numbers, acceptors promise not to accept lower-numbered proposals, and learners track accepted values. A value is decided when a majority of acceptors accepts it, ensuring agreement and termination under normal conditions.

## How It's Best Learned
Implement single-decree Paxos from scratch, tracing through scenarios with message loss and node crashes.

## Common Misconceptions
Paxos requires synchrony; Paxos is simple to implement; Paxos provides strong leader guarantees.

## Explainer

You already know from the consensus problem that getting distributed nodes to agree on a single value is deceptively hard — any protocol must handle crashes, message loss, and reordering. Paxos solves this by splitting nodes into three roles: **proposers** (who suggest values), **acceptors** (who vote on proposals), and **learners** (who observe the outcome). A single node can play multiple roles, but the separation clarifies the protocol's logic. The key insight is that agreement emerges not from a single round of voting, but from a two-phase protocol that prevents conflicting decisions even when messages are lost or delayed.

In **Phase 1 (Prepare)**, a proposer picks a unique, monotonically increasing **ballot number** and sends a Prepare(n) message to a majority of acceptors. Each acceptor compares n to the highest ballot it has seen. If n is higher, the acceptor promises not to accept any proposal with a lower ballot number and replies with whatever value it has already accepted (if any). Think of this like calling ahead to reserve a meeting slot — you are not yet proposing an agenda, just securing the right to propose one. If a majority of acceptors respond with promises, the proposer knows it has a "lock" that no lower-numbered proposal can break.

In **Phase 2 (Accept)**, the proposer sends an Accept(n, v) message to the same majority, where v is either the value from the highest-numbered previously accepted proposal (if any acceptor reported one) or the proposer's own chosen value. This constraint is the heart of Paxos's safety: if a value was already accepted by some majority in an earlier round, every future proposer will discover it during Phase 1 and re-propose it, ensuring the system converges rather than oscillating. An acceptor accepts the proposal if it has not since promised a higher ballot number. Once a majority of acceptors accept, the value is **decided** and learners can be notified.

The elegance of Paxos is that safety — no two nodes decide different values — holds regardless of timing, crashes, or message loss. However, **liveness** (eventually deciding) requires that proposers do not endlessly compete with increasing ballot numbers, each invalidating the other's Phase 1. In practice, systems use a **distinguished proposer** (leader) to avoid dueling proposals, but this is an optimization, not a requirement of the protocol. Understanding this distinction matters: Paxos the algorithm guarantees safety always and progress eventually, while real implementations layer leader election on top to make progress practical. The leap from single-decree Paxos (agreeing on one value) to Multi-Paxos (agreeing on a sequence of values for state machine replication) is where the protocol moves from elegant theory to complex engineering.
