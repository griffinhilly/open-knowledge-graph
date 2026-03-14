---
id: disk-io-scheduling
title: Disk I/O Scheduling Algorithms
domain: computer-science
course: operating-systems
prerequisites:
- id: cpu-scheduling-basic-concepts
  type: soft
- id: kernel-mode-and-privilege-levels
  type: soft
tags:
- io-management
- disk-scheduling
- resource-optimization
stage: formal-systems
status: draft
---

# Disk I/O Scheduling Algorithms

## Core Idea
Disk I/O is slow (milliseconds vs. nanoseconds for CPU operations). I/O scheduling orders requests to minimize seek time and rotational latency. Algorithms like FCFS, SSTF (shortest seek time first), and SCAN (elevator) optimize throughput and reduce average seek time. Request batching and write caching further improve I/O performance.
