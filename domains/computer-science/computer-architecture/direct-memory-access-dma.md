---
id: direct-memory-access-dma
title: Direct Memory Access (DMA) Controllers and Design
domain: computer-science
course: computer-architecture
prerequisites:
- id: interrupts-and-dma
  type: hard
- id: memory-bus-interconnect
  type: soft
builds-toward:
- io-subsystem-design
tags:
- dma
- io-transfer
- memory-access
stage: formal-systems
status: draft
---

# Direct Memory Access (DMA) Controllers and Design

## Core Idea
DMA controllers transfer data between I/O devices and memory without CPU intervention, freeing the CPU for other tasks. The CPU programs the DMA controller with source, destination, and transfer count; the controller then manages the memory bus. After completion, it raises an interrupt. DMA is essential for high-bandwidth I/O (disk, network) and real-time constraints.
