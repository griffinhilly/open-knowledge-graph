---
id: isolation-level-serializable
title: 'Isolation Level: SERIALIZABLE'
domain: computer-science
course: databases
prerequisites:
- id: concurrency-control-databases
  type: hard
tags:
- isolation
- concurrency
- strongest-level
stage: formal-systems
status: draft
---

# Isolation Level: SERIALIZABLE

## Core Idea
SERIALIZABLE is the highest isolation level; it prevents all anomalies (dirty reads, non-repeatable reads, phantom reads) by effectively serializing transactions, though at a performance cost.
