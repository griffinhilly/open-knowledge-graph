---
id: performance-and-benchmarking
title: CPU Performance Metrics and Amdahl's Law
domain: computer-science
course: computer-architecture
prerequisites:
- id: pipelining-fundamentals
  type: soft
- id: time-space-complexity
  type: soft
tags:
- performance
- CPI
- MIPS
- Amdahls-law
- benchmarking
stage: formal-systems
status: draft
---

# CPU Performance Metrics and Amdahl's Law

## Core Idea
CPU performance is quantified by the equation: CPU time = Instruction count × CPI × Clock cycle time. Improving any one factor improves performance, but trade-offs exist — reducing CPI with more pipeline stages may require a faster clock with shorter cycle time. Amdahl's Law states that the speedup from improving a fraction f of execution is bounded by 1/(1−f), meaning serial portions of code form a hard ceiling on total speedup. Benchmarks like SPEC measure real-world application performance rather than synthetic peak numbers, providing honest cross-architecture comparisons.

## How It's Best Learned
Compute execution time using the CPU time equation under different clock speeds and CPI assumptions. Apply Amdahl's Law to predict speedup from parallelizing 80% of a workload. Compare SPEC scores across processor generations to observe the effect of architectural improvements.

## Common Misconceptions
- A higher clock frequency does not always mean better performance; if CPI increases proportionally, execution time does not improve.
- Amdahl's Law applies to any optimization, not just parallelism — the unoptimized fraction always limits the maximum achievable speedup.
