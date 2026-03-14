---
id: at-most-once-semantics
title: At-Most-Once Delivery Semantics
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

# At-Most-Once Delivery Semantics

## Core Idea
At-most-once semantics guarantee zero or one delivery, never more. This is the weakest guarantee: senders do not retry, so messages may be lost. Implementation is simple and low-overhead. This semantic is acceptable for fire-and-forget operations like metrics or logs where occasional loss does not compromise correctness.
