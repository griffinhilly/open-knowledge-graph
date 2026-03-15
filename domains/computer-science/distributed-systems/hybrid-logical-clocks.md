---
id: hybrid-logical-clocks
title: Hybrid Logical Clocks
domain: computer-science
course: distributed-systems
prerequisites:
- id: lamport-timestamps
  type: hard
- id: vector-clocks
  type: soft
builds-toward:
- causal-consistency-implementation
tags:
- clocks
- physical-time
- logical-time
- hybrid
stage: advanced
status: draft
---

# Hybrid Logical Clocks

## Core Idea
Hybrid Logical Clocks (HLC) combine physical time and logical clocks: they advance with physical time (like NTP clocks) but increment logically when events are causally dependent, ensuring that if event A happens before event B in physical time, A's HLC is less than B's. This bounds the clock skew error while preserving causal ordering.
