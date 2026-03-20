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
status: draft
---
# View Change and Leader Failover Protocols

## Core Idea
View change protocols coordinate the transition when a leader fails: they elect a new leader, ensure the new leader learns all prior committed operations, and prevent split-brain (two leaders). Correctness requires all non-faulty replicas to move to the new view in a coordinated manner.

## Explainer

From your study of consensus and state machine replication, you know that replicated systems typically rely on a **leader** to coordinate operations. The leader proposes commands, drives consensus, and tells replicas what to execute next. This works well — until the leader crashes or becomes unreachable. When that happens, the system stalls unless there is a mechanism to replace the failed leader safely. That mechanism is the **view change protocol**.

A **view** is essentially a numbered configuration that names who the current leader is. View 1 might have node A as leader; view 2 might have node B. The view number is monotonically increasing, so the system always moves forward — there is no going back to a previous view. When replicas suspect the leader has failed (typically through a timeout — they stop hearing heartbeats), they initiate a view change by proposing to move to the next view with a new leader. The critical insight is that this transition must be **coordinated**: if some replicas move to view 2 while others still think they are in view 1, you risk **split-brain**, where two nodes both believe they are the leader and issue conflicting commands.

The hardest part of a view change is not electing a new leader — it is ensuring the new leader knows everything the old leader committed. Consider this scenario: the old leader in view 1 proposed command C for log slot 7 and got acknowledgments from a majority, committing C. Then it crashed before telling all replicas about the commitment. The new leader in view 2 must discover that C was committed and include it in its log, or the system loses a committed operation and violates safety. To handle this, view change protocols require the incoming leader to **collect state from a quorum of replicas** before taking over. By examining the logs and preparation messages from a majority, the new leader can reconstruct everything that was committed (and even in-progress proposals that might have been committed). Only after this reconstruction phase does the new leader begin accepting new requests.

Different protocols implement view changes with varying mechanisms — PBFT uses explicit view-change messages with prepared certificates, Raft uses term numbers with log comparison during elections, and Paxos uses ballot numbers that implicitly encode views — but they all solve the same three problems. First, **exactly one leader per view**: the protocol ensures that at most one node can win leadership for any given view number. Second, **no committed work is lost**: the new leader inherits all committed operations from previous views. Third, **liveness under failure**: if the new leader also fails, the protocol can trigger another view change to view 3, and so on, making progress as long as a majority of nodes are eventually reachable. Understanding view changes is essential because they are where correctness bugs most often hide in distributed systems — the steady-state leader path is relatively straightforward, but the edge cases during leadership transitions are where subtle violations of safety and liveness lurk.
