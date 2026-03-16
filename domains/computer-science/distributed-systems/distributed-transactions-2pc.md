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

## Explainer

You already understand the consensus problem — getting distributed nodes to agree on a value — and write-ahead logging, where operations are recorded in a durable log before being applied so they can be recovered after a crash. **Two-phase commit** (2PC) combines these ideas to solve a specific problem: how do you make a transaction span multiple independent nodes and guarantee that either all of them commit or all of them abort?

Consider a money transfer between two banks, each running its own database on a separate server. You need to debit bank A and credit bank B atomically. If bank A commits the debit but bank B crashes before committing the credit, money disappears. 2PC solves this by introducing a **coordinator** that orchestrates the decision. In **Phase 1 (prepare)**, the coordinator sends a "prepare" message to each participant. Each participant checks whether it can commit (locks acquired, constraints satisfied, WAL entry written) and responds with either "yes, I can commit" or "no, I must abort." Critically, a participant that votes "yes" has made a durable promise — it has written enough to its write-ahead log that it can commit later even if it crashes and restarts.

In **Phase 2 (commit or abort)**, the coordinator collects all votes. If every participant voted yes, the coordinator writes a "commit" decision to its own log and sends "commit" to all participants. If any participant voted no, the coordinator sends "abort" to everyone. Each participant then applies or rolls back accordingly. The two-phase structure ensures that no participant commits unilaterally — everyone waits for the coordinator's final decision, and the coordinator only decides after hearing from everyone.

The fundamental weakness of 2PC is **blocking**. If the coordinator crashes after collecting votes but before broadcasting the decision, all participants that voted "yes" are stuck — they have promised to commit but do not know the outcome. They cannot safely commit (maybe another participant voted no) or abort (maybe the coordinator decided to commit). They must hold their locks and wait for the coordinator to recover, which can block other transactions indefinitely. This is why 2PC is described as a **blocking protocol**: it does not tolerate coordinator failure gracefully. Network partitions create the same problem — a participant cut off from the coordinator cannot learn the decision. Three-phase commit (3PC) adds an extra round to reduce blocking, but it still fails under network partitions. Modern distributed databases increasingly use Paxos or Raft-based commit protocols, which replicate the coordinator's state across multiple nodes so that the commit decision survives any single node failure.
