---
id: memory-protection-hardware
title: Memory Protection and Access Control Hardware
domain: computer-science
course: computer-architecture
prerequisites:
- id: memory-management-paging-segmentation
  type: hard
- id: translation-lookaside-buffer-tlb
  type: soft
builds-toward:
- exception-handling-architecture
tags:
- memory-protection
- privilege-levels
- access-control
stage: formal-systems
status: draft
---

# Memory Protection and Access Control Hardware

## Core Idea
MMUs (memory management units) enforce access control: each page has protection bits (read, write, execute) and a privilege level. The processor's current privilege level (user, supervisor, kernel) is checked; privilege violations cause exceptions. Memory protection prevents user programs from accessing other processes' memory and kernel memory.

## Explainer

You already understand how paging divides virtual memory into fixed-size pages mapped to physical frames through page tables, and how the TLB caches these translations for speed. Memory protection builds directly on this infrastructure — the same page table entries that translate addresses also carry **protection bits** that control what operations are allowed on each page. Every time the MMU translates a virtual address, it simultaneously checks whether the requested access type (read, write, or execute) is permitted by those bits.

Each page table entry typically contains at least three protection flags: **read**, **write**, and **execute**. A page holding program code might be marked read and execute but not write, preventing the program from accidentally (or maliciously) overwriting its own instructions. A page holding data would be marked read and write but not execute, so even if an attacker injects malicious code into a data buffer, the processor refuses to execute it. This principle — called **W^X** (write XOR execute) — is a fundamental defense against code injection attacks.

Protection also depends on **privilege levels**, sometimes called rings. Most processors define at least two levels: kernel mode (ring 0) and user mode (ring 3 on x86). Each page table entry records the minimum privilege level required to access that page. When a user-mode program tries to read a page marked as kernel-only, the MMU does not return the data — instead, it triggers a **protection fault**, an exception that transfers control to the operating system's fault handler. This is how the OS prevents applications from reading each other's memory or tampering with kernel data structures.

The beauty of hardware-enforced protection is that it cannot be bypassed by software running at lower privilege. A user program cannot modify its own page table entries because those entries live in kernel-only memory. It cannot disable the MMU because that requires a privileged instruction. Every single memory access passes through the MMU's check, with no opt-out. This creates the isolation boundary that makes multitasking possible — dozens of processes share the same physical RAM, each believing it has the machine to itself, with the hardware guaranteeing that no process can reach beyond its own address space.
