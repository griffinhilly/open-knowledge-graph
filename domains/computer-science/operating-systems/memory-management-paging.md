---
id: memory-management-paging
title: 'Memory Management: Paging and Page Tables'
domain: computer-science
course: operating-systems
prerequisites:
- id: operating-systems-introduction
  type: hard
builds-toward:
- page-replacement-algorithms-lru-fifo
- virtual-memory-and-demand-paging
tags:
- memory-management
- virtual-memory
- address-translation
stage: formal-systems
status: draft
---

# Memory Management: Paging and Page Tables

## Core Idea
Paging divides physical and virtual memory into fixed-size pages. The page table maps virtual page numbers to physical page frames. The MMU (memory management unit) translates virtual addresses using the page table on every access. Multi-level page tables reduce memory overhead; TLBs cache translations for performance.
