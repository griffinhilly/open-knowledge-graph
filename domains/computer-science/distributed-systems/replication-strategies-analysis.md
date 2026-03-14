---
id: replication-strategies-analysis
title: Replication Strategies and Trade-offs
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-systems-introduction
  type: hard
- id: consistency-models
  type: hard
builds-toward:
- primary-backup-replication
- causal-consistency-implementation
- two-phase-commit-protocol
tags:
- replication
- consistency
- availability
- durability
stage: abstract-reasoning
status: draft
---

# Replication Strategies and Trade-offs

## Core Idea
Replication strategies (primary-backup, multi-leader, leaderless, active-passive) represent different points on tradeoffs between consistency, availability, and latency. The choice depends on whether writes must be linearizable, whether replicas can drift temporarily, and how failures should be handled.

## How It's Best Learned
Create a matrix: each strategy as a row, each property (write latency, consistency, failure recovery) as a column. Mark which are strong, weak, or medium. Understand why stronger consistency often means lower availability.
