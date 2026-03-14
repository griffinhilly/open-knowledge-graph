---
id: read-repair-anti-entropy
title: Read Repair and Anti-Entropy Mechanisms
domain: computer-science
course: distributed-systems
prerequisites:
- id: eventual-consistency
  type: hard
- id: primary-backup-replication
  type: soft
builds-toward:
- merkle-trees-data-consistency
tags:
- consistency
- repair
- eventual-consistency
- durability
stage: concrete-techniques
status: draft
---

# Read Repair and Anti-Entropy Mechanisms

## Core Idea
In eventually consistent systems, replicas temporarily hold different data. Read repair fixes inconsistencies on reads by comparing versions from replicas and writing back the newest; anti-entropy runs in the background (using Merkle trees or gossip) to find and fix divergent data without waiting for reads.

## How It's Best Learned
Design a scenario: a replica misses an update while offline. Trace through read repair (client reads from multiple replicas, resolves conflict, writes back) and anti-entropy (background process scans both replicas, finds mismatch, pushes correct value).

## Common Misconceptions
- Anti-entropy must run frequently; even infrequent background repair (e.g., daily) is often sufficient.
- Read repair is free; it adds latency (extra reads from multiple replicas) and complexity (handling conflicting versions).
