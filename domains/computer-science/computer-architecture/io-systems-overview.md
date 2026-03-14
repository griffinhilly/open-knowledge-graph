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
