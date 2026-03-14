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
