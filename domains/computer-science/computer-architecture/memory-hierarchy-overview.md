---
id: memory-hierarchy-overview
title: Memory Hierarchy
domain: computer-science
course: computer-architecture
prerequisites:
- id: memory-organization
  type: hard
- id: registers-and-register-files
  type: soft
builds-toward:
- cache-memory-design
- virtual-memory-basics
tags:
- memory-hierarchy
- cache
- DRAM
- storage
- locality
stage: formal-systems
status: validated
---

# Memory Hierarchy

## Core Idea
The memory hierarchy organizes storage into levels with increasing capacity and decreasing speed moving away from the CPU: registers → L1/L2/L3 cache → main memory (DRAM) → secondary storage (SSD/HDD). The hierarchy exploits temporal locality (recently accessed data will likely be accessed again) and spatial locality (data near recently accessed data will likely be accessed soon). The goal is to provide the illusion of a large, fast, cheap memory by keeping frequently used data at the top of the hierarchy.

## How It's Best Learned
Look up actual latency and capacity numbers for each hierarchy level in a modern processor. Trace what happens when a CPU reads a value: which levels are checked in order and how data is brought up through the hierarchy on a miss. Relate to time-space-complexity trade-offs in algorithms.

## Common Misconceptions
- Cache memory is not explicitly addressed by programs; it is managed automatically by hardware.
- A cache miss does not mean data is lost — it is simply not in the cache and must be fetched from a lower level, which takes more time.

## Explainer

From your understanding of memory organization and registers, you know that the CPU needs data to execute instructions, and that registers provide the fastest possible storage — but only a handful of them exist. The fundamental problem the **memory hierarchy** solves is that we want memory that is simultaneously fast, large, and cheap, but no single technology delivers all three. Fast memory (like the SRAM used in registers) is expensive and physically large per bit. Cheap, dense memory (like DRAM) is orders of magnitude slower. The hierarchy is an engineering compromise that layers these technologies to approximate the ideal.

The levels of the hierarchy, from fastest to slowest, are: **registers** (sub-nanosecond access, tens of words), **L1 cache** (~1 nanosecond, tens of kilobytes), **L2 cache** (~5 nanoseconds, hundreds of kilobytes), **L3 cache** (~20 nanoseconds, megabytes), **main memory/DRAM** (~100 nanoseconds, gigabytes), and **secondary storage** (microseconds to milliseconds, terabytes). Each level is roughly 10–100x slower than the one above it, but also 10–1000x larger. The key insight is that programs do not access memory uniformly — they revisit the same data and nearby data repeatedly. This predictable behavior is what makes the hierarchy work.

The hierarchy exploits two patterns in how programs access data. **Temporal locality** means that data accessed recently is likely to be accessed again soon — think of a loop counter or a frequently called function. **Spatial locality** means that data near a recently accessed address is likely to be accessed next — think of iterating through an array element by element. When the CPU reads a value, the hardware automatically copies not just that value but an entire block of nearby data (a **cache line**) into the faster levels. If the program exhibits good locality, most accesses are served from cache, and the system performs as if all memory were as fast as SRAM.

When a requested value is found in a cache level, it is called a **hit**; when it is not found, it is a **miss**, and the hardware must fetch it from a slower level below. The performance of the entire system depends on the **hit rate** — the fraction of accesses served from each cache level. A well-designed hierarchy with programs that have good locality achieves hit rates above 95% at L1, meaning the CPU rarely waits for slow main memory. This is why the memory hierarchy is arguably the single most important architectural idea in modern computing: it makes the processor's raw speed usable by hiding the latency of the vast, cheap storage behind small, fast buffers that exploit the predictable patterns of real programs.
