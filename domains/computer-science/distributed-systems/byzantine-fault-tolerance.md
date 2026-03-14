---
id: byzantine-fault-tolerance
title: Byzantine Fault Tolerance and Practical BFT
domain: computer-science
course: distributed-systems
prerequisites:
- id: failure-models-distributed
  type: hard
- id: consensus-problem
  type: hard
builds-toward:
- flp-impossibility
tags:
- byzantine
- byzantine-faults
- fault-tolerance
- pbft
stage: advanced
status: draft
---

# Byzantine Fault Tolerance and Practical BFT

## Core Idea
Byzantine fault tolerance (BFT) handles nodes that fail arbitrarily, including lying to different nodes. Consensus among n nodes tolerating f Byzantine failures requires n > 3f. Practical BFT (PBFT) uses a primary and backups, with request phases (pre-prepare, prepare, commit) coordinated by the primary; backups ensure agreement before committing.
