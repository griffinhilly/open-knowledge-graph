---
id: translation-lookaside-buffer-tlb
title: Translation Lookaside Buffer (TLB) Design
domain: computer-science
course: computer-architecture
prerequisites:
- id: virtual-memory-translation
  type: hard
- id: cache-associativity-and-mapping
  type: soft
builds-toward:
- exception-handling-architecture
tags:
- tlb
- address-translation
- cache
stage: formal-systems
status: draft
---

# Translation Lookaside Buffer (TLB) Design

## Core Idea
The TLB is a small associative cache that stores recent virtual-to-physical address translations. A TLB hit provides the physical page number in one cycle; a miss requires a page table walk (several memory accesses). TLB entries include the virtual page number, physical page number, and protection bits. TLB size is a trade-off between speed and area; typical sizes are 32–512 entries.

## Questions

```yaml
- question: "A processor uses 4 KB pages and has a fully loaded 64-entry TLB. What is the maximum total memory range that could be covered without a TLB miss?"
  type: multiple-choice
  options:
    - "64 bytes — each TLB entry covers one byte"
    - "64 KB — one byte per entry times 1,024 entries"
    - "256 KB — 64 entries × 4 KB per page"
    - "4 MB — each TLB entry caches an entire 4 MB segment"
  answer: 2
  explanation: "Each TLB entry maps one virtual page number to one physical page number, and each page is 4 KB. With 64 entries fully populated, the TLB can cover 64 × 4 KB = 256 KB of address space without any misses. This illustrates why even a small TLB achieves high hit rates — programs tend to use a working set of a few dozen pages repeatedly (locality of reference), and those pages fit comfortably in a 64-entry TLB. Options A and B confuse entry count with bytes. Option D describes large page support, not standard 4 KB pages."

- question: "On a MIPS processor (software-managed TLB), what happens when the CPU encounters a TLB miss?"
  type: multiple-choice
  options:
    - "The processor halts until the user program re-issues the memory access"
    - "The hardware automatically walks the page table and fills the TLB entry"
    - "A TLB miss exception is raised, and the OS trap handler looks up the translation and loads it into the TLB"
    - "The memory access is aborted and the process is killed with a segmentation fault"
  answer: 2
  explanation: "MIPS uses a software-managed TLB: on a miss, the CPU raises an exception (TLB miss trap), transferring control to the OS's trap handler. The OS finds the correct translation in the page table and writes it into the TLB, then resumes execution. Option B describes the x86 hardware-managed TLB approach — the processor itself walks the page table. Software management costs more per miss but gives the OS flexibility to use any page table format. Options A and D are wrong — a TLB miss is a normal event handled transparently."

- question: "Because the TLB is fully associative, each virtual page number always maps to the same fixed TLB slot, just like a direct-mapped cache."
  type: true-false
  answer: false
  explanation: "Fully associative means the opposite: any virtual page number can be stored in any TLB slot. The TLB searches all entries simultaneously using parallel comparators to find a match — this is what makes it associative. Direct-mapped caches use modulo indexing to send each address to a fixed slot. Full associativity maximizes hit rates (no conflict misses) at the cost of more complex hardware. This is the same associativity trade-off from your cache design studies, applied here to address translation."

- question: "TLB entries typically include protection bits that specify read, write, and execute permissions for the corresponding page."
  type: true-false
  answer: true
  explanation: "A TLB entry stores more than just the virtual-to-physical mapping. It includes protection bits (R/W/X permissions), a valid bit, and often an Address Space Identifier (ASID) to distinguish between processes. On a memory access, the processor checks the protection bits in the TLB entry against the type of access — if a user process tries to write to a read-only page, the protection check fails and a fault is raised, even though the translation itself was a TLB hit. This makes the TLB the primary enforcement point for memory protection in most architectures."

- question: "Why is the TLB necessary given that modern processors already have L1, L2, and L3 caches for fast data access?"
  type: short-answer
  answer: "Data caches speed up access to data and instructions, but they operate on physical addresses. Before any cache lookup can happen, the virtual address must be translated to a physical address — and that translation requires a page table lookup, which itself involves multiple memory accesses. Without the TLB, every memory access (including cache hits) would first require several slow memory accesses to traverse the page table. The TLB caches these translations so that address translation costs one cycle instead of tens to hundreds, making the rest of the memory hierarchy viable."
  explanation: "The TLB solves the meta-problem of address translation itself being slow. L1/L2/L3 caches reduce the latency of accessing data once you know its physical address. The TLB reduces the latency of computing that physical address in the first place. The two work together: a typical memory access hits the TLB (fast translation) and then hits L1 cache (fast data access), completing in a handful of cycles. Without the TLB, every access — even L1 cache hits — would first pay a page-table-walk penalty."
```

## Explainer

From your study of virtual memory translation, you know that every memory access requires converting a virtual address to a physical address by looking up the page table. The problem is that the page table itself lives in main memory, so a naive implementation would double the cost of every memory access — one access to translate the address, then another to fetch the actual data. The **translation lookaside buffer (TLB)** eliminates this penalty for the vast majority of accesses by caching recent translations in a small, fast, on-chip structure.

The TLB works on the same principle as the caches you have studied — **locality of reference**. Programs tend to access the same pages repeatedly (temporal locality) and access addresses near each other (spatial locality). Since a single page translation covers an entire 4 KB page (or larger), even a small TLB with 64 entries can cover 256 KB of actively used memory. When the processor issues a memory access, it extracts the virtual page number and simultaneously searches the TLB for a matching entry. If found (a **TLB hit**), the physical page number is returned in a single cycle and the memory access proceeds with no delay. If not found (a **TLB miss**), the processor must perform a **page table walk** — traversing the multi-level page table in memory to find the correct translation — which may cost tens to hundreds of cycles.

The TLB is typically organized as a **fully associative** or **set-associative** cache, drawing on the associativity concepts from your cache design studies. Fully associative means any translation can go in any TLB entry, which maximizes hit rates but requires comparing the virtual page number against every entry simultaneously using parallel comparators. Each TLB entry stores not just the virtual-to-physical mapping but also **protection bits** (read, write, execute permissions), a **valid bit**, and often an **address space identifier (ASID)** that tags which process owns the entry, avoiding the need to flush the entire TLB on every context switch.

TLB misses are handled in one of two ways depending on the architecture. In a **hardware-managed TLB** (as in x86), the processor itself walks the page table and fills the TLB entry automatically — software never sees the miss. In a **software-managed TLB** (as in MIPS), a TLB miss triggers an exception, and the operating system's trap handler looks up the translation and loads the TLB entry manually. Hardware management is faster for individual misses; software management gives the OS more flexibility in page table format. Either way, the TLB is the single most performance-critical structure in the memory hierarchy — a typical program experiences TLB hit rates above 99%, and even a small drop in hit rate can devastate performance because every memory access depends on translation.
