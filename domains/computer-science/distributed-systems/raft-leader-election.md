---
id: raft-leader-election
title: 'Raft Consensus: Leader Election'
domain: computer-science
course: distributed-systems
prerequisites:
- id: raft-algorithm
  type: hard
- id: leader-election-algorithms
  type: soft
builds-toward:
- view-change-protocols
- state-machine-replication
tags:
- raft
- leader-election
- consensus
- terms
stage: concrete-operations
status: draft
---

# Raft Consensus: Leader Election

## Core Idea
Raft's leader election mechanism divides time into terms: in each term, a leader is elected, and if the leader fails or becomes unreachable, a new election starts in a higher term. Elections are triggered by timeouts and use voting to ensure only one leader per term, simplifying reasoning compared to Paxos.
