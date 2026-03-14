---
id: d-flip-flop-design
title: D (Data) Flip-Flop and Edge Triggering
domain: computer-science
course: computer-architecture
prerequisites:
- id: sr-flip-flop-design
  type: hard
builds-toward:
- registers-and-register-files
- counters-design-analysis
tags:
- flip-flops
- d-latch
- edge-triggered
- sequential
stage: formal-systems
status: draft
---

# D (Data) Flip-Flop and Edge Triggering

## Core Idea
D flip-flops capture a single data bit at the rising (or falling) edge of a clock signal, isolating input changes from affecting output until the next clock pulse. This edge-triggered behavior is essential for synchronous digital design.

## How It's Best Learned
Compare D latch (level-triggered) with edge-triggered D flip-flop; observe timing diagrams showing setup and hold time requirements.

## Common Misconceptions
D flip-flops respond to input changes only at the clock edge, not continuously. Setup and hold time violations cause metastable states.
