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
status: validated
---

# Cache Line Organization and Byte Offset

## Core Idea
Cache lines (typically 32–128 bytes) are the unit of cache allocation. Addresses split into tag (identifies line), index (line location within set), and offset (byte within line), exploiting spatial locality.

## Questions

```yaml
- question: "Two threads on different CPU cores write frequently to different variables stored 4 bytes apart in memory, within the same 64-byte cache line. Performance is mysteriously poor despite no shared data. What is the most likely cause?"
  type: multiple-choice
  options:
    - "A data race — the threads are inadvertently accessing the same variable."
    - "False sharing — each core's write invalidates the entire cache line on the other core, even though they write to different bytes."
    - "Cache thrashing — the two variables map to the same cache set, causing repeated tag evictions."
    - "Alignment error — the variables straddle word boundaries, causing split-register operations."
  answer: 1
  explanation: "False sharing occurs when threads write to different bytes that share a cache line. Cache coherence protocols operate at the granularity of entire cache lines: when Core A writes to its variable, the whole 64-byte line is marked as modified by Core A, and Core B's copy is invalidated. When Core B writes to its variable (same line), it must first fetch the updated line from Core A, then invalidate Core A's copy. This line bouncing between cores creates enormous overhead with no actual sharing of data — purely an artifact of co-location within a line. The fix is to pad variables to separate cache lines."

- question: "For a 32-bit address with a 16 KB direct-mapped cache using 64-byte lines, how many bits are used for the offset, index, and tag respectively?"
  type: multiple-choice
  options:
    - "Offset: 8, Index: 6, Tag: 18"
    - "Offset: 6, Index: 8, Tag: 18"
    - "Offset: 6, Index: 14, Tag: 12"
    - "Offset: 4, Index: 10, Tag: 18"
  answer: 1
  explanation: "64-byte lines require log₂(64) = 6 offset bits to address every byte within a line. 16 KB / 64 bytes = 256 lines, requiring log₂(256) = 8 index bits. The remaining 32 − 6 − 8 = 18 bits form the tag. This bit decomposition is the mechanism by which the hardware locates a cached address in O(1): the index selects the cache set directly (no search), and the tag disambiguates among the many memory locations that map to that set. The offset then selects the specific byte from the matched line."

- question: "When a cache line is loaded on a miss, subsequent accesses to any other byte within that same line will be cache hits, requiring no additional memory fetches."
  type: true-false
  answer: true
  explanation: "This is spatial locality exploitation in action. When a cache line is loaded, all bytes in that line are stored in the cache together. Any access to any byte within the line finds it already present — a hit — as long as the line has not been evicted. Sequential iteration through an array is cache-friendly for exactly this reason: after the first element of each 64-byte block is accessed (potentially a miss), all subsequent elements in the same block are hits. The cache line is the atomic unit of allocation, so all bytes within it rise and fall together."

- question: "Storing a variable in a smaller data type (e.g., char instead of double) guarantees it occupies fewer cache lines and will always improve cache performance."
  type: true-false
  answer: false
  explanation: "A smaller variable does not necessarily span fewer cache lines — alignment determines this, not size alone. A 1-byte variable placed at a cache-line boundary crossing spans two lines just as a larger misaligned variable would. Additionally, packing many small variables into shared cache lines can cause false sharing in multithreaded code, worsening performance. Smaller size reduces space used within a line, but without proper alignment and layout awareness, it provides no guarantee of better cache behavior."

- question: "Explain why caches fetch an entire cache line rather than just the single byte requested, and what assumption about memory access patterns this design exploits."
  type: short-answer
  answer: "Caches fetch entire lines (typically 64 bytes) because of spatial locality: programs that access address A are very likely to soon access nearby addresses A+1, A+2, etc. Bringing in the whole line on a miss means subsequent nearby accesses are already in the cache, converting future misses into hits at no additional cost. The underlying assumption is that programs access memory in clusters — walking arrays, reading struct fields, executing sequential instructions — rather than jumping randomly across the address space."
  explanation: "The alternative — fetching a single byte — would waste the bandwidth opportunity that cache lines exploit. DRAM transfers have high latency per request but high throughput once a transfer starts. Fetching 64 bytes costs only marginally more than fetching 1 byte (latency dominates, not transfer time), so the cache amortizes the fixed latency cost over 64 bytes rather than 1. Spatial locality ensures most of those 64 bytes will be needed soon, making the larger fetch worthwhile. When spatial locality fails (random access in sparse data structures), lines go partly wasted — a key motivation for designing cache-friendly data layouts."
```

## Explainer

From your study of cache memory design and the memory hierarchy, you know that caches exploit locality to bridge the speed gap between the CPU and main memory. The fundamental design decision is that caches do not store individual bytes — they store **cache lines**, contiguous blocks of memory typically 64 bytes in size. When the CPU requests a single byte, the cache fetches the entire 64-byte block containing that byte. This design exploits **spatial locality**: if you access address 1000, you will likely soon access addresses 1001, 1002, and so on. By bringing in the whole line, subsequent nearby accesses are cache hits at no extra cost.

The hardware needs a fast way to determine whether a requested address is currently in the cache and, if so, where. It does this by splitting every memory address into three fields. The **offset** (lowest bits) identifies which byte within the cache line is being accessed. For a 64-byte line, the offset is 6 bits (2⁶ = 64), selecting one of 64 byte positions. The **index** (middle bits) selects which cache set the line maps to — think of it as a row number in the cache table. The **tag** (remaining upper bits) distinguishes between different memory blocks that map to the same set. When the CPU issues a memory request, the hardware extracts the index to locate the correct set, then compares the tag against stored tags in that set. A match means a cache hit; the offset then selects the specific byte from the cached line.

Consider a concrete example with a 16 KB direct-mapped cache using 64-byte lines. The cache has 16,384 / 64 = 256 lines, so the index is 8 bits (2⁸ = 256). The offset is 6 bits. For a 32-bit address, the tag is the remaining 32 − 8 − 6 = 18 bits. Address `0x0000_1A3C` in binary gives offset `11 1100` (byte 60 within the line), index `0110 1000` (set 104), and tag from the upper 18 bits. The hardware goes directly to set 104, checks if the stored tag matches, and either returns the byte at position 60 (hit) or fetches the 64-byte block from memory (miss).

Understanding this decomposition explains many performance phenomena programmers encounter. **Cache thrashing** happens when two arrays map to the same index but have different tags, causing repeated evictions. **False sharing** in multithreaded programs occurs when two threads modify different variables that happen to share a cache line — each write invalidates the other core's copy of the entire line, even though they are accessing different bytes. **Alignment** matters because a data structure spanning two cache lines requires two lookups instead of one. When you understand that every memory access decomposes into tag-index-offset, you can reason precisely about cache behavior and write code that cooperates with the hardware rather than fighting it.
