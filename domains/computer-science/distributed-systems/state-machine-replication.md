---
id: state-machine-replication
title: State Machine Replication
domain: computer-science
course: distributed-systems
prerequisites:
- id: consensus-problem
  type: hard
- id: strong-consistency-models
  type: soft
builds-toward:
- primary-backup-replication
tags:
- replication
- state-machine
- fault-tolerance
stage: advanced
status: draft
---

# State Machine Replication

## Core Idea
State machine replication replicates a deterministic service by using consensus to agree on a command sequence. All replicas execute identical commands in identical order, producing identical outputs. If f replicas fail, the system survives using consensus for f < n/2. SMR achieves linearizability by having consensus order all operations.
