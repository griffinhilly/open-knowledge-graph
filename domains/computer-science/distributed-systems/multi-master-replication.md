---
id: multi-master-replication
title: Multi-Master Replication
domain: computer-science
course: distributed-systems
prerequisites:
- id: state-machine-replication
  type: hard
- id: consensus-problem
  type: hard
builds-toward:
- consistency-models
tags:
- replication
- topology
- writes
stage: advanced
status: draft
---

# Multi-Master Replication

## Core Idea
Multi-master replication allows writes to be accepted at any replica. All replicas must synchronize through consensus (Paxos, Raft) or eventual consistency with conflict resolution. This enables high availability and low-latency writes in geographically distributed systems but complicates consistency guarantees and conflict handling.

## Explainer

In the replication models you have studied so far — primary-backup and state machine replication — there is a clear distinction between which node accepts writes and which nodes follow. Multi-master replication removes that distinction: **every replica can accept writes independently**. Think of it like a shared document where multiple people can type at the same time in different locations, rather than one person dictating while others copy. This sounds ideal for availability and latency — a user in Tokyo writes to a Tokyo replica, a user in London writes to a London replica — but it introduces a fundamental problem you already understand from the consensus problem: what happens when two replicas accept conflicting writes at the same time?

The answer depends on the consistency model the system chooses. One approach is to run a **consensus protocol** (Paxos or Raft) on every write, so all replicas agree on a single total order of operations before any write is confirmed. This gives you strong consistency — the system behaves as if there were a single copy of the data — but it reintroduces the latency cost of cross-replica coordination, partially defeating the purpose of allowing writes everywhere. The alternative is **eventual consistency with conflict resolution**: each replica accepts writes immediately and propagates them asynchronously, with conflicts detected and resolved after the fact.

Conflict resolution is where multi-master replication gets genuinely hard. Two users might update the same row at the same time on different replicas. Common resolution strategies include **last-writer-wins** (use timestamps to pick a winner, accepting that the "loser" write is silently discarded), **merge functions** (application-specific logic that combines both writes, like a union of set elements), and **conflict-free replicated data types** (CRDTs), which are data structures mathematically designed so that concurrent operations always converge to the same state regardless of the order they are applied. Each strategy trades off simplicity, correctness, and the kinds of operations the system can support.

In practice, most multi-master systems are used when geographic distribution makes single-leader latency unacceptable — global databases like Google Spanner (which uses consensus) or CouchDB (which uses eventual consistency with conflict detection). The design choice between consensus-backed multi-master and eventually-consistent multi-master maps directly to the CAP theorem tradeoff: you can optimize for consistency or availability under network partitions, but not both. Understanding this tradeoff is the key to choosing the right replication topology for a given system.
