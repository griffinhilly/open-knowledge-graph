---
id: gossip-algorithms-convergence
title: Gossip Algorithms and Convergence Properties
domain: computer-science
course: distributed-systems
prerequisites:
- id: gossip-protocols
  type: hard
builds-toward:
- distributed-system-observability
tags:
- gossip
- convergence
- propagation
- epidemic
stage: concrete-operations
status: draft
---

# Gossip Algorithms and Convergence Properties

## Core Idea
Gossip protocols propagate information by having each node randomly exchange state with peers. The propagation is probabilistically guaranteed, and convergence takes O(log N) rounds, making gossip robust to message loss and node failures. Gossip is used for membership, distributed state aggregation, and anti-entropy.

## How It's Best Learned
Simulate a gossip protocol: N nodes, each picks a random peer and exchanges state. Measure how many rounds until all nodes converge. Vary N and observe the logarithmic scaling of rounds.
