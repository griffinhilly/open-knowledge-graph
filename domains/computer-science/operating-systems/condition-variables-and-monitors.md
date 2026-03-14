---
id: condition-variables-and-monitors
title: Condition Variables and Monitors
domain: computer-science
course: operating-systems
prerequisites:
- id: mutual-exclusion-and-locks
  type: hard
builds-toward:
- producer-consumer-classic-sync
- readers-writers-problem-synchronization
tags:
- synchronization
- condition-variables
- monitors
stage: formal-systems
status: draft
---

# Condition Variables and Monitors

## Core Idea
Condition variables allow threads to wait until a specific condition is true. Used with locks, wait() releases the lock and blocks; notify()/notifyAll() wakes waiting threads. Monitors combine locks and condition variables to simplify synchronization. Condition variables are more expressive than semaphores for complex coordination patterns.
