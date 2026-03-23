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
status: validated
---

# Memory Access Timing and Performance

## Core Idea
Memory access time includes address decoding delay, data retrieval, and output stabilization. Cycle time (time between successive accesses) is larger. These delays dominate system performance and guide cache design.

## Questions

```yaml
- question: "A DRAM module has an access time of 50 ns. After reading, the bit lines must be precharged before another access can begin. The total cycle time is 100 ns. A program issues back-to-back read requests as fast as possible. What limits the effective memory bandwidth?"
  type: multiple-choice
  options:
    - "Access time, because that determines how long each read takes"
    - "Cycle time, because the precharge phase must complete before a new access starts"
    - "The processor speed, because the CPU cannot issue requests faster than 50 ns"
    - "The address bus width, because wider buses reduce decoding delay"
  answer: 1
  explanation: "Cycle time — not access time — is the limiting factor for sustained memory bandwidth. Even though valid data appears after 50 ns (access time), the memory cannot begin another access until the bit lines are recharged, adding another 50 ns. This precharge requirement means the memory can only accept one request every 100 ns. Access time tells you the latency of a single read; cycle time tells you the throughput ceiling for successive reads."

- question: "A processor executes one instruction per nanosecond. Each instruction requires one memory access. If main DRAM has an access time of 60 ns, approximately how many instructions does the processor complete per second assuming no caching?"
  type: multiple-choice
  options:
    - "1 billion — the processor speed determines throughput"
    - "About 16.7 million — memory latency limits throughput to roughly 1 access per 60 ns"
    - "About 500 million — memory and CPU share the bottleneck equally"
    - "It depends on the instruction mix, not memory speed"
  answer: 1
  explanation: "Without a cache, every instruction requires waiting for DRAM. At 60 ns per access, the processor can complete at most 1/60×10⁻⁹ ≈ 16.7 million instructions per second — far below its 1 billion/sec capability. This two-order-of-magnitude gap is the 'memory wall.' The processor's speed is irrelevant when it spends nearly all its time waiting. This is precisely why caches exist: to serve most requests from fast SRAM and make the slow DRAM access rate nearly invisible."

- question: "Access time and cycle time are the same quantity, just measured from different reference points in the memory access sequence."
  type: true-false
  answer: false
  explanation: "They are distinct quantities. Access time is the delay from issuing a read request to receiving valid data on the data bus. Cycle time is the minimum interval between the start of successive accesses — it equals access time plus the precharge delay needed to reset bit lines. Cycle time is always larger than access time. Conflating them leads to overestimating memory bandwidth: knowing access time alone tells you latency but not how quickly back-to-back accesses can proceed."

- question: "The fundamental reason caches improve performance is that they exploit locality — the tendency for programs to reuse recently accessed data — to serve most requests at nanosecond speeds instead of waiting tens of nanoseconds for DRAM."
  type: true-false
  answer: true
  explanation: "This is exactly right. Caches work because most memory accesses cluster around recently or nearby used locations (temporal and spatial locality). A small, fast SRAM cache captures these hot data items so the processor rarely needs to pay the full DRAM access time. Without locality, a cache would offer no benefit — every access would miss and fall through to slow DRAM. Understanding access time and cycle time explains why the cache hit/miss distinction matters so much: a hit costs nanoseconds, a miss costs tens of nanoseconds."

- question: "Explain why cycle time is larger than access time in DRAM, and describe what implication this has for memory bandwidth."
  type: short-answer
  answer: "Cycle time exceeds access time because after a read, the memory's bit lines must be precharged — restored to a neutral voltage — before another row can be selected and another access started. Access time only covers request-to-data-valid; cycle time covers the full period until the memory is ready for the next request. The implication is that memory bandwidth (accesses per second) is bounded by 1/cycle_time, not 1/access_time, and is therefore lower than the latency figure alone would suggest."
  explanation: "The precharge step is an inherent property of DRAM cell design: reading destroys the charge on a capacitor cell, which must be refreshed. This refresh happens at the row level, requiring all bit lines in a row to settle before the next access. The distinction matters for architects designing memory systems: you can partially hide access time with pipelining, but cycle time sets a hard throughput ceiling. Techniques like burst mode (reading multiple consecutive words in one cycle) and bank interleaving (multiple DRAM banks precharged in rotation) exist specifically to work around this constraint."
```

## Explainer

From your understanding of memory address decoding, you know that accessing a specific memory location requires translating an address into signals that select the right row and column within a memory chip. Memory access timing quantifies exactly how long each phase of this process takes and why the total delay matters so much for system performance. The fundamental insight is that memory is dramatically slower than the processor, and this gap — often called the **memory wall** — is the central performance bottleneck in modern computing.

**Access time** is the delay from when the processor issues a read request to when valid data appears on the data bus. This includes the time for address decoding, the time for the memory cells to drive their stored values onto internal bit lines, the time for sense amplifiers to detect and strengthen those tiny voltage differences, and finally the time for output buffers to stabilize. Each of these phases adds nanoseconds, and they happen in sequence. A typical DRAM access might take 50–100 nanoseconds, while a modern CPU can execute an instruction every fraction of a nanosecond — a gap of two orders of magnitude.

**Cycle time** is a separate and often larger number: the minimum time between the start of one access and the start of the next. Cycle time exceeds access time because after reading a row, the memory must **precharge** — restore the bit lines to their neutral voltage — before another access can begin. Think of it like a vending machine: the time to dispense your item (access time) is shorter than the time until the machine is ready for the next customer (cycle time), because internal mechanisms need to reset.

These timing parameters directly explain why caches exist and why memory hierarchies are designed the way they are. If every instruction fetch and data load had to wait 50+ nanoseconds for main memory, a 4 GHz processor would spend most of its time stalled. Caches exploit **locality** — the tendency of programs to reuse nearby data — to serve most requests in 1–4 nanoseconds from small, fast SRAM arrays. Understanding access time and cycle time is essential for reasoning about cache miss penalties, memory bandwidth, and why techniques like burst mode and interleaved memory banks were invented to mitigate the fundamental slowness of DRAM.
