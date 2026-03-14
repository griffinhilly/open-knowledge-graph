---
id: process-termination-and-cleanup
title: Process Termination and Resource Cleanup
domain: computer-science
course: operating-systems
prerequisites:
- id: process-creation-fork-exec
  type: hard
builds-toward:
- process-states-and-transitions
tags:
- process-lifecycle
- resource-management
- system-calls
stage: formal-systems
status: draft
---

# Process Termination and Resource Cleanup

## Core Idea
Processes terminate via exit() system call or signal delivery. The OS transitions the process to zombie state until the parent reaps it via waitpid(). Resource cleanup includes freeing memory, closing file descriptors, and notifying child processes. Proper cleanup prevents resource leaks and zombie accumulation.

## Common Misconceptions
Calling exit() immediately frees all resources (some remain in zombie state until reaped). Orphan processes are killed (they are reparented to init/systemd, not killed).
