---
id: segmentation
title: Segmentation
domain: computer-science
course: operating-systems
prerequisites:
- id: memory-management-basics
  type: hard
- id: contiguous-memory-allocation
  type: soft
builds-toward:
- virtual-memory-management
tags:
- segmentation
- segment-table
- code-segment
- data-segment
- stack-segment
stage: formal-systems
status: validated
---

# Segmentation

## Core Idea
Segmentation divides a process's address space into variable-size logical segments that correspond to meaningful program units: code, stack, heap, shared libraries. Each segment has a base (physical start address) and a limit (maximum length), stored in a segment table. Logical addresses are two-dimensional: a segment number and an offset within that segment. The MMU checks that the offset doesn't exceed the segment limit (generating a segmentation fault if it does) and adds the base to produce the physical address. Segmentation supports protection (code segments can be read-only), sharing (two processes map the same code segment), and growing segments (the stack segment grows dynamically). Modern x86-64 systems use paging as the primary mechanism but retain segmentation vestiges.

## Common Misconceptions
- Segmentation does not eliminate external fragmentation because segments are variable-size and must be contiguous in physical memory.
- A segmentation fault is not always due to segmentation hardware; on paging systems it generically means an invalid memory access.
