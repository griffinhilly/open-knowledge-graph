---
id: operating-systems-introduction
title: Introduction to Operating Systems
domain: computer-science
course: operating-systems
prerequisites: []
builds-toward:
- kernel-mode-and-privilege-levels
- process-concept-in-os
- memory-management-paging
tags:
- foundational
- os-concepts
- resource-management
stage: formal-systems
status: draft
---

# Introduction to Operating Systems

## Core Idea
An operating system is system software that manages hardware resources and provides services to applications. It handles resource allocation, execution control, and protection to enable multiple programs to run concurrently and safely share hardware. Modern operating systems are essential intermediaries between applications and physical hardware.

## Explainer

Without an operating system, every program would need to manage hardware directly — writing bytes to specific disk controller registers to save a file, programming the network card to send a packet, managing which region of physical RAM it can use without overwriting another program. An **operating system** (OS) is the layer of software that sits between application programs and the bare hardware, handling all of this complexity so that programs can focus on their actual purpose.

The OS plays three fundamental roles. First, it is a **resource manager**. A computer has finite CPU time, memory, disk space, and I/O bandwidth, and multiple programs want to use all of them simultaneously. The OS decides which program gets the CPU next (scheduling), which memory regions each program can access (memory management), and how disk and network bandwidth are shared (I/O management). Without this arbitration, programs would conflict — one might overwrite another's data in memory, or two programs might send interleaved bytes to the printer producing gibberish.

Second, the OS provides **abstraction**. Rather than requiring programs to understand the specific hardware they run on, the OS presents uniform interfaces. A program calls `write()` to save data to a file without knowing whether the underlying storage is a spinning hard drive, an SSD, or a network-mounted filesystem. This abstraction means the same program runs on vastly different hardware configurations without modification. The set of functions the OS exposes to programs is called the **system call interface**, and it is the boundary between user-level code and the privileged kernel.

Third, the OS enforces **protection and isolation**. Each program runs in its own protected environment where it cannot accidentally (or maliciously) access another program's memory, corrupt the OS itself, or monopolize hardware resources. This is what makes multitasking safe: dozens of programs run simultaneously, each believing it has the machine to itself, while the OS quietly ensures they cannot interfere with one another. This protection is enforced by hardware mechanisms (like privilege levels and memory management units) that the OS configures and manages — a theme you will encounter repeatedly as you study processes, memory management, and file systems.
