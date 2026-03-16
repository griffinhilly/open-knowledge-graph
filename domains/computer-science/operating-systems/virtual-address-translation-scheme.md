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

## Explainer

From your study of virtual memory, you know that each process operates in its own virtual address space, isolated from every other process. The question is: how does the hardware convert a virtual address into a physical address in RAM on every single memory access? **Paging** is the dominant answer. The virtual address space is divided into fixed-size chunks called **pages** (typically 4 KB), and physical memory is divided into same-sized chunks called **frames**. A **page table** — one per process — maps each virtual page number to the physical frame number where that page currently resides.

The translation works by splitting every virtual address into two parts: the **virtual page number** (VPN) and the **offset** within the page. The VPN indexes into the page table to find the corresponding physical frame number. The offset stays the same — it tells you where within the page the byte lives. The hardware concatenates the frame number with the offset to produce the physical address. For example, with 4 KB pages (12-bit offset), a virtual address with VPN 5 and offset 200 might map to frame 17, producing physical address (17 × 4096) + 200. This split-and-lookup operation happens on every memory reference your program makes.

The problem with a simple flat page table is size. A 32-bit address space with 4 KB pages has over a million page table entries; a 64-bit space would need an impossibly large table. **Multi-level page tables** solve this by turning the page table into a tree. The VPN is split into multiple indices — for example, a two-level scheme splits it into a directory index and a table index. The first index finds a page directory entry, which points to a second-level page table, which contains the actual frame mapping. Pages of the page table that correspond to unmapped virtual memory need not exist at all, saving enormous amounts of memory. Modern x86-64 processors use four-level page tables for this reason.

Even with efficient page tables, every memory access would require multiple memory reads just to walk the page table — one read per level. This would make programs several times slower. The **Translation Lookaside Buffer** (TLB) eliminates this cost for the common case. The TLB is a small, fast hardware cache that stores recent virtual-to-physical translations. On a **TLB hit**, the translation completes in a single cycle with no page table walk. On a **TLB miss**, the hardware walks the page table, installs the result in the TLB, and retries. Because programs exhibit strong locality — they access the same pages repeatedly — TLB hit rates typically exceed 99%, making paging nearly free in practice despite the complexity of the translation machinery underneath.
