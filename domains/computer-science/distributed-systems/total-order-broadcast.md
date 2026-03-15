---
id: total-order-broadcast
title: Total Order Broadcast and Strong Consistency
domain: computer-science
course: distributed-systems
prerequisites:
- id: happened-before-relation-causality
  type: hard
- id: consensus-problem
  type: hard
builds-toward:
- state-machine-replication
tags:
- broadcast
- ordering
- consensus
- replication
stage: concrete-operations
status: draft
---

# Total Order Broadcast and Strong Consistency

## Core Idea
Total order broadcast guarantees all processes deliver messages in the same order, which is stronger than causal order (preserving causality is not enough if concurrent messages can be delivered in different orders). It is equivalent to consensus and is the basis for state machine replication.

## How It's Best Learned
Compare scenarios: causal delivery allows reordering of concurrent messages, total order does not. Implement a simple total order broadcast using a coordinator that assigns sequence numbers, then note the bottleneck and why consensus is needed for robustness.

## Common Misconceptions
- Total order is always needed; many applications only need causal order or even weaker guarantees.
- Implementing total order is cheap; any reliable total order has a bottleneck (coordinator) or requires consensus, which is expensive.
