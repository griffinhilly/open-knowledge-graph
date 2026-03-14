---
id: monitor-pattern-definition
title: 'Monitors: Formal Definition and Properties'
domain: computer-science
course: operating-systems
prerequisites:
- id: monitors-and-condition-variables
  type: hard
- id: semaphore-formal-definition
  type: hard
builds-toward:
- message-passing-ipc-semantics
tags:
- monitors
- synchronization
- formal
stage: formal-systems
status: draft
---

# Monitors: Formal Definition and Properties

## Core Idea
A monitor packages data and procedures into a single unit with built-in mutual exclusion; at most one procedure may execute at a time. Condition variables enable threads to wait and signal within the monitor, providing higher-level synchronization than semaphores.
