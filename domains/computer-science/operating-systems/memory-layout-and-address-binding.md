---
id: memory-layout-and-address-binding
title: Memory Layout and Address Binding
domain: computer-science
course: operating-systems
prerequisites:
- id: memory-management-basics
  type: hard
- id: address-space-layout
  type: soft
builds-toward:
- contiguous-allocation-strategies
- virtual-address-translation-scheme
tags:
- memory-management
- address-binding
- layout
stage: formal-systems
status: draft
---

# Memory Layout and Address Binding

## Core Idea
Memory layout divides the address space into segments: code (read-only), initialized data, heap (dynamic), and stack. Address binding (assigning logical to physical addresses) can occur at compile time (static), load time (fixed), or run time (dynamic); dynamic binding enables address space layout randomization (ASLR).

## Questions

```yaml
- question: "Address Space Layout Randomization (ASLR) makes buffer overflow exploits harder by placing the stack, heap, and libraries at different addresses on every program run. Which address binding technique does ASLR depend on?"
  type: multiple-choice
  options:
    - "Compile-time binding — the compiler randomly selects addresses each time it builds the executable"
    - "Load-time binding — the loader patches the executable with random addresses before each run"
    - "Execution-time (dynamic) binding — logical addresses are translated to physical addresses by the MMU at runtime, allowing different physical placements on each execution without modifying the program"
    - "ASLR is implemented in the compiler and does not depend on address binding technique"
  answer: 2
  explanation: "ASLR requires that the same program can run at different physical addresses on different executions — and even run multiple instances simultaneously at different locations. This is only possible with execution-time binding, where logical addresses in the program's code remain fixed but the MMU maps them to different physical locations each run. Compile-time binding hardcodes physical addresses into the binary, making ASLR impossible. Load-time binding could randomize placement at load time, but once running, the process cannot be relocated — and load-time patching of every address reference is incompatible with shared libraries and PIE (position-independent executables) in practice."

- question: "Under compile-time address binding, what is the fundamental practical limitation that makes it unsuitable for modern operating systems?"
  type: multiple-choice
  options:
    - "Compile-time binding slows execution because address translation requires extra CPU cycles at runtime"
    - "The program can only run correctly if the exact physical addresses hardcoded in the executable are available and unoccupied — preventing multiple simultaneous instances and conflicting with other programs"
    - "The compiler cannot perform optimizations when physical addresses are determined at compile time"
    - "The heap and stack cannot be allocated dynamically when addresses are fixed at compile time"
  answer: 1
  explanation: "Compile-time binding embeds specific physical addresses directly in the machine code. If another program is already using those addresses, or if you try to run two instances simultaneously, the programs will collide. There is no mechanism for the OS to place the program anywhere other than where the compiler decreed. This made sense on early single-program systems where the hardware was dedicated to one program at a time, but it is completely incompatible with multitasking operating systems."

- question: "Under execution-time (dynamic) address binding, a running process never directly knows or works with its physical addresses in RAM."
  type: true-false
  answer: true
  explanation: "True. With dynamic binding, the program is entirely written in terms of logical addresses. Every time it accesses memory, the MMU silently translates the logical address to a physical one. The process has no knowledge of where it physically resides. This abstraction is what enables virtual memory, process isolation (two processes can use the same logical address 0x1000 without conflict), relocation of running processes, and ASLR — all without any modification to the program itself."

- question: "Load-time address binding allows the operating system to relocate a running process in physical memory without disrupting the process's execution."
  type: true-false
  answer: false
  explanation: "False. Load-time binding patches all address references in the executable when the program is first loaded. Once running, all addresses are fixed to the physical locations chosen at load time. Moving the process would require re-scanning and re-patching every address reference in the running code and data — an operation that cannot be done transparently while the process is executing. Only execution-time (dynamic) binding, using the MMU to translate on every access, allows the OS to remap a process's physical location without the process noticing."

- question: "Explain why execution-time address binding requires dedicated hardware (the MMU) while compile-time binding does not."
  type: short-answer
  answer: "With compile-time binding, physical addresses are embedded directly in the machine code. The CPU reads them and uses them as-is — no translation needed, no extra hardware required. With execution-time binding, every single memory access requires translating a logical address to a physical one. A modern program may perform hundreds of millions of memory accesses per second. If this translation were done in software (by the OS kernel), each access would require a context switch into the OS, reducing performance by several orders of magnitude. The MMU is dedicated hardware that performs this translation in a single clock cycle, making dynamic binding fast enough to be practical."
  explanation: "The MMU is the hardware mechanism that makes virtual memory possible. Without it, dynamic binding would be too slow to use. This is why virtual memory is a joint achievement of OS design and computer architecture — the OS manages the mapping tables, but the hardware does the per-access translation."
```

## Explainer

When a program is compiled, the compiler generates instructions that reference memory addresses — "store this value at address 0x1000," "jump to the instruction at address 0x2040." But these addresses are not physical locations in RAM; they are **logical addresses** in an abstract space that the program assumes it owns entirely. The question of *when* and *how* these logical addresses get mapped to actual physical RAM locations is the problem of **address binding**, and the answer has profound consequences for flexibility, security, and how the OS manages multiple programs simultaneously.

The program's logical address space is organized into well-defined regions, each serving a different purpose. The **text segment** (or code segment) holds the compiled machine instructions and is typically marked read-only — the program should never modify its own instructions. The **data segment** holds global and static variables that are initialized at compile time. The **heap** grows upward from the end of the data segment and is used for dynamic allocation (`malloc` in C, `new` in C++). The **stack** grows downward from the top of the address space and holds function call frames — local variables, return addresses, and saved registers. Between the heap and stack is a gap that shrinks as either one grows. If they collide, the program has exhausted its address space.

**Address binding** can happen at three stages, each offering different tradeoffs. **Compile-time binding** hardcodes physical addresses into the executable — the compiler decides that the code starts at physical address 0x0000 and the data at 0x5000. This is simple but inflexible: the program can only run if those exact physical addresses are available, which means you can only run one instance and it must always load at the same location. **Load-time binding** delays the decision until the program is loaded into memory. The loader knows which physical addresses are free, patches all the address references in the executable to match, and then runs the program. This allows multiple programs to coexist, but once loaded, the program cannot move — if the OS needs to relocate it (for compaction, say), it would have to re-patch every address.

**Execution-time (dynamic) binding** is what modern operating systems use. The program runs with logical addresses that are translated to physical addresses *on every memory access* by hardware called the **Memory Management Unit (MMU)**. The program never knows or cares where it actually sits in physical RAM. This enables the OS to move processes in memory without their knowledge, run the same program at different physical addresses simultaneously, and implement **Address Space Layout Randomization (ASLR)** — randomly placing the stack, heap, and libraries at different addresses each time a program runs to make exploitation of memory vulnerabilities much harder. Dynamic binding requires hardware support (base and limit registers, or page tables), but it is the foundation on which virtual memory, process isolation, and modern security features are all built.
