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
status: validated
---

# Resource Limits and Process Accounting

## Core Idea
Operating systems limit per-process resource consumption (memory, CPU time, file descriptors, disk I/O) to prevent resource exhaustion and ensure fair allocation. Process accounting tracks resource usage for billing, capacity planning, and auditing. Limits are enforced by the kernel at the per-process, user, or system level and can be adjusted dynamically or by configuration.

## Questions

```yaml
- question: "A process tries to open its 2000th file descriptor. Its soft limit is 1024 and its hard limit is 4096. What can the process do?"
  type: multiple-choice
  options:
    - "The open() call fails; the process cannot open more file descriptors regardless"
    - "The process can raise its own soft limit to up to 4096 and retry the open() call"
    - "The process needs root privileges to open more file descriptors since it exceeded its limit"
    - "The kernel automatically kills the process for exceeding its resource limit"
  answer: 1
  explanation: "A process can raise its own soft limit up to the hard limit without special privileges. Since 2000 < 4096 (the hard limit), the process calls setrlimit() to raise its soft limit (e.g., to 4096), then the open() succeeds. Root is only required to raise the hard limit itself. The soft limit is the currently enforced ceiling, not an absolute cap."

- question: "What is the key distinction between resource limits and process accounting?"
  type: multiple-choice
  options:
    - "Limits control memory usage; accounting controls CPU time"
    - "Limits are enforced by hardware; accounting is a software-only mechanism"
    - "Limits proactively prevent resource exhaustion; accounting reactively records what was consumed"
    - "Limits apply only to privileged processes; accounting applies to all processes"
  answer: 2
  explanation: "The fundamental distinction is proactive vs. reactive: limits cap resource consumption before damage occurs, while accounting records actual usage after the fact. Together they form a governance system — limits prevent abuse, accounting enables analysis, billing, and tuning. Neither substitutes for the other."

- question: "A process can raise its own hard limit without administrator privileges if it needs more resources."
  type: true-false
  answer: false
  explanation: "Hard limits are the absolute ceiling and can only be raised by the superuser (root). A process can freely adjust its soft limit up to the hard limit, but it cannot exceed the hard limit without root access. This two-tier design allows normal processes to tune their own behavior within safe bounds while preventing unprivileged processes from bypassing system-wide resource governance."

- question: "Process accounting data can be used for capacity planning and usage-based billing on shared computing systems."
  type: true-false
  answer: true
  explanation: "Accounting records CPU time consumed, I/O performed, page faults, and run durations per process. On shared systems — university clusters, cloud servers, corporate batch systems — this data directly enables administrators to answer 'which user consumed the most CPU this month?' and to bill accordingly. It also helps identify bottlenecks and unusual resource spikes."

- question: "Why would an operating system use both resource limits and process accounting rather than relying on just one mechanism?"
  type: short-answer
  answer: "Limits are proactive: they prevent a runaway process from exhausting resources before damage occurs. Accounting is reactive: it records what actually happened so administrators can tune limits, identify bottlenecks, and hold users accountable. They serve complementary roles — limits prevent abuse in real time, accounting enables analysis and enforcement after the fact. Neither alone is sufficient: limits without accounting give no visibility into usage patterns; accounting without limits allows damage before it can be analyzed."
  explanation: "The two mechanisms target different time horizons. Limits enforce policy in the present; accounting creates a historical record for the future. A well-governed multi-user system needs both: enforce fair usage now, understand actual usage patterns over time."
```

## Explainer

You already know that a process is the OS's unit of running work — it has its own address space, open files, and CPU state. But imagine a multi-user server where hundreds of processes run simultaneously. Without guardrails, a single runaway process could consume all available memory or open every file descriptor the kernel supports, starving every other process on the machine. **Resource limits** are the kernel's answer: per-process caps that say "you may use this much and no more."

On Unix-like systems, these limits come in two flavors. **Soft limits** are the currently enforced ceiling — a process can raise its own soft limit up to the hard limit without special privileges. **Hard limits** are the absolute maximum, settable only by the superuser. For example, a process might have a soft limit of 1024 open file descriptors and a hard limit of 4096. If it tries to open file descriptor 1025, the `open()` system call fails with an error. The process can call `setrlimit()` to raise its soft limit to 4096, but it cannot exceed the hard limit without root access. Other commonly limited resources include CPU time (the kernel sends a signal when the limit is hit), maximum resident memory size, stack size, and the number of child processes a user can spawn.

**Process accounting** is the bookkeeping side. The kernel can record how much CPU time each process consumed, how many page faults it caused, how much I/O it performed, and when it started and exited. This data gets written to an accounting file that administrators can analyze after the fact. In a shared computing environment — a university cluster, a cloud provider, a corporate server — accounting data answers questions like "which user consumed the most CPU this month?" or "which process caused the I/O spike at 3 AM?" It is the foundation for usage-based billing, capacity planning, and forensic debugging.

The two concepts work together as a resource governance system. Limits are proactive — they prevent abuse before it happens. Accounting is reactive — it records what actually occurred so administrators can tune limits, identify bottlenecks, and hold users accountable. Together, they allow the OS to uphold fairness and stability in environments where many competing processes share finite hardware resources.
