---
id: readers-writers-problem-synchronization
title: Readers-Writers Problem and Lock Patterns
domain: computer-science
course: operating-systems
prerequisites:
- id: condition-variables-and-monitors
  type: hard
tags:
- synchronization-patterns
- fairness
- reader-writer-locks
stage: formal-systems
status: draft
---

# Readers-Writers Problem and Lock Patterns

## Core Idea
The readers-writers problem allows multiple readers concurrently but requires exclusive access for writers. Simple solutions risk starving one group. Reader-preference solutions favor readers; writer-preference favor writers. Fair solutions prevent starvation via condition variables tracking reader/writer counts.

## Common Misconceptions
Any solution works (reader-preference starves writers; writer-preference starves readers). Readers never conflict (they do; writes require exclusive access).
