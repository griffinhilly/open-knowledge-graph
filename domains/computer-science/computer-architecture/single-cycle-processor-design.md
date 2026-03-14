---
id: single-cycle-processor-design
title: Single-Cycle Processor Architecture
domain: computer-science
course: computer-architecture
prerequisites:
- id: cpu-datapath
  type: hard
- id: instruction-fetch-decode-execute
  type: hard
- id: finite-state-machine-processor-design
  type: soft
builds-toward:
- multi-cycle-processor-design
- instruction-level-parallelism
tags:
- processor-design
- single-cycle
- architecture
stage: formal-systems
status: draft
---

# Single-Cycle Processor Architecture

## Core Idea
A single-cycle processor completes one instruction per clock cycle: fetch, decode, execute, memory access, and writeback all happen in a single clock period. The clock period must accommodate the longest critical path through all stages. This design is simple and has no pipeline hazards, but the slow clock limits performance.
