---
id: buddy-system-memory-allocation
title: Buddy System Memory Allocation
domain: computer-science
course: operating-systems
prerequisites:
- id: memory-management-basics
  type: hard
- id: contiguous-memory-allocation
  type: soft
builds-toward:
- slab-allocator-kernel-memory
tags:
- allocation
- memory
- fragmentation
stage: formal-systems
status: validated
---

# Buddy System Memory Allocation

## Core Idea
The buddy system allocates memory in power-of-two sizes, recursively subdividing large blocks and merging free blocks of equal size. It reduces external fragmentation compared to simple contiguous allocation and enables efficient coalescing of freed memory. The algorithm is practical for kernel memory allocation but has internal fragmentation overhead due to power-of-two constraints.

## Questions

```yaml
- question: "A process requests 70 KB of memory from a buddy allocator managing 512 KB total. How much memory is actually allocated to this process?"
  type: multiple-choice
  options:
    - "70 KB — the buddy system allocates exactly the requested amount"
    - "64 KB — the buddy system rounds down to the nearest power of two to save space"
    - "128 KB — the buddy system rounds up to the next power of two that fits the request"
    - "512 KB — the entire managed region is always allocated as a single block"
  answer: 2
  explanation: "The buddy system requires all allocations to be a power of two in size. 64 KB is too small for a 70 KB request, so the smallest power of two that fits is 128 KB. This means 58 KB is wasted inside the block — this is internal fragmentation, the core tradeoff of the buddy system. The benefit is that every block has a predictable buddy address, enabling fast coalescing when freed."

- question: "The buddy system can locate a freed block's buddy extremely quickly using:"
  type: multiple-choice
  options:
    - "A linear scan through all free lists to find a block of matching size"
    - "A single XOR operation on the block's starting address"
    - "A hash table lookup keyed on block size"
    - "Traversal of a binary search tree sorted by starting address"
  answer: 1
  explanation: "Because block sizes are powers of two and blocks are aligned to their own size, a block's buddy is always at a predictable address that differs in exactly one bit — the bit corresponding to the block size. This means the buddy address = block_address XOR block_size. A single XOR is O(1) and is one of the key reasons the buddy system is practical in kernels like Linux: both allocation and deallocation are efficient."

- question: "The buddy system eliminates both internal and external fragmentation, making it the ideal general-purpose memory allocator."
  type: true-false
  answer: false
  explanation: "The buddy system reduces *external* fragmentation (scattered unusable gaps between allocations) by enforcing power-of-two sizes that enable fast, predictable coalescing. But it introduces *internal* fragmentation: any request that isn't exactly a power of two wastes space within its allocated block. A 33 KB request wastes nearly half of its 64 KB block. This is why the buddy system is used for kernel page-frame management — where sizes cluster near powers of two — rather than as a general user-space allocator."

- question: "When a block is freed in the buddy system, the allocator checks whether its buddy is also free, merges them into a double-sized block, then checks whether that merged block's buddy is also free, continuing up the hierarchy."
  type: true-false
  answer: true
  explanation: "This recursive coalescing is the buddy system's primary defense against external fragmentation. Each merge doubles the block size, and the check continues up the hierarchy until a non-free buddy is found or the entire memory region is merged into one block. The XOR property makes each buddy check O(1), so the entire coalescing process is O(log n) where n is the number of levels. This aggressive merging means free memory naturally reassembles into large blocks without any compaction."

- question: "Why does the buddy system impose power-of-two block sizes, and what problem does this constraint create?"
  type: short-answer
  answer: "Power-of-two sizes are required so that every block has a unique, easily computed buddy at a predictable address (found via a single XOR operation). This mathematical regularity is what enables O(1) buddy lookup and O(log n) coalescing — the system can quickly merge free blocks back into larger ones, combating external fragmentation without scanning through arbitrary block sizes. The problem this creates is internal fragmentation: every allocation is rounded up to the next power of two, so a 100 KB request wastes 28 KB of its 128 KB block. In the worst case, nearly 50% of each block is wasted. This is why the buddy system is layered with a slab allocator in Linux — the slab allocator handles small, fixed-size objects that would otherwise waste too much space under buddy constraints."
  explanation: "The design tension in the buddy system is between algorithmic efficiency (power-of-two sizes make buddy finding trivial) and space efficiency (power-of-two sizes cause rounding waste). The system optimizes for time at the cost of space, which is an acceptable tradeoff in kernel page-frame management where allocation sizes tend to be page-sized or multiples of pages."
```

## Explainer

From your study of memory management and contiguous allocation, you know the fundamental problem: as processes allocate and free memory over time, free space becomes scattered into small, unusable fragments — **external fragmentation**. Simple first-fit or best-fit allocators struggle with this because freed blocks of different sizes are difficult to recombine. The buddy system attacks fragmentation with an elegant constraint: every allocated block must be a power of two in size, and every block has exactly one natural partner — its **buddy** — that it can merge with when both are free.

Here is how allocation works. Suppose you manage 1024 KB of memory and a process requests 100 KB. The smallest power of two that fits is 128 KB. You start with the full 1024 KB block and split it in half: two 512 KB blocks. The first 512 KB block is still too large, so you split it again: two 256 KB blocks. Split once more: two 128 KB blocks. You hand one 128 KB block to the process and keep the other as free. The remaining 512 KB and 256 KB blocks stay on their respective free lists. Each split creates two **buddies** — blocks of equal size at adjacent, predictable addresses. The address of a block's buddy can be computed with a single XOR operation on the block's address, which makes the data structure extremely fast.

Deallocation is where the buddy system truly shines. When a block is freed, you check whether its buddy is also free. If it is, you **coalesce** them back into a single block of double the size. Then you check whether that merged block's buddy is free, and merge again if possible, continuing up the hierarchy. This recursive merging happens in O(log n) time and aggressively combats external fragmentation — free blocks naturally reassemble into larger ones without any compaction or copying. Compare this to a general-purpose allocator, where two adjacent free blocks of different sizes require complex bookkeeping to merge.

The tradeoff is **internal fragmentation**: every allocation is rounded up to the next power of two. That 100 KB request gets a 128 KB block, wasting 28 KB. A 33 KB request wastes nearly half its 64 KB block. In the worst case, you waste almost 50% of each allocation. This is why the buddy system is most commonly used in kernel memory allocation (where allocation sizes tend to cluster around powers of two) rather than as a general-purpose user-space allocator. Linux, for example, uses the buddy system to manage physical page frames, with a separate **slab allocator** layered on top to efficiently handle the small, fixed-size objects (like process descriptors and inode structures) that would waste too much space under buddy allocation alone.
