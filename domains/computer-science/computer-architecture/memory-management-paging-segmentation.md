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

## Questions

```yaml
- question: "A system uses segmentation for memory management. After many processes have run, allocated memory, and terminated, the system begins to struggle to find contiguous space for new segments even though total free memory appears sufficient. What problem is occurring?"
  type: multiple-choice
  options:
    - "Internal fragmentation — segments are leaving unused space at their ends"
    - "External fragmentation — free memory is scattered in small non-contiguous gaps between segments"
    - "Page table overflow — the segment table has run out of entries"
    - "Cache thrashing — segments are evicting each other from the CPU cache"
  answer: 1
  explanation: "External fragmentation is the characteristic failure mode of segmentation: because segments are variable in size, allocating and freeing them over time leaves scattered 'holes' of free memory. Even if total free space is larger than the requested segment, no single contiguous block is large enough. This is the fundamental problem that fixed-size paging solves — because any page can go into any frame, there is no external fragmentation."

- question: "What is internal fragmentation in a paging system?"
  type: multiple-choice
  options:
    - "Fragmentation caused by page table entries pointing to the wrong physical frames"
    - "Wasted space when the last page of a process is not fully utilized"
    - "The overhead cost of maintaining multilevel page tables"
    - "Fragmentation caused when two processes share the same physical frame"
  answer: 1
  explanation: "Internal fragmentation occurs because pages have a fixed size (e.g., 4 KB) and a process's last page is rarely exactly full. If a process needs 5 KB of memory, it gets two 4 KB pages (8 KB total), wasting up to 3 KB in the second page. This is the tradeoff paging accepts: no external fragmentation (any page fits any frame), but up to page-size-minus-one bytes wasted per process. This differs from external fragmentation, which is wasted space between allocations."

- question: "In a paging system, any virtual page can be placed into any available physical frame, regardless of its position in memory."
  type: true-false
  answer: true
  explanation: "This is the key advantage of fixed-size paging: because all pages and frames are the same size, there is no requirement that a process's pages occupy contiguous physical memory. The page table simply records which physical frame holds each virtual page. This eliminates external fragmentation entirely — the OS never has to search for a contiguous block large enough for a variable-size allocation. Pages can be scattered throughout physical RAM without any effect on the process's view of a contiguous virtual address space."

- question: "Segmentation eliminates fragmentation problems because each segment is sized exactly to fit the logical program unit it represents."
  type: true-false
  answer: false
  explanation: "Segmentation eliminates internal fragmentation (segments are exactly sized to their contents) but creates external fragmentation. The problem is not whether individual segments fit their contents — they do — but what happens over time as segments of different sizes are allocated and freed. The gaps left by freed segments are rarely exactly the right size for new allocations, so free memory gradually becomes scattered into unusable fragments. This external fragmentation is the primary reason paging, not segmentation, won as the dominant memory management scheme."

- question: "Why do modern operating systems primarily use paging rather than segmentation, even though segmentation more naturally reflects how programs are logically organized?"
  type: short-answer
  answer: "Paging uses fixed-size pages and frames, which eliminates external fragmentation — any page can go into any frame, so allocation is simple and predictable. Segmentation uses variable-size segments, which causes external fragmentation over time as differently-sized holes accumulate in memory. Managing variable-size allocations at hardware speed, maintaining compaction, and avoiding fragmentation are engineering problems that grow severe at scale. The logical elegance of segmentation (code, stack, heap as distinct segments) doesn't outweigh the practical cost of external fragmentation."
  explanation: "Modern x86-64 architectures support segmentation for backward compatibility but flatten it — all segments share the same base address and have the same limit, effectively disabling segmentation as a real memory division mechanism. The OS relies entirely on paging with multilevel page tables and TLB caching for performance. The lesson: the scheme with the simpler allocation model won, even at the cost of internal fragmentation."
```

## Explainer

From your study of virtual memory, you know the core motivation: programs should behave as if they have a large, private, contiguous address space, even though physical RAM is limited and shared. The question is how the hardware and operating system collaborate to translate virtual addresses into physical ones. **Paging** and **segmentation** are the two fundamental schemes for this translation, and understanding their tradeoffs explains why modern systems overwhelmingly use paging.

**Paging** divides the virtual address space into fixed-size blocks called **pages** (typically 4 KB) and physical memory into identically sized blocks called **frames**. A **page table** maps each virtual page number to a physical frame number. When the CPU generates a virtual address, the hardware splits it into a page number (upper bits) and an offset within the page (lower bits), looks up the page number in the page table to find the corresponding frame, and concatenates the frame number with the offset to produce the physical address. Because pages and frames are the same fixed size, any page can go into any available frame — there is no external fragmentation. The tradeoff is **internal fragmentation**: the last page of a process may not be fully used, wasting up to one page minus one byte.

**Segmentation** takes a different approach. Instead of uniform blocks, it divides the address space into variable-size **segments** that correspond to logical units of the program — code, stack, heap, data. Each segment has a base address and a length stored in a **segment table**. The hardware checks that the offset within a segment does not exceed its length (providing bounds checking), then adds the offset to the base address. Segmentation maps naturally onto how programmers think about programs, and it provides fine-grained protection — you can mark the code segment as read-only and executable while the data segment is read-write. However, because segments vary in size, allocating and deallocating them creates **external fragmentation**: free memory becomes scattered into small unusable gaps.

Modern architectures like x86-64 effectively use **paging as the primary mechanism** and have largely flattened segmentation into a compatibility feature. The reason is practical: fixed-size pages make allocation simple and predictable, multi-level page tables (and hardware TLBs that cache recent translations) make lookups fast, and the operating system can swap individual pages to disk without worrying about fitting variable-size chunks. Some historical systems combined both — segmented paging, where each segment is itself paged — to get the logical structure of segmentation with the allocation simplicity of paging. Understanding both schemes clarifies why paging won: the engineering cost of managing variable-size memory blocks at hardware speed is simply too high compared to the elegance of uniform pages.
