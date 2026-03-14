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
