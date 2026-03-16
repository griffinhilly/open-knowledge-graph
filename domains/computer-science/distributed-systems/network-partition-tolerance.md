---
id: network-partition-tolerance
title: Network Partition Tolerance and Split-Brain
domain: computer-science
course: distributed-systems
prerequisites:
- id: failure-models-distributed
  type: hard
- id: cap-theorem
  type: hard
builds-toward:
- distributed-transactions-2pc
- leader-election-algorithms
tags:
- fault-tolerance
- partitions
- split-brain
stage: advanced
status: draft
---

# Network Partition Tolerance and Split-Brain

## Core Idea
Network partition tolerance describes how a distributed system behaves when the network splits into isolated components that cannot communicate. A partition-tolerant system continues operating on both sides, but this can lead to split-brain: multiple components may make conflicting decisions. The CAP theorem states you cannot have consistency, availability, and partition tolerance together.

## Explainer

You already know from the CAP theorem that a distributed system cannot simultaneously guarantee consistency, availability, and partition tolerance — and that network partitions are not optional failures you can engineer away, but inevitable realities of any system spanning multiple machines. **Network partition tolerance** is the property that a system continues to function even when the network fragments into groups of nodes that cannot reach each other. The question is not whether partitions happen, but what your system does when they do.

Imagine a database replicated across two data centers connected by a wide-area link. If that link goes down, each data center can still receive client requests — but neither can coordinate with the other. This is a **partition**. A partition-tolerant system keeps serving requests on both sides rather than shutting down entirely. But this creates an immediate tension: if both sides accept writes independently, they may make conflicting decisions about the same data. User A updates their profile on side 1, while user B updates the same profile on side 2. When the network heals, the system has two divergent versions with no obvious winner. This is the **split-brain** problem.

Systems handle split-brain through the tradeoff the CAP theorem forces. A **CP system** (consistency over availability) stops serving requests on the minority side of the partition — it refuses to answer rather than risk inconsistency. ZooKeeper works this way: if a node cannot reach a quorum, it rejects operations. An **AP system** (availability over consistency) keeps serving on both sides and reconciles conflicts after the partition heals, using techniques like last-writer-wins timestamps or conflict-free replicated data types (CRDTs). Dynamo-style databases take this approach.

The practical challenge is that most real systems need different tradeoffs for different operations. A shopping cart can tolerate temporary inconsistency (merge conflicts later), but a bank balance transfer cannot. This leads to hybrid designs where some paths through the system are CP and others are AP. Understanding partition tolerance means recognizing that the design choice is not a global setting but a per-operation decision about what kind of incorrectness your application can tolerate during the minutes or hours when the network is split.
