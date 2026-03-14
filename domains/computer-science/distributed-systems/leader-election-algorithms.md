---
id: leader-election-algorithms
title: Leader Election Algorithms
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-systems-overview
  type: hard
builds-toward:
- raft-algorithm
- primary-backup-replication
tags:
- leader-election
- coordination
- agreements
stage: advanced
status: draft
---

# Leader Election Algorithms

## Core Idea
Leader election allows a group of processes to select one coordinator. Classic algorithms include Bully (highest ID wins via comparison messages), Ring (messages circulate), and randomized (Raft uses randomized timeouts). All algorithms must ensure at most one leader is elected, handle leader failures, and elect a new leader when needed.
