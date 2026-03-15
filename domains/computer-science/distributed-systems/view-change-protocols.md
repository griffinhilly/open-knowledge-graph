---
id: view-change-protocols
title: View Change and Leader Failover Protocols
domain: computer-science
course: distributed-systems
prerequisites:
- id: consensus-problem
  type: hard
- id: state-machine-replication
  type: soft
builds-toward:
- raft-leader-election
- paxos-made-practical
tags:
- failover
- leader-change
- consistency
- protocol
stage: advanced
status: draft
---

# View Change and Leader Failover Protocols

## Core Idea
View change protocols coordinate the transition when a leader fails: they elect a new leader, ensure the new leader learns all prior committed operations, and prevent split-brain (two leaders). Correctness requires all non-faulty replicas to move to the new view in a coordinated manner.
