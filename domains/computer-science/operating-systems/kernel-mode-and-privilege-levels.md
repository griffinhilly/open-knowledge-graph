---
id: kernel-mode-and-privilege-levels
title: Kernel Mode and Privilege Levels
domain: computer-science
course: operating-systems
prerequisites:
- id: operating-systems-introduction
  type: hard
builds-toward:
- system-calls
- process-creation-fork-exec
- interrupt-exception-handling
tags:
- security
- hardware-abstraction
- privilege
- protection
stage: formal-systems
status: draft
---

# Kernel Mode and Privilege Levels

## Core Idea
Modern CPUs support multiple privilege levels (typically user and kernel modes) to protect the OS from applications. Kernel mode allows unrestricted hardware access and is used for OS operations. User mode restricts operations to prevent applications from interfering with each other or the OS. Privilege transitions occur via system calls or interrupts.

## How It's Best Learned
Use system call tracing tools (strace, ltrace) to observe transitions between user and kernel mode during application execution.

## Common Misconceptions
Applications can do nothing in user mode (they perform computation and I/O via system calls). Kernel mode is always secure (it requires careful validation to prevent bugs).
