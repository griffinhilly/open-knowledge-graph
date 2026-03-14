---
id: flp-impossibility
title: FLP Impossibility Theorem
domain: computer-science
course: distributed-systems
prerequisites:
- id: consensus-problem
  type: hard
- id: synchronous-asynchronous-systems
  type: hard
builds-toward:
- raft-algorithm
- paxos-algorithm
tags:
- impossibility
- bounds
- theory
- flp
stage: advanced
status: draft
---

# FLP Impossibility Theorem

## Core Idea
The FLP impossibility theorem proves that in asynchronous systems with even one crash failure, no algorithm can guarantee both safety (never violate agreement) and liveness (all processes terminate) for consensus. This foundational result shows that real systems must assume synchrony, use randomization, or sacrifice liveness (e.g., timeouts) to solve consensus.
