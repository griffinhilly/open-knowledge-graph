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

## Explainer

From your study of interrupts, you know that I/O devices can signal the CPU when they need attention, freeing the CPU from constantly polling device status. But interrupts alone do not solve the data transfer problem. Consider reading a 4 KB block from disk: without DMA, the CPU would handle an interrupt for every word transferred — potentially thousands of interrupts, each requiring the CPU to execute a load-store sequence. The CPU spends nearly all its time shuttling data between the device and memory, unable to do any useful computation. **Direct Memory Access (DMA)** solves this by offloading the entire bulk transfer to a dedicated hardware controller.

The protocol works in three phases. First, the CPU **programs the DMA controller** by writing to its registers: the memory address where data should go (or come from), the device address or port, the number of bytes to transfer, and the direction (device-to-memory or memory-to-device). Second, the DMA controller **takes over the memory bus** and performs the transfer autonomously — reading from the device and writing to memory (or vice versa) one word at a time, incrementing the address and decrementing the count after each transfer. The CPU is not involved in any of these individual word transfers. Third, when the count reaches zero, the DMA controller **raises an interrupt** to notify the CPU that the transfer is complete. The CPU handles this single interrupt, checks for errors, and moves on.

The mechanism by which the DMA controller accesses the bus varies. In **cycle stealing**, the DMA controller "borrows" individual bus cycles from the CPU — the CPU is briefly stalled for one cycle per word transferred but otherwise continues executing. In **burst mode**, the DMA controller takes exclusive control of the bus for the entire transfer, which is faster for large blocks but stalls the CPU completely until the transfer finishes. In **transparent mode** (where supported), the DMA controller only uses the bus during cycles when the CPU is not accessing memory, achieving zero CPU stall at the cost of slower transfers. The choice depends on the latency sensitivity of the I/O device and the CPU's tolerance for bus contention.

DMA is what makes high-bandwidth I/O practical. A disk controller, network interface card, or GPU can transfer megabytes of data while the CPU runs application code — the CPU's only involvement is the initial setup and the final completion interrupt. Modern systems often have multiple DMA channels, each independently managing a different transfer, and the DMA controller may support scatter-gather operations that transfer data to or from non-contiguous memory regions in a single programmed operation. Understanding DMA is essential for grasping why modern systems achieve I/O throughput far beyond what programmed I/O or interrupt-driven I/O could deliver.
