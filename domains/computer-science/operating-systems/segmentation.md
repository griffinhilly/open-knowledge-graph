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

## Explainer

From memory management basics, you know that the OS must translate logical addresses into physical addresses and protect processes from accessing each other's memory. Contiguous memory allocation gave each process a single block of physical memory, but that approach is rigid — a process's code, data, and stack have different sizes, growth patterns, and access permissions, yet they are all crammed into one undifferentiated chunk. **Segmentation** solves this by splitting the process's address space into distinct logical units — a code segment, a data segment, a stack segment, a heap segment — each of which gets its own contiguous region in physical memory.

Every logical address under segmentation is two-dimensional: a **segment number** that identifies which segment, and an **offset** within that segment. When a program generates an address, the hardware looks up the segment number in the process's **segment table**, which stores two values per entry: the **base** (where this segment starts in physical memory) and the **limit** (the maximum valid offset). The MMU first checks that the offset is less than the limit — if it exceeds it, the hardware traps with a segmentation fault. If the check passes, the physical address is computed as base + offset. This two-step check-and-translate happens on every memory access, entirely in hardware, so the programmer writes code using logical segment-relative addresses and never needs to know where the segment actually lives in physical memory.

Segmentation enables two powerful capabilities that contiguous allocation cannot easily provide. First, **per-segment protection**: the segment table can mark the code segment as read-only and executable, the data segment as read-write but not executable, and the stack as read-write. An attempt to write to the code segment or execute data on the stack triggers a protection fault. Second, **segment sharing**: if two processes run the same program, their segment tables can point their code segments to the same physical memory, sharing one copy of the instructions while each maintains a private data and stack segment.

The major weakness of segmentation is **external fragmentation**. Because each segment must occupy a contiguous block of physical memory and segments vary in size, free memory becomes scattered into small gaps between allocated segments over time — the same problem you saw with contiguous allocation, just at a finer granularity. Compaction (shifting segments to consolidate free space) is expensive. This is precisely why modern systems moved to paging, which uses fixed-size pages and eliminates external fragmentation entirely. Modern x86-64 processors still have segment registers, but they are largely vestigial — the OS sets all segment bases to zero and limits to the full address space, effectively disabling segmentation and relying on paging for all address translation and protection.
