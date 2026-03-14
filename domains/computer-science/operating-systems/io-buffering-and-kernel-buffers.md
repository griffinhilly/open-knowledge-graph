---
id: io-buffering-and-kernel-buffers
title: I/O Buffering and Kernel Buffer Caches
domain: computer-science
course: operating-systems
prerequisites:
- id: io-systems-overview
  type: hard
- id: cache-design-principles
  type: soft
tags:
- io
- buffering
- cache
stage: formal-systems
status: draft
---

# I/O Buffering and Kernel Buffer Caches

## Core Idea
The kernel maintains buffer caches between processes and storage devices to reduce I/O latency and optimize bandwidth utilization. Write-back caching defers writes to disk; read caching avoids repeated disk accesses for the same data. Buffer cache management, including dirty buffer flushing and page replacement policies, is critical to both performance and data durability guarantees.
