---
id: nonrepeatable-read-anomaly
title: Non-Repeatable Read Anomaly
domain: computer-science
course: databases
prerequisites:
- id: isolation-level-read-committed
  type: hard
tags:
- concurrency
- anomalies
- isolation-problems
stage: formal-systems
status: draft
---

# Non-Repeatable Read Anomaly

## Core Idea
A non-repeatable read occurs when a transaction reads a row, another transaction modifies it, and the first transaction re-reads the same row and sees different data.
