---
id: quorum-based-replication
title: Quorum-Based Replication
domain: computer-science
course: distributed-systems
prerequisites:
- id: primary-backup-replication
  type: soft
- id: state-machine-replication
  type: soft
builds-toward:
- distributed-hash-tables
tags:
- quorum
- replication
- majority
stage: advanced
status: draft
---

# Quorum-Based Replication

## Core Idea
Quorum-based replication requires writes to be acknowledged by a quorum (majority) of replicas and reads to contact a quorum, ensuring read and write quorums always overlap. This decentralizes replication without a single primary and tolerates minority failures. Trade-off: reads and writes are slower since they must contact multiple replicas.
