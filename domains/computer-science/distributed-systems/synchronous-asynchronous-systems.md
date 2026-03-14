---
id: synchronous-asynchronous-systems
title: Synchronous vs. Asynchronous Distributed Systems
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-system-models
  type: hard
builds-toward:
- failure-models-distributed
- consensus-problem
tags:
- timing
- models
- asynchrony
stage: advanced
status: draft
---

# Synchronous vs. Asynchronous Distributed Systems

## Core Idea
Synchronous systems guarantee bounded communication rounds and clock rates, enabling deterministic algorithms. Asynchronous systems provide no timing guarantees, reflecting real networks with unbounded delays. Synchrony simplifies reasoning but is unrealistic; asynchrony is realistic but makes some problems provably unsolvable.
