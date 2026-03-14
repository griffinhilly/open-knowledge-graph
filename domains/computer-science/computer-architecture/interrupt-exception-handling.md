---
id: interrupt-exception-handling
title: Interrupt and Exception Handling
domain: computer-science
course: computer-architecture
prerequisites:
- id: interrupts-and-dma
  type: hard
- id: instruction-fetch-decode-execute
  type: soft
builds-toward:
- io-architecture-system-integration
- power-thermal-performance-metrics
tags:
- interrupts
- exceptions
- handling
- synchronization
stage: formal-systems
status: draft
---

# Interrupt and Exception Handling

## Core Idea
Interrupts signal asynchronous events (I/O, timer); exceptions signal synchronous faults (divide-by-zero, page fault). Both cause context switches, saving processor state and jumping to handler code. Priority and masking manage multiple simultaneous events.
