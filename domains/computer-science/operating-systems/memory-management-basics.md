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
status: draft
---

# Memory Management Fundamentals

## Core Idea
Memory management is the OS subsystem responsible for tracking which memory is in use, allocating memory to processes, and reclaiming it when processes terminate. A key abstraction is the separation between logical addresses (the address a program generates, also called virtual addresses) and physical addresses (the actual location in RAM). Address binding — mapping logical to physical — can occur at compile time, load time, or execution time; execution-time binding via hardware (the Memory Management Unit, MMU) is used by modern systems because it allows the OS to relocate a process freely. The MMU performs address translation on every memory access, enabling isolation and protection between processes.

## How It's Best Learned
Trace how a pointer dereference in a C program becomes a physical memory access: compiler generates logical address, MMU translates, physical RAM is accessed. Then explain why two processes can have the same logical address but different physical locations.

## Common Misconceptions
- Virtual/logical and physical addresses are not the same thing; confusing them leads to deep misunderstandings of paging and segmentation.
- The MMU is hardware, not software, though its configuration (page tables) is managed by the OS kernel.
