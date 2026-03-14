---
id: isolation-level-repeatable-read
title: 'Isolation Level: REPEATABLE READ'
domain: computer-science
course: databases
prerequisites:
- id: concurrency-control-databases
  type: hard
builds-toward:
- phantom-read-anomaly
tags:
- isolation
- concurrency
- anomalies
stage: formal-systems
status: draft
---

# Isolation Level: REPEATABLE READ

## Core Idea
REPEATABLE READ prevents dirty reads and non-repeatable reads by holding read locks for the duration of the transaction, but allows phantom reads (new rows matching a WHERE clause).

## How It's Best Learned
Demonstrate that the same query in a transaction returns the same rows, even if another session inserts new matching rows.
