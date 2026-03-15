---
id: three-phase-commit-protocol
title: Three-Phase Commit Protocol
domain: computer-science
course: distributed-systems
prerequisites:
- id: two-phase-commit-protocol
  type: hard
builds-toward:
- saga-pattern-distributed-transactions
tags:
- transactions
- commit
- protocol
- fault-tolerant
stage: advanced
status: draft
---

# Three-Phase Commit Protocol

## Core Idea
Three-phase commit (3PC) adds a pre-commit phase between prepare and commit: if all participants can commit, the coordinator tells them to pre-commit (releasing read locks but keeping write locks), then commit. If the coordinator fails after pre-commit, participants can safely commit themselves, avoiding indefinite blocking.
