---
id: vector-clocks
title: Vector Clocks and Capturing Causality
domain: computer-science
course: distributed-systems
prerequisites:
- id: logical-clocks
  type: hard
builds-toward:
- causal-ordering
- causal-consistency
tags:
- vector-clocks
- causality
- ordering
stage: advanced
status: draft
---

# Vector Clocks and Capturing Causality

## Core Idea
Vector clocks extend logical clocks with a vector of integers (one per process). Each process increments its own entry on local events and sets each entry to the maximum of its value and the sender's on message receipt. Vector clocks precisely capture causality: event A happened-before B iff A's vector is less than B's element-wise, and concurrent events have incomparable vectors.

## How It's Best Learned
Implement vector clock logic and trace scenarios with concurrent writes and message chains.

## Common Misconceptions
Vector clocks require clock synchronization; they can totally order all events; they are necessary for all distributed algorithms.
