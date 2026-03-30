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
- id: paxos-algorithm
  type: soft
builds-toward:
- state-machine-replication
tags:
- raft
- consensus
- leader-based
stage: expert
status: validated
---
# Raft Consensus Algorithm

## Core Idea
Raft is a consensus algorithm prioritizing understandability over Paxos through a strong leader approach. A leader is elected via randomized timeouts, appends log entries to followers, and waits for quorum acknowledgment before committing. Followers accept entries only from the current leader and reject stale proposals, ensuring a consistent log order.

## Questions

```yaml
- question: "A Raft cluster has 5 nodes. The current leader and one follower become partitioned from the other three nodes. What happens in the partition containing three nodes?"
  type: multiple-choice
  options:
    - "The three nodes wait indefinitely for the leader to return, since they do not know it has failed"
    - "The three nodes elect a new leader from among themselves and continue processing client requests"
    - "The three nodes cannot elect a leader because they lack full information about the last committed log entry"
    - "The system halts entirely to avoid split-brain: no partition can proceed without all 5 nodes"
  answer: 1
  explanation: "Three nodes constitute a majority of a 5-node cluster. When their election timeouts expire without hearing from the leader, one becomes a candidate and wins an election by receiving votes from the other two — meeting the quorum requirement of 3 out of 5. The two-node partition cannot elect a leader (only 2 votes, need 3) and cannot commit new entries. Raft is designed so the majority partition continues operating safely while the minority stalls, preventing split-brain."

- question: "In Raft, what mechanism guarantees that a committed log entry will never be lost, even after multiple leader failures?"
  type: multiple-choice
  options:
    - "Committed entries are immediately written to durable storage on all nodes before the leader acknowledges them"
    - "The leader keeps a backup copy of all committed entries and transfers them to new leaders upon election"
    - "A candidate can only win an election if its log is at least as up-to-date as a majority of nodes, and committed entries are by definition on a majority of logs"
    - "Followers reject any leader whose log does not contain all previously committed entries"
  answer: 2
  explanation: "An entry is committed only after a majority of nodes have written it. Raft's election safety property requires a candidate to have a log at least as up-to-date as a majority of voters to win — meaning any elected leader must have all committed entries. Option A is too strong: Raft requires majority acknowledgment, not all-node acknowledgment. Option D is close but incorrect: followers accept leadership based on the log-currency comparison in the vote request, not by independently checking a list of committed entries."

- question: "In Raft, a candidate can only win an election if its log is at least as up-to-date as the logs of a majority of nodes in the cluster."
  type: true-false
  answer: true
  explanation: "This is Raft's election safety condition. When a candidate requests votes, each voter compares the candidate's last log entry (term and index) against its own. A node only votes for a candidate whose log is at least as current. Because any committed entry is on a majority of logs, and any winning candidate must receive votes from a majority, the winning candidate is guaranteed to have all committed entries — ensuring no committed entry is ever lost across leader changes."

- question: "In Raft, any node can accept client write requests and replicate them to the rest of the cluster."
  type: true-false
  answer: false
  explanation: "Raft's strong-leader design means only the current leader accepts client requests. If a client contacts a follower, the follower redirects to the leader. This constraint is fundamental to Raft's simplicity: funneling all writes through a single leader ensures data flows in one direction (leader to followers), eliminating the need for complex protocols to reconcile concurrent writes from multiple nodes."

- question: "Why do Raft nodes use randomized election timeouts instead of a single fixed timeout value shared by all nodes?"
  type: short-answer
  answer: "If all nodes had identical timeouts, they would all time out simultaneously when the leader fails, all become candidates at the same time, and split the vote — each node voting for itself with no candidate reaching a majority. Randomized timeouts ensure that, most of the time, exactly one node times out first and starts an election before others have timed out, allowing it to collect votes from nodes still in the follower state and win cleanly."
  explanation: "The randomized timeout is the key trick that makes Raft's leader election practical without a separate coordination mechanism. Split votes can still occur occasionally (if two nodes time out nearly simultaneously), but Raft handles this by incrementing the term and starting a new election after another randomized timeout — with high probability, one candidate wins quickly."
```

## Explainer

From your study of the consensus problem, you know the fundamental challenge: getting a group of machines to agree on a sequence of values even when some machines crash. Paxos solved this decades ago, but its specification is notoriously difficult to implement correctly. **Raft** was designed to solve the same problem with a structure that maps cleanly onto how engineers actually think about systems. It decomposes consensus into three relatively independent subproblems: leader election, log replication, and safety.

Every Raft node is in one of three states: **follower**, **candidate**, or **leader**. Normally, one node is the leader and all others are followers. The leader handles all client requests and tells followers what to write. If a follower stops hearing from the leader (its election timeout expires), it becomes a candidate and starts an election. It increments its **term number** — a logical clock that increases monotonically — votes for itself, and asks other nodes to vote. Each node votes for at most one candidate per term, and the first candidate to receive votes from a majority becomes the new leader. The randomized timeout is the key trick: because each node's timeout is slightly different, usually only one node times out first, preventing most split votes.

Once elected, the leader accepts client requests, appends each as a new entry in its **log**, and sends the entry to all followers. When a majority of nodes have written the entry to their logs and acknowledged it, the leader **commits** the entry and applies it to its state machine. The leader then notifies followers of the commit. If a follower's log falls behind — say it was temporarily disconnected — the leader detects the gap and sends the missing entries. The critical safety property is that if an entry is committed, it will appear in the logs of all future leaders. Raft enforces this by requiring that a candidate can only win an election if its log is at least as up-to-date as a majority of nodes, which guarantees that no committed entry is ever lost.

What makes Raft practical is that its strong-leader design simplifies reasoning about the system. Data flows in only one direction: from leader to followers. There is at most one leader per term. A follower that receives a request from a leader with a stale (lower) term number rejects it. These constraints mean that to understand the system's behavior, you mostly need to understand what the leader does. Real systems like etcd (the coordination backbone of Kubernetes), CockroachDB, and Consul all use Raft or Raft variants, because the algorithm's clarity translates directly into implementations that engineers can audit, debug, and extend with confidence.
