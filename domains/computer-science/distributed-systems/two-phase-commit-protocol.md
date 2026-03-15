---
id: two-phase-commit-protocol
title: Two-Phase Commit Protocol
domain: computer-science
course: distributed-systems
prerequisites:
- id: consensus-problem
  type: hard
- id: replication-strategies-analysis
  type: soft
builds-toward:
- three-phase-commit-protocol
- saga-pattern-distributed-transactions
tags:
- transactions
- commit
- protocol
- coordinator
stage: advanced
status: draft
---

# Two-Phase Commit Protocol

## Core Idea
Two-phase commit (2PC) coordinates distributed transactions: in the prepare phase, a coordinator asks all participants if they can commit (they lock resources and say yes/no); in the commit phase, it tells them to commit or abort. It ensures atomicity but blocks resources during the prepare phase and becomes unavailable if the coordinator crashes during commit.

## How It's Best Learned
Trace through a successful 2PC and a failure scenario (coordinator crashes after prepare, before commit decision). Understand why participants must log before responding 'yes' and why the coordinator must log the commit decision before sending commit messages.

## Common Misconceptions
- 2PC is always safe; if the coordinator crashes, participants cannot know whether to commit and must block indefinitely.
- 2PC is obsolete; it is still used in traditional databases and remains the standard for ACID transactions.
