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

## Questions

```yaml
- question: "On a system with 4 KB pages (12-bit offset), what are the two components of a 32-bit virtual address 0x00A01B3C?"
  type: multiple-choice
  options:
    - "Virtual page number = 0x00A01B3C (all bits); offset = determined at runtime"
    - "Virtual page number = 0x00A01 (upper 20 bits); offset = 0xB3C (lower 12 bits)"
    - "Virtual page number = 0x00A (upper 12 bits); offset = 0x01B3C (lower 20 bits)"
    - "Virtual page number = 0xB3C (lower 12 bits); offset = 0x00A01 (upper 20 bits)"
  answer: 1
  explanation: "With 4 KB = 2¹² bytes per page, the page offset is 12 bits (the low bits), and all remaining high bits form the virtual page number. For 0x00A01B3C: low 12 bits = 0xB3C (the offset within the page), upper 20 bits = 0x00A01 (the VPN used to index the page table). The offset is always preserved unchanged through translation — it identifies the same byte position within whatever physical frame the VPN maps to."

- question: "A 64-bit address space with 4 KB pages would need a flat single-level page table with roughly 2⁵² entries. Why do multi-level page tables solve this problem?"
  type: multiple-choice
  options:
    - "Multi-level page tables use smaller page sizes, reducing the total number of entries required"
    - "Only the second-level tables corresponding to address regions the process actually uses need to be allocated, leaving most of the address space without a table"
    - "Multi-level tables compress entries using variable-length encoding"
    - "Multiple processes share page table entries, dividing the total memory cost among them"
  answer: 1
  explanation: "The key insight is sparse allocation. A flat page table must preallocate entries for the entire address space. A multi-level table uses a directory at the first level — if a region of the address space is unused, the corresponding directory entry is null and no second-level table is ever allocated. Since most programs use only a tiny fraction of a 64-bit address space, this saves enormous amounts of memory."

- question: "The page offset portion of a virtual address passes through address translation unchanged and becomes the same offset in the physical address."
  type: true-false
  answer: true
  explanation: "Translation only changes the virtual page number to a physical frame number — the offset within the page stays identical. This works because pages and frames are the same size: if a byte is at position 0xB3C within virtual page N, it is at position 0xB3C within whatever physical frame N maps to. The page-frame mapping changes which 'page' the byte lives in, but not where within that page it sits."

- question: "A TLB miss means the requested page is not in physical memory and must be loaded from disk."
  type: true-false
  answer: false
  explanation: "A TLB miss means the address translation (VPN → PFN mapping) is not currently cached in the TLB. The hardware or OS must look up the page table in memory to find the mapping — the page itself may well be in physical memory. A page fault occurs when the page table entry's valid bit is 0, meaning the page is not in RAM at all and must be fetched from disk. TLB miss = cached translation unavailable; page fault = page not in physical memory."

- question: "What is the purpose of the TLB, and why does it make address translation practical given that it would otherwise require an extra memory access on every instruction?"
  type: short-answer
  answer: "The TLB is a small, fast hardware cache for recently used VPN-to-PFN mappings. Without it, every memory access would require one or more additional memory accesses to traverse the page table, doubling or tripling memory latency. The TLB works because programs exhibit strong locality — they access the same pages repeatedly, keeping TLB hit rates above 99%. In the common case, translation adds essentially no latency."
  explanation: "The TLB exploits temporal locality: if you accessed a page once, you will very likely access it again soon. On a TLB hit, translation is done in hardware in a single fast lookup. On a TLB miss, the hardware walks the page table — slow but rare. This is why virtual memory is practical despite the conceptual overhead of address translation on every memory reference."
```

## Explainer

From your study of paging and segmentation, you know that virtual memory gives each process the illusion of its own large, contiguous address space, even though physical memory is smaller and shared. The mechanism that maintains this illusion is **address translation** — the hardware converts every virtual address the program uses into a physical address that points to actual RAM. This translation happens on every single memory access, so it must be fast and correct.

A virtual address is divided into two parts: the **virtual page number** (VPN) and the **page offset**. If pages are 4 KB (2¹² bytes), then the low 12 bits of the address are the offset within the page, and all remaining upper bits form the VPN. The offset passes through translation unchanged — it identifies the same byte position within the page regardless of where the page lives in physical memory. The VPN is used to index into a **page table**, a data structure maintained by the operating system that maps each virtual page to a **physical frame number** (PFN). The translated physical address is simply the PFN concatenated with the original offset.

A single flat page table would be enormous. A 32-bit address space with 4 KB pages has 2²⁰ (about one million) entries; a 64-bit space would require an impossibly large table. The solution is **multi-level page tables**. Instead of one giant table, the VPN is split into multiple fields, each indexing a separate level. A two-level scheme uses the upper VPN bits to index a first-level **page directory**, which points to second-level page tables. Only the second-level tables that correspond to memory the process actually uses need to exist — the rest are never allocated. This dramatically reduces memory consumption for processes that use a sparse address space, which is the common case.

Each page table entry contains more than just the physical frame number. **Control bits** indicate whether the page is present in physical memory (the valid bit), whether it has been modified (the dirty bit), whether it has been accessed recently (the reference bit), and what access permissions apply (read, write, execute). When a program accesses a page whose valid bit is clear, the hardware raises a **page fault**, transferring control to the operating system, which loads the page from disk and updates the table. This is the mechanism that allows programs to use more memory than physically exists — the OS transparently swaps pages between RAM and disk.

The fundamental cost of translation is that every memory access now requires at least one additional memory access to read the page table (or two for a two-level scheme). This would double or triple memory latency, which is why hardware includes a **translation lookaside buffer** (TLB) — a small, fast cache that stores recently used VPN-to-PFN mappings. Because programs exhibit strong locality (they access the same pages repeatedly), the TLB hit rate is typically above 99%, making translation nearly free in the common case. Understanding this entire chain — address splitting, page table lookup, control bits, and TLB caching — is essential for reasoning about memory performance and operating system behavior.
