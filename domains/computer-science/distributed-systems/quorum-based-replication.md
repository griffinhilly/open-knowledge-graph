---
id: quorum-based-replication
title: Quorum-Based Replication
domain: computer-science
course: distributed-systems
prerequisites:
- id: primary-backup-replication
  type: soft
- id: state-machine-replication
  type: soft
builds-toward:
- distributed-hash-tables
tags:
- quorum
- replication
- majority
stage: advanced
status: draft
---

# Quorum-Based Replication

## Core Idea
Quorum-based replication requires writes to be acknowledged by a quorum (majority) of replicas and reads to contact a quorum, ensuring read and write quorums always overlap. This decentralizes replication without a single primary and tolerates minority failures. Trade-off: reads and writes are slower since they must contact multiple replicas.

## Explainer

In primary-backup replication, a single leader handles all writes and forwards them to followers. This is simple but creates a bottleneck and a single point of failure — if the primary crashes before replicating, writes can be lost, and electing a new primary takes time. **Quorum-based replication** removes the need for a designated leader by requiring that every write reach enough replicas, and every read contact enough replicas, that at least one replica in any read set has seen the most recent write.

The math behind quorums is straightforward. Suppose you have N replicas. You choose a write quorum W (the number of replicas that must acknowledge a write) and a read quorum R (the number of replicas you must contact on a read). The key invariant is **W + R > N**. This guarantees that the write set and read set always overlap — at least one replica contacted during a read has the latest written value. For example, with 5 replicas, you might set W = 3 and R = 3. Any 3 replicas you read from must include at least one of the 3 that acknowledged the last write. When reading, you take the response with the highest version number or timestamp, which is the most recent value.

This gives you a tunable knob between read and write performance. Setting W = N and R = 1 means writes are slow (all replicas must respond) but reads are fast (any single replica has the latest data). Setting W = 1 and R = N reverses the tradeoff. The classic balanced choice is W = R = (N/2) + 1 — a simple majority. The system tolerates up to N - W write failures and N - R read failures while remaining available. With the majority quorum on 5 nodes, any 2 nodes can fail and the system continues operating.

Quorum replication does not automatically give you strong consistency. If you simply take the first R responses, a slow replica might return stale data. Systems must attach version numbers or vector clocks to values so that the reader can identify which response is freshest. Some systems also use **read repair** — when a quorum read discovers that some replicas have stale data, it pushes the latest value back to them. The quorum mechanism provides the mathematical guarantee that freshness information is always reachable; the protocol layered on top determines how that guarantee translates into the consistency the application actually sees.
