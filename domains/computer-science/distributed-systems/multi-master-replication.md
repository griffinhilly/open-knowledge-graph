---
id: multi-master-replication
title: Multi-Master Replication
domain: computer-science
course: distributed-systems
prerequisites:
- id: state-machine-replication
  type: hard
- id: consensus-problem
  type: hard
builds-toward:
- consistency-models
tags:
- replication
- topology
- writes
stage: advanced
status: draft
---

# Multi-Master Replication

## Core Idea
Multi-master replication allows writes to be accepted at any replica. All replicas must synchronize through consensus (Paxos, Raft) or eventual consistency with conflict resolution. This enables high availability and low-latency writes in geographically distributed systems but complicates consistency guarantees and conflict handling.
