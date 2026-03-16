---
id: memory-bus-interconnect
title: Memory Bus Architecture and Interconnect
domain: computer-science
course: computer-architecture
prerequisites:
- id: cpu-datapath
  type: hard
- id: memory-address-decoding
  type: soft
builds-toward:
- io-architecture-system-integration
- cache-design-principles
tags:
- bus
- memory
- interconnect
- protocol
stage: formal-systems
status: draft
---

# Memory Bus Architecture and Interconnect

## Core Idea
Memory buses connect CPU, cache, memory, and I/O; they must coordinate address, data, and control signals with proper timing. Bus arbitration resolves conflicts; protocols (like AXI) standardize handshaking and flow control.

## Explainer

You already know from studying the CPU datapath that the processor has internal pathways carrying data between the ALU, registers, and control unit. The **memory bus** extends this idea beyond the processor chip, providing a shared communication highway that connects the CPU to main memory, cache, and I/O devices. Just as a city's road system connects neighborhoods, the bus connects the major subsystems of a computer. But a shared road creates a problem that dedicated internal pathways don't have: contention.

A bus carries three types of signals simultaneously. **Address lines** specify which memory location or device the CPU wants to access. **Data lines** carry the actual values being read or written. **Control lines** coordinate the transaction — they indicate whether the operation is a read or write, signal when data is valid, and manage timing. The width of these lines matters enormously: a 32-bit data bus can transfer 4 bytes per cycle, while a 64-bit bus doubles that throughput. This is why bus width is one of the fundamental parameters of system design, directly affecting how fast data can flow between components.

The central challenge of bus design is **arbitration** — deciding who gets to use the shared bus when multiple components want to communicate at the same time. If the CPU wants to read from memory while a DMA controller wants to write, someone has to go first. Arbitration schemes range from simple priority-based approaches (where the CPU always wins) to round-robin schemes that give each device a fair turn. Without arbitration, two devices could drive conflicting voltages on the same wires simultaneously, corrupting data and potentially damaging hardware.

Modern systems address bus bottlenecks through standardized **bus protocols** like ARM's AXI (Advanced eXtensible Interface), which define precise handshaking rules for each transaction. These protocols specify how a master device initiates a transfer, how the target acknowledges readiness, and how data validity is signaled — ensuring reliable communication even at high clock speeds where timing margins are razor-thin. Many modern architectures have moved beyond a single shared bus to point-to-point interconnects and crossbar switches, which allow multiple simultaneous transfers. But the fundamental concepts — address/data/control separation, arbitration, and protocol-based handshaking — remain the building blocks for understanding any interconnect architecture.
