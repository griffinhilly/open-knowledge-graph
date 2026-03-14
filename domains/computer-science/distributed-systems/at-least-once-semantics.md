---
id: at-least-once-semantics
title: At-Least-Once Delivery Semantics
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-systems-overview
  type: hard
builds-toward:
- exactly-once-semantics
- distributed-transactions-2pc
tags:
- semantics
- delivery
- correctness
stage: advanced
status: draft
---

# At-Least-Once Delivery Semantics

## Core Idea
At-least-once semantics guarantee delivery one or more times through retries until acknowledgment. This prevents message loss but allows duplication. It sits between at-most-once and exactly-once. Applications must either be idempotent or handle duplicates explicitly. It is simpler than exactly-once but stronger than at-most-once.
