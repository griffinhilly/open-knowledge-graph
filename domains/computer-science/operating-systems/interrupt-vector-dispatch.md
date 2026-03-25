---
id: interrupt-vector-dispatch
title: Interrupt Vector Tables and Dispatch
domain: computer-science
course: operating-systems
prerequisites:
- id: interrupts-and-dma
  type: hard
- id: cpu-control-unit
  type: soft
builds-toward:
- exception-handling-os-internals
tags:
- interrupts
- hardware
- dispatch
stage: formal-systems
status: validated
---

# Interrupt Vector Tables and Dispatch

## Core Idea
When a hardware interrupt or exception occurs, the CPU consults an interrupt vector table indexed by interrupt number to find the handler address. This enables the OS to dispatch control rapidly without querying what caused the interrupt.

## Questions

```yaml
- question: "When interrupt number 14 (page fault) fires on an x86 processor, how does the CPU determine which handler to execute?"
  type: multiple-choice
  options:
    - "The CPU scans kernel code for a function named 'page_fault_handler'"
    - "The CPU raises a special page-fault signal and waits for the OS to respond"
    - "The CPU indexes into the interrupt descriptor table at position 14, reads the stored handler address, and jumps to it"
    - "The CPU checks the interrupt type register and executes a switch statement in microcode"
  answer: 2
  explanation: "The interrupt vector table (IDT on x86) is an array where each position stores the address of the corresponding handler. Interrupt 14 → IDT[14] → address of page fault handler → jump. This is a single indexed memory access, not a search. The entire mechanism is designed for speed — interrupts can happen millions of times per second and cannot afford conditional logic. Option A describes an impossible runtime search; Option D confuses hardware dispatch with software logic."

- question: "An interrupt fires while a user process is executing on x86. What does the CPU automatically do before jumping to the kernel handler?"
  type: multiple-choice
  options:
    - "The CPU does nothing automatically — the handler is responsible for saving all state before using any registers"
    - "The CPU saves the instruction pointer and flags register onto the stack, and switches to the kernel stack if crossing privilege levels"
    - "The CPU pauses all other processes and sends an acknowledgment signal to the interrupting device"
    - "The CPU copies the entire process address space into a kernel buffer for safe handling"
  answer: 1
  explanation: "x86 automatically saves the instruction pointer (so execution can resume) and the flags register onto the stack when an interrupt fires. If the interrupt occurred during user-mode execution, the CPU also switches to the kernel stack and saves the user stack pointer and code segment — enforcing the privilege boundary. This automatic save enables the handler to run in kernel context and then execute 'iret' to restore the saved state and resume the interrupted code exactly where it left off. Option A would make reliable interrupt handling impossible."

- question: "When a hardware interrupt fires, the CPU searches through kernel code to find the correct handler function based on the type of interrupt."
  type: true-false
  answer: false
  explanation: "The interrupt vector table exists precisely to avoid any searching. Dispatch is a single O(1) array lookup: interrupt number → table index → handler address → jump. This is the fundamental design insight — speed is critical because interrupts are frequent and latency matters. A search through kernel code would be far too slow and error-prone. The OS pre-populates the table at boot so that all dispatching at runtime is just one indexed memory read."

- question: "The operating system populates the interrupt vector table during boot, before any user processes run."
  type: true-false
  answer: true
  explanation: "Boot-time initialization of the interrupt vector table is essential — if the table isn't set up before devices start firing interrupts, the CPU would have nowhere valid to jump. During early kernel initialization, the OS writes handler addresses into each IDT slot, then loads the table's base address into the IDTR register (on x86) so the CPU knows where the table lives. Hardware device drivers also register their handlers as devices are initialized. All of this happens before the kernel starts scheduling user processes."

- question: "Why does the interrupt dispatch mechanism use an indexed array (the interrupt vector table) rather than a set of if-else conditions in the kernel, and what makes this design critical for system performance?"
  type: short-answer
  answer: "An indexed array makes dispatch O(1): given interrupt number k, the CPU reads one memory location (table[k]) to get the handler address — no comparison, no branching. If-else chains would require O(n) comparisons in the worst case, and n can be 256 on x86. More importantly, interrupt dispatch must complete in a handful of cycles — timer interrupts fire thousands of times per second, disk and network interrupts fire continuously under load. Any latency in dispatch directly impacts I/O throughput and system responsiveness. The array design offloads all flexibility to boot-time setup while keeping runtime dispatch instant."
  explanation: "The interrupt vector table is a textbook example of trading setup cost for runtime speed. The OS pays a one-time cost at boot to populate the table; thereafter, every dispatch is a single indexed read. This pattern — precomputed lookup tables for performance-critical paths — appears throughout systems software. The alternative (conditional dispatch) would be not just slow but fragile, as devices are added and removed dynamically."
```

## Explainer

From your study of interrupt and exception handling, you know that hardware devices signal the CPU when they need attention — a keyboard press, a disk transfer completing, a timer tick. The CPU must stop what it is doing and jump to the appropriate handler code in the operating system. The question is: how does the CPU know *where* to jump? It cannot run a search through kernel code looking for the right handler. Interrupts happen millions of times per second, so the dispatch mechanism must be essentially instant.

The answer is the **interrupt vector table** (IVT), sometimes called the **interrupt descriptor table** (IDT) on x86 processors. This is simply an array stored at a known memory address, where each entry corresponds to a specific interrupt number. Entry 0 might point to the divide-by-zero exception handler. Entry 14 points to the page fault handler. Entry 32 might point to the timer interrupt handler. When interrupt number *k* fires, the CPU indexes into the table at position *k*, reads the address stored there, and jumps to that address. The entire dispatch is a single array lookup — no conditionals, no searching, just one indexed memory access followed by a jump.

The operating system populates the interrupt vector table during boot. For each interrupt number, the kernel writes the address of the corresponding handler function into the table. Some entries are fixed by the hardware architecture — for instance, on x86, interrupts 0–31 are reserved for CPU exceptions (divide error, page fault, general protection fault, etc.). The remaining entries (32–255 on x86) are available for hardware devices and software interrupts. When a device like a network card is initialized, its driver registers a handler by writing the handler's address into the appropriate slot. The CPU itself knows the table's base address because the OS loads it into a special register (the IDTR on x86) during startup.

The dispatch process involves more than just jumping to a handler. When an interrupt fires, the CPU automatically saves critical state — at minimum the instruction pointer and flags register — onto the stack so it can resume the interrupted code later. On x86, the CPU also switches to a kernel stack if the interrupt occurred while running user code, enforcing the privilege boundary you studied in kernel mode and privilege levels. After the handler finishes (typically by executing an `iret` instruction), the saved state is restored and execution resumes exactly where it left off. This save-dispatch-handle-restore cycle is the fundamental mechanism by which the OS responds to hardware events while maintaining the illusion that user programs run uninterrupted.
