---
id: lost-update-problem
title: 'Lost Update Problem: Overwriting Concurrent Writes'
domain: computer-science
course: databases
prerequisites:
- id: concurrency-control-databases
  type: hard
builds-toward:
- optimistic-concurrency-control
- pessimistic-concurrency-control
tags:
- concurrency
- data-integrity
- write-conflicts
stage: formal-systems
status: draft
---

# Lost Update Problem: Overwriting Concurrent Writes

## Core Idea
A lost update occurs when two transactions read the same row, modify it independently, and write back their versions in sequence—the first write is overwritten by the second.

## How It's Best Learned
Simulate two concurrent sessions reading a balance, incrementing it, and writing it back to observe the first increment disappearing.

## Common Misconceptions
Lost updates can occur even under READ COMMITTED isolation if explicit locking is not used. Row-level locks prevent this only if the lock is held until COMMIT.
