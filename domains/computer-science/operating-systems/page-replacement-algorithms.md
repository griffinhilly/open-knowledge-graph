---
id: page-replacement-algorithms
title: Page Replacement Algorithms
domain: computer-science
course: operating-systems
prerequisites:
- id: virtual-memory-management
  type: hard
- id: cache-replacement-policies
  type: soft
builds-toward:
- thrashing-and-working-set
tags:
- page-replacement
- FIFO
- LRU
- optimal
- clock-algorithm
- Belady-anomaly
stage: formal-systems
status: draft
---

# Page Replacement Algorithms

## Core Idea
When a page fault occurs and no free frames exist, the OS must evict a page — the page replacement algorithm chooses which one. The Optimal algorithm (OPT) evicts the page that will be used furthest in the future, minimizing page faults, but requires future knowledge so it serves only as a theoretical benchmark. FIFO evicts the oldest page but exhibits Belady's Anomaly (more frames can cause more faults). LRU (Least Recently Used) approximates OPT by evicting the page unused longest and is well-supported by the principle of temporal locality. The Clock (Second-Chance) algorithm approximates LRU efficiently using a reference bit and a circular scan, and is widely used in practice.

## How It's Best Learned
Apply each algorithm to the same reference string (e.g., 1,2,3,4,1,2,5,1,2,3,4,5) with 3 frames, counting page faults. Then verify Belady's anomaly by running FIFO with 4 frames on the same string.

## Common Misconceptions
- LRU cannot be implemented exactly in hardware because tracking the exact access order for all pages is too expensive; approximations are used.
- More physical frames always reduce page faults for LRU and OPT, but not necessarily for FIFO (Belady's Anomaly).
