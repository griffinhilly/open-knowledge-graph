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

## Questions

```yaml
- question: "A database primary receives a write and immediately crashes before sending the update to any replica. Under synchronous replication (waiting for 1 replica), what happens? Under asynchronous replication?"
  type: multiple-choice
  options:
    - "Both lose the write, because the primary crashed before completing its local write in either case"
    - "Synchronous: the write is safe on the replica; Asynchronous: the write is lost because the primary crashed before propagating"
    - "Synchronous: the write is lost because the primary never acknowledged it; Asynchronous: the write is safe in a buffer"
    - "Both preserve the write, because replicas maintain write-ahead logs independently"
  answer: 1
  explanation: "Under synchronous replication, the primary only acknowledges the write to the client after at least one replica confirms durable storage — so the data exists on the replica even if the primary crashes immediately after. Under asynchronous replication, the primary acknowledges as soon as it stores the data locally, then propagates in the background. A crash before propagation means the write is permanently lost. This durability gap is the fundamental cost of asynchronous replication."

- question: "An e-commerce platform requires that no committed orders ever be lost, even if a database node fails. A replica is temporarily slow due to network congestion. Under strict synchronous replication, what happens to writes during this period?"
  type: multiple-choice
  options:
    - "Writes complete normally because the primary buffers them and retries"
    - "Writes slow down or stall because the primary must wait for the slow replica to acknowledge before returning to clients"
    - "The slow replica is automatically promoted to primary, restoring performance"
    - "Writes fall back to asynchronous mode automatically until the replica recovers"
  answer: 1
  explanation: "This is the core availability cost of synchronous replication: the primary's write latency is bounded below by the slowest required replica. If that replica is slow (due to network congestion, load, or partial failure), every write to the system slows with it. If the replica becomes unreachable, writes may stall entirely. This is why purely synchronous replication is rarely used in geographically distributed systems — the latency of cross-region round trips is simply too high to impose on every client write."

- question: "Synchronous replication always provides higher availability than asynchronous replication because it ensures replicas are always up to date."
  type: true-false
  answer: false
  explanation: "Synchronous replication reduces availability in the face of replica failures or slowness. If a required synchronous replica becomes unreachable, the primary cannot safely accept writes — the system loses write availability. Asynchronous replication keeps the primary available for writes regardless of replica state. The tradeoff is inverted: synchronous replication provides stronger durability and consistency but at the cost of availability; asynchronous provides higher availability at the cost of potential data loss and stale reads."

- question: "With asynchronous replication, a write that has been acknowledged to the client could be permanently lost if the primary fails before the update reaches any replica."
  type: true-false
  answer: true
  explanation: "This is the defining risk of asynchronous replication and is called the durability gap. The primary acknowledges the write immediately after local storage, then propagates asynchronously. If the primary crashes in the interval between acknowledgment and propagation, the write exists nowhere — the client was told 'success' but the data is gone. This is not a theoretical concern: it has caused real data loss in production systems. Systems with strong durability requirements use synchronous or semi-synchronous replication to close this gap."

- question: "Why do most production distributed databases use semi-synchronous or quorum-based replication rather than purely synchronous or purely asynchronous replication?"
  type: short-answer
  answer: "Purely synchronous replication provides the strongest durability but makes every write as slow as the slowest required replica and makes writes unavailable if any required replica is down. Purely asynchronous provides the lowest latency but risks losing acknowledged writes if the primary crashes. Quorum-based approaches thread the needle: by waiting for a majority (or a specified minimum) of replicas, the system guarantees durability against any single node failure while avoiding the latency penalty of waiting for the slowest node. The remaining replicas update asynchronously, preserving throughput. This tradeoff — tunable between durability and performance — is why systems like Raft, PostgreSQL synchronous standbys, and Cassandra's consistency levels all implement quorum variants."
  explanation: "The fundamental insight is that synchronous and asynchronous are endpoints on a continuous spectrum of durability vs. latency. Real systems need to be positioned on this spectrum based on their specific requirements — a financial ledger needs different guarantees than an analytics event log. Quorum-based designs expose this as a tunable parameter rather than a binary choice."
```

## Explainer

From your work on primary-backup and state machine replication, you understand that replicated systems maintain copies of data across multiple nodes. The question this topic addresses is deceptively simple: when a client sends a write, at what point does the system tell the client "done"? The answer to that question — before or after replicas confirm — defines the fundamental tradeoff between consistency and performance in every distributed data system.

In **synchronous replication**, the primary does not acknowledge a write to the client until one or more replicas have confirmed they have durably stored the update. Imagine depositing money at a bank: synchronous replication is like the teller waiting until the backup ledger in the vault is updated before handing you a receipt. If the primary crashes immediately after acknowledging the write, the data is safe on at least one replica. The cost is latency — every write must wait for a network round trip to the slowest required replica, and if that replica is across the country or temporarily slow, the entire system slows down. Worse, if a required replica is unreachable, the system cannot accept writes at all, reducing availability.

In **asynchronous replication**, the primary acknowledges the write immediately after storing it locally, then propagates the update to replicas in the background. This is like the teller handing you a receipt instantly and updating the vault ledger later. Writes are fast and availability is high — the system keeps working even if replicas lag behind. But there is a durability gap: if the primary crashes before the update reaches any replica, that acknowledged write is lost. There is also a consistency gap: a client reading from a replica might see stale data because the replica has not yet received the latest writes. This is called **replication lag**, and it is the source of many subtle bugs in eventually consistent systems.

Most production systems use a **semi-synchronous** or **quorum-based** hybrid. For example, a system with five replicas might synchronously wait for two replicas to confirm (giving a quorum of three including the primary) and asynchronously update the remaining two. This provides durability — the write survives any single node failure — without waiting for the slowest replica. PostgreSQL's synchronous_standby_names setting, MySQL's semi-synchronous replication plugin, and consensus protocols like Raft all implement variations of this pattern. The key insight is that synchronous and asynchronous replication are not binary choices but endpoints on a spectrum, and the right position on that spectrum depends on your system's tolerance for data loss versus its latency requirements.
