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
status: validated
---

# I/O Device Addressing and Interface Design

## Core Idea
Devices are accessed via memory-mapped I/O (addresses in the same space as RAM) or port I/O (separate address space). Memory-mapped I/O is common: writes to device addresses trigger control actions, reads from device addresses return status. Timing and handshaking protocols (ready, acknowledge signals) coordinate CPU and device. Interrupt and polling modes handle completion notification.

## Questions

```yaml
- question: "A system uses memory-mapped I/O. A programmer writes a store instruction to address 0xFFFF0000 to send data to a display controller. What is the key advantage of this approach over port-mapped I/O?"
  type: multiple-choice
  options:
    - "Memory-mapped I/O is faster because device registers are physically closer to RAM"
    - "Memory-mapped I/O allows all existing memory addressing modes and instructions to work with device registers without needing special I/O instructions"
    - "Memory-mapped I/O provides better security because device addresses are hidden from user programs"
    - "Memory-mapped I/O requires less hardware because the device address space is smaller than RAM"
  answer: 1
  explanation: "The key advantage of memory-mapped I/O is that devices appear to the CPU as ordinary memory locations. Every addressing mode, every load/store instruction, and every data manipulation instruction that works with RAM automatically works with device registers too — no special 'IN' or 'OUT' instructions are needed. This simplifies the ISA and allows compilers and programmers to interact with devices using familiar memory operations. Port-mapped I/O (as in x86) requires separate dedicated instructions and a separate address space."

- question: "An embedded system needs to read temperature data from a slow sensor that takes 50 milliseconds to produce a reading. The CPU core runs at 1 GHz. Which I/O approach is most appropriate, and why?"
  type: multiple-choice
  options:
    - "Polling, because it is simpler to implement and 50 ms is fast enough that the CPU won't waste much time"
    - "Interrupt-driven I/O, because 50 ms represents ~50 million wasted CPU cycles if polling; the CPU can do useful work and handle the sensor only when it signals completion"
    - "Direct memory access (DMA), because slow sensors always require DMA to avoid bottlenecks"
    - "Port-mapped I/O, because polling over memory-mapped addresses is too slow for 50 ms devices"
  answer: 1
  explanation: "At 1 GHz, 50 milliseconds = 50 million CPU cycles. Polling during this entire wait means burning 50 million cycles doing nothing productive — checking the status register over and over. With interrupt-driven I/O, the CPU initiates the sensor read, then continues executing other instructions. When the sensor is ready (50 ms later), it sends an interrupt signal; the CPU pauses briefly to handle the data and then resumes. This is the doorbell vs. repeatedly-checking-the-mailbox distinction. Polling is only preferable when interrupt overhead itself is too costly relative to the wait time (e.g., ultra-low-latency microsecond-scale devices)."

- question: "In memory-mapped I/O, writing to a device register address can trigger a hardware control action such as starting a motor or updating a display."
  type: true-false
  answer: true
  explanation: "This is the defining behavior of memory-mapped I/O. The CPU issues a store instruction to a specific address; the memory bus routes that write not to RAM but to the device controller at that address. The controller interprets the written value as a command or data and takes the corresponding action — setting a display pixel, adjusting motor speed, etc. From the CPU's perspective, it is just a memory write; the device controller handles the interpretation."

- question: "Polling is generally preferred over interrupt-driven I/O in modern systems because it requires less hardware support and is easier to implement."
  type: true-false
  answer: false
  explanation: "While polling is simpler to implement, modern systems overwhelmingly prefer interrupt-driven I/O for most devices. Polling wastes CPU cycles in a busy-wait loop — the processor cannot do useful work while checking device status repeatedly. Interrupts allow the CPU to execute other tasks and handle the device only when it signals readiness, dramatically improving throughput and responsiveness. Polling is reserved for specific situations where interrupt latency and overhead are unacceptable, such as ultra-high-speed network interfaces or real-time control loops where deterministic response time matters more than CPU efficiency."

- question: "Explain the tradeoff between polling and interrupt-driven I/O, and describe a situation where each approach is preferable."
  type: short-answer
  answer: "Polling: the CPU repeatedly reads the device status register in a loop until the device is ready. It is simple (no interrupt hardware needed) and deterministic (response happens immediately on the next poll cycle). But it wastes CPU cycles doing nothing productive during the wait. Best for: ultra-low-latency devices where even interrupt handling overhead is too slow, or very fast devices where the wait is typically under a few cycles. Interrupt-driven I/O: the CPU initiates a device operation, continues executing other code, and receives an interrupt signal when the device is done. The CPU handles the device only when notified, freeing it for useful work in between. Best for: slow or unpredictable devices (disks, keyboards, network cards) where wait times span millions of CPU cycles."
  explanation: "The core insight is that polling inverts the natural relationship: the fast component (CPU) waits on the slow component (device). Interrupts restore the correct relationship: the slow component notifies the fast component when it is needed. The overhead of interrupt handling (saving/restoring state, looking up the interrupt vector) makes interrupts wasteful only when the device is so fast that it would be ready again before the interrupt handling overhead completes — a situation rare outside of specialized high-performance computing."
```

## Explainer

From your study of I/O systems, you know that processors need to communicate with external devices — keyboards, disks, network cards, displays. The fundamental question is: how does the CPU actually talk to these devices? It turns out the answer builds directly on something you already understand: memory addressing. The two main approaches — **memory-mapped I/O** and **port-mapped I/O** — differ in whether devices share the same address space as RAM or get their own separate one.

In **memory-mapped I/O**, device registers are assigned addresses in the same space as regular memory. When the CPU executes a store instruction to address 0xFFFF0000, for example, that write doesn't go to RAM — it goes to a device controller, perhaps telling a display to update a pixel or a motor to start spinning. From the CPU's perspective, the instruction looks identical to a normal memory write. This is elegant because it means all the addressing modes and instructions that work with memory automatically work with devices too. No special instructions are needed. In **port-mapped I/O**, devices live in a separate address space accessed through dedicated instructions (like x86's `IN` and `OUT`). This keeps the device space cleanly separated from memory but requires the ISA to provide those special instructions.

The harder problem is timing. The CPU runs at gigahertz speeds while most devices operate orders of magnitude slower. A disk drive might take milliseconds to respond — millions of CPU cycles. **Handshaking protocols** solve this coordination problem using status and control signals. The device exposes a status register with a "ready" bit; the CPU checks this bit before sending data or reading results. Think of it like a traffic light at an intersection — neither side proceeds until the signal confirms it is safe.

This leads to two strategies for checking device readiness. **Polling** means the CPU repeatedly reads the device's status register in a loop, asking "are you done yet?" over and over. It is simple but wasteful — the CPU burns cycles doing nothing productive while waiting. **Interrupts** flip the model: the device sends a signal to the CPU when it is ready, and the CPU handles the device only at that moment. This is like the difference between repeatedly checking your mailbox versus having a doorbell that rings when a package arrives. Interrupts free the CPU to do useful work between device interactions, which is why modern systems overwhelmingly prefer interrupt-driven I/O for most devices, reserving polling only for ultra-low-latency situations where interrupt overhead would be too costly.
