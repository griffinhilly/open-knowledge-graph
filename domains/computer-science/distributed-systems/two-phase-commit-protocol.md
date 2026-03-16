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

## Explainer

From your study of the consensus problem, you know that getting distributed nodes to agree on a value is fundamentally difficult — the FLP impossibility result shows that no deterministic protocol can guarantee agreement in an asynchronous system with even one crash. The **two-phase commit protocol** (2PC) sidesteps this impossibility by accepting a specific tradeoff: it guarantees atomicity (all commit or all abort) but sacrifices availability when the coordinator fails. Understanding this tradeoff is the key to understanding both when 2PC is the right tool and when it is not.

The protocol has two phases, each named for what the coordinator does. In the **prepare phase**, the coordinator sends a "prepare" message to every participant. Each participant must decide whether it can commit — it acquires locks on all relevant resources, writes a prepare record to its local log (so it can recover after a crash), and responds with either "yes" (I promise I can commit if asked) or "no" (I cannot commit). A "yes" vote is a binding promise: the participant has guaranteed that it can commit no matter what happens next. This is why logging before responding is critical — if the participant crashes after voting yes, it must be able to honor that vote after recovery.

In the **commit phase**, the coordinator collects all votes. If every participant voted yes, the coordinator writes a commit record to its own log, then sends "commit" to all participants. If any participant voted no (or timed out), the coordinator writes an abort record and sends "abort." Each participant, upon receiving the decision, applies or discards the transaction and releases its locks. The coordinator's log entry is the single point of truth — once the commit record is written, the transaction is committed regardless of subsequent failures.

The vulnerability of 2PC lies in the window between a participant voting yes and receiving the coordinator's decision. During this interval, the participant has promised to commit but does not yet know the outcome. If the coordinator crashes, the participant is **blocked** — it cannot commit (because maybe another participant voted no) and it cannot abort (because it promised to commit if asked). It must hold its locks and wait for the coordinator to recover. This blocking window is the fundamental weakness of 2PC, and it is why the protocol is unsuitable for long-running transactions or environments where coordinator failure is likely. The three-phase commit protocol attempts to address this by adding an intermediate phase, though it introduces its own complexity.

Despite this limitation, 2PC remains the workhorse protocol for distributed transactions in traditional relational databases. When the coordinator is a highly available database engine and transactions last milliseconds, the blocking window is brief and the risk is manageable. The protocol is simple, well-understood, and provides true ACID atomicity across multiple resource managers — a guarantee that weaker alternatives like sagas cannot match.
