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
- id: memory-bus-interconnect
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

## Questions

```yaml
- question: "A programmer uses a standard store instruction to write to address 0xFFFE0010 and successfully configures a graphics card register. Which I/O model does this describe?"
  type: multiple-choice
  options:
    - "Port-mapped I/O — the OUT instruction is implicitly called by the compiler"
    - "Memory-mapped I/O — device registers occupy reserved addresses in the main address space"
    - "Direct Memory Access — the CPU is bypassed and the device writes directly to RAM"
    - "Interrupt-driven I/O — the device signals the CPU when it is ready"
  answer: 1
  explanation: "Memory-mapped I/O is the key: device control registers are assigned addresses within the same address space as regular memory, so ordinary load/store instructions interact with devices — no special instructions needed. Port-mapped I/O requires dedicated IN/OUT instructions and a separate I/O address space. DMA and interrupt-driven I/O are different mechanisms for handling data transfer and timing, not the fundamental addressing model being described here."

- question: "A slow hard drive transfers data at 100 MB/s while the system bus operates at 8 GB/s. Which component primarily bridges this speed mismatch?"
  type: multiple-choice
  options:
    - "The CPU cache, which stores recently accessed disk data for fast retrieval"
    - "The device controller, which buffers data from the peripheral before transferring it in bursts to the bus"
    - "The OS scheduler, which pauses the CPU while waiting for disk data"
    - "Port-mapped I/O, which provides a dedicated channel for slow devices"
  answer: 1
  explanation: "The device controller bridges the speed mismatch by accumulating data from the slow peripheral and then transferring it to the system bus in bursts when a meaningful chunk is ready. This prevents the CPU from waiting one byte at a time for a device 80x slower than the bus. CPU caches handle processor-memory latency, not peripheral-bus mismatches. OS schedulers manage CPU time but don't solve the underlying hardware speed gap. Port-mapped I/O is an addressing scheme, not a buffering solution."

- question: "In memory-mapped I/O, device registers occupy the same address space as physical RAM, which reduces the total memory available to programs."
  type: true-false
  answer: false
  explanation: "Memory-mapped I/O assigns addresses in the CPU's address space to device registers, but those addresses do not correspond to physical DRAM chips — they're reserved ranges that hardware routes to device controllers. Programs cannot use those addresses for normal memory, but the physical RAM is not reduced. The CPU's address space is a logical construct; memory-mapped I/O occupies parts of that logical space without consuming physical memory."

- question: "A bus can be understood as simply a collection of wires connecting the CPU to peripheral devices."
  type: true-false
  answer: false
  explanation: "A bus is a shared communication pathway that includes a protocol — rules for arbitration (deciding which device can use the bus when multiple want to simultaneously), timing (synchronizing data transfer), and error detection. Without arbitration, two devices transmitting simultaneously would corrupt each other's signals. The wires are the physical medium; the bus protocol is what makes communication reliable and orderly. This distinction matters when comparing buses: PCIe, USB, and SATA differ not just in wire count but in their protocols, bandwidth, and arbitration mechanisms."

- question: "Explain why device controllers are necessary in an I/O system, even when the CPU could theoretically poll devices directly."
  type: short-answer
  answer: "Device controllers buffer data between slow peripherals and the fast system bus, preventing the CPU from being forced to wait for each byte one at a time. They translate between the bus protocol and device-specific interfaces, handle error detection, and accumulate data until a useful chunk is ready for transfer. Without them, the CPU would waste enormous time busy-waiting for devices thousands of times slower than itself, or every peripheral would need to match CPU speeds — both impractical."
  explanation: "The speed mismatch is the fundamental driver. A keyboard generates data at human typing speeds (~10 characters/second); the CPU operates at billions of cycles per second. A controller buffers keystrokes so the CPU can handle them in bursts when interrupted, rather than polling constantly. This buffering model also motivates DMA (Direct Memory Access) for high-bandwidth devices: by removing the CPU from the data path entirely, DMA frees the processor for computation while the controller manages large transfers autonomously."
```

## Explainer

From your study of the CPU datapath and memory organization, you know that the processor executes instructions by moving data between registers, the ALU, and memory. But a real computer does more than compute — it reads keyboards, writes to displays, communicates over networks, and stores files on disks. The **I/O system** is the machinery that connects the CPU and memory to all of these peripheral devices, and the **bus** is the shared communication pathway that makes those connections possible.

A bus carries three kinds of signals: **address** signals (which device or memory location to talk to), **data** signals (the actual information being transferred), and **control** signals (read/write commands, clock timing, and arbitration). When the CPU wants to send data to a device, it places an address on the address lines, puts the data on the data lines, and asserts the appropriate control signal. The device controller — a small piece of hardware built into each peripheral — watches the bus for its assigned address and responds accordingly. Think of a bus like a shared hallway in an office building: everyone uses the same corridor, but each office has a unique room number and only responds when someone knocks on their specific door.

There are two fundamental approaches to how the CPU addresses devices. In **memory-mapped I/O**, device registers are assigned addresses within the same address space as regular memory. The CPU uses ordinary load and store instructions to read from and write to devices — no special instructions needed. This is elegant because all the existing memory instructions and addressing modes work with devices automatically. In **port-mapped I/O**, devices live in a separate address space accessed through dedicated IN and OUT instructions. x86 processors support both approaches; most modern architectures favor memory-mapped I/O for its simplicity and uniformity.

A critical design tension in I/O systems is the speed mismatch between peripherals and the CPU. A modern processor can execute billions of operations per second, while a mechanical hard drive might deliver data thousands of times more slowly. **Device controllers** bridge this gap by buffering data — accumulating bytes from a slow peripheral until a meaningful chunk is ready, then transferring it to memory in a burst. Without this buffering, the CPU would waste enormous amounts of time waiting for slow devices one byte at a time. This speed mismatch also motivates more sophisticated I/O techniques like interrupts and DMA, which you will encounter next as natural extensions of the bus-based I/O model introduced here.
