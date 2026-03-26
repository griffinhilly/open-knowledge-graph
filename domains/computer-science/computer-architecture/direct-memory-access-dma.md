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
- io-systems-overview
tags:
- dma
- io-transfer
- memory-access
stage: formal-systems
status: validated
---

# Direct Memory Access (DMA) Controllers and Design

## Core Idea
DMA controllers transfer data between I/O devices and memory without CPU intervention, freeing the CPU for other tasks. The CPU programs the DMA controller with source, destination, and transfer count; the controller then manages the memory bus. After completion, it raises an interrupt. DMA is essential for high-bandwidth I/O (disk, network) and real-time constraints.

## Questions

```yaml
- question: "Using DMA, a disk controller transfers 4 KB of data to memory. How many times is the CPU directly involved in the individual word-by-word data transfer?"
  type: multiple-choice
  options:
    - "Zero — the DMA controller handles all word transfers autonomously; the CPU is only involved in initial setup and the final completion interrupt"
    - "Once per byte, since memory write operations always require a CPU instruction"
    - "Once per 4-byte word, for each load-store operation"
    - "Twice — once at the start of each disk sector and once when the buffer fills"
  answer: 0
  explanation: "This is the defining feature of DMA. After the CPU programs the DMA controller (source address, destination address, byte count, direction), the DMA controller independently manages every individual word transfer — reading from the device, writing to memory, incrementing the address register, and decrementing the count — without any CPU instruction per word. The CPU is interrupted exactly once, when the count reaches zero and the transfer is complete. This is why DMA is so much more efficient than interrupt-driven I/O for large transfers."

- question: "In cycle-stealing DMA mode, what happens to the CPU during the data transfer?"
  type: multiple-choice
  options:
    - "The CPU is briefly stalled for one bus cycle per word transferred but can otherwise continue executing between steals"
    - "The CPU is completely halted for the entire duration of the transfer"
    - "The CPU runs at half clock speed to share bus bandwidth with the DMA controller"
    - "The CPU is completely unaffected — cycle stealing uses a dedicated DMA bus that does not contend with the CPU"
  answer: 0
  explanation: "In cycle stealing, the DMA controller 'borrows' individual bus cycles from the CPU — one stall per word transferred. Between steals, the CPU resumes execution normally. This contrasts with burst mode, where the DMA controller takes exclusive bus control for the entire transfer (CPU halted throughout), and transparent mode, where the DMA controller only uses the bus during cycles the CPU is not accessing memory (no stall at all, but slower). Cycle stealing is a middle ground: some CPU stall, but execution continues between transfers."

- question: "After programming a DMA controller to perform a transfer, the CPU can execute other instructions while the transfer is in progress."
  type: true-false
  answer: true
  explanation: "True — this is the primary performance benefit of DMA. Once the CPU writes the source address, destination address, byte count, and direction to the DMA controller's registers, it is free to execute other code. The DMA controller independently manages the bus cycles required to complete the transfer. The CPU is not involved again until it receives the completion interrupt. This overlap of I/O and computation is what enables high-bandwidth I/O without sacrificing CPU throughput."

- question: "DMA eliminates the need for interrupts largely, since the data transfer occurs without CPU involvement."
  type: true-false
  answer: false
  explanation: "False. DMA does not eliminate interrupts — it dramatically reduces their number. Without DMA (interrupt-driven I/O), the device raises one interrupt per word transferred, potentially thousands for a large block. With DMA, the DMA controller raises exactly one interrupt at the end of the entire transfer to notify the CPU of completion. The completion interrupt is essential: without it, the CPU would not know when the data is ready and would have to poll the DMA controller's status register, which is inefficient. DMA replaces thousands of fine-grained interrupts with one coarse-grained one."

- question: "Explain why DMA dramatically improves I/O throughput compared to interrupt-driven I/O for large data transfers."
  type: short-answer
  answer: "In interrupt-driven I/O without DMA, the device raises one interrupt per word transferred. Each interrupt requires saving CPU registers, executing an interrupt handler that performs the load-store, and restoring state — tens to hundreds of CPU cycles per word. For a 4 KB block, this means thousands of interrupts and nearly all CPU time spent on data movement, leaving little for useful computation. DMA replaces this with one programmed setup (writing to DMA registers) and one completion interrupt at the end. The DMA controller handles all address incrementing and memory writes autonomously, and the CPU runs application code throughout the entire transfer."
  explanation: "The key insight is that the bottleneck in interrupt-driven I/O is not the memory bandwidth — it is the per-word CPU overhead. DMA offloads this overhead to dedicated hardware. Modern systems exploit this further with scatter-gather DMA, which can transfer data to or from non-contiguous memory regions in a single programmed operation, and with multiple independent DMA channels managing different I/O streams simultaneously."
```

## Explainer

From your study of interrupts, you know that I/O devices can signal the CPU when they need attention, freeing the CPU from constantly polling device status. But interrupts alone do not solve the data transfer problem. Consider reading a 4 KB block from disk: without DMA, the CPU would handle an interrupt for every word transferred — potentially thousands of interrupts, each requiring the CPU to execute a load-store sequence. The CPU spends nearly all its time shuttling data between the device and memory, unable to do any useful computation. **Direct Memory Access (DMA)** solves this by offloading the entire bulk transfer to a dedicated hardware controller.

The protocol works in three phases. First, the CPU **programs the DMA controller** by writing to its registers: the memory address where data should go (or come from), the device address or port, the number of bytes to transfer, and the direction (device-to-memory or memory-to-device). Second, the DMA controller **takes over the memory bus** and performs the transfer autonomously — reading from the device and writing to memory (or vice versa) one word at a time, incrementing the address and decrementing the count after each transfer. The CPU is not involved in any of these individual word transfers. Third, when the count reaches zero, the DMA controller **raises an interrupt** to notify the CPU that the transfer is complete. The CPU handles this single interrupt, checks for errors, and moves on.

The mechanism by which the DMA controller accesses the bus varies. In **cycle stealing**, the DMA controller "borrows" individual bus cycles from the CPU — the CPU is briefly stalled for one cycle per word transferred but otherwise continues executing. In **burst mode**, the DMA controller takes exclusive control of the bus for the entire transfer, which is faster for large blocks but stalls the CPU completely until the transfer finishes. In **transparent mode** (where supported), the DMA controller only uses the bus during cycles when the CPU is not accessing memory, achieving zero CPU stall at the cost of slower transfers. The choice depends on the latency sensitivity of the I/O device and the CPU's tolerance for bus contention.

DMA is what makes high-bandwidth I/O practical. A disk controller, network interface card, or GPU can transfer megabytes of data while the CPU runs application code — the CPU's only involvement is the initial setup and the final completion interrupt. Modern systems often have multiple DMA channels, each independently managing a different transfer, and the DMA controller may support scatter-gather operations that transfer data to or from non-contiguous memory regions in a single programmed operation. Understanding DMA is essential for grasping why modern systems achieve I/O throughput far beyond what programmed I/O or interrupt-driven I/O could deliver.
