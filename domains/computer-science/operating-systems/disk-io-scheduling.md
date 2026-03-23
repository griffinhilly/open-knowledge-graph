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
status: validated
---

# Disk I/O Scheduling Algorithms

## Core Idea
Disk I/O is slow (milliseconds vs. nanoseconds for CPU operations). I/O scheduling orders requests to minimize seek time and rotational latency. Algorithms like FCFS, SSTF (shortest seek time first), and SCAN (elevator) optimize throughput and reduce average seek time. Request batching and write caching further improve I/O performance.

## Questions

```yaml
- question: "A disk head is at track 53. Pending requests are queued for tracks: 10, 45, 65, 180, and 20. Which track does SSTF service next?"
  type: multiple-choice
  options:
    - "Track 10 — FCFS order, the first request in the queue"
    - "Track 65 — the next track in the outward direction"
    - "Track 45 — closest to the current head position"
    - "Track 180 — highest-priority because it has waited longest"
  answer: 2
  explanation: "SSTF (Shortest Seek Time First) always services the request that requires the least head movement from the current position. From track 53: |53−45| = 8, |53−65| = 12, |53−10| = 43, |53−20| = 33, |53−180| = 127. Track 45 is closest at distance 8. Option A describes FCFS (no reordering). Options B and D are not SSTF — SSTF is purely greedy on distance, not direction or arrival time."

- question: "SSTF dramatically reduces average seek time compared to FCFS. What is its primary drawback?"
  type: multiple-choice
  options:
    - "It requires storing the entire disk geometry in memory, making it impractical on most systems"
    - "Requests at tracks far from the current head may never be serviced if closer requests keep arriving — starvation"
    - "SSTF produces worse average seek time than SCAN for uniformly distributed requests"
    - "It cannot handle write requests, only reads"
  answer: 1
  explanation: "SSTF is greedy: it always jumps to the nearest pending request. If requests continuously arrive near the current head position, outer-track or inner-track requests can wait indefinitely — this is starvation. SCAN (the elevator algorithm) solves this by sweeping the full disk in one direction, guaranteeing every pending request is eventually reached. SSTF trades fairness for throughput, and the tradeoff can be severe in practice for certain workloads."

- question: "The SCAN (elevator) algorithm guarantees that every pending disk request will eventually be serviced, unlike SSTF."
  type: true-false
  answer: true
  explanation: "SCAN sweeps the head from one end of the disk to the other, servicing all requests along the way, then reverses. Because it always completes a full sweep before reversing, every request is reached within at most two full sweeps. SSTF provides no such guarantee — a request at a distant track can be indefinitely delayed if closer requests keep arriving. This is the defining fairness advantage of SCAN over SSTF."

- question: "Disk I/O scheduling algorithms like SCAN and SSTF are equally important for solid-state drives (SSDs) as for spinning hard disk drives (HDDs)."
  type: true-false
  answer: false
  explanation: "SSDs have no moving parts — there is no read/write head to move, no spinning platter to wait for. Seek time and rotational latency are effectively zero. The entire rationale for reordering disk requests (minimizing mechanical movement) disappears. I/O scheduling still exists for SSDs but focuses on different concerns (write amplification, flash cell wear, queue depth management) rather than seek time. This is a significant architectural difference that obsoletes the classical scheduling algorithms for modern storage."

- question: "Why does the order in which disk I/O requests are serviced matter so much for spinning hard drives, and why does this concern largely disappear with SSDs?"
  type: short-answer
  answer: "Spinning hard drives have a physical read/write head that must mechanically move to the correct track (seek) and then wait for the disk to rotate the target sector into position (rotational latency). Seek time alone can be 10–15 ms for a full-disk traverse — an eternity relative to CPU speeds. Servicing requests in a poor order (e.g., alternating between inner and outer tracks) wastes this mechanical time repeatedly. Intelligent reordering minimizes total head travel. SSDs use flash memory with no moving parts, so data can be accessed in any order in roughly the same time (~0.1ms) — eliminating the seek/rotation penalty entirely and making request ordering largely irrelevant."
  explanation: "This is why storage architecture is not a single static field: algorithms designed for HDDs in the 1970s–1990s do not transfer to modern SSDs. Understanding the physical substrate is essential for understanding why any I/O scheduling policy exists."
```

## Explainer

You have seen how CPU scheduling decides which process gets the processor next. Disk I/O scheduling solves an analogous problem — deciding which pending disk request to service next — but the optimization target is different. CPU scheduling optimizes for fairness and responsiveness. Disk scheduling optimizes for **minimizing mechanical movement**, because the physical geometry of a spinning disk makes the order of requests matter enormously.

A traditional hard disk has a read/write head that moves across a spinning platter. Servicing a request involves two physical delays: **seek time** (moving the head to the correct track) and **rotational latency** (waiting for the platter to spin the target sector under the head). Seek time dominates — moving the head from the innermost to outermost track can take 10–15 milliseconds, while a full rotation at 7200 RPM takes about 8 ms. If the OS processes requests in the order they arrive (**FCFS**), the head bounces wildly across the disk: track 50, then track 180, then track 12, then track 175. Each jump wastes milliseconds of seek time. With dozens of pending requests, intelligent reordering can cut total seek time by an order of magnitude.

**SSTF** (Shortest Seek Time First) always services the request closest to the current head position, much like choosing the nearest unvisited city in the traveling salesman problem. This dramatically reduces average seek time, but it has a starvation problem: if requests keep arriving near the current head position, distant requests may wait indefinitely. The **SCAN** algorithm (also called the **elevator algorithm**) fixes this by moving the head in one direction — say, from the inner tracks outward — servicing all requests along the way, then reversing direction. Just like a building elevator that goes all the way up before coming down, SCAN guarantees every pending request is eventually reached. **C-SCAN** (Circular SCAN) is a variant that only services requests in one direction and then jumps back to the beginning without servicing requests on the return trip, providing more uniform wait times.

The relevance of these algorithms has shifted with modern storage hardware. Solid-state drives (SSDs) have no moving parts, so seek time and rotational latency are zero — making I/O scheduling far less critical for SSDs. However, understanding disk scheduling remains important for three reasons. First, spinning disks are still widely used in data centers for bulk storage. Second, the same principles apply whenever request ordering affects performance — network packet scheduling, elevator control, and even database query optimization involve analogous tradeoffs between throughput, latency, and fairness. Third, the starvation and fairness problems in SSTF mirror issues you will encounter throughout systems design: greedy optimization of one metric often comes at the cost of another.
