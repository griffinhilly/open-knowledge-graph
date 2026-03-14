---
id: test-and-set-primitive
title: Test-and-Set and Atomic Primitives
domain: computer-science
course: operating-systems
prerequisites:
- id: software-mutual-exclusion-solutions
  type: hard
- id: atomic-operations-compare-and-swap
  type: soft
builds-toward:
- semaphore-formal-definition
tags:
- synchronization
- atomic
- hardware
stage: formal-systems
status: draft
---

# Test-and-Set and Atomic Primitives

## Core Idea
Test-and-set, compare-and-swap, and similar atomic operations read and modify memory in a single indivisible instruction. These enable efficient lock implementation without polling or context switches, providing the hardware foundation for high-level synchronization primitives.
