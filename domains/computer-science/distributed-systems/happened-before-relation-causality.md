---
id: happened-before-relation-causality
title: Happened-Before Relation and Causal Ordering
domain: computer-science
course: distributed-systems
prerequisites:
- id: lamport-timestamps
  type: hard
- id: vector-clocks
  type: hard
builds-toward:
- causal-consistency-implementation
- distributed-snapshots-chandy-lamport
- total-order-broadcast
tags:
- causality
- ordering
- logical-clocks
- partial-order
stage: abstract-reasoning
status: draft
---

# Happened-Before Relation and Causal Ordering

## Core Idea
The happened-before relation (→) defines a partial order on events: event A happened before event B if A caused B (through message exchange or local sequencing). This relation is the foundation for reasoning about distributed computations without requiring synchronized physical clocks, and it distinguishes causally-dependent events from concurrent ones.

## How It's Best Learned
Draw message diagrams with labeled events and identify the partial order. Use Lamport timestamps and vector clocks to detect causality. Understand that concurrency (neither A→B nor B→A) means events can be ordered arbitrarily without violating causality.

## Common Misconceptions
- Happened-before is the same as physical time ordering; it depends only on communication and local computation, not wall-clock time.
- If two events are not ordered by →, one must be reordered to fix 'bugs'; actually, concurrent events can remain unordered.
