---
id: raft-algorithm
title: Raft Consensus Algorithm
domain: computer-science
course: distributed-systems
prerequisites:
- id: consensus-problem
  type: hard
- id: leader-election-algorithms
  type: soft
builds-toward:
- state-machine-replication
tags:
- raft
- consensus
- leader-based
stage: advanced
status: draft
---

# Raft Consensus Algorithm

## Core Idea
Raft is a consensus algorithm prioritizing understandability over Paxos through a strong leader approach. A leader is elected via randomized timeouts, appends log entries to followers, and waits for quorum acknowledgment before committing. Followers accept entries only from the current leader and reject stale proposals, ensuring a consistent log order.
