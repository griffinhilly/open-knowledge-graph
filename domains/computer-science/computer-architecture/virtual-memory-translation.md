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

## Explainer

From your study of paging and segmentation, you know that virtual memory gives each process the illusion of its own large, contiguous address space, even though physical memory is smaller and shared. The mechanism that maintains this illusion is **address translation** — the hardware converts every virtual address the program uses into a physical address that points to actual RAM. This translation happens on every single memory access, so it must be fast and correct.

A virtual address is divided into two parts: the **virtual page number** (VPN) and the **page offset**. If pages are 4 KB (2¹² bytes), then the low 12 bits of the address are the offset within the page, and all remaining upper bits form the VPN. The offset passes through translation unchanged — it identifies the same byte position within the page regardless of where the page lives in physical memory. The VPN is used to index into a **page table**, a data structure maintained by the operating system that maps each virtual page to a **physical frame number** (PFN). The translated physical address is simply the PFN concatenated with the original offset.

A single flat page table would be enormous. A 32-bit address space with 4 KB pages has 2²⁰ (about one million) entries; a 64-bit space would require an impossibly large table. The solution is **multi-level page tables**. Instead of one giant table, the VPN is split into multiple fields, each indexing a separate level. A two-level scheme uses the upper VPN bits to index a first-level **page directory**, which points to second-level page tables. Only the second-level tables that correspond to memory the process actually uses need to exist — the rest are never allocated. This dramatically reduces memory consumption for processes that use a sparse address space, which is the common case.

Each page table entry contains more than just the physical frame number. **Control bits** indicate whether the page is present in physical memory (the valid bit), whether it has been modified (the dirty bit), whether it has been accessed recently (the reference bit), and what access permissions apply (read, write, execute). When a program accesses a page whose valid bit is clear, the hardware raises a **page fault**, transferring control to the operating system, which loads the page from disk and updates the table. This is the mechanism that allows programs to use more memory than physically exists — the OS transparently swaps pages between RAM and disk.

The fundamental cost of translation is that every memory access now requires at least one additional memory access to read the page table (or two for a two-level scheme). This would double or triple memory latency, which is why hardware includes a **translation lookaside buffer** (TLB) — a small, fast cache that stores recently used VPN-to-PFN mappings. Because programs exhibit strong locality (they access the same pages repeatedly), the TLB hit rate is typically above 99%, making translation nearly free in the common case. Understanding this entire chain — address splitting, page table lookup, control bits, and TLB caching — is essential for reasoning about memory performance and operating system behavior.
