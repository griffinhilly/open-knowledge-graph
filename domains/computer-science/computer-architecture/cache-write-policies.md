---
id: cache-write-policies
title: Cache Write-Through and Write-Back Policies
domain: computer-science
course: computer-architecture
prerequisites:
- id: cache-design-principles
  type: hard
- id: cache-memory-design
  type: soft
builds-toward:
- cache-coherence-protocols
tags:
- cache
- write-policy
- memory-consistency
stage: formal-systems
status: draft
---

# Cache Write-Through and Write-Back Policies

## Core Idea
Write-through writes to both cache and main memory immediately; it guarantees memory consistency but is slow. Write-back writes only to the cache, marking the block dirty; the block is written back when evicted. Write-back is faster but requires careful coherence protocols in multi-core systems. Most modern systems use write-back with a write-combine buffer.
