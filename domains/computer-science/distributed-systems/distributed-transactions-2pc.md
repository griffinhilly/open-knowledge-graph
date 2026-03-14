---
id: distributed-transactions-2pc
title: Distributed Transactions and Two-Phase Commit
domain: computer-science
course: distributed-systems
prerequisites:
- id: consensus-problem
  type: hard
- id: write-ahead-logging
  type: hard
tags:
- transactions
- consensus
- correctness
stage: advanced
status: draft
---

# Distributed Transactions and Two-Phase Commit

## Core Idea
Two-phase commit (2PC) is a protocol for atomically executing operations across multiple nodes. Phase 1 (prepare): a coordinator asks all participants if they can commit; Phase 2 (commit/abort): the coordinator tells all to apply or roll back. 2PC blocks until consensus, so it is slow and doesn't tolerate partition faults. Modern systems prefer Paxos or Raft-based consensus.
