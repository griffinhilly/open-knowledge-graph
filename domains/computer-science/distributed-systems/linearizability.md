---
id: linearizability
title: Linearizability
domain: computer-science
course: distributed-systems
prerequisites:
- id: consistency-models
  type: hard
builds-toward:
- distributed-transactions-2pc
- strong-eventual-consistency
tags:
- consistency
- formal-semantics
- correctness
stage: advanced
status: draft
---

# Linearizability

## Core Idea
Linearizability is the strongest consistency model: all operations appear to execute atomically at some point between their invocation and completion, and the execution respects a total order. A linearizable system behaves as if there is a single copy of the data. This model prevents stale reads, causality violations, and ensures a consistent view of shared state across all clients.

## How It's Best Learned
Compare linearizable and non-linearizable execution histories side by side. Understand why linearizability is stricter than sequential consistency and more expensive to implement. Implement a simple linearizable register and test with concurrent operations from multiple clients.

## Common Misconceptions
- Linearizability is the same as serializability (linearizability is stronger and applies to concurrent objects, not just transactions). - Linearizability requires centralized state (distributed linearizable systems exist). - Linearizability solves all consistency problems (availability and latency are separate concerns).
