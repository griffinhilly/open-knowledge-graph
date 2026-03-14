---
id: multilevel-cache-organization
title: Multilevel Cache Design and Coordination
domain: computer-science
course: computer-architecture
prerequisites:
- id: cache-associativity-and-mapping
  type: hard
- id: cache-coherence-protocols
  type: soft
builds-toward:
- multi-core-system-design
tags:
- cache-hierarchy
- l1-l2-l3
- memory-hierarchy
stage: formal-systems
status: draft
---

# Multilevel Cache Design and Coordination

## Core Idea
Modern processors use multiple cache levels: L1 (small, fast, on-core), L2 (larger, slower), L3 (shared, slowest). Each level acts as a victim cache for the next. Inclusion and coherence policies define relationships: an inclusive cache holds a superset of lower levels; an exclusive cache holds data not in lower levels. Proper coordination minimizes memory latency.
