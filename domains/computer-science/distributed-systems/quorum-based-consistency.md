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
stage: advanced
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

## Explainer

You already know from quorum-based replication that distributing data across multiple replicas improves availability — if one node fails, others still serve requests. The fundamental question is: how do you ensure a reader sees the most recent write when data lives on multiple nodes that may be out of sync? Quorum-based consistency answers this with a simple but powerful mathematical constraint.

Consider a system with **N replicas**. Every write must be acknowledged by at least **W** replicas before it is considered successful. Every read must query at least **R** replicas and take the most recent value. The key invariant is **R + W > N**. When this holds, any read quorum and any write quorum must share at least one replica in common — and that overlapping replica has seen the latest write. Picture N = 5 replicas arranged in a circle. If a write goes to any 3 of them (W = 3) and a read queries any 3 of them (R = 3), there is no way to pick two groups of 3 from 5 without at least one node appearing in both groups. That shared node guarantees the read sees fresh data.

The beauty of this approach is its flexibility. You are not locked into a single configuration. Setting **W = N and R = 1** means every write updates all replicas, so any single replica can serve a read — this optimizes for read-heavy workloads. Setting **W = 1 and R = N** does the opposite: writes are fast (only one replica needed), but reads must check every replica to find the latest value. The classic balanced choice is **W = ⌊N/2⌋ + 1 and R = ⌊N/2⌋ + 1**, which distributes the cost evenly between reads and writes. Each configuration trades read latency against write latency while preserving the R + W > N invariant.

There are important subtleties that the basic formula does not capture. If a write reaches W replicas but the client crashes before learning this, a subsequent read may or may not see that write depending on timing — this is where versioning and conflict resolution enter the picture. Additionally, quorum consistency alone does not guarantee linearizability; it guarantees **regular register** semantics, meaning a read returns either the most recent write or a concurrent one. Achieving stronger guarantees requires additional mechanisms like read-repair (updating stale replicas during reads) or consensus protocols layered on top. Still, the quorum approach provides a remarkably practical middle ground between full consensus (expensive, slow) and eventual consistency (fast, but with stale reads), making it the backbone of systems like Dynamo, Cassandra, and Riak.
