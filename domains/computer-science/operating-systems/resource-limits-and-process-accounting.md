---
id: resource-limits-and-process-accounting
title: Resource Limits and Process Accounting
domain: computer-science
course: operating-systems
prerequisites:
- id: process-concept-in-os
  type: hard
- id: system-calls
  type: soft
tags:
- resources
- limits
- accounting
stage: formal-systems
status: draft
---

# Resource Limits and Process Accounting

## Core Idea
Operating systems limit per-process resource consumption (memory, CPU time, file descriptors, disk I/O) to prevent resource exhaustion and ensure fair allocation. Process accounting tracks resource usage for billing, capacity planning, and auditing. Limits are enforced by the kernel at the per-process, user, or system level and can be adjusted dynamically or by configuration.

## Explainer

You already know that a process is the OS's unit of running work — it has its own address space, open files, and CPU state. But imagine a multi-user server where hundreds of processes run simultaneously. Without guardrails, a single runaway process could consume all available memory or open every file descriptor the kernel supports, starving every other process on the machine. **Resource limits** are the kernel's answer: per-process caps that say "you may use this much and no more."

On Unix-like systems, these limits come in two flavors. **Soft limits** are the currently enforced ceiling — a process can raise its own soft limit up to the hard limit without special privileges. **Hard limits** are the absolute maximum, settable only by the superuser. For example, a process might have a soft limit of 1024 open file descriptors and a hard limit of 4096. If it tries to open file descriptor 1025, the `open()` system call fails with an error. The process can call `setrlimit()` to raise its soft limit to 4096, but it cannot exceed the hard limit without root access. Other commonly limited resources include CPU time (the kernel sends a signal when the limit is hit), maximum resident memory size, stack size, and the number of child processes a user can spawn.

**Process accounting** is the bookkeeping side. The kernel can record how much CPU time each process consumed, how many page faults it caused, how much I/O it performed, and when it started and exited. This data gets written to an accounting file that administrators can analyze after the fact. In a shared computing environment — a university cluster, a cloud provider, a corporate server — accounting data answers questions like "which user consumed the most CPU this month?" or "which process caused the I/O spike at 3 AM?" It is the foundation for usage-based billing, capacity planning, and forensic debugging.

The two concepts work together as a resource governance system. Limits are proactive — they prevent abuse before it happens. Accounting is reactive — it records what actually occurred so administrators can tune limits, identify bottlenecks, and hold users accountable. Together, they allow the OS to uphold fairness and stability in environments where many competing processes share finite hardware resources.
