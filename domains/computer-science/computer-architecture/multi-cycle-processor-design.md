---
id: multi-cycle-processor-design
title: Multi-Cycle Processor Design and Execution States
domain: computer-science
course: computer-architecture
prerequisites:
- id: single-cycle-processor-design
  type: hard
- id: finite-state-machine-processor-design
  type: soft
builds-toward:
- instruction-pipelining-design
tags:
- processor-design
- multi-cycle
- state-control
stage: formal-systems
status: draft
---

# Multi-Cycle Processor Design and Execution States

## Core Idea
A multi-cycle processor breaks instruction execution into multiple states (fetch, decode, execute, memory, writeback), with each state occupying one clock cycle. Different instruction types require different numbers of cycles. This allows a faster clock but requires explicit state management and introduces latency between instructions.
