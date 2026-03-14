---
id: phantom-read-anomaly
title: 'Phantom Read Anomaly: New Rows Appearing'
domain: computer-science
course: databases
prerequisites:
- id: isolation-level-repeatable-read
  type: hard
tags:
- concurrency
- anomalies
- isolation-problems
stage: formal-systems
status: draft
---

# Phantom Read Anomaly: New Rows Appearing

## Core Idea
A phantom read occurs when a transaction executes a query twice, and between the two executions another transaction inserts rows matching the WHERE clause, causing the result set size to change.
