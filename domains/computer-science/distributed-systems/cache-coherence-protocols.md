---
id: cache-coherence-protocols
title: Cache Coherence Protocols and Memory Consistency
domain: computer-science
course: distributed-systems
prerequisites:
- id: consistency-models
  type: hard
- id: synchronization-problem
  type: hard
tags:
- caching
- consistency
- coherence
stage: advanced
status: draft
---

# Cache Coherence Protocols and Memory Consistency

## Core Idea
Cache coherence protocols maintain consistency between multiple caches in a system. MESI (Modified, Exclusive, Shared, Invalid) is a common protocol that tracks cache line states and coordinates through snooping or directory-based schemes. Correct coherence is essential to prevent processes from seeing inconsistent data when multiple CPUs or nodes have copies of the same memory location.
