---
id: disk-scheduling
title: Disk Scheduling Algorithms
domain: computer-science
course: operating-systems
prerequisites:
- id: io-systems-overview
  type: hard
builds-toward:
- io-management
tags:
- disk-scheduling
- seek-time
- SSTF
- SCAN
- C-SCAN
- rotational-latency
stage: formal-systems
status: draft
---

# Disk Scheduling Algorithms

## Core Idea
Disk access time for a spinning hard disk has three components: seek time (moving the read/write head to the correct cylinder), rotational latency (waiting for the platter to rotate the target sector under the head), and transfer time (reading/writing the data). Disk scheduling algorithms order pending I/O requests to minimize total seek time. FCFS is fair but unoptimized; SSTF (Shortest Seek Time First) picks the closest pending request but may starve far requests; SCAN (the elevator algorithm) services requests in one direction then reverses; C-SCAN only services requests in one direction, returning quickly to the start, providing more uniform wait times. SSDs have no mechanical latency, making disk scheduling less critical for them.

## How It's Best Learned
Given a list of pending cylinder requests and a starting head position, calculate total head movement for FCFS, SSTF, and SCAN. Identify which algorithm is most appropriate for a high-throughput database workload.

## Common Misconceptions
- SSTF can cause starvation of requests far from the current head position if a cluster of nearby requests keeps arriving.
- These algorithms matter for HDDs; SSDs have uniform access latency so different scheduling priorities apply.
