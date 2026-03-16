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

## Explainer

You have seen how CPU scheduling decides which process gets the processor next. Disk I/O scheduling solves an analogous problem — deciding which pending disk request to service next — but the optimization target is different. CPU scheduling optimizes for fairness and responsiveness. Disk scheduling optimizes for **minimizing mechanical movement**, because the physical geometry of a spinning disk makes the order of requests matter enormously.

A traditional hard disk has a read/write head that moves across a spinning platter. Servicing a request involves two physical delays: **seek time** (moving the head to the correct track) and **rotational latency** (waiting for the platter to spin the target sector under the head). Seek time dominates — moving the head from the innermost to outermost track can take 10–15 milliseconds, while a full rotation at 7200 RPM takes about 8 ms. If the OS processes requests in the order they arrive (**FCFS**), the head bounces wildly across the disk: track 50, then track 180, then track 12, then track 175. Each jump wastes milliseconds of seek time. With dozens of pending requests, intelligent reordering can cut total seek time by an order of magnitude.

**SSTF** (Shortest Seek Time First) always services the request closest to the current head position, much like choosing the nearest unvisited city in the traveling salesman problem. This dramatically reduces average seek time, but it has a starvation problem: if requests keep arriving near the current head position, distant requests may wait indefinitely. The **SCAN** algorithm (also called the **elevator algorithm**) fixes this by moving the head in one direction — say, from the inner tracks outward — servicing all requests along the way, then reversing direction. Just like a building elevator that goes all the way up before coming down, SCAN guarantees every pending request is eventually reached. **C-SCAN** (Circular SCAN) is a variant that only services requests in one direction and then jumps back to the beginning without servicing requests on the return trip, providing more uniform wait times.

The relevance of these algorithms has shifted with modern storage hardware. Solid-state drives (SSDs) have no moving parts, so seek time and rotational latency are zero — making I/O scheduling far less critical for SSDs. However, understanding disk scheduling remains important for three reasons. First, spinning disks are still widely used in data centers for bulk storage. Second, the same principles apply whenever request ordering affects performance — network packet scheduling, elevator control, and even database query optimization involve analogous tradeoffs between throughput, latency, and fairness. Third, the starvation and fairness problems in SSTF mirror issues you will encounter throughout systems design: greedy optimization of one metric often comes at the cost of another.
