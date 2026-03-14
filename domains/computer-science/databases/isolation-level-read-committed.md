---
id: isolation-level-read-committed
title: 'Isolation Level: READ COMMITTED'
domain: computer-science
course: databases
prerequisites:
- id: concurrency-control-databases
  type: hard
builds-toward:
- nonrepeatable-read-anomaly
tags:
- isolation
- concurrency
- anomalies
stage: formal-systems
status: draft
---

# Isolation Level: READ COMMITTED

## Core Idea
READ COMMITTED prevents dirty reads by only reading committed data, but allows non-repeatable reads and phantom reads. It is the default level in many databases.

## How It's Best Learned
Observe how two concurrent sessions interact: the first reads data, the second modifies and commits, and the first re-reads and sees the change.
