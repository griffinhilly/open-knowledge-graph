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
stage: formal-systems
status: draft
---

# Slab Allocator for Kernel Memory

## Core Idea
The slab allocator pre-allocates memory in slabs (contiguous blocks containing multiple objects of the same type) to reduce allocation overhead. Each object type (inode, file descriptor, task structure, etc.) has its own cache of slabs. The allocator caches pre-constructed objects to reduce initialization cost and dramatically improves kernel memory allocation performance.

## Explainer

From the buddy system, you know how the kernel can allocate and free memory in power-of-two-sized blocks while keeping fragmentation manageable through splitting and coalescing. But the buddy system has a problem: the kernel constantly allocates and frees small, identically-sized objects — a task_struct here, an inode there, a file descriptor over there — and the buddy system treats every allocation as a generic block request. It wastes memory on internal fragmentation (a 96-byte inode gets a 128-byte block), and it pays initialization costs every time because each freed block is returned to the pool as raw memory. The **slab allocator** solves both problems by recognizing that the kernel allocates the same types of objects over and over.

The design works in three layers: **caches**, **slabs**, and **objects**. A cache is created for each type of kernel object — there's a cache for inodes, a cache for dentry structures, a cache for task_struct, and so on. Each cache contains one or more slabs, where a slab is a contiguous chunk of memory (typically one or a few pages obtained from the buddy system) that has been pre-divided into slots exactly the right size for that object type. When the kernel needs a new inode, it asks the inode cache, which hands back an already-sized slot from a slab. No searching, no splitting, no size rounding — just grab the next free slot.

The key insight that makes slab allocation fast is **object caching**. When an object is freed, it isn't destroyed — it's returned to the slab in a **pre-initialized** state, ready to be handed out again. Many kernel objects require expensive initialization (setting up internal locks, zeroing fields, linking pointers), and this initialization is identical every time. By keeping freed objects constructed, the allocator avoids redoing that setup work on each allocation. Think of it like a restaurant that washes and resets table settings after each customer rather than buying new plates every time. The plates are "freed" but remain ready to use.

Slabs within a cache exist in three states: **full** (all object slots occupied), **partial** (some slots free), and **empty** (all slots free). The allocator satisfies requests from partial slabs first, falling back to empty slabs, and only requesting new pages from the buddy system when no empty slabs remain. This layered approach means the slab allocator and the buddy system work together: the buddy system handles large, coarse-grained page allocations, and the slab allocator handles the fine-grained, type-specific allocations that dominate kernel activity. The result is dramatically reduced fragmentation, faster allocation, and lower initialization overhead — all of which matter in an environment where millions of small objects are created and destroyed every second.
