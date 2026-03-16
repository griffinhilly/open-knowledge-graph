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
status: draft
---

# Buddy System Memory Allocation

## Core Idea
The buddy system allocates memory in power-of-two sizes, recursively subdividing large blocks and merging free blocks of equal size. It reduces external fragmentation compared to simple contiguous allocation and enables efficient coalescing of freed memory. The algorithm is practical for kernel memory allocation but has internal fragmentation overhead due to power-of-two constraints.

## Explainer

From your study of memory management and contiguous allocation, you know the fundamental problem: as processes allocate and free memory over time, free space becomes scattered into small, unusable fragments — **external fragmentation**. Simple first-fit or best-fit allocators struggle with this because freed blocks of different sizes are difficult to recombine. The buddy system attacks fragmentation with an elegant constraint: every allocated block must be a power of two in size, and every block has exactly one natural partner — its **buddy** — that it can merge with when both are free.

Here is how allocation works. Suppose you manage 1024 KB of memory and a process requests 100 KB. The smallest power of two that fits is 128 KB. You start with the full 1024 KB block and split it in half: two 512 KB blocks. The first 512 KB block is still too large, so you split it again: two 256 KB blocks. Split once more: two 128 KB blocks. You hand one 128 KB block to the process and keep the other as free. The remaining 512 KB and 256 KB blocks stay on their respective free lists. Each split creates two **buddies** — blocks of equal size at adjacent, predictable addresses. The address of a block's buddy can be computed with a single XOR operation on the block's address, which makes the data structure extremely fast.

Deallocation is where the buddy system truly shines. When a block is freed, you check whether its buddy is also free. If it is, you **coalesce** them back into a single block of double the size. Then you check whether that merged block's buddy is free, and merge again if possible, continuing up the hierarchy. This recursive merging happens in O(log n) time and aggressively combats external fragmentation — free blocks naturally reassemble into larger ones without any compaction or copying. Compare this to a general-purpose allocator, where two adjacent free blocks of different sizes require complex bookkeeping to merge.

The tradeoff is **internal fragmentation**: every allocation is rounded up to the next power of two. That 100 KB request gets a 128 KB block, wasting 28 KB. A 33 KB request wastes nearly half its 64 KB block. In the worst case, you waste almost 50% of each allocation. This is why the buddy system is most commonly used in kernel memory allocation (where allocation sizes tend to cluster around powers of two) rather than as a general-purpose user-space allocator. Linux, for example, uses the buddy system to manage physical page frames, with a separate **slab allocator** layered on top to efficiently handle the small, fixed-size objects (like process descriptors and inode structures) that would waste too much space under buddy allocation alone.
