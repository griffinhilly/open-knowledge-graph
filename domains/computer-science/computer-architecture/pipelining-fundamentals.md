---
id: pipelining-fundamentals
title: CPU Pipelining
domain: computer-science
course: computer-architecture
prerequisites:
- id: cpu-datapath
  type: hard
- id: instruction-set-architecture
  type: hard
builds-toward:
- pipeline-hazards
tags:
- pipelining
- throughput
- latency
- RISC
- stages
stage: formal-systems
status: draft
---

# CPU Pipelining

## Core Idea
Pipelining overlaps the execution of multiple instructions by dividing the CPU datapath into stages — typically Fetch, Decode, Execute, Memory, and Write-back — and processing a different instruction in each stage simultaneously. While the latency of a single instruction stays the same or increases slightly, throughput approaches one instruction completed per clock cycle (ideal CPI = 1). Pipelining is the primary reason RISC designs with uniform instruction formats are efficient; the fixed-length instruction encoding allows stage work to be balanced and pipelined cleanly.

## How It's Best Learned
Draw a pipeline timing diagram for a 5-stage pipeline executing 8 instructions. Count total cycles and compute CPI. Compare to a non-pipelined processor executing the same sequence. Identify how stage boundaries in the datapath require pipeline registers to hold intermediate values.

## Common Misconceptions
- Pipelining does not speed up individual instructions; it speeds up the throughput of many instructions executing in parallel.
- A deeper pipeline does not always mean more performance; each stage boundary adds pipeline register latency and increases exposure to hazard penalties.
