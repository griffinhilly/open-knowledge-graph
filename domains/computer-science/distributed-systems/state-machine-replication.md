---
id: state-machine-replication
title: State Machine Replication
domain: computer-science
course: distributed-systems
prerequisites:
- id: consensus-problem
  type: hard
- id: strong-consistency-models
  type: soft
builds-toward:
- primary-backup-replication
tags:
- replication
- state-machine
- fault-tolerance
stage: advanced
status: draft
---

# State Machine Replication

## Core Idea
State machine replication replicates a deterministic service by using consensus to agree on a command sequence. All replicas execute identical commands in identical order, producing identical outputs. If f replicas fail, the system survives using consensus for f < n/2. SMR achieves linearizability by having consensus order all operations.

## Explainer

You already understand the consensus problem: getting a group of nodes to agree on a single value despite failures. **State machine replication** (SMR) takes that idea and applies it repeatedly, turning consensus from a one-shot agreement into a continuous mechanism for keeping multiple copies of a service perfectly synchronized.

The core principle is deceptively simple. A **deterministic state machine** is any system where, given the same starting state and the same sequence of inputs, you always get the same ending state and outputs. A key-value store is a good example: if you start with an empty store and apply "SET x=1" then "SET y=2" then "DELETE x," every copy that processes those commands in that exact order will end up in the same state — just {y: 2}. SMR exploits this by running the same state machine on multiple nodes and using consensus to ensure every node processes the same commands in the same order. If the state machine is deterministic and the input sequence is identical, the replicas are guaranteed to stay in lockstep.

In practice, SMR works by assigning each client request a **log position** (slot number) through consensus. A client sends a request — say, "SET x=5" — to the system. The replicas run a consensus protocol (like Paxos or Raft) to agree that this request occupies slot 47 in the shared log. Once consensus is reached, every replica executes the command at slot 47 and moves on to slot 48. The log is the single source of truth for ordering. Even if messages arrive at different replicas in different orders, consensus ensures they all agree on what goes in each slot. This is why the consensus prerequisite is essential — without it, you cannot build the ordered log that SMR depends on.

The fault tolerance guarantee follows directly. If you have **2f + 1** replicas, up to **f** can crash and the system continues operating. The surviving f + 1 nodes still form a majority, so consensus can still make progress. When a crashed replica recovers, it simply replays the log from where it left off, reapplying each command in order until it catches up with the others. Because the state machine is deterministic, replay produces the exact same state as if the replica had never crashed. This combination — consensus for ordering, determinism for consistency, and log replay for recovery — is what makes SMR the foundational technique behind virtually every strongly consistent replicated system, from replicated databases to distributed lock services like Chubby and ZooKeeper.
