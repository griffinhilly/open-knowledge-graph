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
