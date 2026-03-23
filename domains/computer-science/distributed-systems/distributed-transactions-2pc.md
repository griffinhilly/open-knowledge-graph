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
status: validated
---

# Distributed Transactions and Two-Phase Commit

## Core Idea
Two-phase commit (2PC) is a protocol for atomically executing operations across multiple nodes. Phase 1 (prepare): a coordinator asks all participants if they can commit; Phase 2 (commit/abort): the coordinator tells all to apply or roll back. 2PC blocks until consensus, so it is slow and doesn't tolerate partition faults. Modern systems prefer Paxos or Raft-based consensus.

## Questions

```yaml
- question: "In a 2PC transaction, all participants vote 'yes' in Phase 1, and the coordinator writes the commit decision to its log. Before it can send commit messages, the coordinator crashes. What happens to the participants?"
  type: multiple-choice
  options:
    - "The participants time out and safely abort, since no commit message arrived"
    - "The participants time out and safely commit, since they all voted yes"
    - "The participants are blocked indefinitely — they cannot safely commit or abort without the coordinator's decision"
    - "A new coordinator is automatically elected among the participants, who then complete the commit"
  answer: 2
  explanation: "This is the blocking problem at the heart of 2PC. A participant that voted 'yes' has made a durable promise to commit — it cannot unilaterally abort, because the coordinator may have already decided to commit (and one or more other participants may have already received and applied the commit). It also cannot safely commit, because perhaps the coordinator actually crashed before writing its decision and the outcome was abort. The participant must hold its locks and wait for the coordinator to recover. The 'time out and abort' option sounds reasonable but is incorrect: aborting unilaterally risks inconsistency if any other participant already committed."

- question: "Why can't a participant that has voted 'yes' in Phase 1 safely abort the transaction after a coordinator timeout, even if it would release its locks and unblock other transactions?"
  type: multiple-choice
  options:
    - "Because the participant hasn't written anything to disk yet, so rolling back has no effect"
    - "Because the coordinator might have already sent a 'commit' message that some participants received and applied, making a unilateral abort inconsistent"
    - "Because 2PC requires unanimous agreement to abort, and the other participants may not agree"
    - "Because aborting is more expensive than committing in terms of log writes"
  answer: 1
  explanation: "The atomicity guarantee of 2PC requires that all participants commit or all abort. Once a participant votes 'yes,' it has promised to commit if the coordinator decides to. If the coordinator decided 'commit' and sent commit messages before crashing, some participants may have already applied the transaction. If the timed-out participant unilaterally aborts, its state diverges — the transaction would be committed on some nodes and aborted on others, violating atomicity. The 'yes' vote is an irrevocable commitment to go along with whatever the coordinator decides; the participant must wait for that decision to be learned (usually when the coordinator recovers)."

- question: "In two-phase commit, if the coordinator receives at least one 'yes' vote and the remaining participants have not yet responded, it can proceed with a partial commit for the consenting participants."
  type: true-false
  answer: false
  explanation: "2PC requires unanimity: the coordinator commits only if every participant votes 'yes.' If any participant votes 'no,' or fails to respond, the coordinator sends 'abort' to all participants. Partial commits would violate atomicity — the fundamental guarantee that the transaction either fully succeeds or fully fails across all nodes. A partial commit would leave the distributed system in an inconsistent state where some nodes have applied the transaction and others have not."

- question: "A participant that votes 'yes' in Phase 1 of 2PC must hold its locks until it receives the Phase 2 commit or abort message from the coordinator."
  type: true-false
  answer: true
  explanation: "Once a participant votes 'yes,' it has durably promised to commit. To honor that promise and maintain isolation, it must continue holding any locks acquired during the transaction — it cannot release them until it knows whether to apply or roll back its changes. This is the direct cause of 2PC's blocking behavior: if the coordinator fails after Phase 1, participants are stuck holding locks indefinitely. In a busy system, this can cascade into severe contention as other transactions queue up waiting for those locks."

- question: "Explain why 2PC is called a 'blocking' protocol and describe the exact scenario in which it blocks."
  type: short-answer
  answer: "2PC is blocking because, in certain failure scenarios, participants cannot make progress — they must wait for an unavailable coordinator before they can commit or abort. The blocking scenario occurs when: (1) the coordinator crashes after all participants have voted 'yes' in Phase 1, but before the coordinator broadcasts the Phase 2 commit or abort decision. Participants that voted 'yes' cannot safely commit (the coordinator might not have decided to commit) or safely abort (the coordinator might have decided to commit and some other participant might have already applied it). They must hold their locks and wait for the coordinator to recover, potentially blocking indefinitely."
  explanation: "The blocking arises precisely at the boundary between Phase 1 and Phase 2, where participants have made an irrevocable promise but the coordinator's final decision hasn't been communicated. This is why 2PC is often described as a protocol that trades fault tolerance for atomicity: it guarantees atomicity under normal operation, but surrenders availability when the coordinator fails at the worst possible moment."
```

## Explainer

You already understand the consensus problem — getting distributed nodes to agree on a value — and write-ahead logging, where operations are recorded in a durable log before being applied so they can be recovered after a crash. **Two-phase commit** (2PC) combines these ideas to solve a specific problem: how do you make a transaction span multiple independent nodes and guarantee that either all of them commit or all of them abort?

Consider a money transfer between two banks, each running its own database on a separate server. You need to debit bank A and credit bank B atomically. If bank A commits the debit but bank B crashes before committing the credit, money disappears. 2PC solves this by introducing a **coordinator** that orchestrates the decision. In **Phase 1 (prepare)**, the coordinator sends a "prepare" message to each participant. Each participant checks whether it can commit (locks acquired, constraints satisfied, WAL entry written) and responds with either "yes, I can commit" or "no, I must abort." Critically, a participant that votes "yes" has made a durable promise — it has written enough to its write-ahead log that it can commit later even if it crashes and restarts.

In **Phase 2 (commit or abort)**, the coordinator collects all votes. If every participant voted yes, the coordinator writes a "commit" decision to its own log and sends "commit" to all participants. If any participant voted no, the coordinator sends "abort" to everyone. Each participant then applies or rolls back accordingly. The two-phase structure ensures that no participant commits unilaterally — everyone waits for the coordinator's final decision, and the coordinator only decides after hearing from everyone.

The fundamental weakness of 2PC is **blocking**. If the coordinator crashes after collecting votes but before broadcasting the decision, all participants that voted "yes" are stuck — they have promised to commit but do not know the outcome. They cannot safely commit (maybe another participant voted no) or abort (maybe the coordinator decided to commit). They must hold their locks and wait for the coordinator to recover, which can block other transactions indefinitely. This is why 2PC is described as a **blocking protocol**: it does not tolerate coordinator failure gracefully. Network partitions create the same problem — a participant cut off from the coordinator cannot learn the decision. Three-phase commit (3PC) adds an extra round to reduce blocking, but it still fails under network partitions. Modern distributed databases increasingly use Paxos or Raft-based commit protocols, which replicate the coordinator's state across multiple nodes so that the commit decision survives any single node failure.
