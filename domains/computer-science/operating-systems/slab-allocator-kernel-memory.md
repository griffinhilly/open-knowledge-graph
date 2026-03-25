---
id: slab-allocator-kernel-memory
title: Slab Allocator for Kernel Memory
domain: computer-science
course: operating-systems
prerequisites:
- id: buddy-system-memory-allocation
  type: hard
- id: kernel-architecture
  type: soft
tags:
- allocation
- kernel
- performance
stage: advanced
status: validated
---

# Slab Allocator for Kernel Memory

## Core Idea
The slab allocator pre-allocates memory in slabs (contiguous blocks containing multiple objects of the same type) to reduce allocation overhead. Each object type (inode, file descriptor, task structure, etc.) has its own cache of slabs. The allocator caches pre-constructed objects to reduce initialization cost and dramatically improves kernel memory allocation performance.

## Questions

```yaml
- question: "What is the primary performance advantage of keeping freed kernel objects in a pre-initialized state in the slab allocator?"
  type: multiple-choice
  options:
    - "It allows the operating system to reclaim memory during idle periods by reusing object slots"
    - "It eliminates the cost of re-initializing objects on each allocation — since freed objects are returned ready-to-use, the next allocation just grabs a pre-constructed slot"
    - "It prevents memory leaks by maintaining a reference count on every allocated object"
    - "It allows multiple object types to share the same slab, increasing memory utilization"
  answer: 1
  explanation: "Kernel objects like task_struct or inodes require expensive setup every time they're created: zeroing fields, initializing internal locks, linking pointers. Without a slab allocator, every allocation means raw memory that must be fully initialized. With object caching, freed objects are returned to their slab in constructed state — the next allocation skips all that setup and just hands back an already-initialized slot. This is analogous to a restaurant that resets table settings after each customer rather than buying new plates every time."

- question: "A kernel developer argues: 'We should use the buddy system for all kernel allocations — it already handles fragmentation and is simpler.' What is the strongest objection to this proposal?"
  type: multiple-choice
  options:
    - "The buddy system cannot allocate memory on modern multi-core hardware"
    - "The buddy system allocates power-of-two blocks, so a 96-byte inode gets a 128-byte block (wasting 32 bytes per allocation), and it returns freed blocks as raw uninitialized memory — the slab allocator eliminates both the fragmentation and the re-initialization overhead"
    - "The buddy system is too slow for allocations larger than one page"
    - "The buddy system can only be used for user-space allocations, not kernel objects"
  answer: 1
  explanation: "The buddy system's power-of-two constraint causes internal fragmentation for small objects: a 96-byte inode rounded up to 128 bytes wastes 25% of allocated memory. More importantly, the buddy system treats every freed block as raw memory — the kernel must re-run the full initialization sequence each time. The slab allocator solves both: it pre-divides pages into exact-fit slots (no rounding) and caches objects in constructed state. The two systems work together rather than competing: buddy handles page-level allocation; slab handles fine-grained type-specific allocation."

- question: "In a slab allocator, each object type (inode, task_struct, file descriptor) has its own dedicated cache containing slabs sized for that type."
  type: true-false
  answer: true
  explanation: "This type-specific design is central to the slab allocator's efficiency. By creating a separate cache per object type, the allocator can size slots exactly for each type (no rounding), pre-initialize objects in the form they need, and locate free slots instantly without searching. When the kernel needs a new inode, it asks the inode cache — which hands back an already-sized, pre-constructed slot with no search, no splitting, no initialization."

- question: "The slab allocator replaces the buddy system, taking over page-level memory management from the Linux kernel."
  type: true-false
  answer: false
  explanation: "The slab allocator and the buddy system work together at different levels of granularity. The buddy system handles coarse-grained page allocation — it gives the slab allocator the pages it needs for new slabs. The slab allocator then sub-divides those pages into fine-grained, type-specific object slots. Neither replaces the other: remove the buddy system and the slab allocator has no source of pages; remove the slab allocator and the buddy system must handle millions of small object allocations inefficiently."

- question: "Why does the slab allocator reduce internal memory fragmentation compared to the buddy system, and how does object caching further improve performance beyond just fragmentation reduction?"
  type: short-answer
  answer: "The buddy system allocates power-of-two blocks, so small objects are rounded up: a 96-byte inode gets a 128-byte block, wasting 32 bytes per object — internal fragmentation. The slab allocator pre-divides pages into slots exactly sized for one object type, so a 96-byte inode occupies exactly 96 bytes with no rounding waste. Object caching adds a second improvement that fragmentation reduction alone doesn't provide: instead of returning freed memory to a raw pool (requiring full re-initialization next time), the slab keeps freed objects in constructed state. Since many kernel objects require expensive setup (zeroing fields, initializing spinlocks, setting up internal pointers), avoiding redundant initialization on each allocation dramatically reduces allocation latency beyond what merely eliminating fragmentation would achieve."
  explanation: "The two benefits are independent: you could eliminate fragmentation with a non-power-of-two allocator without caching pre-initialized objects, and you could cache objects without eliminating fragmentation. The slab allocator does both simultaneously because type-specific caches naturally enable type-specific object sizes."
```

## Explainer

From the buddy system, you know how the kernel can allocate and free memory in power-of-two-sized blocks while keeping fragmentation manageable through splitting and coalescing. But the buddy system has a problem: the kernel constantly allocates and frees small, identically-sized objects — a task_struct here, an inode there, a file descriptor over there — and the buddy system treats every allocation as a generic block request. It wastes memory on internal fragmentation (a 96-byte inode gets a 128-byte block), and it pays initialization costs every time because each freed block is returned to the pool as raw memory. The **slab allocator** solves both problems by recognizing that the kernel allocates the same types of objects over and over.

The design works in three layers: **caches**, **slabs**, and **objects**. A cache is created for each type of kernel object — there's a cache for inodes, a cache for dentry structures, a cache for task_struct, and so on. Each cache contains one or more slabs, where a slab is a contiguous chunk of memory (typically one or a few pages obtained from the buddy system) that has been pre-divided into slots exactly the right size for that object type. When the kernel needs a new inode, it asks the inode cache, which hands back an already-sized slot from a slab. No searching, no splitting, no size rounding — just grab the next free slot.

The key insight that makes slab allocation fast is **object caching**. When an object is freed, it isn't destroyed — it's returned to the slab in a **pre-initialized** state, ready to be handed out again. Many kernel objects require expensive initialization (setting up internal locks, zeroing fields, linking pointers), and this initialization is identical every time. By keeping freed objects constructed, the allocator avoids redoing that setup work on each allocation. Think of it like a restaurant that washes and resets table settings after each customer rather than buying new plates every time. The plates are "freed" but remain ready to use.

Slabs within a cache exist in three states: **full** (all object slots occupied), **partial** (some slots free), and **empty** (all slots free). The allocator satisfies requests from partial slabs first, falling back to empty slabs, and only requesting new pages from the buddy system when no empty slabs remain. This layered approach means the slab allocator and the buddy system work together: the buddy system handles large, coarse-grained page allocations, and the slab allocator handles the fine-grained, type-specific allocations that dominate kernel activity. The result is dramatically reduced fragmentation, faster allocation, and lower initialization overhead — all of which matter in an environment where millions of small objects are created and destroyed every second.
