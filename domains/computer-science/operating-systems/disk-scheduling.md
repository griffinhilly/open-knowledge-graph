---
id: disk-scheduling
title: Disk Scheduling Algorithms
domain: computer-science
course: operating-systems
prerequisites:
- id: io-systems-overview
  type: hard
builds-toward: []
tags:
- disk-scheduling
- seek-time
- SSTF
- SCAN
- C-SCAN
- rotational-latency
stage: formal-systems
status: validated
---
# Disk Scheduling Algorithms

## Core Idea
Disk access time for a spinning hard disk has three components: seek time (moving the read/write head to the correct cylinder), rotational latency (waiting for the platter to rotate the target sector under the head), and transfer time (reading/writing the data). Disk scheduling algorithms order pending I/O requests to minimize total seek time. FCFS is fair but unoptimized; SSTF (Shortest Seek Time First) picks the closest pending request but may starve far requests; SCAN (the elevator algorithm) services requests in one direction then reverses; C-SCAN only services requests in one direction, returning quickly to the start, providing more uniform wait times. SSDs have no mechanical latency, making disk scheduling less critical for them.

## How It's Best Learned
Given a list of pending cylinder requests and a starting head position, calculate total head movement for FCFS, SSTF, and SCAN. Identify which algorithm is most appropriate for a high-throughput database workload.

## Common Misconceptions
- SSTF can cause starvation of requests far from the current head position if a cluster of nearby requests keeps arriving.
- These algorithms matter for HDDs; SSDs have uniform access latency so different scheduling priorities apply.

## Explainer

From your study of I/O systems, you know that the CPU communicates with storage devices through I/O requests and that disk access is orders of magnitude slower than memory access. For a spinning hard disk drive, the bottleneck is mechanical: the read/write head must physically move to the correct track (**seek time**, typically 3-15 ms), then wait for the platter to rotate the target sector underneath it (**rotational latency**, up to ~4 ms at 7200 RPM), and finally read the data (**transfer time**, usually negligible for small reads). Since seek time dominates, minimizing total head movement across a queue of pending requests is the central goal of disk scheduling.

**FCFS (First-Come, First-Served)** processes requests in arrival order. It is fair and simple but can produce wild head swings — if requests arrive for cylinders 98, 5, 120, 3, 110, the head zigzags across the entire disk. **SSTF (Shortest Seek Time First)** always picks the request closest to the current head position, much like a greedy nearest-neighbor algorithm. This dramatically reduces total seek distance but has a critical flaw: if requests keep arriving near the head's current position, distant requests starve indefinitely. A request at cylinder 2 could wait forever if the head stays busy around cylinder 100.

**SCAN** (the elevator algorithm) fixes starvation by imposing direction. The head sweeps in one direction — say, toward higher cylinder numbers — servicing all requests along the way. When it reaches the highest pending request (or the disk edge), it reverses direction and sweeps back. Every request is guaranteed to be serviced within two full sweeps. However, requests just behind the head's current position must wait for the head to travel to the end and come back, creating uneven wait times. **C-SCAN (Circular SCAN)** addresses this by only servicing requests in one direction; when the head reaches the end, it jumps back to the beginning without servicing requests on the return trip, then sweeps forward again. This provides more uniform wait times because the head always arrives "from the same direction," eliminating the bias that SCAN creates toward the middle of the disk.

It is worth noting that these algorithms were designed for the mechanical reality of spinning platters. **Solid-state drives** have no moving parts — accessing any block takes roughly the same time regardless of its logical address. For SSDs, scheduling focuses on different concerns: parallelizing requests across internal flash channels, minimizing write amplification, and managing wear leveling. Understanding disk scheduling remains important both for systems that still use HDDs (large-scale storage arrays, archival systems) and because the same algorithmic thinking — optimizing access patterns to match the physical characteristics of hardware — applies broadly to system design.
