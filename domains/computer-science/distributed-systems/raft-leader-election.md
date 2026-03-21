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

## Questions

```yaml
- question: "In a 5-server Raft cluster, two servers simultaneously time out and both become candidates in term 3. Server A receives votes from servers C and D (3 total including itself). Server B receives a vote from server E (2 total including itself). What happens?"
  type: multiple-choice
  options:
    - "Both A and B become co-leaders for term 3 and coordinate log replication jointly"
    - "Server A becomes the leader because it achieved a majority of 3 out of 5 votes"
    - "The election is invalid because two candidates competed; all servers reset to term 1 and restart"
    - "Server B becomes the leader because it sent RequestVote RPCs first"
  answer: 1
  explanation: "Server A received votes from itself, C, and D — 3 votes out of 5, which is a strict majority. In Raft, a candidate becomes leader as soon as it receives votes from a majority of all servers (not just those that responded). Server A immediately begins sending heartbeats to suppress further elections. Server B, having received only 2 votes, never achieves a majority and does not become leader. If neither candidate had achieved a majority (a split vote), both would wait out their randomized timeouts and start fresh elections in term 4."

- question: "Why does Raft use randomized election timeouts rather than a fixed, uniform timeout for all servers?"
  type: multiple-choice
  options:
    - "To ensure the fastest server always wins, since a healthy server times out and campaigns before slower ones"
    - "To stagger election starts probabilistically, making it likely one server campaigns and wins before others even begin"
    - "To implement exponential backoff so that frequent elections become progressively slower and less disruptive"
    - "To allow the current leader to use a shorter timeout, giving it priority in re-election campaigns"
  answer: 1
  explanation: "Randomized timeouts solve the split vote problem: if all servers had the same timeout, they would all time out simultaneously after a leader failure, all become candidates simultaneously, all split the available votes, and elections would repeatedly fail. By having each server pick a random timeout from a range (typically 150–300ms), it becomes likely that one server times out first, starts its election, and collects votes from other servers before they even begin campaigning. This probabilistic approach provides liveness without complex coordination machinery."

- question: "When a Raft server receives any message with a term number higher than its own current term, it must immediately revert to follower state, even if it is currently acting as leader."
  type: true-false
  answer: true
  explanation: "Term numbers in Raft function as protocol-wide fencing tokens. If a server receives a message with a higher term, it knows a new election has already occurred and a new term has begun — its own leadership is stale. Continuing to act as leader for an outdated term risks split-brain: two nodes behaving as leaders and potentially accepting conflicting log entries. By immediately stepping down and adopting the new term, the old leader prevents this conflict. This property ensures Raft's safety guarantee that at most one leader exists per term."

- question: "It is possible for two different servers to simultaneously be leaders in the same term in Raft, if the network partitions exactly when a new election begins."
  type: true-false
  answer: false
  explanation: "Raft's majority voting guarantee prevents two leaders in the same term. To become leader, a candidate must receive votes from a majority of all servers. Because any two majorities must overlap by at least one server, and each server votes at most once per term, no term can have two candidates who both achieved a majority — they would need to share a voter, but that voter cast at most one vote. A network partition may create a minority partition that is leaderless, while the majority partition elects a new leader in a higher term — but these are different terms, never the same one."

- question: "Why does Raft's voting restriction — only vote for a candidate whose log is at least as up-to-date as your own — guarantee that committed log entries are never lost when a new leader is elected?"
  type: short-answer
  answer: "A log entry is committed in Raft only after it has been replicated to a majority of servers. When a new leader is elected, it must also receive votes from a majority of servers. Any two majorities must share at least one server, so the newly elected leader necessarily received a vote from at least one server that holds every committed entry. The voting restriction ensures the winner's log is at least as up-to-date as this shared voter — meaning the new leader's log must already contain all committed entries. No explicit log transfer is needed during the election; the committed history is guaranteed to be present in the winner's log as a consequence of the quorum intersection."
  explanation: "This is a quorum intersection argument: any two sets of servers each containing a majority must share at least one member. Raft exploits this to guarantee that leadership transitions preserve all committed state through the voting process itself. The restriction rules out candidates with stale logs, ensuring the winner carries all committed history forward."
```

## Explainer

From your study of the Raft algorithm, you know that Raft divides consensus into three subproblems: leader election, log replication, and safety. Leader election is the mechanism that bootstraps the entire protocol — without a leader, no new log entries can be committed, so the system stalls. Understanding how Raft elects a leader and guarantees exactly one leader per **term** is essential to understanding why the protocol works.

Raft organizes time into **terms**, which are consecutive integers that act like logical clocks. Each term begins with an election. Every server starts as a **follower**, passively waiting for heartbeat messages from the current leader. If a follower does not hear from a leader within a randomized **election timeout** (typically 150–300ms), it assumes the leader has failed, increments its term number, transitions to **candidate** state, and votes for itself. It then sends RequestVote RPCs to all other servers. A server grants its vote to the first candidate it hears from in a given term, and it votes at most once per term. If a candidate receives votes from a majority of servers, it becomes the leader for that term and immediately begins sending heartbeats to suppress new elections.

The randomized timeout is a deceptively simple but crucial design choice. Without it, multiple followers might time out simultaneously, all become candidates, split the vote, and no one wins — a situation called a **split vote**. Raft handles this by having each server pick a random timeout from a range, making it likely that one server times out first and wins before others even start campaigning. If a split vote does occur, all candidates time out again with new random intervals, and a fresh election begins in the next term. In practice, elections resolve within a few hundred milliseconds.

Two safety properties make the election mechanism sound. First, the **term number** acts as a protocol-wide fencing token: if a server receives a message with a higher term than its own, it immediately steps down to follower and updates its term. This means a stale leader from a previous term cannot continue acting as leader once a new term begins — its messages are rejected. Second, the **voting restriction** ensures that a candidate can only win if its log is at least as up-to-date as a majority of servers. This prevents a server with a stale log from becoming leader and overwriting committed entries. Together, these properties guarantee that Raft never has two leaders in the same term and that leader transitions never lose committed data.

Compared to Paxos, where leader election is often left as an implementation detail and multiple proposers can compete indefinitely, Raft's term-based election is explicit and easy to reason about. Each term has at most one leader, terms only increase, and the randomized timeout provides probabilistic liveness without complex protocol machinery. This clarity is why Raft has become the dominant consensus algorithm in production systems like etcd, CockroachDB, and TiKV.
