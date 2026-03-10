---
id: thrashing-and-working-set
title: Thrashing and the Working Set Model
domain: computer-science
course: operating-systems
prerequisites:
- id: page-replacement-algorithms
  type: hard
tags:
- thrashing
- working-set
- locality
- frame-allocation
- multiprogramming-degree
stage: formal-systems
status: draft
---

# Thrashing and the Working Set Model

## Core Idea
Thrashing occurs when a system spends more time handling page faults than executing useful work — processes constantly page in and page out, and CPU utilization collapses. The cause is over-commitment: too many processes compete for too few frames. Denning's Working Set Model addresses this by tracking the set of pages a process has referenced in the last Δ time units (the working set), which captures its locality of reference. The OS should allocate each process at least its working set size worth of frames; if the sum of working sets exceeds available frames, the OS should reduce the degree of multiprogramming (suspend processes) rather than allow thrashing.

## How It's Best Learned
Plot CPU utilization against degree of multiprogramming. Explain the knee of the curve where thrashing begins. Then compute working set sizes for a sample reference string at different window sizes.

## Common Misconceptions
- Adding more processes to a thrashing system makes it worse, not better; reducing multiprogramming is the correct response.
- The working set window Δ must be chosen carefully; too small misses the current locality, too large includes stale references.
