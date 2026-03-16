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

## Explainer

From your study of memory array organization, you know that memory is structured as a grid of rows and columns, with each intersection holding one bit. A **DRAM cell** is the simplest possible storage element: just one transistor and one tiny capacitor. The capacitor holds a charge (representing 1) or no charge (representing 0), and the transistor acts as a switch connecting the capacitor to a shared wire called the **bit line**. Compare this to an SRAM cell, which uses six transistors to hold its state in a feedback loop. DRAM's one-transistor design is why it achieves far higher density and lower cost per bit — and why virtually all main memory in computers is DRAM.

The fundamental tradeoff is that a capacitor leaks charge. Left alone, a DRAM cell will lose its stored value within milliseconds as the charge dissipates through the transistor and surrounding silicon. This means every cell must be periodically **refreshed** — read out and written back — before its charge drops below the threshold where the sense amplifier can distinguish 0 from 1. Modern DRAM refreshes every row in the array within a 64-millisecond window, typically using **distributed refresh** that spreads refresh operations across time rather than stalling the entire array at once. Each refresh cycle occupies the memory bus, stealing bandwidth from actual read and write requests. This refresh overhead is a constant tax on DRAM performance.

Accessing a DRAM cell is a multi-step process. First, the **row address** is sent and the corresponding row is activated — all cells in that row dump their charge onto the bit lines, where sense amplifiers detect and latch the values. This destructive read (the capacitors lose their charge) is why every access implicitly refreshes the row. Then the **column address** selects which bits from the activated row to output. The two-step addressing allows DRAM to share address pins between row and column signals (multiplexing), cutting the pin count in half compared to sending the full address at once. This pin reduction was a critical design decision that kept DRAM packages small and cheap, at the cost of requiring two address cycles per access.

Modern DRAM standards like DDR (Double Data Rate) build on this foundation with techniques to improve effective bandwidth: transferring data on both rising and falling clock edges, widening the internal bus, and allowing multiple banks to operate concurrently so one bank can be accessed while another refreshes. Understanding the basic cell structure and refresh requirement explains why DRAM latency is fundamentally higher than SRAM — and why the memory hierarchy you will study next uses small, fast SRAM caches in front of large, slow DRAM main memory to bridge the performance gap.
