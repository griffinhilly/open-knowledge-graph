---
id: consistency-models
title: Consistency Models in Distributed Systems
domain: computer-science
course: distributed-systems
prerequisites:
- id: causal-ordering
  type: soft
- id: distributed-systems-overview
  type: hard
builds-toward:
- eventual-consistency
- causal-consistency
- strong-consistency-models
tags:
- consistency
- correctness
- models
stage: advanced
status: draft
---

# Consistency Models in Distributed Systems

## Core Idea
Consistency models define what values a read can return after a write in a replicated system. Strong models (linearizability, sequential consistency) provide intuitive semantics but require coordination overhead. Weaker models (eventual consistency, causal consistency) improve availability and latency by tolerating temporary disagreement and concurrent write conflicts.
