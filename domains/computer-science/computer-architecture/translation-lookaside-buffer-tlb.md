---
id: translation-lookaside-buffer-tlb
title: Translation Lookaside Buffer (TLB) Design
domain: computer-science
course: computer-architecture
prerequisites:
- id: virtual-memory-translation
  type: hard
- id: cache-associativity-and-mapping
  type: soft
builds-toward:
- exception-handling-architecture
tags:
- tlb
- address-translation
- cache
stage: formal-systems
status: draft
---

# Translation Lookaside Buffer (TLB) Design

## Core Idea
The TLB is a small associative cache that stores recent virtual-to-physical address translations. A TLB hit provides the physical page number in one cycle; a miss requires a page table walk (several memory accesses). TLB entries include the virtual page number, physical page number, and protection bits. TLB size is a trade-off between speed and area; typical sizes are 32–512 entries.
