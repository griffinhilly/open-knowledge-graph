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
