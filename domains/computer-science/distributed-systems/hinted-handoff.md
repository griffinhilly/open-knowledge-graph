---
id: hinted-handoff
title: Hinted Handoff Recovery
domain: computer-science
course: distributed-systems
prerequisites:
- id: primary-backup-replication
  type: hard
- id: failure-detection-heartbeats
  type: hard
builds-toward:
- gossip-protocols
tags:
- replication
- recovery
- fault-tolerance
stage: advanced
status: draft
---

# Hinted Handoff Recovery

## Core Idea
Hinted handoff is a technique used when a replica is temporarily unavailable: another node accepts the write and stores a 'hint' indicating the intended replica. When the failed node recovers, the hinting node forwards the write. This improves write availability but introduces complexity in hint management and requires that the original replica can accept delayed writes.

## Explainer

You already understand primary-backup replication — where writes go to a primary and are forwarded to backup replicas — and failure detection via heartbeats, which lets nodes determine when a peer has gone down. **Hinted handoff** addresses a practical problem that arises when replication and failure detection intersect: what should the system do when a write arrives but the replica that should store it is temporarily unreachable?

The straightforward answer would be to reject the write or wait for the replica to come back, but both options hurt availability. Instead, with hinted handoff, another node — often a neighbor on the hash ring — accepts the write on behalf of the unavailable replica and stores it along with a **hint**: metadata recording which node the data actually belongs to. The hint says, in effect, "this data is not mine; deliver it to node X when X recovers." The write succeeds from the client's perspective, and the system continues operating without blocking.

When the failed node recovers (detected by resumed heartbeats), the hinting node replays its stored hints — forwarding each write to the now-healthy replica. Once the intended replica confirms receipt, the hinting node deletes the hint. This mechanism is what makes systems like Cassandra and Dynamo maintain write availability during transient failures. The key word is **transient**: hinted handoff assumes the failure is temporary. If a node is permanently gone, hints accumulate indefinitely, consuming disk space on the hinting node and never getting delivered. Production systems typically set a maximum hint retention window (e.g., a few hours) after which undelivered hints are dropped and other repair mechanisms like anti-entropy or read repair take over.

There are important limitations to understand. Hinted handoff does **not** guarantee that a read immediately after a write will see the latest value — the write may still be sitting as a hint on a different node, not yet on the replica a read request hits. It is an **eventual consistency** mechanism, not a strong consistency guarantee. Additionally, if the hinting node itself crashes before delivering its hints, those writes can be lost unless the hints were also replicated. Careful tuning is required: too many hints can overwhelm a recovering node with a flood of replayed writes, while too few can leave data gaps. Despite these tradeoffs, hinted handoff is a pragmatic and widely deployed technique for maintaining availability in partition-tolerant distributed systems.
