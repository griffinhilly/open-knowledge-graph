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
status: validated
---

# Primary-Backup Replication

## Core Idea
In primary-backup replication, one primary handles all writes and forwards updates to backups; reads go to any replica. On primary failure, a backup is promoted. This approach is simpler than consensus-based replication but requires availability of the primary for writes and careful handling of failures to prevent split-brain (two primaries claiming authority).

## Questions

```yaml
- question: "An engineer uses asynchronous primary-backup replication for a database handling financial transactions. The primary crashes 100ms after acknowledging a write to the client. What is the outcome?"
  type: multiple-choice
  options:
    - "No data is lost because the backup will eventually catch up once the primary recovers"
    - "The write is lost — the backup had not yet received it, so the client was acknowledged but the data exists only on the dead primary"
    - "The system automatically detects the crash and replays the lost write from the client's acknowledgment log"
    - "Split-brain occurs because both the primary and backup acknowledged the write"
  answer: 1
  explanation: "In asynchronous replication, the primary acknowledges the client immediately after its own local write, before the backup receives it. If the primary crashes in that window, the write is lost — gone with the dead node. The client was told the write succeeded, but no surviving replica holds it. This is the core durability tradeoff: asynchronous replication has lower write latency but risks losing recently acknowledged writes on primary failure. Synchronous replication prevents this by waiting for backup confirmation before responding. Option D describes split-brain, which is a different failure mode requiring two active primaries."

- question: "What is 'split-brain' in primary-backup replication, and why is it dangerous?"
  type: multiple-choice
  options:
    - "A network partition where backups can no longer receive writes from the primary"
    - "Two nodes both believing they are the active primary and independently accepting writes, causing their states to diverge irreconcilably"
    - "A backup that holds a partial write after a crash mid-transmission"
    - "A condition where the primary has more backup replicas than it can synchronously replicate to"
  answer: 1
  explanation: "Split-brain occurs when both the original primary and a promoted backup believe they are the authoritative primary — typically after a network partition where the backup promotes itself without the old primary stepping down. Both nodes independently accept writes, and their states diverge in ways that may be impossible to reconcile. Fencing mechanisms (revoking the old primary's access to shared storage, lease-based timeouts) are designed to prevent this by ensuring only one node can act as primary at a time."

- question: "In synchronous primary-backup replication, the primary acknowledges a write to the client as soon as it has written the data to its own local storage."
  type: true-false
  answer: false
  explanation: "In synchronous replication, the primary waits until at least one backup confirms it has stored the update before acknowledging the write to the client. This guarantees that on primary failure, at least one backup holds the data — no data loss. The tradeoff is that every write pays the round-trip latency to the backup. Acknowledging immediately after local write is the definition of asynchronous replication, which trades durability for lower latency."

- question: "In primary-backup replication, write availability is maintained even when the primary is unreachable, because backups can accept writes directly."
  type: true-false
  answer: false
  explanation: "Write availability depends entirely on the primary in this pattern — only the primary makes ordering decisions. When the primary is down and failover has not yet completed, the system is unavailable for writes. This is the fundamental availability tradeoff of primary-backup replication: simplicity comes at the cost of a write-unavailability window during failover. Reads may continue through backups, but writes are blocked until a new primary is promoted and confirmed."

- question: "Explain the durability vs. latency tradeoff between synchronous and asynchronous primary-backup replication, and describe a scenario where each mode is the appropriate choice."
  type: short-answer
  answer: "In synchronous replication, the primary waits for at least one backup to confirm the write before acknowledging success — zero data loss on primary failure, but every write pays round-trip latency to the backup. In asynchronous replication, the primary responds immediately; backups catch up later — lower write latency, but recent writes can be lost if the primary crashes before the backup receives them. Synchronous is appropriate for financial transactions, medical records, or any workload where losing a confirmed write is unacceptable. Asynchronous is appropriate for high-throughput workloads where write latency matters and occasional data loss on failure is tolerable — real-time analytics feeds, session-state caching, or read-heavy reporting replicas."
  explanation: "The choice between sync and async is ultimately a business decision about what failure mode is worse: slower writes (sync) or possible data loss (async). Many production systems offer both modes with per-operation control."
```

## Explainer

From your work on leader election, you know that distributed systems can designate a single node to coordinate activity. **Primary-backup replication** builds directly on that idea: one node — the **primary** (also called the leader or master) — accepts all write requests, and one or more **backup** nodes (also called replicas or standbys) receive copies of those writes so the data survives if the primary fails.

The write path works like this: a client sends a write to the primary, the primary applies the update locally, then forwards the update to each backup. The key design decision is *when* the primary acknowledges the write back to the client. In **synchronous replication**, the primary waits until at least one backup confirms it has stored the update before responding — this guarantees no data loss on primary failure, but every write pays the round-trip latency to the backup. In **asynchronous replication**, the primary responds immediately after its own local write, and backups catch up in the background — this is faster but risks losing recent writes if the primary crashes before the backups have received them.

The hardest problem is **failover**. When the primary becomes unreachable, the system must promote a backup to become the new primary. This is where leader election comes in: the backups must agree on which one takes over, and they must do so without accidentally creating two primaries (a situation called **split-brain**). Split-brain is dangerous because both nodes accept writes independently, and their states diverge in ways that may be impossible to reconcile later. Fencing mechanisms — like revoking the old primary's access to shared storage or using lease-based timeouts — help prevent this.

Primary-backup replication is the workhorse of practical systems: PostgreSQL streaming replication, Redis Sentinel, and many cloud databases use this pattern. It is simpler than full consensus protocols like Raft or Paxos because only the primary makes ordering decisions — there is no need for a majority vote on every write. The tradeoff is that the system is unavailable for writes whenever the primary is down and failover has not yet completed. For many workloads, this brief unavailability window is acceptable, making primary-backup the default choice when simplicity and read scalability matter more than continuous write availability.
