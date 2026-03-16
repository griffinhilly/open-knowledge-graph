---
id: io-device-addressing-and-interfaces
title: I/O Device Addressing and Interface Design
domain: computer-science
course: computer-architecture
prerequisites:
- id: io-systems-overview
  type: hard
- id: memory-bus-interconnect
  type: soft
builds-toward:
- io-subsystem-design
tags:
- io-interfaces
- device-addressing
- memory-mapped-io
stage: formal-systems
status: draft
---

# I/O Device Addressing and Interface Design

## Core Idea
Devices are accessed via memory-mapped I/O (addresses in the same space as RAM) or port I/O (separate address space). Memory-mapped I/O is common: writes to device addresses trigger control actions, reads from device addresses return status. Timing and handshaking protocols (ready, acknowledge signals) coordinate CPU and device. Interrupt and polling modes handle completion notification.

## Explainer

From your study of I/O systems, you know that processors need to communicate with external devices — keyboards, disks, network cards, displays. The fundamental question is: how does the CPU actually talk to these devices? It turns out the answer builds directly on something you already understand: memory addressing. The two main approaches — **memory-mapped I/O** and **port-mapped I/O** — differ in whether devices share the same address space as RAM or get their own separate one.

In **memory-mapped I/O**, device registers are assigned addresses in the same space as regular memory. When the CPU executes a store instruction to address 0xFFFF0000, for example, that write doesn't go to RAM — it goes to a device controller, perhaps telling a display to update a pixel or a motor to start spinning. From the CPU's perspective, the instruction looks identical to a normal memory write. This is elegant because it means all the addressing modes and instructions that work with memory automatically work with devices too. No special instructions are needed. In **port-mapped I/O**, devices live in a separate address space accessed through dedicated instructions (like x86's `IN` and `OUT`). This keeps the device space cleanly separated from memory but requires the ISA to provide those special instructions.

The harder problem is timing. The CPU runs at gigahertz speeds while most devices operate orders of magnitude slower. A disk drive might take milliseconds to respond — millions of CPU cycles. **Handshaking protocols** solve this coordination problem using status and control signals. The device exposes a status register with a "ready" bit; the CPU checks this bit before sending data or reading results. Think of it like a traffic light at an intersection — neither side proceeds until the signal confirms it is safe.

This leads to two strategies for checking device readiness. **Polling** means the CPU repeatedly reads the device's status register in a loop, asking "are you done yet?" over and over. It is simple but wasteful — the CPU burns cycles doing nothing productive while waiting. **Interrupts** flip the model: the device sends a signal to the CPU when it is ready, and the CPU handles the device only at that moment. This is like the difference between repeatedly checking your mailbox versus having a doorbell that rings when a package arrives. Interrupts free the CPU to do useful work between device interactions, which is why modern systems overwhelmingly prefer interrupt-driven I/O for most devices, reserving polling only for ultra-low-latency situations where interrupt overhead would be too costly.
