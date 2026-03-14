---
id: replica-placement-strategies
title: Replica Placement Strategies
domain: computer-science
course: distributed-systems
prerequisites:
- id: primary-backup-replication
  type: hard
- id: quorum-based-replication
  type: hard
tags:
- replication
- placement
- availability
stage: advanced
status: draft
---

# Replica Placement Strategies

## Core Idea
Replica placement determines where copies of data are stored in the system. Strategies include: geographic distribution to minimize latency and enable survivability across datacenters, rack-awareness to tolerate correlated failures, and load-aware placement to avoid hot nodes. Placement decisions affect availability guarantees, network usage, and read latency.
