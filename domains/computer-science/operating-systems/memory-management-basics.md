---
id: memory-management-basics
title: Memory Management Fundamentals
domain: computer-science
course: operating-systems
prerequisites:
- id: memory-hierarchy-overview
  type: hard
- id: memory-organization
  type: hard
builds-toward:
- contiguous-memory-allocation
- paging
- segmentation
tags:
- logical-address
- physical-address
- address-binding
- MMU
- relocation
stage: formal-systems
status: validated
---

# Memory Management Fundamentals

## Core Idea
Memory management is the OS subsystem responsible for tracking which memory is in use, allocating memory to processes, and reclaiming it when processes terminate. A key abstraction is the separation between logical addresses (the address a program generates, also called virtual addresses) and physical addresses (the actual location in RAM). Address binding — mapping logical to physical — can occur at compile time, load time, or execution time; execution-time binding via hardware (the Memory Management Unit, MMU) is used by modern systems because it allows the OS to relocate a process freely. The MMU performs address translation on every memory access, enabling isolation and protection between processes.

## How It's Best Learned
Trace how a pointer dereference in a C program becomes a physical memory access: compiler generates logical address, MMU translates, physical RAM is accessed. Then explain why two processes can have the same logical address but different physical locations.

## Common Misconceptions
- Virtual/logical and physical addresses are not the same thing; confusing them leads to deep misunderstandings of paging and segmentation.
- The MMU is hardware, not software, though its configuration (page tables) is managed by the OS kernel.

## Questions

```yaml
- question: "A program running on a modern OS generates the address 0x4000. At what point is this logical address translated to a physical address?"
  type: multiple-choice
  options: ["When the program is compiled", "When the program is loaded into memory", "At execution time, by the MMU hardware", "At execution time, by the OS kernel in software"]
  answer: 2
  explanation: "Modern systems use execution-time binding via hardware (the MMU). This allows the OS to relocate processes freely in physical memory without recompiling or reloading. The MMU — not the OS kernel software — performs the translation on every memory access; the kernel only configures the MMU's mapping tables."

- question: "Two processes can legally have identical logical address values (e.g., both use address 0x1000) without interfering with each other."
  type: true-false
  answer: true
  explanation: "Because logical addresses are translated to physical addresses by the MMU using per-process mapping tables, two processes can each have a logical address 0x1000 that maps to completely different physical locations. This is one of the key benefits of execution-time binding — it enables process isolation."

- question: "Why is execution-time address binding preferred over compile-time or load-time binding in modern operating systems?"
  type: short-answer
  answer: "Execution-time binding allows the OS to move a process to a different physical memory location at any time, because the MMU translates addresses on every access. Compile-time and load-time binding fix physical addresses early, preventing relocation and making multiprogramming and memory isolation much harder."
  explanation: "If addresses are baked in at compile or load time, the OS cannot freely place or relocate processes — every program would need exclusive access to a fixed memory region. Execution-time binding via the MMU decouples logical layout (what the program sees) from physical layout (where RAM is actually used), enabling flexible multiprogramming and process protection."
```

## Explainer

When a program runs, it constantly refers to memory addresses — to read variables, call functions, and access data structures. But here is the key insight: the address a program generates (a *logical* address) is not the address where its data actually lives in RAM (the *physical* address). These two address spaces are intentionally kept separate, and the hardware unit that bridges them on every single memory access is the Memory Management Unit (MMU).

Why go to this trouble? Consider what happens when two programs are both running. Both might generate the address `0x4000` in their own code — perhaps both have a variable at the start of their memory. If these addresses referred directly to RAM, the two programs would collide. Instead, the OS configures the MMU with a different mapping for each process: process A's `0x4000` maps to physical address `0x10000`, while process B's `0x4000` maps to `0x20000`. Each process is isolated in its own logical address space, invisible to the other.

Address binding — the act of deciding where in physical memory a logical address maps — can happen at different times. Compile-time binding bakes physical addresses into the binary, which is inflexible and essentially requires the program to always load at the same location. Load-time binding sets addresses when the program is loaded into memory, which is more flexible but still commits to a fixed location for the entire run. Execution-time binding, used by all modern systems, defers the mapping to the MMU hardware and allows the OS to move a process freely at any time. This flexibility is what makes paging, segmentation, and virtual memory possible.

One critical distinction to keep straight: the MMU is hardware, not software. It is a physical chip (integrated into the CPU on modern processors) that intercepts every memory access and performs the logical-to-physical translation at wire speed. The OS *configures* the MMU by writing mapping tables (page tables) into memory, but the translation itself happens in hardware with no software involvement. This is why the overhead of address translation is negligible — the MMU does it in the same clock cycles as the memory access itself.

Memory management is the foundation on which everything else in an OS rests. Paging divides logical and physical memory into fixed-size pages and frames. Segmentation divides by logical region (code, stack, heap). Virtual memory extends these ideas to allow processes to use more address space than physical RAM exists. All of these build on the core abstraction you have just learned: logical addresses are a program's view of memory, physical addresses are reality, and the MMU is what connects them.

