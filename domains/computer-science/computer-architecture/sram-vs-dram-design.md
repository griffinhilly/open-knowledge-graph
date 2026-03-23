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
status: validated
---

# SRAM vs DRAM: Design and Tradeoffs

## Core Idea
SRAM uses flip-flops (fast, no refresh, high power); DRAM uses capacitors (dense, needs refresh, slower). SRAM is used for caches; DRAM for main memory. Cost, speed, density, and power determine the choice.

## Questions

```yaml
- question: "A computer designer needs to maximize main memory capacity (gigabytes) at the lowest cost. Which technology is appropriate, and why?"
  type: multiple-choice
  options:
    - "SRAM, because it does not require refresh logic and is simpler to interface with"
    - "DRAM, because its one-transistor-one-capacitor design gives far higher density at much lower cost per bit"
    - "SRAM, because it is faster and the CPU will spend less time waiting for memory"
    - "DRAM, because it uses write-back caching to hide its latency"
  answer: 1
  explanation: "DRAM's one-transistor-one-capacitor cell is roughly 6x more compact than SRAM's six-transistor flip-flop, yielding dramatically higher density and lower cost per bit — the reason DRAM fills main memory. SRAM's speed advantage is real, but for gigabytes of main memory the cost would be prohibitive. Speed is addressed by placing fast SRAM caches in front of slow DRAM, not by replacing DRAM."

- question: "Reading from a DRAM cell is described as a 'destructive' operation. What does this mean?"
  type: multiple-choice
  options:
    - "The read voltage is high enough to permanently damage the capacitor after repeated accesses"
    - "Sensing the capacitor's charge drains it, so the stored value is destroyed and must be rewritten after every read"
    - "DRAM cells share transistors across rows, so reading one cell overwrites its neighbor"
    - "The refresh cycle that must follow every read corrupts adjacent cells"
  answer: 1
  explanation: "DRAM stores a bit as charge on a tiny capacitor. Sensing that charge — necessary to determine if it is a 1 or 0 — drains the capacitor. The value is therefore destroyed in the act of reading it, requiring an immediate rewrite to restore the data. This destructive read, combined with the periodic refresh needed to compensate for capacitor leakage, contributes to DRAM's slower effective access time compared to SRAM."

- question: "SRAM is faster than DRAM primarily because SRAM cells use a cross-coupled flip-flop that holds its value without periodic refresh, while DRAM cells use a leaky capacitor that must be refreshed thousands of times per second."
  type: true-false
  answer: true
  explanation: "This is accurate. An SRAM flip-flop is a stable bistable circuit — once set, it holds its state indefinitely without any external intervention. DRAM capacitors leak charge and must be refreshed (read and rewritten) every ~64 milliseconds to prevent data loss. The refresh overhead consumes bandwidth and adds latency, contributing to DRAM's 5–10x slower random-access time versus SRAM."

- question: "DRAM cells use more transistors than SRAM cells, which is why DRAM is slower — more transistors means more complexity and longer access times."
  type: true-false
  answer: false
  explanation: "This is backwards. DRAM cells use *fewer* transistors — just one transistor and one capacitor per bit. SRAM cells use six transistors. DRAM's slowness comes from the leaky capacitor requiring refresh and destructive reads requiring rewrites, not from transistor count. SRAM's higher transistor count per cell is precisely what makes it expensive and less dense — more silicon area per bit — while also making it fast and stable."

- question: "Why does modern computer architecture use both SRAM and DRAM rather than choosing one technology for all memory?"
  type: short-answer
  answer: "SRAM and DRAM occupy complementary positions on the speed-cost-density spectrum. SRAM is fast (sub-nanosecond access), stable (no refresh), but expensive and bulky — practical only for small capacities. DRAM is slow (nanoseconds to tens of nanoseconds), requires refresh, but is cheap and dense — practical for gigabytes. The memory hierarchy exploits both: SRAM caches absorb most CPU requests at high speed while DRAM provides affordable bulk storage behind them."
  explanation: "A computer with only SRAM main memory would be prohibitively expensive; only DRAM caches would be too slow to hide memory latency. The hierarchical design — L1/L2/L3 SRAM caches in front of DRAM main memory — delivers most of the performance of SRAM at most of the cost of DRAM, because caches exploit temporal and spatial locality to ensure the CPU usually finds what it needs in fast memory."
```

## Explainer

From your study of memory organization, you know that digital memory stores binary values and that the CPU accesses memory through addresses. But not all memory is built the same way. The two dominant technologies for building memory cells — **SRAM** (Static Random-Access Memory) and **DRAM** (Dynamic Random-Access Memory) — use fundamentally different circuit designs, and understanding their tradeoffs explains why modern computers use both rather than choosing one.

An **SRAM cell** stores a bit using a cross-coupled pair of inverters — essentially a tiny flip-flop made from six transistors. Once you write a 1 or 0 into this circuit, it holds that value indefinitely as long as power is supplied. There is no need to periodically "remind" the cell what it is storing. This makes SRAM fast (access times under a nanosecond) and simple to interface with, but expensive in silicon area — six transistors per bit adds up quickly. A **DRAM cell**, by contrast, stores a bit as a charge on a tiny capacitor, controlled by a single transistor. This is extraordinarily compact — one transistor and one capacitor per bit versus six transistors — which is why DRAM can pack billions of bits onto a single chip at low cost.

The capacitor in a DRAM cell is what creates both its advantage and its main limitation. Capacitors leak charge over time, so a stored 1 gradually drains toward 0. To prevent data loss, DRAM must be **refreshed** — every cell must be read and rewritten thousands of times per second (typically every 64 milliseconds). This refresh process consumes power, adds complexity to the memory controller, and briefly makes the memory unavailable during each refresh cycle. Reading a DRAM cell is also destructive: sensing the charge on the tiny capacitor drains it, so every read must be followed by a rewrite. These overheads make DRAM roughly 5–10x slower than SRAM for random access.

This is why modern computers use both technologies in complementary roles. **SRAM** fills the upper levels of the memory hierarchy — L1, L2, and L3 caches — where speed is paramount and the total capacity needed is small (kilobytes to megabytes). **DRAM** fills main memory, where capacity demands are large (gigabytes) and the slightly slower access time is acceptable because the caches absorb most of the CPU's requests. The cost difference is dramatic: SRAM costs roughly 10–100x more per bit than DRAM. A system with 16 GB of SRAM main memory would be prohibitively expensive, while a system with DRAM-based caches would be too slow. The memory hierarchy works precisely because these two technologies occupy different points on the speed-cost-density spectrum, and clever caching hides DRAM's latency behind SRAM's speed.
