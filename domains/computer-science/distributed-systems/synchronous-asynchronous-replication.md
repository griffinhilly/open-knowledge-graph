---
id: synchronous-asynchronous-replication
title: Synchronous vs. Asynchronous Replication
domain: computer-science
course: distributed-systems
prerequisites:
- id: primary-backup-replication
  type: hard
- id: state-machine-replication
  type: hard
builds-toward:
- consistency-models
- quorum-based-replication
tags:
- replication
- durability
- performance
stage: advanced
status: draft
---

# Synchronous vs. Asynchronous Replication

## Core Idea
Synchronous replication waits for replicas to acknowledge writes before returning to the client, ensuring strong durability and consistency but increasing latency. Asynchronous replication returns immediately and applies updates in the background, trading consistency for throughput and low latency. Most systems use a hybrid: synchronously wait for some replicas, asynchronously update others.

## Explainer

From your work on primary-backup and state machine replication, you understand that replicated systems maintain copies of data across multiple nodes. The question this topic addresses is deceptively simple: when a client sends a write, at what point does the system tell the client "done"? The answer to that question — before or after replicas confirm — defines the fundamental tradeoff between consistency and performance in every distributed data system.

In **synchronous replication**, the primary does not acknowledge a write to the client until one or more replicas have confirmed they have durably stored the update. Imagine depositing money at a bank: synchronous replication is like the teller waiting until the backup ledger in the vault is updated before handing you a receipt. If the primary crashes immediately after acknowledging the write, the data is safe on at least one replica. The cost is latency — every write must wait for a network round trip to the slowest required replica, and if that replica is across the country or temporarily slow, the entire system slows down. Worse, if a required replica is unreachable, the system cannot accept writes at all, reducing availability.

In **asynchronous replication**, the primary acknowledges the write immediately after storing it locally, then propagates the update to replicas in the background. This is like the teller handing you a receipt instantly and updating the vault ledger later. Writes are fast and availability is high — the system keeps working even if replicas lag behind. But there is a durability gap: if the primary crashes before the update reaches any replica, that acknowledged write is lost. There is also a consistency gap: a client reading from a replica might see stale data because the replica has not yet received the latest writes. This is called **replication lag**, and it is the source of many subtle bugs in eventually consistent systems.

Most production systems use a **semi-synchronous** or **quorum-based** hybrid. For example, a system with five replicas might synchronously wait for two replicas to confirm (giving a quorum of three including the primary) and asynchronously update the remaining two. This provides durability — the write survives any single node failure — without waiting for the slowest replica. PostgreSQL's synchronous_standby_names setting, MySQL's semi-synchronous replication plugin, and consensus protocols like Raft all implement variations of this pattern. The key insight is that synchronous and asynchronous replication are not binary choices but endpoints on a spectrum, and the right position on that spectrum depends on your system's tolerance for data loss versus its latency requirements.
