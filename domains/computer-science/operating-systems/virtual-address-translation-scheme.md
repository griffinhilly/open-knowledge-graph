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
status: validated
---

# Virtual Address Translation: Paging and TLBs

## Core Idea
Paging divides virtual and physical spaces into fixed-size pages; a page table maps virtual page numbers to physical frame numbers. Multi-level page tables reduce memory overhead; TLBs (translation lookaside buffers) cache recent translations for hardware-speed lookups.

## Questions

```yaml
- question: "A system uses 4 KB pages (12-bit offset) and 32-bit virtual addresses. A process references virtual address 0x00005200. The page table shows that virtual page 5 maps to physical frame 17. What is the physical address?"
  type: multiple-choice
  options:
    - "0x00005200 — virtual and physical addresses are the same after a TLB lookup"
    - "0x00011200 — frame 17 × 4096 + offset 0x200"
    - "0x00011000 — frame 17 × 4096, with the offset discarded after translation"
    - "Cannot be determined without knowing whether the TLB contains this entry"
  answer: 1
  explanation: "With 4 KB pages, the bottom 12 bits are the offset (0x200 = 512). The upper bits form VPN = 5. The page table maps VPN 5 → frame 17. Physical address = (17 × 4096) + 0x200 = 0x11000 + 0x200 = 0x11200. The offset is preserved unchanged — it tells you where within the page the byte lives. The TLB state affects performance (hit vs. miss) but not the final physical address."

- question: "Why do modern 64-bit operating systems use multi-level page tables instead of a single flat page table per process?"
  type: multiple-choice
  options:
    - "Flat page tables cannot store permission bits like read/write/execute"
    - "A flat page table for a 64-bit address space would require terabytes of memory per process, most of it wasted on unmapped regions"
    - "Multi-level tables allow the TLB to cache more entries simultaneously"
    - "Flat page tables only support 32-bit virtual addresses"
  answer: 1
  explanation: "A flat page table needs one entry per virtual page. A 64-bit address space with 4 KB pages has 2^52 possible pages — storing one 8-byte entry per page would require 32 petabytes per process. Multi-level page tables solve this by only allocating page table nodes for virtual address ranges the process actually uses. Unmapped regions (the vast majority of a 64-bit space) require no page table storage at all, making the structure sparse and practical."

- question: "On a TLB hit, the CPU must still access main memory once to verify the cached translation has not been invalidated."
  type: true-false
  answer: false
  explanation: "The entire purpose of the TLB is to eliminate page table memory accesses for the common case. On a TLB hit, the cached virtual-to-physical translation is used directly in a single cycle — no main memory access is needed for address translation. If TLB entries required verification on every access, the performance benefit would be entirely lost. Entries are invalidated by the OS on context switches and explicit flushes; between invalidations, cached translations are trusted."

- question: "The page offset portion of a virtual address is identical to the page offset in the resulting physical address."
  type: true-false
  answer: true
  explanation: "Paging maps entire pages to entire frames of the same size. The offset specifies a byte position within the page, and since the whole page is relocated to a frame, that relative position is unchanged. Only the page number changes (VPN → PFN); the offset carries through unchanged. This is why the translation formula is always: physical address = (frame number × page size) + offset, with the offset preserved exactly."

- question: "Why do TLB hit rates typically exceed 99% even though the TLB holds only a few dozen to a few hundred entries — a tiny fraction of a process's virtual address space?"
  type: short-answer
  answer: "Programs exhibit strong spatial and temporal locality: they repeatedly access the same variables, loop through the same arrays, and call the same functions. At any moment, most memory accesses cluster in a small working set of pages. The TLB only needs to cache the currently active pages. Because the same pages are accessed over and over in tight loops, a small cache covering those few active pages achieves near-perfect hit rates even though the full address space is enormous."
  explanation: "This matters enormously for performance. Without a TLB, every memory access would require 3–4 additional memory reads to walk a multi-level page table — reducing effective memory bandwidth by 4–5×. With >99% hit rates, translation overhead is nearly zero. Programs with poor locality (random memory access patterns) suffer lower TLB hit rates and significant slowdowns — TLB 'thrashing' — analogous to cache thrashing but at the page-table level."
```

## Explainer

From your study of virtual memory, you know that each process operates in its own virtual address space, isolated from every other process. The question is: how does the hardware convert a virtual address into a physical address in RAM on every single memory access? **Paging** is the dominant answer. The virtual address space is divided into fixed-size chunks called **pages** (typically 4 KB), and physical memory is divided into same-sized chunks called **frames**. A **page table** — one per process — maps each virtual page number to the physical frame number where that page currently resides.

The translation works by splitting every virtual address into two parts: the **virtual page number** (VPN) and the **offset** within the page. The VPN indexes into the page table to find the corresponding physical frame number. The offset stays the same — it tells you where within the page the byte lives. The hardware concatenates the frame number with the offset to produce the physical address. For example, with 4 KB pages (12-bit offset), a virtual address with VPN 5 and offset 200 might map to frame 17, producing physical address (17 × 4096) + 200. This split-and-lookup operation happens on every memory reference your program makes.

The problem with a simple flat page table is size. A 32-bit address space with 4 KB pages has over a million page table entries; a 64-bit space would need an impossibly large table. **Multi-level page tables** solve this by turning the page table into a tree. The VPN is split into multiple indices — for example, a two-level scheme splits it into a directory index and a table index. The first index finds a page directory entry, which points to a second-level page table, which contains the actual frame mapping. Pages of the page table that correspond to unmapped virtual memory need not exist at all, saving enormous amounts of memory. Modern x86-64 processors use four-level page tables for this reason.

Even with efficient page tables, every memory access would require multiple memory reads just to walk the page table — one read per level. This would make programs several times slower. The **Translation Lookaside Buffer** (TLB) eliminates this cost for the common case. The TLB is a small, fast hardware cache that stores recent virtual-to-physical translations. On a **TLB hit**, the translation completes in a single cycle with no page table walk. On a **TLB miss**, the hardware walks the page table, installs the result in the TLB, and retries. Because programs exhibit strong locality — they access the same pages repeatedly — TLB hit rates typically exceed 99%, making paging nearly free in practice despite the complexity of the translation machinery underneath.
