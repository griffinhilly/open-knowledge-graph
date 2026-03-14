---
id: process-states-and-transitions
title: Process States and State Transitions
domain: computer-science
course: operating-systems
prerequisites:
- id: process-creation-fork-exec
  type: hard
- id: process-termination-and-cleanup
  type: soft
builds-toward:
- context-switching-and-cpu-dispatch
- cpu-scheduling-basic-concepts
tags:
- process-lifecycle
- scheduling
- state-machine
stage: formal-systems
status: draft
---

# Process States and State Transitions

## Core Idea
Processes cycle through states: new (created), ready (waiting for CPU), running (executing), blocked (waiting for I/O or event), and terminated. State transitions are triggered by the scheduler, I/O completion, or system calls. Understanding the process state machine is fundamental to comprehending OS behavior and scheduling.
