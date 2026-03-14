---
id: dirty-read-anomaly
title: 'Dirty Read Anomaly: Reading Uncommitted Changes'
domain: computer-science
course: databases
prerequisites:
- id: isolation-level-read-uncommitted
  type: hard
tags:
- concurrency
- anomalies
- isolation-problems
stage: formal-systems
status: draft
---

# Dirty Read Anomaly: Reading Uncommitted Changes

## Core Idea
A dirty read occurs when a transaction reads data written by another uncommitted transaction. If the writing transaction rolls back, the reading transaction has consumed invalid data.
