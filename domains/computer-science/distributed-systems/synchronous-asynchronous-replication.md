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
