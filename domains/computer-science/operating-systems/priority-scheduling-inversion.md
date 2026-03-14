---
id: priority-scheduling-inversion
title: Priority Scheduling and Priority Inversion
domain: computer-science
course: operating-systems
prerequisites:
- id: scheduling-algorithm-analysis
  type: hard
- id: mutex-and-locks
  type: hard
builds-toward:
- critical-section-problem-formalization
tags:
- priority
- scheduling
- inversion
stage: formal-systems
status: draft
---

# Priority Scheduling and Priority Inversion

## Core Idea
Priority inversion occurs when a high-priority task waits for a low-priority task holding a lock. Solutions include priority inheritance (temporarily boost lock-holder to waiter's priority) and priority ceiling (pre-set lock priority to max priority that might acquire it).
