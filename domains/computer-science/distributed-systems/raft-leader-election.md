---
id: raft-leader-election
title: 'Raft Consensus: Leader Election'
domain: computer-science
course: distributed-systems
prerequisites:
- id: raft-algorithm
  type: hard
- id: leader-election-algorithms
  type: soft
builds-toward:
- view-change-protocols
- state-machine-replication
tags:
- raft
- leader-election
- consensus
- terms
stage: advanced
status: draft
---

# Raft Consensus: Leader Election

## Core Idea
Raft's leader election mechanism divides time into terms: in each term, a leader is elected, and if the leader fails or becomes unreachable, a new election starts in a higher term. Elections are triggered by timeouts and use voting to ensure only one leader per term, simplifying reasoning compared to Paxos.

## Explainer

From your study of the Raft algorithm, you know that Raft divides consensus into three subproblems: leader election, log replication, and safety. Leader election is the mechanism that bootstraps the entire protocol — without a leader, no new log entries can be committed, so the system stalls. Understanding how Raft elects a leader and guarantees exactly one leader per **term** is essential to understanding why the protocol works.

Raft organizes time into **terms**, which are consecutive integers that act like logical clocks. Each term begins with an election. Every server starts as a **follower**, passively waiting for heartbeat messages from the current leader. If a follower does not hear from a leader within a randomized **election timeout** (typically 150–300ms), it assumes the leader has failed, increments its term number, transitions to **candidate** state, and votes for itself. It then sends RequestVote RPCs to all other servers. A server grants its vote to the first candidate it hears from in a given term, and it votes at most once per term. If a candidate receives votes from a majority of servers, it becomes the leader for that term and immediately begins sending heartbeats to suppress new elections.

The randomized timeout is a deceptively simple but crucial design choice. Without it, multiple followers might time out simultaneously, all become candidates, split the vote, and no one wins — a situation called a **split vote**. Raft handles this by having each server pick a random timeout from a range, making it likely that one server times out first and wins before others even start campaigning. If a split vote does occur, all candidates time out again with new random intervals, and a fresh election begins in the next term. In practice, elections resolve within a few hundred milliseconds.

Two safety properties make the election mechanism sound. First, the **term number** acts as a protocol-wide fencing token: if a server receives a message with a higher term than its own, it immediately steps down to follower and updates its term. This means a stale leader from a previous term cannot continue acting as leader once a new term begins — its messages are rejected. Second, the **voting restriction** ensures that a candidate can only win if its log is at least as up-to-date as a majority of servers. This prevents a server with a stale log from becoming leader and overwriting committed entries. Together, these properties guarantee that Raft never has two leaders in the same term and that leader transitions never lose committed data.

Compared to Paxos, where leader election is often left as an implementation detail and multiple proposers can compete indefinitely, Raft's term-based election is explicit and easy to reason about. Each term has at most one leader, terms only increase, and the randomized timeout provides probabilistic liveness without complex protocol machinery. This clarity is why Raft has become the dominant consensus algorithm in production systems like etcd, CockroachDB, and TiKV.
