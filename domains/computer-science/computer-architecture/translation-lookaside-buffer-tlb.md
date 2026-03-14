---
id: translation-lookaside-buffer-tlb
title: Translation Lookaside Buffer (TLB)
domain: computer-science
course: computer-architecture
prerequisites:
- id: virtual-memory-management
  type: hard
- id: paging
  type: hard
tags:
- tlb
- virtual-memory
- address-translation
stage: formal-systems
status: draft
---

# Translation Lookaside Buffer (TLB)

## Core Idea
The TLB caches virtual-to-physical address translations, avoiding expensive page table lookups on every access. TLB misses trigger page table walks; high miss rates severely degrade performance.
