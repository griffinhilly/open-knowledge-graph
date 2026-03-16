---
id: raft-algorithm
title: Raft Consensus Algorithm
domain: computer-science
course: distributed-systems
prerequisites:
- id: consensus-problem
  type: hard
- id: leader-election-algorithms
  type: soft
builds-toward:
- state-machine-replication
tags:
- raft
- consensus
- leader-based
stage: advanced
status: draft
---

# Raft Consensus Algorithm

## Core Idea
Raft is a consensus algorithm prioritizing understandability over Paxos through a strong leader approach. A leader is elected via randomized timeouts, appends log entries to followers, and waits for quorum acknowledgment before committing. Followers accept entries only from the current leader and reject stale proposals, ensuring a consistent log order.

## Explainer

From your study of the consensus problem, you know the fundamental challenge: getting a group of machines to agree on a sequence of values even when some machines crash. Paxos solved this decades ago, but its specification is notoriously difficult to implement correctly. **Raft** was designed to solve the same problem with a structure that maps cleanly onto how engineers actually think about systems. It decomposes consensus into three relatively independent subproblems: leader election, log replication, and safety.

Every Raft node is in one of three states: **follower**, **candidate**, or **leader**. Normally, one node is the leader and all others are followers. The leader handles all client requests and tells followers what to write. If a follower stops hearing from the leader (its election timeout expires), it becomes a candidate and starts an election. It increments its **term number** — a logical clock that increases monotonically — votes for itself, and asks other nodes to vote. Each node votes for at most one candidate per term, and the first candidate to receive votes from a majority becomes the new leader. The randomized timeout is the key trick: because each node's timeout is slightly different, usually only one node times out first, preventing most split votes.

Once elected, the leader accepts client requests, appends each as a new entry in its **log**, and sends the entry to all followers. When a majority of nodes have written the entry to their logs and acknowledged it, the leader **commits** the entry and applies it to its state machine. The leader then notifies followers of the commit. If a follower's log falls behind — say it was temporarily disconnected — the leader detects the gap and sends the missing entries. The critical safety property is that if an entry is committed, it will appear in the logs of all future leaders. Raft enforces this by requiring that a candidate can only win an election if its log is at least as up-to-date as a majority of nodes, which guarantees that no committed entry is ever lost.

What makes Raft practical is that its strong-leader design simplifies reasoning about the system. Data flows in only one direction: from leader to followers. There is at most one leader per term. A follower that receives a request from a leader with a stale (lower) term number rejects it. These constraints mean that to understand the system's behavior, you mostly need to understand what the leader does. Real systems like etcd (the coordination backbone of Kubernetes), CockroachDB, and Consul all use Raft or Raft variants, because the algorithm's clarity translates directly into implementations that engineers can audit, debug, and extend with confidence.
