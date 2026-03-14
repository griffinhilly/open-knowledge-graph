---
id: counting-semaphores-resource-pools
title: Counting Semaphores and Resource Pools
domain: computer-science
course: operating-systems
prerequisites:
- id: binary-semaphores-mutexes
  type: hard
builds-toward:
- producer-consumer-classic-sync
tags:
- semaphores
- resource-management
- synchronization
stage: formal-systems
status: draft
---

# Counting Semaphores and Resource Pools

## Core Idea
Counting semaphores have integer values (≥0) representing available resources. wait() decrements (blocks if 0); signal() increments and wakes a waiting thread. Counting semaphores express resource constraints naturally and manage pools of identical resources such as buffer slots or thread pools.

## How It's Best Learned
Use counting semaphores to implement a bounded buffer, thread pool, or resource pool manager.
