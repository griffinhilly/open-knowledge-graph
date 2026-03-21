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

## Questions

```yaml
- question: "The disk head is currently at cylinder 50. Pending requests are at cylinders 2, 48, 51, 52, 53, and 99. A steady stream of new requests keeps arriving near cylinder 50. Which scheduling algorithm risks permanently delaying the request at cylinder 2?"
  type: multiple-choice
  options:
    - "FCFS, because it services requests in arrival order and may skip cylinder 2"
    - "SCAN, because the head only moves in one direction and may never reach cylinder 2"
    - "SSTF, because it always picks the closest pending request and nearby requests will keep arriving"
    - "C-SCAN, because it only services requests on the forward sweep and ignores cylinder 2 on the return"
  answer: 2
  explanation: "SSTF (Shortest Seek Time First) greedily picks the closest pending request. If requests continually arrive near cylinder 50, the head stays busy serving those and the request at cylinder 2 waits indefinitely — this is starvation. FCFS, SCAN, and C-SCAN all guarantee eventual service: FCFS by arrival order, and SCAN/C-SCAN by servicing all requests within each sweep. SSTF's greedy optimization has no starvation prevention mechanism."

- question: "Why does C-SCAN provide more uniform wait times than SCAN for disk requests distributed across all cylinders?"
  type: multiple-choice
  options:
    - "C-SCAN services requests in both directions simultaneously, halving average wait time"
    - "C-SCAN skips the return sweep, so the head always arrives from the same end, giving every cylinder position roughly the same maximum wait"
    - "C-SCAN uses a priority queue to ensure distant requests are served before nearby ones"
    - "C-SCAN reduces seek time by jumping directly to the highest-numbered pending request first"
  answer: 1
  explanation: "SCAN creates uneven wait times because requests just behind the head's current position must wait for it to travel to the end and sweep back — that is nearly two full disk traversals. Requests near the middle of the disk get served more often because the head crosses them twice per cycle. C-SCAN fixes this by only servicing requests on the outward sweep, then jumping back to the beginning without servicing requests on the return. Every cylinder position is visited once per cycle from the same direction, making maximum wait time approximately equal across positions."

- question: "SSTF always prevents request starvation because, by definition, it always moves toward some pending request."
  type: true-false
  answer: false
  explanation: "SSTF prevents the head from being idle — it always moves toward the nearest request — but this is not the same as preventing starvation. Starvation occurs when a specific request waits indefinitely, not when the head sits still. If new requests keep arriving near the head's current position, the nearest request is always one of those nearby ones, and distant requests can wait forever. Starvation requires a fairness guarantee, which SSTF lacks. SCAN and C-SCAN provide starvation freedom by sweeping the entire disk within a bounded number of passes."

- question: "Disk scheduling algorithms like SCAN and C-SCAN are largely unnecessary for solid-state drives because SSDs have no moving parts and all logical block addresses have approximately equal access latency."
  type: true-false
  answer: true
  explanation: "SCAN and C-SCAN exist to minimize mechanical seek time — the time the physical read/write head takes to move between cylinders. SSDs have no such mechanism: any flash cell can be read in roughly the same time (typically 50–100 microseconds) regardless of its logical address. This eliminates the need to reorder requests for seek minimization. SSD scheduling instead focuses on different physical realities: parallelizing requests across internal flash channels, minimizing write amplification, and managing wear leveling across flash cells."

- question: "Explain why FCFS disk scheduling can produce much greater total head movement than SSTF, even though FCFS treats all requests fairly."
  type: short-answer
  answer: "FCFS processes requests in arrival order with no regard for head position, so requests can arrive in a pattern that zigzags the head across the entire disk — e.g., 5, 190, 3, 185, 10, 180. Total head movement becomes a large fraction of the disk's cylinder range repeated for every pair of requests. SSTF instead always moves to the nearest pending request, minimizing each individual step, so total head movement is far less. Fairness (first-come order) and efficiency (minimum seek distance) are competing goals — FCFS optimizes one, SSTF optimizes the other."
  explanation: "This is the classic performance-vs-fairness tradeoff. FCFS's 'fairness' means it makes no optimization decisions at all, so adversarial arrival patterns produce worst-case seek behavior. SSTF's greedy optimization dramatically cuts seek distance but sacrifices fairness guarantees. SCAN and C-SCAN are the practical compromise: they bound head movement to at most two full disk sweeps while still servicing all requests in a predictable order."
```

## Explainer

From your study of I/O systems, you know that the CPU communicates with storage devices through I/O requests and that disk access is orders of magnitude slower than memory access. For a spinning hard disk drive, the bottleneck is mechanical: the read/write head must physically move to the correct track (**seek time**, typically 3-15 ms), then wait for the platter to rotate the target sector underneath it (**rotational latency**, up to ~4 ms at 7200 RPM), and finally read the data (**transfer time**, usually negligible for small reads). Since seek time dominates, minimizing total head movement across a queue of pending requests is the central goal of disk scheduling.

**FCFS (First-Come, First-Served)** processes requests in arrival order. It is fair and simple but can produce wild head swings — if requests arrive for cylinders 98, 5, 120, 3, 110, the head zigzags across the entire disk. **SSTF (Shortest Seek Time First)** always picks the request closest to the current head position, much like a greedy nearest-neighbor algorithm. This dramatically reduces total seek distance but has a critical flaw: if requests keep arriving near the head's current position, distant requests starve indefinitely. A request at cylinder 2 could wait forever if the head stays busy around cylinder 100.

**SCAN** (the elevator algorithm) fixes starvation by imposing direction. The head sweeps in one direction — say, toward higher cylinder numbers — servicing all requests along the way. When it reaches the highest pending request (or the disk edge), it reverses direction and sweeps back. Every request is guaranteed to be serviced within two full sweeps. However, requests just behind the head's current position must wait for the head to travel to the end and come back, creating uneven wait times. **C-SCAN (Circular SCAN)** addresses this by only servicing requests in one direction; when the head reaches the end, it jumps back to the beginning without servicing requests on the return trip, then sweeps forward again. This provides more uniform wait times because the head always arrives "from the same direction," eliminating the bias that SCAN creates toward the middle of the disk.

It is worth noting that these algorithms were designed for the mechanical reality of spinning platters. **Solid-state drives** have no moving parts — accessing any block takes roughly the same time regardless of its logical address. For SSDs, scheduling focuses on different concerns: parallelizing requests across internal flash channels, minimizing write amplification, and managing wear leveling. Understanding disk scheduling remains important both for systems that still use HDDs (large-scale storage arrays, archival systems) and because the same algorithmic thinking — optimizing access patterns to match the physical characteristics of hardware — applies broadly to system design.
