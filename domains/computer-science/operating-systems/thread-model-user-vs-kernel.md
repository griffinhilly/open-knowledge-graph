---
id: thread-model-user-vs-kernel
title: 'Thread Models: User-Level and Kernel Threads'
domain: computer-science
course: operating-systems
prerequisites:
- id: process-concept-in-os
  type: hard
builds-toward:
- thread-creation-and-lifecycle
- concurrency-and-race-conditions
tags:
- threading
- lightweight-concurrency
- kernel-vs-user
stage: formal-systems
status: draft
---

# Thread Models: User-Level and Kernel Threads

## Core Idea
Threads are lightweight execution units sharing an address space within a process. User-level threads are scheduled by user-space libraries, reducing kernel overhead but limiting parallelism to one thread per process. Kernel threads are scheduled by the OS, enabling true parallelism. Hybrid models (M:N) attempt to balance overhead and parallelism.
