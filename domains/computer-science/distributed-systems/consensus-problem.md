---
id: consensus-problem
title: The Consensus Problem
domain: computer-science
course: distributed-systems
prerequisites:
- id: synchronous-asynchronous-systems
  type: hard
- id: failure-models-distributed
  type: hard
builds-toward:
- paxos-algorithm
- raft-algorithm
- byzantine-fault-tolerance
tags:
- consensus
- agreement
- agreement-protocols
stage: advanced
status: draft
---

# The Consensus Problem

## Core Idea
Consensus requires all non-faulty processes to decide on a single value, even when some processes fail or propose conflicting values. Consensus must satisfy: agreement (all non-faulty processes decide identically), validity (a decided value was proposed), and termination (all non-faulty processes eventually decide). This foundational problem subsumes many practical coordination challenges.
