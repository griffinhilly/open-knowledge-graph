---
id: multicore-processors-and-hardware-multithreading
title: Multicore Processors and Hardware Multithreading
domain: computer-science
course: computer-architecture
prerequisites:
- id: pipelining-fundamentals
  type: hard
- id: cache-memory-design
  type: hard
- id: performance-and-benchmarking
  type: soft
- id: cache-coherence-protocols
  type: soft
builds-toward:
- gpu-architecture-and-simt
tags:
- multicore
- parallelism
- multithreading
- SMT
- flynn-taxonomy
- shared-memory
- thread-level-parallelism
stage: formal-systems
status: validated
---
# Multicore Processors and Hardware Multithreading

## Core Idea
A multicore processor places several complete processor cores on one chip, each able to run its own thread, usually sharing a last-level cache and main memory. Chip makers turned to multicore designs in the mid-2000s because raising clock rates further had become limited by power and heat. Hardware multithreading is a related idea inside a single core: the core keeps the state of several threads and switches among them, or issues from several at once, to keep its pipeline busy while one thread waits. Both deliver speed only when software supplies multiple threads of work.

## How It's Best Learned
Start from the power problem: show that dynamic power grows with clock frequency and with the square of voltage, so faster single cores ran into heat limits. Use Flynn's taxonomy to place a multicore chip as MIMD. Then sketch one pipeline over time for coarse-grained, fine-grained and simultaneous multithreading, coloring each issue slot by thread, and finish with Amdahl's law calculations to show why serial code limits the gain.

## Common Misconceptions
- A program runs faster on more cores without any changes. (A single-threaded program uses one core; it gains only if the work is split into threads or processes.)
- Simultaneous multithreading doubles performance like a second core. (SMT threads share one core's execution units and caches, so gains are usually far smaller and depend on the workload.)
- Each core has a private copy of memory, so threads cannot interfere. (Cores share main memory; coherence hardware keeps cached copies consistent, and software still needs synchronization to avoid races.)

## Questions

```yaml
- question: "Why did mainstream processor makers shift from ever-faster single cores to multicore chips in the mid-2000s?"
  type: multiple-choice
  options:
    - "Transistors stopped getting smaller, so no more cores could be added"
    - "Raising clock rates further caused too much power use and heat, so extra transistors were spent on more cores instead"
    - "Operating systems could not schedule threads on a single core"
    - "Memory became faster than processors, so single cores sat idle"
  answer: 1
  explanation: "Transistor counts kept growing, but the power and heat from higher clock rates hit practical limits, a problem often called the power wall. Designers used the growing transistor budget to place several cores on a chip instead of making one core run faster."

- question: "In a core with simultaneous multithreading (SMT), such as Intel's Hyper-Threading, which statement is most accurate?"
  type: multiple-choice
  options:
    - "Each hardware thread has its own complete set of execution units"
    - "Each hardware thread has its own program counter and registers, while the threads share the core's execution units and caches"
    - "Only one thread can issue instructions in any given cycle"
    - "The threads must belong to the same process"
  answer: 1
  explanation: "SMT duplicates the per-thread architectural state (program counter, registers) so the core can track several threads, and it can issue instructions from more than one thread in the same cycle into shared functional units. Fine-grained and coarse-grained multithreading issue from only one thread at a time."

- question: "A program with no threading code will run about four times faster on a four-core processor than on a one-core processor with the same core design."
  type: true-false
  answer: false
  explanation: "A single-threaded program runs on one core at a time. The other cores can run other programs, but this program does not speed up unless it is rewritten to divide its work among threads or processes."

- question: "A program spends 90% of its time in work that can be split perfectly across cores and 10% in work that must run serially. Using Amdahl's law, estimate its speedup on 8 cores."
  type: short-answer
  answer: "Speedup = 1 / (0.10 + 0.90 / 8) = 1 / (0.10 + 0.1125) = 1 / 0.2125, which is about 4.7."
  explanation: "Even with 8 cores, the serial 10% limits the result to well under 8x. As cores grow without limit, the speedup approaches 1 / 0.10 = 10, never more."
```

## Explainer

For decades, programs got faster each year without any changes because processor clock rates kept climbing. In the mid-2000s that trend stalled. Dynamic power in a chip grows with clock frequency and with the square of supply voltage. Voltages could no longer be lowered much, so higher clock rates meant chips too hot to cool cheaply. Transistors were still shrinking, though, so designers had more of them to spend. They spent them on more cores.

A **multicore processor** is several full cores, each with its own pipeline, registers and usually private L1 and L2 caches, on one chip. The cores typically share a last-level cache and the connection to main memory. In Michael Flynn's 1966 taxonomy, which classifies machines by instruction streams and data streams, a multicore chip is **MIMD**: multiple instruction streams operating on multiple data streams. All cores see one shared address space, so threads communicate by reading and writing memory. Because each core caches data, the chip needs a **cache coherence** protocol so that a write by one core is seen correctly by the others.

**Hardware multithreading** attacks a different problem: a single core's pipeline often sits idle, for example while waiting hundreds of cycles for a cache miss. If the core holds the state of several threads, with a separate program counter and register set for each, it can use those idle slots. In **coarse-grained** multithreading the core switches threads only on long stalls. In **fine-grained** multithreading it switches every cycle. In **simultaneous multithreading** (SMT), used in Intel's Hyper-Threading, a superscalar core issues instructions from several threads in the same cycle. The operating system sees each hardware thread as a logical processor.

None of this helps a program that has only one thread. Software must expose parallelism, and **Amdahl's law** limits the payoff. If a fraction s of the work is serial, the speedup on n cores is at most 1 / (s + (1 - s) / n). With s = 0.1, even unlimited cores cannot exceed 10x. Sharing also brings costs: threads that touch the same data need locks or atomic operations, and cores contending for one memory system can slow one another down.

Multicore and multithreaded designs are now standard in phones, laptops and servers. The next step in the same direction is the GPU, which runs thousands of simple threads at once.
