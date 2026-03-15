---
id: quorum-based-consistency
title: Quorum-Based Consistency
domain: computer-science
course: distributed-systems
prerequisites:
- id: quorum-based-replication
  type: hard
- id: consistency-models
  type: soft
builds-toward:
- strong-consistency-models
- paxos-made-practical
tags:
- quorum
- consistency
- replication
- read-write
stage: concrete-operations
status: draft
---

# Quorum-Based Consistency

## Core Idea
Quorum-based replication requires reads to consult a quorum (majority) of replicas and writes to update a quorum, ensuring any two quorums overlap. This guarantees a reader always sees the latest write (if R + W > N), reducing the need for consensus while still achieving strong consistency.

## How It's Best Learned
Work through scenarios: N=3 replicas, choose R and W such that R + W > N (e.g., R=2, W=2). Show that a write to 2 replicas followed by a read from 2 replicas always sees the new value. Examine what happens if R + W ≤ N (e.g., R=1, W=1).

## Common Misconceptions
- Quorums require exactly a majority; any subset where R + W > N works (e.g., R=1, W=N).
- Quorum reads are always slower; with R=1, a single replica read is fast, but then W must be high to ensure consistency.
