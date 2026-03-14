---
id: distributed-system-models
title: Models of Distributed Computation
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-systems-overview
  type: hard
builds-toward:
- synchronous-asynchronous-systems
- failure-models-distributed
tags:
- models
- computation
- theory
stage: advanced
status: draft
---

# Models of Distributed Computation

## Core Idea
Distributed computation models formalize assumptions about timing, communication, and failures. Synchronous models assume bounded message delays and clock synchronization; asynchronous models make no timing guarantees. The choice of model fundamentally affects which problems are solvable and determines which algorithms can guarantee correctness.
