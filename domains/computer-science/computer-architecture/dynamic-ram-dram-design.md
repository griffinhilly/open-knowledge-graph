---
id: dynamic-ram-dram-design
title: Dynamic RAM (DRAM) Organization and Refresh Cycles
domain: computer-science
course: computer-architecture
prerequisites:
- id: memory-array-organization
  type: hard
- id: memory-bus-interconnect
  type: soft
builds-toward:
- memory-hierarchy-design
tags:
- dram
- memory-design
- refresh
- timing
stage: formal-systems
status: draft
---

# Dynamic RAM (DRAM) Organization and Refresh Cycles

## Core Idea
A DRAM cell stores charge on a capacitor; a transistor gate controls access. DRAM is dense and cheap but must be refreshed (rewritten) periodically before charge leaks. Access is slower than SRAM and requires address multiplexing (row and column addresses on the same pins). Main memory uses DRAM; refresh cycles reduce available bandwidth.
