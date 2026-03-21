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

## Questions

```yaml
- question: "A keyboard generates one keystroke every 50 milliseconds. With polling, the CPU checks the keyboard status register every 1 millisecond. What is the primary advantage of switching to interrupt-driven I/O?"
  type: multiple-choice
  options:
    - "The keyboard can process keystrokes faster because it no longer waits for the CPU to check"
    - "The CPU is freed to execute other instructions between keystrokes instead of spinning in a polling loop"
    - "Interrupts eliminate the need to save and restore CPU state when handling device events"
    - "The CPU can handle multiple devices simultaneously without any performance overhead"
  answer: 1
  explanation: "With polling, the CPU wastes the vast majority of its cycles checking a status register that almost always says 'not ready.' Interrupt-driven I/O inverts the relationship: the device signals the CPU only when it has something to report, freeing the processor to do useful work in between. Option C is wrong — saving and restoring state is a cost of interrupts, not an elimination. The key insight is that polling wastes CPU time proportional to how often you check; interrupts spend CPU time proportional to how often events actually occur."

- question: "A disk controller needs to transfer 16 KB of data from disk to RAM. Comparing interrupt-driven I/O (one interrupt per byte) versus DMA, what is the primary advantage of DMA?"
  type: multiple-choice
  options:
    - "DMA bypasses the memory bus entirely, so CPU memory accesses are completely unaffected during the transfer"
    - "DMA eliminates the need for the CPU to set up the transfer — the disk controller handles everything autonomously"
    - "DMA reduces the number of CPU interrupts from thousands (one per byte) to a single completion interrupt"
    - "DMA transfers data faster than interrupt-driven I/O because the DMA controller uses a dedicated high-speed bus"
  answer: 2
  explanation: "The core advantage of DMA is drastically reducing CPU involvement. For a 16 KB transfer, interrupt-driven I/O would generate 16,384 separate interrupts — each requiring the CPU to save state, run the ISR, and restore state. DMA offloads the entire bulk transfer to a dedicated controller, which performs the move autonomously and generates exactly one interrupt when done. Option A is false — DMA uses the same memory bus as the CPU (cycle stealing), so CPU accesses are slightly slowed. Option B is false — the CPU must still set up the DMA transfer parameters."

- question: "An interrupt is triggered by the instruction currently executing in the CPU, while an exception is triggered by an external hardware device."
  type: true-false
  answer: false
  explanation: "This has the definitions exactly reversed. An interrupt is asynchronous — it is triggered by an external hardware device (keyboard, disk, network card) at an unpredictable moment, unrelated to the current instruction. An exception is synchronous — it is triggered by the instruction itself (divide-by-zero, invalid memory access, page fault). Both use similar handler mechanisms, but their causes are fundamentally different: interrupts come from outside, exceptions come from inside."

- question: "After an interrupt service routine completes, the interrupted program resumes execution exactly where it was paused, with all register state restored."
  type: true-false
  answer: true
  explanation: "True. This transparent resumption is essential to how interrupts work correctly. When an interrupt arrives, the CPU finishes the current instruction, saves the program counter and registers to a stack, executes the ISR, then executes a 'return from interrupt' instruction that restores the saved state. The interrupted program has no way of knowing an interrupt occurred — it resumes from the exact instruction it would have executed next. This is why interrupts can handle device events without corrupting the execution of arbitrary user programs."

- question: "Explain why polling is less CPU-efficient than interrupt-driven I/O, and describe the step-by-step sequence from when a device needs service to when the CPU resumes its original work."
  type: short-answer
  answer: "Polling wastes CPU cycles because the processor must repeatedly check a device status register regardless of whether the device is ready — most checks find 'not ready' and discard the result. Interrupt-driven I/O is efficient because the CPU only responds when there is actually something to handle. The interrupt sequence: (1) device signals the CPU's interrupt pin when it needs service; (2) CPU finishes the current instruction; (3) CPU saves the program counter and key registers to a stack; (4) CPU jumps to the pre-defined interrupt service routine (ISR); (5) ISR handles the device event (e.g., reads a byte, acknowledges a transfer); (6) ISR executes 'return from interrupt'; (7) CPU restores saved registers and PC; (8) original program resumes from where it was paused."
  explanation: "The efficiency difference is especially stark for slow devices. A disk might take milliseconds to complete an operation — during which time a polling CPU checks the status register thousands of times, accomplishing nothing. An interrupt-driven CPU runs other processes for those milliseconds and handles the disk event in a single well-timed ISR invocation."
```

## Explainer

From your study of I/O systems, you know that the CPU must somehow communicate with external devices — disks, keyboards, network cards. The simplest approach is **polling**: the CPU repeatedly checks a device's status register in a tight loop, asking "are you ready yet?" This works, but it is enormously wasteful. Imagine standing at your front door checking every second whether a package has arrived, unable to do anything else. Interrupts solve this problem by inverting the relationship: the device notifies the CPU when it needs attention, freeing the processor to execute other instructions in the meantime.

When a device raises an **interrupt**, it sends an electrical signal to the CPU's interrupt pin. The CPU finishes its current instruction, saves the program counter and key registers onto a stack (so it can return later), and jumps to a pre-defined **interrupt service routine (ISR)** — a small handler written specifically for that device. The ISR does whatever the device needs (reads a byte from a keyboard buffer, acknowledges a completed disk transfer), then executes a "return from interrupt" instruction that restores the saved state and resumes the original program exactly where it left off. The entire process is transparent to the interrupted program. This is why your understanding of the control unit matters: it is the control unit that orchestrates the save-jump-restore sequence.

There is an important distinction between interrupts and exceptions. **Interrupts are asynchronous** — they arrive from external hardware at unpredictable times, unrelated to the instruction currently executing. **Exceptions are synchronous** — they are triggered by the instruction itself (a divide-by-zero, an invalid opcode, a page fault). Both use similar handler mechanisms, but their causes and timing are fundamentally different.

Even with interrupts, transferring large blocks of data byte-by-byte through the CPU is inefficient. Consider reading a 4 KB block from disk: with interrupt-driven I/O, the CPU would handle 4,096 separate interrupts, each copying one byte. **Direct Memory Access (DMA)** eliminates this bottleneck by offloading bulk transfers to a dedicated DMA controller. The CPU sets up the transfer by telling the DMA controller the source address, destination address, and byte count, then goes back to running programs. The DMA controller takes over the memory bus, moves the data directly between the device and RAM, and generates a single interrupt when the entire transfer is complete. The CPU's involvement drops from thousands of interrupts to one setup operation and one completion interrupt. The tradeoff is that the DMA controller and CPU must share the memory bus — a technique called **cycle stealing** — so there is some minor slowdown of CPU memory accesses during the transfer, but the net efficiency gain is dramatic.
