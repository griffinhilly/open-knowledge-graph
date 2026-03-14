---
id: process-states-lifecycle
title: Process States and Lifecycle
domain: computer-science
course: operating-systems
prerequisites:
- id: process-concept
  type: hard
builds-toward:
- cpu-scheduling-basics
- threads-and-concurrency
tags:
- process-states
- new
- ready
- running
- waiting
- terminated
- context-switch
stage: formal-systems
status: validated
---

# Process States and Lifecycle

## Core Idea
A process moves through a defined set of states during its lifetime: New (being created), Ready (waiting to be assigned to a CPU), Running (instructions executing), Waiting/Blocked (waiting for an event such as I/O completion), and Terminated (finished execution). The OS maintains separate queues for ready and waiting processes, and a scheduler selects which ready process runs next. Context switching — saving one process's state and loading another's — is the mechanism that allows multitasking on a single CPU core.

## How It's Best Learned
Draw the state transition diagram and trace a concrete scenario: a process does a disk read, moves to Waiting, the I/O completes, it moves to Ready, then gets scheduled to Running.

## Common Misconceptions
- A process in Waiting state is not consuming CPU; it is blocked on an event.
- Context switches have nonzero cost — they involve saving/restoring registers and potentially flushing TLB entries.
