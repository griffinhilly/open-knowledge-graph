---
id: memory-management-paging-segmentation
title: 'Memory Management: Paging and Segmentation'
domain: computer-science
course: computer-architecture
prerequisites:
- id: virtual-memory-basics
  type: hard
- id: memory-array-organization
  type: soft
builds-toward:
- cache-design-principles
- io-architecture-system-integration
tags:
- memory
- paging
- segmentation
- virtual
stage: formal-systems
status: draft
---

# Memory Management: Paging and Segmentation

## Core Idea
Paging divides virtual address space into fixed-size pages mapped to physical frames via a page table; segmentation divides address space into variable-size logical segments. Both separate logical and physical memory, enabling isolation and larger address spaces.
