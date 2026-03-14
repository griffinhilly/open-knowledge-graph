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
