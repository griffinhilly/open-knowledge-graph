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
status: validated
---

# Interrupts and Direct Memory Access (DMA)

## Core Idea
An interrupt is a hardware signal that causes the CPU to suspend the current program, save its state, and execute an interrupt service routine (ISR) to handle a device event. Interrupts are far more efficient than polling (repeatedly checking device status), freeing the CPU for other work between I/O events. Direct Memory Access (DMA) allows a specialized controller to transfer large data blocks directly between a device and memory without per-byte CPU involvement, generating a single interrupt on completion. Together, interrupts and DMA form the foundation of efficient I/O in operating systems.

## How It's Best Learned
Trace the full interrupt handling cycle: device signals interrupt → CPU saves PC and registers → ISR executes → context restored. Compare polling, interrupt-driven, and DMA-based I/O for a disk read operation in terms of CPU utilization and latency.

## Common Misconceptions
- An interrupt is not the same as an exception; exceptions are synchronous (caused by the current instruction) while interrupts are asynchronous (caused by external devices).
- DMA does not bypass the memory bus; it uses the same physical bus as the CPU, so CPU and DMA transfers must be coordinated to avoid bus conflicts.

## Explainer

From your study of I/O systems, you know that the CPU must somehow communicate with external devices — disks, keyboards, network cards. The simplest approach is **polling**: the CPU repeatedly checks a device's status register in a tight loop, asking "are you ready yet?" This works, but it is enormously wasteful. Imagine standing at your front door checking every second whether a package has arrived, unable to do anything else. Interrupts solve this problem by inverting the relationship: the device notifies the CPU when it needs attention, freeing the processor to execute other instructions in the meantime.

When a device raises an **interrupt**, it sends an electrical signal to the CPU's interrupt pin. The CPU finishes its current instruction, saves the program counter and key registers onto a stack (so it can return later), and jumps to a pre-defined **interrupt service routine (ISR)** — a small handler written specifically for that device. The ISR does whatever the device needs (reads a byte from a keyboard buffer, acknowledges a completed disk transfer), then executes a "return from interrupt" instruction that restores the saved state and resumes the original program exactly where it left off. The entire process is transparent to the interrupted program. This is why your understanding of the control unit matters: it is the control unit that orchestrates the save-jump-restore sequence.

There is an important distinction between interrupts and exceptions. **Interrupts are asynchronous** — they arrive from external hardware at unpredictable times, unrelated to the instruction currently executing. **Exceptions are synchronous** — they are triggered by the instruction itself (a divide-by-zero, an invalid opcode, a page fault). Both use similar handler mechanisms, but their causes and timing are fundamentally different.

Even with interrupts, transferring large blocks of data byte-by-byte through the CPU is inefficient. Consider reading a 4 KB block from disk: with interrupt-driven I/O, the CPU would handle 4,096 separate interrupts, each copying one byte. **Direct Memory Access (DMA)** eliminates this bottleneck by offloading bulk transfers to a dedicated DMA controller. The CPU sets up the transfer by telling the DMA controller the source address, destination address, and byte count, then goes back to running programs. The DMA controller takes over the memory bus, moves the data directly between the device and RAM, and generates a single interrupt when the entire transfer is complete. The CPU's involvement drops from thousands of interrupts to one setup operation and one completion interrupt. The tradeoff is that the DMA controller and CPU must share the memory bus — a technique called **cycle stealing** — so there is some minor slowdown of CPU memory accesses during the transfer, but the net efficiency gain is dramatic.
