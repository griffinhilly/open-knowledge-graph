---
id: sram-vs-dram-design
title: 'SRAM vs DRAM: Design and Tradeoffs'
domain: computer-science
course: computer-architecture
prerequisites:
- id: memory-organization
  type: hard
builds-toward:
- memory-access-timing
tags:
- memory-types
- sram
- dram
stage: formal-systems
status: draft
---

# SRAM vs DRAM: Design and Tradeoffs

## Core Idea
SRAM uses flip-flops (fast, no refresh, high power); DRAM uses capacitors (dense, needs refresh, slower). SRAM is used for caches; DRAM for main memory. Cost, speed, density, and power determine the choice.

## Explainer

From your study of memory organization, you know that digital memory stores binary values and that the CPU accesses memory through addresses. But not all memory is built the same way. The two dominant technologies for building memory cells — **SRAM** (Static Random-Access Memory) and **DRAM** (Dynamic Random-Access Memory) — use fundamentally different circuit designs, and understanding their tradeoffs explains why modern computers use both rather than choosing one.

An **SRAM cell** stores a bit using a cross-coupled pair of inverters — essentially a tiny flip-flop made from six transistors. Once you write a 1 or 0 into this circuit, it holds that value indefinitely as long as power is supplied. There is no need to periodically "remind" the cell what it is storing. This makes SRAM fast (access times under a nanosecond) and simple to interface with, but expensive in silicon area — six transistors per bit adds up quickly. A **DRAM cell**, by contrast, stores a bit as a charge on a tiny capacitor, controlled by a single transistor. This is extraordinarily compact — one transistor and one capacitor per bit versus six transistors — which is why DRAM can pack billions of bits onto a single chip at low cost.

The capacitor in a DRAM cell is what creates both its advantage and its main limitation. Capacitors leak charge over time, so a stored 1 gradually drains toward 0. To prevent data loss, DRAM must be **refreshed** — every cell must be read and rewritten thousands of times per second (typically every 64 milliseconds). This refresh process consumes power, adds complexity to the memory controller, and briefly makes the memory unavailable during each refresh cycle. Reading a DRAM cell is also destructive: sensing the charge on the tiny capacitor drains it, so every read must be followed by a rewrite. These overheads make DRAM roughly 5–10x slower than SRAM for random access.

This is why modern computers use both technologies in complementary roles. **SRAM** fills the upper levels of the memory hierarchy — L1, L2, and L3 caches — where speed is paramount and the total capacity needed is small (kilobytes to megabytes). **DRAM** fills main memory, where capacity demands are large (gigabytes) and the slightly slower access time is acceptable because the caches absorb most of the CPU's requests. The cost difference is dramatic: SRAM costs roughly 10–100x more per bit than DRAM. A system with 16 GB of SRAM main memory would be prohibitively expensive, while a system with DRAM-based caches would be too slow. The memory hierarchy works precisely because these two technologies occupy different points on the speed-cost-density spectrum, and clever caching hides DRAM's latency behind SRAM's speed.
