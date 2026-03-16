---
id: io-architecture-system-integration
title: I/O Architecture and System Integration
domain: computer-science
course: computer-architecture
prerequisites:
- id: io-systems-overview
  type: hard
- id: interrupt-exception-handling
  type: soft
builds-toward:
- power-thermal-performance-metrics
tags:
- io
- architecture
- system
- integration
stage: formal-systems
status: draft
---

# I/O Architecture and System Integration

## Core Idea
I/O architecture bridges CPU, memory, and external devices via buses and controllers. DMA transfers data without CPU intervention; memory-mapped I/O treats devices as memory addresses; programmed I/O uses load/store instructions.

## Explainer

From your study of I/O systems, you know that a processor needs ways to communicate with the outside world — disks, network interfaces, keyboards, displays. I/O architecture is the engineering discipline of designing the pathways and protocols that connect these diverse devices to the CPU and memory in a coherent, efficient system. The central challenge is that the CPU operates at nanosecond speeds while most I/O devices operate at microsecond or millisecond speeds, creating a mismatch that must be managed without wasting processor time.

The simplest approach is **programmed I/O**, where the CPU explicitly executes load and store instructions to read from or write to device registers. This is straightforward but wasteful: the CPU sits in a polling loop, checking whether a device is ready, burning cycles that could be spent on computation. The interrupt-driven approach you encountered in your prerequisites improves this by letting the device signal the CPU when it needs attention, freeing the processor to do useful work in the meantime. But even with interrupts, the CPU still handles every byte of data transfer — fine for a keyboard, but catastrophic for a disk transferring megabytes.

**Direct Memory Access (DMA)** solves the bulk-transfer problem by giving a dedicated DMA controller the ability to move data directly between device and memory without CPU involvement. The CPU sets up the transfer — specifying source, destination, and byte count — then the DMA controller takes over, using the memory bus to shuttle data while the CPU continues executing instructions. The CPU is only interrupted once, when the entire transfer completes. This is why modern systems can stream video, write to disk, and run applications simultaneously without grinding to a halt.

**Memory-mapped I/O** unifies device access with memory access by assigning device registers to specific memory addresses. When the CPU writes to address 0xFFFF0000, it is not writing to RAM — it is sending a command to a device controller mapped to that address. The alternative, **port-mapped I/O**, uses separate instruction opcodes (like x86's IN and OUT) and a distinct address space. Memory-mapped I/O is elegant because it lets the CPU use its existing load/store instructions and addressing modes to interact with devices, and it allows devices to be accessed through the same virtual memory and protection mechanisms that govern regular memory. Most modern architectures, including ARM, use memory-mapped I/O exclusively.

Tying these mechanisms together is the **bus architecture** — the shared communication channels that connect CPU, memory, and I/O controllers. A modern system typically uses a hierarchy of buses: a fast processor bus connecting CPU and cache, a memory bus to DRAM, and one or more I/O buses (like PCIe) for peripherals. Bus arbitration determines which device gets to use the bus at any moment, and bridge chips translate between buses of different speeds and protocols. The art of I/O architecture is balancing bandwidth, latency, and CPU involvement across this hierarchy so that no single bottleneck starves the rest of the system.
