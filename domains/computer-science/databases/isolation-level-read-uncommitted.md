---
id: isolation-level-read-uncommitted
title: 'Isolation Level: READ UNCOMMITTED (Dirty Reads)'
domain: computer-science
course: databases
prerequisites:
- id: concurrency-control-databases
  type: hard
builds-toward:
- dirty-read-anomaly
tags:
- isolation
- concurrency
- anomalies
stage: formal-systems
status: draft
---

# Isolation Level: READ UNCOMMITTED (Dirty Reads)

## Core Idea
READ UNCOMMITTED is the lowest isolation level; it allows transactions to read uncommitted (dirty) data from other transactions, offering maximum concurrency but minimum isolation.
