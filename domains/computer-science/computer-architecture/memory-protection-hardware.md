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
