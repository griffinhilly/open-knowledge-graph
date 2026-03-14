---
id: static-ram-sram-design
title: Static RAM (SRAM) Cell Design and Arrays
domain: computer-science
course: computer-architecture
prerequisites:
- id: flip-flops-and-latches
  type: hard
- id: memory-array-organization
  type: soft
builds-toward:
- register-file-design
- cache-memory-design
tags:
- sram
- memory-cell
- memory-design
stage: formal-systems
status: draft
---

# Static RAM (SRAM) Cell Design and Arrays

## Core Idea
An SRAM cell is a cross-coupled NOR or NAND latch that stores one bit and requires continuous power. Unlike DRAM, SRAM is fast (single-cycle access) but power-hungry and area-inefficient. SRAM arrays use row and column decoders for addressing. Register files and caches are typically built from SRAM; main memory uses DRAM.
