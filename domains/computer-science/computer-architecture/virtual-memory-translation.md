---
id: virtual-memory-translation
title: Virtual Memory Address Translation and Page Tables
domain: computer-science
course: computer-architecture
prerequisites:
- id: memory-management-paging-segmentation
  type: hard
- id: memory-address-decoding
  type: soft
builds-toward:
- translation-lookaside-buffer-tlb
tags:
- virtual-memory
- paging
- address-translation
stage: formal-systems
status: draft
---

# Virtual Memory Address Translation and Page Tables

## Core Idea
Virtual addresses are translated to physical addresses via page tables stored in memory. Each virtual address is split into a virtual page number (looked up in the page table) and an offset (unchanged in translation). Multi-level page tables reduce memory overhead. Translation adds latency; the TLB (translation lookaside buffer) caches recent translations to hide this cost.
