---
id: network-partition-tolerance
title: Network Partitions and Partition Tolerance
domain: computer-science
course: distributed-systems
prerequisites:
- id: failure-models-distributed
  type: hard
- id: cap-theorem
  type: soft
builds-toward:
- consistency-models
- eventual-consistency-guarantees
tags:
- failures
- partitions
- availability
- cap
stage: abstract-reasoning
status: draft
---

# Network Partitions and Partition Tolerance

## Core Idea
A network partition occurs when the network becomes segmented, preventing messages from being delivered between parts of the system. Partition tolerance means a system can continue operating despite partitions, but it forces a tradeoff: either unavailable replicas in one partition, or potentially inconsistent data across partitions.

## How It's Best Learned
Consider real scenarios: a data center network split, a slow link making one replica unreachable. Work through what guarantees each partition can make and when they can rejoin.

## Common Misconceptions
- Partitions are rare and can be ignored; in large systems, partitions are inevitable and must be explicitly handled.
- A system can be both consistent and available during a partition; the CAP theorem proves this is impossible if the partition persists.
