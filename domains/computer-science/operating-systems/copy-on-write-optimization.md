---
id: copy-on-write-optimization
title: Copy-on-Write Memory Optimization
domain: computer-science
course: operating-systems
prerequisites:
- id: demand-paging-and-page-faults
  type: hard
- id: process-creation-fork-exec
  type: soft
tags:
- optimization
- paging
- fork
stage: formal-systems
status: draft
---

# Copy-on-Write Memory Optimization

## Core Idea
Copy-on-write defers copying memory pages until a process modifies them, reducing overhead when child processes immediately exec(). When fork() creates a child, both parent and child share physical pages; modification triggers a page fault and copy. CoW is essential for efficient process creation in modern operating systems and reduces memory waste.
