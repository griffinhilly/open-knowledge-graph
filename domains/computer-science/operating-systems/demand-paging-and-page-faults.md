---
id: demand-paging-and-page-faults
title: Demand Paging and Page Faults
domain: computer-science
course: operating-systems
prerequisites:
- id: virtual-memory-and-demand-paging
  type: hard
- id: page-replacement-algorithms
  type: soft
builds-toward:
- copy-on-write-optimization
- thrashing-and-working-set
tags:
- paging
- memory
- virtual-memory
stage: formal-systems
status: draft
---

# Demand Paging and Page Faults

## Core Idea
Demand paging loads pages into memory only when accessed, reducing memory pressure and enabling programs larger than physical RAM. A page fault occurs when accessing a page not in memory; the kernel fetches it from disk and resumes execution. Frequent page faults (thrashing) severely degrade performance and indicate excessive memory overcommitment or poor working set behavior.
