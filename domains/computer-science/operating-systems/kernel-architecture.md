---
id: kernel-architecture
title: Kernel Architecture and OS Structure
domain: computer-science
course: operating-systems
prerequisites:
- id: instruction-set-architecture
  type: soft
builds-toward:
- system-calls
- process-concept
- os-security-basics
tags:
- kernel
- monolithic
- microkernel
- os-structure
stage: formal-systems
status: draft
---

# Kernel Architecture and OS Structure

## Core Idea
An operating system kernel is the core software layer that mediates between user programs and hardware, managing resources and enforcing protection boundaries. Kernels come in three primary architectural styles: monolithic (all OS services run in a single privileged address space), microkernel (only minimal services run in kernel mode; others run as user-space servers), and hybrid (a pragmatic blend used by macOS and Windows). The architectural choice determines performance characteristics, reliability, and extensibility tradeoffs. Understanding kernel structure is the foundation for understanding every other OS concept.

## How It's Best Learned
Compare Linux (monolithic) and macOS/Mach (hybrid microkernel) side-by-side. Draw the privilege boundary and identify which services cross it. Then explore what a system call looks like at the assembly level.

## Common Misconceptions
- 'Microkernel = slower' is an oversimplification; modern microkernels (e.g., seL4) can be highly performant.
- The kernel is not the entire OS; utilities, shell, and libraries all live in user space.
