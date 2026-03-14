---
id: optimistic-concurrency-control
title: 'Optimistic Concurrency Control: Version Numbers'
domain: computer-science
course: databases
prerequisites:
- id: lost-update-problem
  type: hard
tags:
- concurrency
- conflict-detection
- mvcc
stage: formal-systems
status: draft
---

# Optimistic Concurrency Control: Version Numbers

## Core Idea
Optimistic concurrency control avoids locks by versioning rows (timestamps or counters) and detecting conflicts at UPDATE time. If the version has changed since READ, the UPDATE is rejected.

## How It's Best Learned
Implement an UPDATE with a WHERE clause checking the current version, simulating an application-level conflict detection.

## Common Misconceptions
Optimistic control assumes conflicts are rare and works well with low contention. Under high contention, rollbacks and retries degrade performance.
