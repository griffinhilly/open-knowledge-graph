---
id: memory-access-timing
title: Memory Access Timing and Performance
domain: computer-science
course: computer-architecture
prerequisites:
- id: memory-address-decoding
  type: hard
tags:
- memory
- timing
- performance
stage: formal-systems
status: draft
---

# Memory Access Timing and Performance

## Core Idea
Memory access time includes address decoding delay, data retrieval, and output stabilization. Cycle time (time between successive accesses) is larger. These delays dominate system performance and guide cache design.

## Explainer

From your understanding of memory address decoding, you know that accessing a specific memory location requires translating an address into signals that select the right row and column within a memory chip. Memory access timing quantifies exactly how long each phase of this process takes and why the total delay matters so much for system performance. The fundamental insight is that memory is dramatically slower than the processor, and this gap — often called the **memory wall** — is the central performance bottleneck in modern computing.

**Access time** is the delay from when the processor issues a read request to when valid data appears on the data bus. This includes the time for address decoding, the time for the memory cells to drive their stored values onto internal bit lines, the time for sense amplifiers to detect and strengthen those tiny voltage differences, and finally the time for output buffers to stabilize. Each of these phases adds nanoseconds, and they happen in sequence. A typical DRAM access might take 50–100 nanoseconds, while a modern CPU can execute an instruction every fraction of a nanosecond — a gap of two orders of magnitude.

**Cycle time** is a separate and often larger number: the minimum time between the start of one access and the start of the next. Cycle time exceeds access time because after reading a row, the memory must **precharge** — restore the bit lines to their neutral voltage — before another access can begin. Think of it like a vending machine: the time to dispense your item (access time) is shorter than the time until the machine is ready for the next customer (cycle time), because internal mechanisms need to reset.

These timing parameters directly explain why caches exist and why memory hierarchies are designed the way they are. If every instruction fetch and data load had to wait 50+ nanoseconds for main memory, a 4 GHz processor would spend most of its time stalled. Caches exploit **locality** — the tendency of programs to reuse nearby data — to serve most requests in 1–4 nanoseconds from small, fast SRAM arrays. Understanding access time and cycle time is essential for reasoning about cache miss penalties, memory bandwidth, and why techniques like burst mode and interleaved memory banks were invented to mitigate the fundamental slowness of DRAM.
