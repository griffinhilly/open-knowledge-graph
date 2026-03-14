---
id: cache-associativity-and-mapping
title: Cache Associativity and Address Mapping Strategies
domain: computer-science
course: computer-architecture
prerequisites:
- id: cache-design-principles
  type: hard
- id: cache-replacement-policies
  type: soft
builds-toward:
- multilevel-cache-organization
tags:
- cache-associativity
- cache-mapping
- address-mapping
stage: formal-systems
status: draft
---

# Cache Associativity and Address Mapping Strategies

## Core Idea
Cache mapping strategy determines where a memory address can reside in the cache. Direct-mapped: each address maps to one cache location (fast but prone to conflicts). Fully associative: any address can be stored in any location (flexible but slow to search). N-way set-associative: intermediate approach, dividing the cache into sets and allowing N locations per set. Associativity increases hit rate but complexity.
