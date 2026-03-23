---
id: virtual-memory-and-demand-paging
title: Virtual Memory and Demand Paging
domain: computer-science
course: operating-systems
prerequisites:
- id: memory-management-paging
  type: hard
- id: page-replacement-algorithms-lru-fifo
  type: soft
tags:
- virtual-memory
- memory-management
- demand-paging
stage: formal-systems
status: validated
---

# Virtual Memory and Demand Paging

## Core Idea
Virtual memory abstracts hardware memory, giving processes the illusion of a large, contiguous address space. Demand paging loads pages on-demand from disk when accessed, not preemptively. This enables oversubscription (total virtual memory > physical memory) and strong process isolation. Page faults trigger I/O; performance depends on locality and page replacement policy.

## Questions

```yaml
- question: "A process accesses a virtual address that is marked 'not present' in the page table. What sequence of events follows?"
  type: multiple-choice
  options:
    - "The CPU returns a null pointer and the process handles the error"
    - "The hardware raises a page fault; the OS locates the page on disk, loads it into a free frame, updates the page table, and resumes the faulting instruction"
    - "The OS immediately terminates the process with a segmentation fault"
    - "The memory management unit skips the access and moves to the next instruction"
  answer: 1
  explanation: "A page fault is a trap, not an error. The hardware detects the missing present-bit and transfers control to the OS page fault handler. The OS performs the I/O to bring the page from disk (or the executable file) into a physical frame, updates the page table entry, and then resumes the original instruction — which now succeeds. From the process's perspective, nothing unusual happened other than the access taking longer. Option C (segfault) only occurs if the address is invalid (not mapped at all), not merely not-present."

- question: "Why does 'thrashing' occur in a system using demand paging?"
  type: multiple-choice
  options:
    - "The CPU runs too many processes simultaneously, causing hardware overheating"
    - "A process's working set exceeds available physical memory, causing continuous page faults that consume more time than useful computation"
    - "The page table grows too large to fit in RAM"
    - "Demand paging loads too many pages at process startup, immediately exhausting memory"
  answer: 1
  explanation: "Thrashing happens when the combined working sets of active processes exceed physical memory. Every page brought in requires evicting another page that will be faulted back in moments later. The system spends almost all its time on disk I/O (page faults take ~10ms) rather than computation. Option D is precisely backwards — demand paging deliberately avoids loading pages at startup; it is the lazy nature of demand paging that normally prevents this kind of memory exhaustion."

- question: "Two processes that both reference virtual address 0x4000 are actually accessing different physical memory locations."
  type: true-false
  answer: true
  explanation: "Each process has its own independent page table. Virtual address 0x4000 in process A maps through A's page table to some physical frame, while the same virtual address in process B maps through B's page table to a completely different frame. This address space isolation is an architectural guarantee: a process cannot name any physical address outside its own mapping, making inter-process memory corruption structurally impossible (absent explicit shared memory)."

- question: "Demand paging loads all pages of a program into physical memory when the process starts, ensuring fast access throughout execution."
  type: true-false
  answer: false
  explanation: "This describes eager loading, which is the opposite of demand paging. Demand paging is explicitly lazy: the OS marks most pages as not-present and loads them only when a page fault occurs. This makes processes start faster (no waiting for all pages to load), uses memory efficiently (pages never touched are never loaded), and enables overcommitment (total virtual allocations can exceed physical RAM). The cost is that the first access to any page incurs a fault."

- question: "Why is demand paging's lazy loading strategy beneficial even though page faults are extremely slow compared to normal memory accesses?"
  type: short-answer
  answer: "Demand paging is beneficial because most programs exhibit locality — they actively use only a small fraction of their allocated memory (the working set) at any given time. Pages that are never accessed never need to be loaded, saving both time and physical memory. Programs start faster because startup only loads what is immediately needed. Physical memory can be oversubscribed across many processes, each using a fraction of their virtual space. The slowness of individual faults is acceptable because they are rare for well-behaved programs."
  explanation: "The key insight is that the cost of a page fault matters less than the frequency of faults. A program that uses 10% of its virtual pages will rarely fault once its working set is warm. The 1-million-times speed difference between RAM and disk only becomes catastrophic if faults happen constantly (thrashing). For programs with good locality, demand paging provides the illusion of vast memory at the cost of occasional slow faults — an excellent trade-off in practice."
```

## Explainer

From your study of paging, you know that physical memory is divided into fixed-size frames and that a page table translates virtual addresses to physical frame numbers. **Virtual memory** extends this idea to its logical conclusion: every process gets its own complete virtual address space — typically 2^48 bytes or more on a 64-bit system — regardless of how much physical RAM is installed. The operating system and hardware collaborate to maintain the illusion that all of this space is available, even though only a fraction is backed by physical memory at any moment. The rest lives on disk, ready to be brought in when needed.

**Demand paging** is the strategy that makes this practical. Rather than loading an entire program into memory at startup, the OS marks most pages as "not present" in the page table. When the CPU tries to access a not-present page, the hardware raises a **page fault** — a trap to the operating system. The OS then locates the page's contents on disk (in a swap area or the original executable file), finds a free physical frame, reads the page data from disk into that frame, updates the page table to point to the new frame, and resumes the faulting instruction. From the process's perspective, nothing unusual happened — the memory access simply took a bit longer. This lazy loading means programs start faster (no waiting for everything to load) and memory-efficient programs never load pages they do not actually touch.

The critical tradeoff is performance. A normal memory access takes nanoseconds; a page fault that requires reading from disk takes milliseconds — roughly a million times slower. This is why **locality of reference** matters so much. Programs that access memory in predictable patterns (sequential array traversal, repeatedly using the same working set of data) fault rarely because their active pages stay in memory. Programs with scattered, unpredictable access patterns generate frequent faults and grind to a halt — a condition called **thrashing**, where the system spends more time swapping pages than doing useful work. You may recall page replacement algorithms like LRU and FIFO from your prerequisites; these algorithms decide which page to evict when all physical frames are occupied. A good replacement policy keeps the working set in memory and evicts pages that will not be needed soon.

Virtual memory also provides **process isolation** as an architectural guarantee, not just a convention. Because each process has its own page table, process A literally cannot name a physical address belonging to process B — the address "0x4000" in process A maps to a completely different frame than "0x4000" in process B. A buggy or malicious process can corrupt its own memory but cannot reach another process's data. This same mechanism enables features like copy-on-write (sharing pages between processes until one writes, at which point the OS transparently duplicates the page), memory-mapped files (mapping a file's contents directly into the address space), and overcommit (allocating more virtual memory than physical RAM plus swap, betting that not all of it will be used simultaneously).
