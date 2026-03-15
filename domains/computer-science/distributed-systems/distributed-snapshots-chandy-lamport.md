---
id: distributed-snapshots-chandy-lamport
title: Distributed Snapshots and Chandy-Lamport Algorithm
domain: computer-science
course: distributed-systems
prerequisites:
- id: happened-before-relation-causality
  type: hard
- id: vector-clocks
  type: soft
builds-toward:
- distributed-system-observability
- causal-consistency-implementation
tags:
- snapshots
- consistency
- global-state
- algorithm
stage: advanced
status: draft
---

# Distributed Snapshots and Chandy-Lamport Algorithm

## Core Idea
The Chandy-Lamport algorithm captures a consistent global snapshot of a distributed system without stopping all processes. It uses markers sent along message channels to identify which in-flight messages belong to the snapshot, ensuring the snapshot respects the happened-before relation and represents a feasible system state.

## How It's Best Learned
Trace through the algorithm by hand on a small system (3 processes, messages) and verify the snapshot is consistent. Understand why the marker must be sent immediately and why receiving the marker on all channels is necessary.

## Common Misconceptions
- Snapshots must freeze all processes; Chandy-Lamport allows processes to continue running.
- The snapshot captures the exact moment of a query; it captures a state that could have been reached through some ordering of events.
