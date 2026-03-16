---
id: cache-line-and-offset
title: Cache Line Organization and Byte Offset
domain: computer-science
course: computer-architecture
prerequisites:
- id: cache-memory-design
  type: hard
- id: memory-hierarchy-overview
  type: hard
tags:
- cache
- memory-organization
stage: formal-systems
status: draft
---

# Cache Line Organization and Byte Offset

## Core Idea
Cache lines (typically 32–128 bytes) are the unit of cache allocation. Addresses split into tag (identifies line), index (line location within set), and offset (byte within line), exploiting spatial locality.

## Explainer

From your study of cache memory design and the memory hierarchy, you know that caches exploit locality to bridge the speed gap between the CPU and main memory. The fundamental design decision is that caches do not store individual bytes — they store **cache lines**, contiguous blocks of memory typically 64 bytes in size. When the CPU requests a single byte, the cache fetches the entire 64-byte block containing that byte. This design exploits **spatial locality**: if you access address 1000, you will likely soon access addresses 1001, 1002, and so on. By bringing in the whole line, subsequent nearby accesses are cache hits at no extra cost.

The hardware needs a fast way to determine whether a requested address is currently in the cache and, if so, where. It does this by splitting every memory address into three fields. The **offset** (lowest bits) identifies which byte within the cache line is being accessed. For a 64-byte line, the offset is 6 bits (2⁶ = 64), selecting one of 64 byte positions. The **index** (middle bits) selects which cache set the line maps to — think of it as a row number in the cache table. The **tag** (remaining upper bits) distinguishes between different memory blocks that map to the same set. When the CPU issues a memory request, the hardware extracts the index to locate the correct set, then compares the tag against stored tags in that set. A match means a cache hit; the offset then selects the specific byte from the cached line.

Consider a concrete example with a 16 KB direct-mapped cache using 64-byte lines. The cache has 16,384 / 64 = 256 lines, so the index is 8 bits (2⁸ = 256). The offset is 6 bits. For a 32-bit address, the tag is the remaining 32 − 8 − 6 = 18 bits. Address `0x0000_1A3C` in binary gives offset `11 1100` (byte 60 within the line), index `0110 1000` (set 104), and tag from the upper 18 bits. The hardware goes directly to set 104, checks if the stored tag matches, and either returns the byte at position 60 (hit) or fetches the 64-byte block from memory (miss).

Understanding this decomposition explains many performance phenomena programmers encounter. **Cache thrashing** happens when two arrays map to the same index but have different tags, causing repeated evictions. **False sharing** in multithreaded programs occurs when two threads modify different variables that happen to share a cache line — each write invalidates the other core's copy of the entire line, even though they are accessing different bytes. **Alignment** matters because a data structure spanning two cache lines requires two lookups instead of one. When you understand that every memory access decomposes into tag-index-offset, you can reason precisely about cache behavior and write code that cooperates with the hardware rather than fighting it.
