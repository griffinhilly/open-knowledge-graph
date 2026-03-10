---
id: interrupts-and-dma
title: Interrupts and Direct Memory Access (DMA)
domain: computer-science
course: computer-architecture
prerequisites:
- id: io-systems-overview
  type: hard
- id: cpu-control-unit
  type: soft
tags:
- interrupts
- DMA
- interrupt-handler
- polling
- IO
stage: formal-systems
status: draft
---

# Interrupts and Direct Memory Access (DMA)

## Core Idea
An interrupt is a hardware signal that causes the CPU to suspend the current program, save its state, and execute an interrupt service routine (ISR) to handle a device event. Interrupts are far more efficient than polling (repeatedly checking device status), freeing the CPU for other work between I/O events. Direct Memory Access (DMA) allows a specialized controller to transfer large data blocks directly between a device and memory without per-byte CPU involvement, generating a single interrupt on completion. Together, interrupts and DMA form the foundation of efficient I/O in operating systems.

## How It's Best Learned
Trace the full interrupt handling cycle: device signals interrupt → CPU saves PC and registers → ISR executes → context restored. Compare polling, interrupt-driven, and DMA-based I/O for a disk read operation in terms of CPU utilization and latency.

## Common Misconceptions
- An interrupt is not the same as an exception; exceptions are synchronous (caused by the current instruction) while interrupts are asynchronous (caused by external devices).
- DMA does not bypass the memory bus; it uses the same physical bus as the CPU, so CPU and DMA transfers must be coordinated to avoid bus conflicts.
