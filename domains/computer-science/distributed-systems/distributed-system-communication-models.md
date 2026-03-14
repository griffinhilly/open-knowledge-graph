---
id: distributed-system-communication-models
title: Communication Models in Distributed Systems
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-systems-introduction
  type: hard
builds-toward:
- total-order-broadcast
- byzantine-agreement-algorithms
tags:
- models
- synchrony
- assumptions
stage: abstract-reasoning
status: draft
---

# Communication Models in Distributed Systems

## Core Idea
Distributed systems operate under different communication assumptions: synchronous (bounded network delays and processing time), asynchronous (no bounds on delays), or partial synchrony (periods of synchrony and asynchrony). The choice of model fundamentally determines what consensus algorithms are possible.

## How It's Best Learned
Compare algorithms in different models: Paxos and Raft tolerate asynchrony; synchronous Byzantine agreement requires fewer messages. Understand why certain impossibility results (like FLP) apply to asynchronous systems but not synchronous ones.

## Common Misconceptions
- All real systems are asynchronous; in practice, they are partially synchronous with occasional partitions.
- Synchronous models are only theoretical; synchronous assumptions are useful for bounded-time guarantees in real systems.
