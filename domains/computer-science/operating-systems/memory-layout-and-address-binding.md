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

## Explainer

When a program is compiled, the compiler generates instructions that reference memory addresses — "store this value at address 0x1000," "jump to the instruction at address 0x2040." But these addresses are not physical locations in RAM; they are **logical addresses** in an abstract space that the program assumes it owns entirely. The question of *when* and *how* these logical addresses get mapped to actual physical RAM locations is the problem of **address binding**, and the answer has profound consequences for flexibility, security, and how the OS manages multiple programs simultaneously.

The program's logical address space is organized into well-defined regions, each serving a different purpose. The **text segment** (or code segment) holds the compiled machine instructions and is typically marked read-only — the program should never modify its own instructions. The **data segment** holds global and static variables that are initialized at compile time. The **heap** grows upward from the end of the data segment and is used for dynamic allocation (`malloc` in C, `new` in C++). The **stack** grows downward from the top of the address space and holds function call frames — local variables, return addresses, and saved registers. Between the heap and stack is a gap that shrinks as either one grows. If they collide, the program has exhausted its address space.

**Address binding** can happen at three stages, each offering different tradeoffs. **Compile-time binding** hardcodes physical addresses into the executable — the compiler decides that the code starts at physical address 0x0000 and the data at 0x5000. This is simple but inflexible: the program can only run if those exact physical addresses are available, which means you can only run one instance and it must always load at the same location. **Load-time binding** delays the decision until the program is loaded into memory. The loader knows which physical addresses are free, patches all the address references in the executable to match, and then runs the program. This allows multiple programs to coexist, but once loaded, the program cannot move — if the OS needs to relocate it (for compaction, say), it would have to re-patch every address.

**Execution-time (dynamic) binding** is what modern operating systems use. The program runs with logical addresses that are translated to physical addresses *on every memory access* by hardware called the **Memory Management Unit (MMU)**. The program never knows or cares where it actually sits in physical RAM. This enables the OS to move processes in memory without their knowledge, run the same program at different physical addresses simultaneously, and implement **Address Space Layout Randomization (ASLR)** — randomly placing the stack, heap, and libraries at different addresses each time a program runs to make exploitation of memory vulnerabilities much harder. Dynamic binding requires hardware support (base and limit registers, or page tables), but it is the foundation on which virtual memory, process isolation, and modern security features are all built.
