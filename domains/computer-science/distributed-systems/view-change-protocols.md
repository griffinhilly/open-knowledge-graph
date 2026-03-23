---
id: view-change-protocols
title: View Change and Leader Failover Protocols
domain: computer-science
course: distributed-systems
prerequisites:
- id: consensus-problem
  type: hard
- id: state-machine-replication
  type: soft
builds-toward:
  - paxos-made-practical
tags:
- failover
- leader-change
- consistency
- protocol
stage: advanced
status: validated
---
# View Change and Leader Failover Protocols

## Core Idea
View change protocols coordinate the transition when a leader fails: they elect a new leader, ensure the new leader learns all prior committed operations, and prevent split-brain (two leaders). Correctness requires all non-faulty replicas to move to the new view in a coordinated manner.

## Questions

```yaml
- question: "In a distributed system using a view change protocol, the old leader committed operation C in log slot 7 and received majority acknowledgments — but crashed before broadcasting the commit notice to all replicas. A new leader is elected. What must the new leader do before accepting any new client requests?"
  type: multiple-choice
  options:
    - "Start with an empty log and rebuild state from client re-requests to avoid inheriting potentially corrupt state"
    - "Collect log state from a quorum of replicas to reconstruct what was committed (and in-progress) during the previous view, then bring all replicas to a consistent state"
    - "Trust its own local log as definitive, since it was elected leader by a majority"
    - "Ask each client to re-submit their requests so the new leader can decide which ones to commit"
  answer: 1
  explanation: "The new leader being elected by a majority does NOT mean its log is complete. The old leader could have committed operations that the new leader's replica never heard about — exactly the scenario in this question. By collecting state from a quorum (majority) of replicas, the new leader is guaranteed to find evidence of any committed operation: if C was committed (majority acknowledged it), then at least one member of any quorum saw it. Only after reconstructing committed history and advancing all replicas to match can the new leader safely begin serving new requests without losing committed work."

- question: "What is 'split-brain' in the context of view change protocols, and why is it the critical safety failure the protocol must prevent?"
  type: multiple-choice
  options:
    - "A situation where two nodes simultaneously believe they are the active leader for the same view, potentially issuing conflicting commands and corrupting the replicated log"
    - "A network partition that splits replicas into two groups that cannot communicate with each other"
    - "A scenario where the leader's log splits into two conflicting branches during rapid writes"
    - "A race condition where two clients submit conflicting commands at the same time"
  answer: 0
  explanation: "Split-brain is the safety violation where multiple nodes believe they are the authoritative leader simultaneously. If both issue commands, the replicated state machine receives different command streams on different replicas, violating the consistency invariant that all non-faulty replicas execute the same sequence of operations in the same order. View numbers prevent this: the protocol ensures at most one node can win leadership for any given view number. When replicas detect a suspected leader failure and initiate a view change, they refuse to acknowledge commands from the old leader's view number, causing it to become a no-op even if it is still running."

- question: "A replica that holds the longest log among all candidates is always the safest choice for the new leader, since its log is most up-to-date and no committed operations can be missing."
  type: true-false
  answer: false
  explanation: "Log length alone is an insufficient criterion for leader selection. A long log might contain uncommitted proposals that were never acknowledged by a majority — the former leader could have appended entries optimistically that were never replicated. Conversely, a committed operation might exist on a different replica that has a shorter total log length. View change protocols address this by requiring the new leader to collect and reconcile state from a quorum, not by simply picking the replica with the most entries. Raft's election rules use term numbers and log index together, and Paxos uses ballot numbers to reason about which proposals might have been committed."

- question: "View numbers in view change protocols are monotonically increasing, meaning the system always transitions to a higher-numbered view and can never revert to a previous leader."
  type: true-false
  answer: true
  explanation: "Monotonically increasing view numbers are essential for preventing split-brain. If a replica receives a message from a leader claiming a lower view number than its current view, it rejects the message — the old leader has been superseded and its commands are invalid. This ensures that once a view change succeeds and replicas have moved to view N+1, the old leader in view N cannot interfere even if it recovers and believes itself still active. The monotonic property is also what allows liveness: if the new leader also fails, view N+2 is triggered, and so on, making progress as long as a majority of nodes are eventually reachable."

- question: "Why is ensuring the new leader learns all previously committed operations the hardest challenge in a view change, and how does collecting state from a quorum address it?"
  type: short-answer
  answer: "The challenge is that 'committed' is distributed knowledge: an operation is committed when a majority acknowledged it, but no single node may have received the leader's final commit broadcast before it crashed. The new leader therefore cannot determine what was committed just by inspecting its own log. Collecting state from a quorum solves this because any committed operation must have been acknowledged by a majority — and any majority overlaps with any quorum by at least one node. So the new leader's survey of a quorum is guaranteed to include at least one replica that holds evidence of every committed operation, allowing full reconstruction before new work begins."
  explanation: "This question targets the deepest insight about why view changes are where consistency bugs hide. The steady-state leader path is simple — but leader transitions require reasoning about distributed state that no single node fully holds. The quorum intersection property (any two majorities share at least one member) is the mathematical guarantee that makes reconstruction possible and safe."
```

## Explainer

From your study of consensus and state machine replication, you know that replicated systems typically rely on a **leader** to coordinate operations. The leader proposes commands, drives consensus, and tells replicas what to execute next. This works well — until the leader crashes or becomes unreachable. When that happens, the system stalls unless there is a mechanism to replace the failed leader safely. That mechanism is the **view change protocol**.

A **view** is essentially a numbered configuration that names who the current leader is. View 1 might have node A as leader; view 2 might have node B. The view number is monotonically increasing, so the system always moves forward — there is no going back to a previous view. When replicas suspect the leader has failed (typically through a timeout — they stop hearing heartbeats), they initiate a view change by proposing to move to the next view with a new leader. The critical insight is that this transition must be **coordinated**: if some replicas move to view 2 while others still think they are in view 1, you risk **split-brain**, where two nodes both believe they are the leader and issue conflicting commands.

The hardest part of a view change is not electing a new leader — it is ensuring the new leader knows everything the old leader committed. Consider this scenario: the old leader in view 1 proposed command C for log slot 7 and got acknowledgments from a majority, committing C. Then it crashed before telling all replicas about the commitment. The new leader in view 2 must discover that C was committed and include it in its log, or the system loses a committed operation and violates safety. To handle this, view change protocols require the incoming leader to **collect state from a quorum of replicas** before taking over. By examining the logs and preparation messages from a majority, the new leader can reconstruct everything that was committed (and even in-progress proposals that might have been committed). Only after this reconstruction phase does the new leader begin accepting new requests.

Different protocols implement view changes with varying mechanisms — PBFT uses explicit view-change messages with prepared certificates, Raft uses term numbers with log comparison during elections, and Paxos uses ballot numbers that implicitly encode views — but they all solve the same three problems. First, **exactly one leader per view**: the protocol ensures that at most one node can win leadership for any given view number. Second, **no committed work is lost**: the new leader inherits all committed operations from previous views. Third, **liveness under failure**: if the new leader also fails, the protocol can trigger another view change to view 3, and so on, making progress as long as a majority of nodes are eventually reachable. Understanding view changes is essential because they are where correctness bugs most often hide in distributed systems — the steady-state leader path is relatively straightforward, but the edge cases during leadership transitions are where subtle violations of safety and liveness lurk.
