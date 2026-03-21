---
id: paging
title: Paging and Page Tables
domain: computer-science
course: operating-systems
prerequisites:
- id: memory-management-basics
  type: hard
- id: contiguous-memory-allocation
  type: soft
builds-toward:
- virtual-memory-management
- file-system-implementation
tags:
- paging
- page-table
- frame
- TLB
- page-number
- offset
stage: formal-systems
status: validated
---

# Paging and Page Tables

## Core Idea
Paging eliminates external fragmentation by dividing the logical address space into fixed-size pages and physical memory into equal-size frames. The OS maintains a page table per process that maps each logical page number to its physical frame number; the MMU performs translation on every access by splitting the logical address into a page number and an offset. The Translation Lookaside Buffer (TLB) is a fast hardware cache for recent page table entries, critical for performance since every memory access would otherwise require two memory accesses (one for the page table, one for the data). Modern systems use multi-level (hierarchical) page tables to avoid allocating large contiguous page table space for sparse address spaces.

## How It's Best Learned
Work through a manual TLB lookup: given a logical address, extract page number and offset, check TLB for hit or miss, look up page table on miss, combine frame number with offset to get physical address.

## Common Misconceptions
- Paging eliminates external fragmentation but introduces internal fragmentation within the last page.
- Page size is not configurable by the programmer; it is set by the hardware and OS (typically 4KB).

## Questions

```yaml
- question: "A paging system uses 4 KB pages (12-bit offset). A process issues logical address 0x000050B3. The page table shows page 5 → frame 200. What is the physical address?"
  type: multiple-choice
  options:
    - "0x000050B3 — the MMU passes the logical address through unchanged on a TLB hit"
    - "Frame 200 concatenated with offset 0x0B3, giving physical address 0x000C80B3"
    - "200 × 4096 + 0x50B3, which adds the full logical address to the frame base"
    - "The offset 0x0B3 is added to frame 200, giving physical address 200 + 0x0B3"
  answer: 1
  explanation: "With 4 KB pages (2¹² bytes), the lowest 12 bits of the logical address are the offset: 0x0B3. The upper bits are the page number: 0x000050B3 >> 12 = 5. The MMU looks up page 5 in the page table, finds frame 200 (0xC8), and constructs the physical address as (200 << 12) | 0x0B3 = 0x000C80B3. The offset is preserved exactly — it identifies the same byte position within the physical frame as it did within the logical page. Only the page number is replaced by the frame number."

- question: "Why is the Translation Lookaside Buffer (TLB) essential for making paging practical rather than merely a performance optimization?"
  type: multiple-choice
  options:
    - "Without the TLB, the page table cannot store entries for more than 1024 pages, limiting address space"
    - "Without the TLB, every memory access requires two memory accesses — one to read the page table, one to read the actual data — effectively doubling the cost of every instruction and data reference"
    - "Without the TLB, the MMU cannot distinguish page faults from valid translations"
    - "Without the TLB, processes could read each other's page tables, violating memory isolation"
  answer: 1
  explanation: "The page table lives in main memory. Without the TLB, translating any logical address requires first reading the page table entry from memory (one access), then reading the actual data or instruction (second access). This doubles the effective memory access time for every single operation — every instruction fetch, every data read, every data write. The TLB is a small fast hardware cache (typically 64–1024 entries) of recent page-to-frame mappings; on a TLB hit, translation adds essentially zero overhead. Because programs exhibit locality, TLB hit rates above 99% are typical, making paging's performance overhead negligible in practice."

- question: "Paging completely eliminates memory fragmentation."
  type: true-false
  answer: false
  explanation: "False. Paging eliminates *external* fragmentation — scattered free blocks that individually cannot accommodate a process even when their total size is sufficient. Because any free frame can hold any page, there are no unusable gaps between allocations. However, paging introduces *internal* fragmentation: the last page allocated to a process is rarely completely full. If a process needs 4097 bytes with 4 KB pages, it occupies two pages but uses only 1 byte of the second, wasting 4095 bytes. On average, half a page is wasted per process — a small, predictable cost compared to the unpredictable waste of external fragmentation."

- question: "In a paging system, the offset portion of a logical address is passed through unchanged to become the low-order bits of the physical address."
  type: true-false
  answer: true
  explanation: "True. Address translation replaces only the page number (the high-order bits) with the frame number from the page table. The offset — the low-order bits identifying the exact byte within the page — is preserved unchanged. This works because a page and its corresponding frame are the same size by definition: once you know which physical frame holds the page, you access the same relative byte position within that frame. The offset is neither translated nor modified."

- question: "Explain what problem paging solves that contiguous memory allocation cannot, and describe the new (minor) problem paging introduces."
  type: short-answer
  answer: "Paging solves external fragmentation: in contiguous allocation, as processes load and terminate, physical memory becomes fragmented into small scattered free regions that may collectively be large enough for a new process but are individually too small to hold it. Paging eliminates this by allowing any free frame to hold any page — a process's pages can be scattered anywhere in physical memory with no adjacency requirement. The new problem paging introduces is internal fragmentation: since processes are allocated whole pages, the last page is often only partially used, wasting on average half a page per process. This is a much smaller and more predictable cost."
  explanation: "The core trade-off is abandoning the contiguity requirement. Contiguous allocation strands memory in unusable gaps between live allocations — gaps that grow and fragment over time. Paging eliminates gaps entirely because frames are interchangeable. The only downside is that fixed-size pages don't perfectly fit variable-size processes, but wasting on average 2 KB (half a 4 KB page) per process is trivially small compared to the potentially large and unpredictable holes created by external fragmentation."
```

## Explainer

From memory management basics, you know that the OS must allocate physical memory to multiple processes while providing each one with the illusion of a private, contiguous address space. You also know the problem with contiguous allocation: as processes are loaded and terminated, physical memory becomes fragmented into small, scattered free blocks (**external fragmentation**), eventually preventing even small processes from fitting despite sufficient total free memory. **Paging** solves this by abandoning the requirement that a process occupy contiguous physical memory.

The idea is to divide both logical memory and physical memory into fixed-size chunks. On the logical side, these chunks are called **pages**; on the physical side, they are called **frames**. A typical page/frame size is 4 KB. A process's logical address space might consist of 256 pages (1 MB total), but those pages can be scattered across any 256 available frames in physical memory — they need not be adjacent. The OS maintains a **page table** for each process that records the mapping: page 0 is in frame 47, page 1 is in frame 312, page 2 is in frame 5, and so on. External fragmentation is eliminated because any free frame can hold any page. The only waste is **internal fragmentation** — the last page of a process may not be completely full (on average, half a page is wasted per process).

Every memory access by the CPU triggers address translation. The hardware splits the logical address into two parts: the high-order bits form the **page number**, which indexes into the page table to find the corresponding frame number; the low-order bits form the **offset** within the page, which is unchanged. The frame number replaces the page number, and the result is the physical address. For example, with a 4 KB page size (12-bit offset), the logical address 0x00003A7F has page number 3 and offset 0xA7F. If the page table says page 3 maps to frame 100 (0x64), the physical address is 0x00064A7F. This translation happens on every single memory access, so it must be fast.

The problem is that the page table itself lives in memory, so a naive implementation doubles every memory access: one access to read the page table entry, then another to read the actual data. The **Translation Lookaside Buffer (TLB)** solves this. The TLB is a small, fast hardware cache (typically 64-1024 entries) that stores recently used page-to-frame mappings. On a TLB hit, translation adds zero extra memory accesses. On a TLB miss, the hardware walks the page table, caches the result in the TLB, and future accesses to that page are fast. Because programs exhibit spatial and temporal locality — they tend to access the same pages repeatedly — TLB hit rates above 99% are common, making the performance overhead of paging negligible in practice. For large address spaces (64-bit systems), a flat page table would itself consume gigabytes of memory, so modern systems use **multi-level page tables** that only allocate table entries for portions of the address space actually in use, trading a few extra memory accesses on TLB misses for dramatic space savings.
