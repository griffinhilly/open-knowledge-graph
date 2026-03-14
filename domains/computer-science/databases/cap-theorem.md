---
id: cap-theorem
title: CAP Theorem
domain: computer-science
course: databases
prerequisites:
- id: nosql-concepts
  type: hard
- id: acid-properties
  type: soft
- id: key-value-stores
  type: soft
tags:
- CAP theorem
- consistency
- availability
- partition tolerance
- distributed systems
- CP
- AP
stage: formal-systems
status: validated
---
# CAP Theorem

## Core Idea
The CAP theorem states that a distributed data system can guarantee at most two of three properties: Consistency (every read receives the most recent write or an error), Availability (every request receives a non-error response, possibly stale), and Partition tolerance (the system continues operating despite network partitions). Since partitions are unavoidable in real distributed systems, the practical tradeoff is CP (consistency during partitions, possibly refusing requests) vs. AP (availability during partitions, possibly returning stale data). Most real systems allow tunable consistency rather than a strict binary choice.

## How It's Best Learned
Study the behavior of real systems: how does ZooKeeper (CP) behave during a partition vs. Cassandra (AP)? Understand that CAP describes worst-case partition scenarios, not normal steady-state operation.

## Common Misconceptions
- CAP consistency (linearizability — always reading the latest write) is not the same as ACID consistency (preserving application invariants) — these are different properties with the same word.
- CA systems (sacrificing partition tolerance) do not exist in practical distributed systems — partitions always happen eventually.
- The theorem is a theoretical impossibility result, not a design prescription; PACELC and other models better capture the latency-consistency tradeoffs of real systems.
