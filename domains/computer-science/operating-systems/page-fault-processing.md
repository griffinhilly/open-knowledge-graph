---
id: page-fault-processing
title: Page Fault Handling and Recovery
domain: computer-science
course: operating-systems
prerequisites:
- id: virtual-address-translation-scheme
  type: hard
- id: exception-handling-os-internals
  type: hard
builds-toward:
- working-set-model
tags:
- page-faults
- virtual-memory
- handling
stage: formal-systems
status: draft
---

# Page Fault Handling and Recovery

## Core Idea
A page fault occurs when a process accesses a non-resident page. The handler finds or allocates the page, evicts a victim if needed, performs disk I/O, updates page tables, and resumes. Replacement policy (LRU, FIFO) significantly affects performance.
