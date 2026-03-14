---
id: virtual-address-translation-scheme
title: 'Virtual Address Translation: Paging and TLBs'
domain: computer-science
course: operating-systems
prerequisites:
- id: virtual-memory-translation
  type: hard
- id: contiguous-allocation-strategies
  type: hard
builds-toward:
- page-fault-processing
- working-set-model
tags:
- virtual-memory
- paging
- translation
stage: formal-systems
status: draft
---

# Virtual Address Translation: Paging and TLBs

## Core Idea
Paging divides virtual and physical spaces into fixed-size pages; a page table maps virtual page numbers to physical frame numbers. Multi-level page tables reduce memory overhead; TLBs (translation lookaside buffers) cache recent translations for hardware-speed lookups.
