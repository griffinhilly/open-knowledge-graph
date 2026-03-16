---
id: total-order-broadcast
title: Total Order Broadcast and Strong Consistency
domain: computer-science
course: distributed-systems
prerequisites:
- id: happened-before-relation-causality
  type: hard
- id: consensus-problem
  type: hard
builds-toward:
- state-machine-replication
tags:
- broadcast
- ordering
- consensus
- replication
stage: advanced
status: draft
---

# Total Order Broadcast and Strong Consistency

## Core Idea
Total order broadcast guarantees all processes deliver messages in the same order, which is stronger than causal order (preserving causality is not enough if concurrent messages can be delivered in different orders). It is equivalent to consensus and is the basis for state machine replication.

## How It's Best Learned
Compare scenarios: causal delivery allows reordering of concurrent messages, total order does not. Implement a simple total order broadcast using a coordinator that assigns sequence numbers, then note the bottleneck and why consensus is needed for robustness.

## Common Misconceptions
- Total order is always needed; many applications only need causal order or even weaker guarantees.
- Implementing total order is cheap; any reliable total order has a bottleneck (coordinator) or requires consensus, which is expensive.

## Explainer

You already understand the happened-before relation and how it defines a partial order on events: if event A causally precedes event B, every node must see A before B. But what about **concurrent** events — those with no causal relationship? Causal broadcast lets different nodes deliver concurrent messages in different orders. For many applications this is fine, but consider a replicated bank account where two concurrent operations each deduct from the same balance. If node 1 processes deduction A then B, and node 2 processes B then A, they might diverge — one allows both and the other rejects the second. **Total order broadcast** eliminates this problem by guaranteeing that all nodes deliver all messages in exactly the same sequence.

The formal definition has two properties: **total order** (if any two correct processes both deliver messages m1 and m2, they deliver them in the same order) and **reliability** (if a correct process delivers a message, all correct processes eventually deliver it). These two properties together are surprisingly powerful. If every node starts in the same state and applies the same sequence of operations, they will end in the same state — this is exactly the **state machine replication** principle that total order broadcast enables.

The simplest implementation uses a single **coordinator** node that assigns sequence numbers to all messages. Every node sends its messages to the coordinator, which stamps them with increasing numbers and broadcasts them. Nodes deliver messages in sequence number order. This works, but the coordinator is a bottleneck and a single point of failure. If the coordinator crashes, the system stalls until a new one is elected — and electing a new coordinator without losing or reordering messages is itself a consensus problem.

This reveals the deep equivalence: **total order broadcast and consensus are computationally equivalent**. Given a consensus algorithm, you can build total order broadcast (use consensus to agree on each next message in the sequence). Given total order broadcast, you can solve consensus (broadcast your proposed value; the first one delivered wins). This equivalence means that total order broadcast inherits the impossibility results and performance costs of consensus — it cannot be implemented in a purely asynchronous system with crash failures (FLP impossibility), and practical implementations require either timing assumptions or a leader to make progress. Understanding this equivalence clarifies why strong consistency in distributed systems is fundamentally expensive: it requires solving consensus, whether explicitly or through an equivalent mechanism like total order broadcast.
