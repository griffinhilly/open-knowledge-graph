---
id: io-systems-overview
title: I/O Systems and Buses
domain: computer-science
course: computer-architecture
prerequisites:
- id: cpu-datapath
  type: soft
- id: memory-organization
  type: soft
builds-toward:
- interrupts-and-dma
tags:
- IO
- bus
- device-controller
- memory-mapped-io
- port-mapped-io
stage: formal-systems
status: validated
---

# I/O Systems and Buses

## Core Idea
I/O systems connect the CPU and memory to peripheral devices through buses — shared electrical connections carrying address, data, and control signals. Memory-mapped I/O places device control registers in the address space so the CPU can interact with devices using standard load/store instructions. Port-mapped I/O uses special IN/OUT instructions with a separate I/O address space. Device controllers buffer data between slow peripherals and the fast system bus. Bus bandwidth and device count are key design constraints in modern systems.

## How It's Best Learned
Trace how the CPU writes to a display controller using memory-mapped I/O. Examine bus transaction sequences (address phase, data phase) in a simple bus protocol. Compare the bandwidth of common buses such as PCIe, USB, and SATA and relate them to device requirements.

## Common Misconceptions
- Memory-mapped I/O does not consume physical RAM; device registers occupy reserved address ranges that do not correspond to actual DRAM chips.
- A bus is not just a collection of wires; it includes a protocol for arbitration, timing, and error detection that all connected devices must follow.

## Explainer

From your study of the CPU datapath and memory organization, you know that the processor executes instructions by moving data between registers, the ALU, and memory. But a real computer does more than compute — it reads keyboards, writes to displays, communicates over networks, and stores files on disks. The **I/O system** is the machinery that connects the CPU and memory to all of these peripheral devices, and the **bus** is the shared communication pathway that makes those connections possible.

A bus carries three kinds of signals: **address** signals (which device or memory location to talk to), **data** signals (the actual information being transferred), and **control** signals (read/write commands, clock timing, and arbitration). When the CPU wants to send data to a device, it places an address on the address lines, puts the data on the data lines, and asserts the appropriate control signal. The device controller — a small piece of hardware built into each peripheral — watches the bus for its assigned address and responds accordingly. Think of a bus like a shared hallway in an office building: everyone uses the same corridor, but each office has a unique room number and only responds when someone knocks on their specific door.

There are two fundamental approaches to how the CPU addresses devices. In **memory-mapped I/O**, device registers are assigned addresses within the same address space as regular memory. The CPU uses ordinary load and store instructions to read from and write to devices — no special instructions needed. This is elegant because all the existing memory instructions and addressing modes work with devices automatically. In **port-mapped I/O**, devices live in a separate address space accessed through dedicated IN and OUT instructions. x86 processors support both approaches; most modern architectures favor memory-mapped I/O for its simplicity and uniformity.

A critical design tension in I/O systems is the speed mismatch between peripherals and the CPU. A modern processor can execute billions of operations per second, while a mechanical hard drive might deliver data thousands of times more slowly. **Device controllers** bridge this gap by buffering data — accumulating bytes from a slow peripheral until a meaningful chunk is ready, then transferring it to memory in a burst. Without this buffering, the CPU would waste enormous amounts of time waiting for slow devices one byte at a time. This speed mismatch also motivates more sophisticated I/O techniques like interrupts and DMA, which you will encounter next as natural extensions of the bus-based I/O model introduced here.
