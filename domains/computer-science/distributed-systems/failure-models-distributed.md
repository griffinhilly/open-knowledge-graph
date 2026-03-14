---
id: failure-models-distributed
title: Failure Models in Distributed Systems
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-system-models
  type: hard
builds-toward:
- byzantine-fault-tolerance
- consensus-problem
tags:
- failures
- faults
- robustness
stage: advanced
status: draft
---

# Failure Models in Distributed Systems

## Core Idea
Distributed systems must account for different failure classes: crash failures (nodes stop), omission failures (lost messages), timing failures (delays exceed bounds), and Byzantine failures (nodes act arbitrarily). More severe failure models require stronger algorithms; Byzantine systems are hardest since even faulty nodes appear responsive.
