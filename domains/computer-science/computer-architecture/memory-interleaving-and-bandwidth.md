---
id: memory-interleaving-and-bandwidth
title: Memory Interleaving and Bandwidth Optimization
domain: computer-science
course: computer-architecture
prerequisites:
- id: memory-organization
  type: hard
- id: dynamic-ram-dram-design
  type: soft
- id: direct-memory-access-dma
  type: soft
builds-toward:
- memory-hierarchy-overview
tags:
- memory-interleaving
- bandwidth
- memory-access
stage: formal-systems
status: validated
---
# Memory Interleaving and Bandwidth Optimization

## Core Idea
Interleaving distributes consecutive addresses across multiple memory banks so that successive accesses can proceed in parallel. N-way interleaving achieves N× bandwidth improvement if successive addresses are accessed. Low-order address bits select the bank; higher bits select the address within that bank. Interleaving is essential for maintaining throughput in pipelined systems.

## Questions

```yaml
- question: "A program accesses memory addresses 0, 4, 8, 12, and 16 in sequence using a 4-way low-order interleaved system where the 2 low-order address bits select the bank. What happens to memory bandwidth?"
  type: multiple-choice
  options:
    - "The accesses are distributed evenly across all four banks, achieving 4× bandwidth"
    - "All accesses hit bank 0, creating bank conflicts and eliminating the parallelism"
    - "The memory controller automatically detects the stride and redistributes the accesses"
    - "Two banks are accessed in parallel, achieving 2× bandwidth"
  answer: 1
  explanation: "With 4-way low-order interleaving, bank = address mod 4. Addresses 0, 4, 8, 12, 16 all give remainder 0, so every access goes to bank 0. This stride-4 access pattern — exactly the width of the interleaving — creates a bank conflict on every access and collapses parallelism to single-bank throughput. Sequential access (0, 1, 2, 3, 4, ...) would distribute across all four banks and achieve the full 4× benefit."

- question: "Why does low-order interleaving improve bandwidth for sequential access but not for a stride-N access pattern (where N equals the number of banks)?"
  type: multiple-choice
  options:
    - "Low-order interleaving only works when the CPU cache is disabled"
    - "Sequential access hits a different bank each cycle; stride-N access hits the same bank every time, serializing requests"
    - "Stride-N accesses are too large for the memory address space"
    - "Low-order interleaving was designed only for instruction fetch, not data access"
  answer: 1
  explanation: "The bank assignment is address mod N. Sequential addresses (0, 1, 2, 3, ...) produce consecutive bank indices (0, 1, 2, 3, 0, 1, ...), spreading load and enabling parallelism. A stride-N pattern (0, N, 2N, 3N, ...) always maps to bank 0, leaving the other N−1 banks idle. The benefit of interleaving is entirely determined by whether the access pattern actually uses different banks — hardware cannot compensate for a pathological stride."

- question: "In low-order memory interleaving, consecutive memory addresses are placed in the same bank to improve locality of reference."
  type: true-false
  answer: false
  explanation: "This describes high-order interleaving, not low-order. In low-order interleaving, the least significant address bits select the bank, which means consecutive addresses map to consecutive banks (0, 1, 2, 3, 0, 1, ...). This is the property that enables parallel access for sequential patterns. High-order interleaving uses the most significant bits, placing large contiguous blocks in the same bank — useful for reducing inter-bank contention in multiprocessor systems, but providing no bandwidth improvement for sequential single-processor access."

- question: "N-way memory interleaving can achieve up to N times the memory bandwidth of a single-bank system when access patterns spread requests across all N banks."
  type: true-false
  answer: true
  explanation: "This is the design goal of interleaving. When N successive requests each go to a different bank, all N banks can be working simultaneously, pipelining their access cycles. The first bank finishes and delivers data while banks 2 through N are still working — so one result arrives every cycle instead of one result every full access cycle. The N× improvement is the ideal maximum, achieved only when every access hits a different bank."

- question: "Why does the benefit of N-way memory interleaving depend on the access pattern rather than just the number of banks?"
  type: short-answer
  answer: "Interleaving distributes consecutive addresses across banks so parallel accesses can overlap. If the access pattern spreads requests to different banks, all N banks work simultaneously. If the pattern repeatedly hits the same bank (a bank conflict), each access must wait for the previous one to complete — the parallelism collapses entirely. The hardware can only exploit the N banks if the software's memory access pattern actually uses them."
  explanation: "The key insight is that N-way interleaving is a potential, not a guarantee. The memory system provides the parallel infrastructure; whether it's utilized depends entirely on whether successive addresses happen to fall in different banks. This is why access patterns — sequential, random, strided — matter so much in memory system design, and why compiler and hardware architects think carefully about array layout and prefetching."
```

## Explainer

From your study of memory organization, you know that a single memory module has a fixed access time — typically many clock cycles. During that time, the module is busy and cannot serve another request. If a processor needs data from consecutive addresses (which it frequently does, since instructions and array elements are stored sequentially), it must wait for each access to complete before starting the next. This creates a bottleneck: the processor is idle while memory finishes its work. **Memory interleaving** solves this by spreading consecutive addresses across separate, independent memory banks that can operate simultaneously.

The key insight is how addresses are distributed. In **low-order interleaving**, the least significant bits of the address select which bank to use, and the remaining higher bits select the location within that bank. With four banks (2-bit selection), address 0 goes to bank 0, address 1 to bank 1, address 2 to bank 2, address 3 to bank 3, and address 4 wraps back to bank 0. This means that when a program reads addresses 0 through 3 in sequence, each request goes to a different bank. Bank 0 starts working on address 0, and one cycle later bank 1 begins address 1 — even though bank 0 is still busy. By the time the processor needs the data from address 0, bank 0 has had several cycles to complete its work.

Think of it like a four-lane toll plaza compared to a single toll booth. Each car (memory request) takes the same time to pass through, but because four cars can be processed in parallel, the overall throughput quadruples. With **N-way interleaving**, you get up to N times the bandwidth — but only when accesses hit different banks. If a program repeatedly accesses addresses that all map to the same bank (a **bank conflict**), the parallelism collapses and you are back to waiting sequentially. This is why access patterns matter: sequential access patterns benefit enormously, while strided access patterns can accidentally hit the same bank every time.

There is also **high-order interleaving**, where the most significant address bits select the bank. This places large contiguous blocks of addresses in the same bank rather than distributing them. High-order interleaving does not improve bandwidth for sequential access, but it allows different programs or threads to use different banks simultaneously, reducing contention in multiprocessor systems. Modern memory systems often combine both strategies, using low-order interleaving within a channel for bandwidth and high-order partitioning across channels for isolation. Understanding interleaving is essential for designing memory hierarchies that keep pipelined processors fed with data at the rate they need.
