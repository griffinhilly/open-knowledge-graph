---
id: registers-and-register-files
title: Registers and Register Files
domain: computer-science
course: computer-architecture
prerequisites:
- id: d-flip-flop-design
  type: hard
- id: sequential-circuit-design
  type: soft
builds-toward:
- cpu-datapath
- memory-array-organization
tags:
- registers
- storage
- register-file
- datapath
stage: formal-systems
status: draft
---

# Registers and Register Files

## Core Idea
Registers are arrays of flip-flops that store multi-bit values (often 32 or 64 bits), while register files are collections of named registers with multiplexed read and write ports. They provide fast, on-chip storage for operands and intermediate results.

## How It's Best Learned
Design a 4-register by 8-bit register file with dual read ports and single write port; trace address decoding and data paths.

## Common Misconceptions
Registers cannot hold different values per bit unless explicitly stored separately. Register file write typically takes one clock cycle and read is combinational.
