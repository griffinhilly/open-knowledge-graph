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

## Questions

```yaml
- question: "In a two-phase commit protocol, participant P has voted 'yes' in the prepare phase. Before P receives the coordinator's commit or abort decision, the coordinator crashes. What must P do?"
  type: multiple-choice
  options:
    - "Immediately abort the transaction to release its locks and become available again"
    - "Immediately commit the transaction, since it already voted yes and promised it could commit"
    - "Block indefinitely — hold its locks and wait for the coordinator to recover before taking any action"
    - "Contact other participants to take a vote on whether to commit or abort"
  answer: 2
  explanation: "A 'yes' vote is a binding promise: P has guaranteed it can commit if asked. It cannot abort unilaterally because the coordinator might have sent 'commit' to other participants before crashing — aborting would violate atomicity if others committed. It cannot commit unilaterally because the coordinator might have decided to abort (perhaps another participant voted no). Contacting other participants does not help if they are also in the uncertain state. P must block and wait — this is the fundamental weakness of 2PC."

- question: "The coordinator in a two-phase commit logs the commit decision and begins sending commit messages. It successfully notifies two of three participants before crashing. When the coordinator recovers, what does it do?"
  type: multiple-choice
  options:
    - "Restart the entire transaction from the prepare phase because the commit was not fully delivered"
    - "Send abort messages to all participants to ensure a clean state"
    - "Re-send commit messages to complete the delivery, since the logged commit decision is authoritative"
    - "Ask participants to vote again to determine the correct outcome"
  answer: 2
  explanation: "The coordinator's log entry is the single point of truth. Once a commit record exists in the log, the transaction is committed — period. Recovery simply means re-delivering the decision to participants who haven't yet received it. This is why logging before sending is critical: the log establishes the outcome before any participant learns of it, so recovery can always reconstruct the correct decision."

- question: "Two-phase commit guarantees that a distributed transaction will complete within a bounded time, even if the coordinator crashes partway through."
  type: true-false
  answer: false
  explanation: "This is 2PC's fundamental limitation. If the coordinator crashes after participants have voted yes but before sending the commit or abort decision, those participants are in an uncertain state: they've promised to commit but don't know the outcome. They must hold their locks and block until the coordinator recovers — an indefinite wait. This blocking behavior is why 2PC is called a blocking protocol and why it is unsuitable for long-running transactions or high-availability requirements."

- question: "A participant that votes 'yes' in the prepare phase of 2PC is not permitted to unilaterally abort the transaction, even if it has been waiting for the coordinator's decision for an extended period."
  type: true-false
  answer: true
  explanation: "This constraint is essential for atomicity. A 'yes' vote is a durable commitment: the participant has logged that it can commit and promised to honor the coordinator's decision. If it were allowed to unilaterally abort after a timeout, and the coordinator had already decided to commit and notified some other participants, the transaction would be partially committed — violating atomicity. The blocking behavior is the price of this atomicity guarantee."

- question: "Explain the fundamental tradeoff that 2PC makes between atomicity and availability. What specific failure scenario exposes this tradeoff, and why can't the remaining participants resolve it on their own?"
  type: short-answer
  answer: "2PC guarantees atomicity (all participants commit or all abort) by requiring unanimous agreement before committing, and by making 'yes' votes irrevocable. The cost is availability: if the coordinator crashes after participants have voted yes but before sending the decision, participants are blocked — they cannot commit (maybe another participant voted no) or abort (they promised to commit if asked). They cannot resolve it by consulting each other because no participant knows whether others voted yes or no, and even if all voted yes, no one knows whether the coordinator logged a commit or abort decision before crashing. The only safe option is to wait for the coordinator to recover and reveal its decision."
  explanation: "The key insight is that the blocking arises specifically because 2PC places the decision authority in a single coordinator and makes participant votes binding. The coordinator is the only entity that knows the complete vote tally and the final decision. In the absence of the coordinator, participants have incomplete information and must choose between violating atomicity (aborting when the coordinator might have committed) or blocking. There is no third option that preserves atomicity without availability loss."
```

## Explainer

From your study of the consensus problem, you know that getting distributed nodes to agree on a value is fundamentally difficult — the FLP impossibility result shows that no deterministic protocol can guarantee agreement in an asynchronous system with even one crash. The **two-phase commit protocol** (2PC) sidesteps this impossibility by accepting a specific tradeoff: it guarantees atomicity (all commit or all abort) but sacrifices availability when the coordinator fails. Understanding this tradeoff is the key to understanding both when 2PC is the right tool and when it is not.

The protocol has two phases, each named for what the coordinator does. In the **prepare phase**, the coordinator sends a "prepare" message to every participant. Each participant must decide whether it can commit — it acquires locks on all relevant resources, writes a prepare record to its local log (so it can recover after a crash), and responds with either "yes" (I promise I can commit if asked) or "no" (I cannot commit). A "yes" vote is a binding promise: the participant has guaranteed that it can commit no matter what happens next. This is why logging before responding is critical — if the participant crashes after voting yes, it must be able to honor that vote after recovery.

In the **commit phase**, the coordinator collects all votes. If every participant voted yes, the coordinator writes a commit record to its own log, then sends "commit" to all participants. If any participant voted no (or timed out), the coordinator writes an abort record and sends "abort." Each participant, upon receiving the decision, applies or discards the transaction and releases its locks. The coordinator's log entry is the single point of truth — once the commit record is written, the transaction is committed regardless of subsequent failures.

The vulnerability of 2PC lies in the window between a participant voting yes and receiving the coordinator's decision. During this interval, the participant has promised to commit but does not yet know the outcome. If the coordinator crashes, the participant is **blocked** — it cannot commit (because maybe another participant voted no) and it cannot abort (because it promised to commit if asked). It must hold its locks and wait for the coordinator to recover. This blocking window is the fundamental weakness of 2PC, and it is why the protocol is unsuitable for long-running transactions or environments where coordinator failure is likely. The three-phase commit protocol attempts to address this by adding an intermediate phase, though it introduces its own complexity.

Despite this limitation, 2PC remains the workhorse protocol for distributed transactions in traditional relational databases. When the coordinator is a highly available database engine and transactions last milliseconds, the blocking window is brief and the risk is manageable. The protocol is simple, well-understood, and provides true ACID atomicity across multiple resource managers — a guarantee that weaker alternatives like sagas cannot match.
