---
id: primary-backup-replication
title: Primary-Backup Replication
domain: computer-science
course: distributed-systems
prerequisites:
- id: state-machine-replication
  type: soft
- id: leader-election-algorithms
  type: hard
builds-toward:
- quorum-based-replication
tags:
- replication
- primary-backup
- active-passive
stage: advanced
status: draft
---

# Primary-Backup Replication

## Core Idea
In primary-backup replication, one primary handles all writes and forwards updates to backups; reads go to any replica. On primary failure, a backup is promoted. This approach is simpler than consensus-based replication but requires availability of the primary for writes and careful handling of failures to prevent split-brain (two primaries claiming authority).

## Explainer

From your work on leader election, you know that distributed systems can designate a single node to coordinate activity. **Primary-backup replication** builds directly on that idea: one node — the **primary** (also called the leader or master) — accepts all write requests, and one or more **backup** nodes (also called replicas or standbys) receive copies of those writes so the data survives if the primary fails.

The write path works like this: a client sends a write to the primary, the primary applies the update locally, then forwards the update to each backup. The key design decision is *when* the primary acknowledges the write back to the client. In **synchronous replication**, the primary waits until at least one backup confirms it has stored the update before responding — this guarantees no data loss on primary failure, but every write pays the round-trip latency to the backup. In **asynchronous replication**, the primary responds immediately after its own local write, and backups catch up in the background — this is faster but risks losing recent writes if the primary crashes before the backups have received them.

The hardest problem is **failover**. When the primary becomes unreachable, the system must promote a backup to become the new primary. This is where leader election comes in: the backups must agree on which one takes over, and they must do so without accidentally creating two primaries (a situation called **split-brain**). Split-brain is dangerous because both nodes accept writes independently, and their states diverge in ways that may be impossible to reconcile later. Fencing mechanisms — like revoking the old primary's access to shared storage or using lease-based timeouts — help prevent this.

Primary-backup replication is the workhorse of practical systems: PostgreSQL streaming replication, Redis Sentinel, and many cloud databases use this pattern. It is simpler than full consensus protocols like Raft or Paxos because only the primary makes ordering decisions — there is no need for a majority vote on every write. The tradeoff is that the system is unavailable for writes whenever the primary is down and failover has not yet completed. For many workloads, this brief unavailability window is acceptable, making primary-backup the default choice when simplicity and read scalability matter more than continuous write availability.
