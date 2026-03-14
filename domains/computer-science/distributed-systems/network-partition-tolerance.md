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
