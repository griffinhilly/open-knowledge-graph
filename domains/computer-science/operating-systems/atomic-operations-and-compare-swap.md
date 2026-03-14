---
id: atomic-operations-and-compare-swap
title: Atomic Operations and Compare-and-Swap
domain: computer-science
course: operating-systems
prerequisites:
- id: synchronization-problem
  type: hard
- id: kernel-mode-and-privilege-levels
  type: soft
builds-toward:
- spinlocks-and-busy-waiting
tags:
- synchronization
- atomic
- lock-free
stage: formal-systems
status: draft
---

# Atomic Operations and Compare-and-Swap

## Core Idea
Atomic operations execute indivisibly without interruption, enabling lock-free synchronization primitives. Compare-and-swap (CAS) atomically compares a memory location's value and conditionally updates it in a single operation. Lock-free algorithms using CAS can improve concurrency and reduce context switch overhead but are notoriously difficult to implement and reason about correctly.
