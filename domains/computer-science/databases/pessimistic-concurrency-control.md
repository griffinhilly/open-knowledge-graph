---
id: pessimistic-concurrency-control
title: 'Pessimistic Concurrency Control: Locking'
domain: computer-science
course: databases
prerequisites:
- id: lost-update-problem
  type: hard
tags:
- concurrency
- locking
- locks
stage: formal-systems
status: draft
---

# Pessimistic Concurrency Control: Locking

## Core Idea
Pessimistic concurrency control acquires locks on rows before reading or modifying them. Locks are held until commit, ensuring no other transaction can interfere.

## How It's Best Learned
Use SELECT...FOR UPDATE to lock rows, observe how other sessions block, and commit to release locks.

## Common Misconceptions
Locks are held until COMMIT, not after the UPDATE statement finishes. Deadlocks can occur if two transactions lock resources in different orders.
