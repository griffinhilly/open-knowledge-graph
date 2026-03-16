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
builds-toward:
- memory-hierarchy-design
tags:
- memory-interleaving
- bandwidth
- memory-access
stage: formal-systems
status: draft
---

# Memory Interleaving and Bandwidth Optimization

## Core Idea
Interleaving distributes consecutive addresses across multiple memory banks so that successive accesses can proceed in parallel. N-way interleaving achieves N× bandwidth improvement if successive addresses are accessed. Low-order address bits select the bank; higher bits select the address within that bank. Interleaving is essential for maintaining throughput in pipelined systems.

## Explainer

From your study of memory organization, you know that a single memory module has a fixed access time — typically many clock cycles. During that time, the module is busy and cannot serve another request. If a processor needs data from consecutive addresses (which it frequently does, since instructions and array elements are stored sequentially), it must wait for each access to complete before starting the next. This creates a bottleneck: the processor is idle while memory finishes its work. **Memory interleaving** solves this by spreading consecutive addresses across separate, independent memory banks that can operate simultaneously.

The key insight is how addresses are distributed. In **low-order interleaving**, the least significant bits of the address select which bank to use, and the remaining higher bits select the location within that bank. With four banks (2-bit selection), address 0 goes to bank 0, address 1 to bank 1, address 2 to bank 2, address 3 to bank 3, and address 4 wraps back to bank 0. This means that when a program reads addresses 0 through 3 in sequence, each request goes to a different bank. Bank 0 starts working on address 0, and one cycle later bank 1 begins address 1 — even though bank 0 is still busy. By the time the processor needs the data from address 0, bank 0 has had several cycles to complete its work.

Think of it like a four-lane toll plaza compared to a single toll booth. Each car (memory request) takes the same time to pass through, but because four cars can be processed in parallel, the overall throughput quadruples. With **N-way interleaving**, you get up to N times the bandwidth — but only when accesses hit different banks. If a program repeatedly accesses addresses that all map to the same bank (a **bank conflict**), the parallelism collapses and you are back to waiting sequentially. This is why access patterns matter: sequential access patterns benefit enormously, while strided access patterns can accidentally hit the same bank every time.

There is also **high-order interleaving**, where the most significant address bits select the bank. This places large contiguous blocks of addresses in the same bank rather than distributing them. High-order interleaving does not improve bandwidth for sequential access, but it allows different programs or threads to use different banks simultaneously, reducing contention in multiprocessor systems. Modern memory systems often combine both strategies, using low-order interleaving within a channel for bandwidth and high-order partitioning across channels for isolation. Understanding interleaving is essential for designing memory hierarchies that keep pipelined processors fed with data at the rate they need.
