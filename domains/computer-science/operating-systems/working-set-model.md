---
id: working-set-model
title: Working Set Model and Thrashing
domain: computer-science
course: operating-systems
prerequisites:
- id: page-fault-processing
  type: hard
- id: memory-hierarchy-overview
  type: soft
tags:
- virtual-memory
- working-set
- thrashing
stage: formal-systems
status: draft
---

# Working Set Model and Thrashing

## Core Idea
The working set of a process is the pages it actively uses in a time window. Temporal and spatial locality mean programs reuse nearby pages; keeping the working set resident minimizes page faults. Thrashing occurs when working set exceeds available frames, causing excessive disk I/O and performance collapse.
