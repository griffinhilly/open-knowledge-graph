---
id: exactly-once-semantics
title: Exactly-Once Delivery Semantics
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-systems-overview
  type: hard
builds-toward:
- idempotent-operations
- distributed-transactions-2pc
tags:
- semantics
- delivery
- correctness
stage: advanced
status: draft
---

# Exactly-Once Delivery Semantics

## Core Idea
Exactly-once semantics guarantee that a message is delivered and processed exactly one time, neither zero nor multiple. This is the strongest correctness guarantee but requires deduplication state and coordination. It is essential for operations with side effects (charging a payment, updating a counter) where duplicates would cause data corruption.
