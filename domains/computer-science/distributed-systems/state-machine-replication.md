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
status: validated
---

# State Machine Replication

## Core Idea
State machine replication replicates a deterministic service by using consensus to agree on a command sequence. All replicas execute identical commands in identical order, producing identical outputs. If f replicas fail, the system survives using consensus for f < n/2. SMR achieves linearizability by having consensus order all operations.

## Questions

```yaml
- question: "Two clients simultaneously send 'SET x=1' and 'SET x=2' to a replicated key-value store using state machine replication. What must happen to ensure all replicas end in the same state?"
  type: multiple-choice
  options:
    - "Both commands must be rejected — concurrent writes are not allowed in SMR"
    - "Each replica independently processes whichever command arrives first, since they will eventually converge"
    - "Consensus must assign a single ordering to the two commands (e.g., slot 5: SET x=1, slot 6: SET x=2), and all replicas execute them in that order"
    - "The system picks the command from the client with the lower ID and discards the other"
  answer: 2
  explanation: "The entire point of SMR is that replicas must execute the same commands in the same order. If different replicas process the commands in different orders — replica A applies SET x=1 then SET x=2; replica B applies SET x=2 then SET x=1 — they end in different states (x=2 vs x=1 respectively). Consensus solves this by assigning a global ordering: all replicas agree that slot 5 is SET x=1 and slot 6 is SET x=2 (or whichever order is chosen), then everyone executes in that order. The specific order chosen doesn't matter; what matters is that it is the same for every replica."

- question: "A replica in an SMR system was offline for several hours due to a hardware failure. It has now recovered. How does it return to a consistent state with the other replicas?"
  type: multiple-choice
  options:
    - "It cannot recover — any replica that misses commands is permanently inconsistent and must be replaced"
    - "It requests the current state from a majority of replicas and takes the most recent snapshot"
    - "It replays the shared command log from its last executed slot, re-executing each command in order until it catches up"
    - "It waits for the next client request, which will trigger a full state synchronization"
  answer: 2
  explanation: "This is one of SMR's most elegant properties. Because the state machine is deterministic, replaying the same commands in the same order from any consistent starting state produces the same result. The recovered replica simply reads the log entries it missed and re-applies them in sequence. Because every command was already agreed upon by consensus before being written to the log, there is no ambiguity about what to execute or in what order. The determinism of the state machine guarantees that after replay, the recovered replica is in exactly the same state as the others. This is why the log is the single source of truth."

- question: "In state machine replication, each replica independently executes client requests and consensus is only invoked when replicas disagree about the result."
  type: true-false
  answer: false
  explanation: "False. This describes a reactive, after-the-fact consistency repair — not SMR. In state machine replication, consensus is used proactively and continuously to assign every command to a specific position in the shared log *before* any replica executes it. Replicas do not execute commands independently and then compare results. They first agree on what command occupies each log slot, then all execute commands in log order. This is how SMR guarantees that replicas never diverge in the first place, rather than detecting and repairing divergence after the fact."

- question: "A non-deterministic state machine — one that uses the current wall-clock time or a random number generator as part of its operation — cannot be replicated correctly using standard state machine replication."
  type: true-false
  answer: true
  explanation: "True. SMR's consistency guarantee rests entirely on determinism: given the same starting state and the same command sequence, every replica must produce the same ending state. A state machine that reads the wall-clock time or generates random numbers will produce different results on different replicas even if they execute the same commands in the same order — because the wall-clock time or random seed will differ. To replicate a non-deterministic service, you must either (a) externalize the non-determinism (agree on the random value or timestamp through consensus before executing) or (b) use a different replication strategy. Standard SMR assumes determinism as a hard prerequisite."

- question: "Why must the state machine be deterministic for state machine replication to guarantee that all replicas remain consistent?"
  type: short-answer
  answer: "State machine replication guarantees consistency by having all replicas execute the same sequence of commands, relying on determinism to ensure they reach the same state. If the state machine is deterministic, then identical inputs in identical order always produce identical outputs — no matter when or where execution happens. Consensus ensures all replicas agree on the same command sequence (the same log). Determinism then ensures that executing that sequence from the same starting state produces the same ending state on every replica. If the machine were non-deterministic, replicas could execute the same commands in the same order and still diverge — because non-deterministic choices (random values, timestamps) would differ between nodes. Consensus fixes the 'what' and 'when'; determinism fixes the 'outcome given what and when.'"
  explanation: "The key insight is that SMR is a two-part guarantee: consensus handles ordering, determinism handles outcome. Both are required. Students who understand only the consensus part may think that agreement on the command log is sufficient — but a non-deterministic state machine can produce different outputs from the same log on different nodes. The determinism requirement is not a technicality; it is the mechanism by which the ordered log translates into consistent state."
```

## Explainer

You already understand the consensus problem: getting a group of nodes to agree on a single value despite failures. **State machine replication** (SMR) takes that idea and applies it repeatedly, turning consensus from a one-shot agreement into a continuous mechanism for keeping multiple copies of a service perfectly synchronized.

The core principle is deceptively simple. A **deterministic state machine** is any system where, given the same starting state and the same sequence of inputs, you always get the same ending state and outputs. A key-value store is a good example: if you start with an empty store and apply "SET x=1" then "SET y=2" then "DELETE x," every copy that processes those commands in that exact order will end up in the same state — just {y: 2}. SMR exploits this by running the same state machine on multiple nodes and using consensus to ensure every node processes the same commands in the same order. If the state machine is deterministic and the input sequence is identical, the replicas are guaranteed to stay in lockstep.

In practice, SMR works by assigning each client request a **log position** (slot number) through consensus. A client sends a request — say, "SET x=5" — to the system. The replicas run a consensus protocol (like Paxos or Raft) to agree that this request occupies slot 47 in the shared log. Once consensus is reached, every replica executes the command at slot 47 and moves on to slot 48. The log is the single source of truth for ordering. Even if messages arrive at different replicas in different orders, consensus ensures they all agree on what goes in each slot. This is why the consensus prerequisite is essential — without it, you cannot build the ordered log that SMR depends on.

The fault tolerance guarantee follows directly. If you have **2f + 1** replicas, up to **f** can crash and the system continues operating. The surviving f + 1 nodes still form a majority, so consensus can still make progress. When a crashed replica recovers, it simply replays the log from where it left off, reapplying each command in order until it catches up with the others. Because the state machine is deterministic, replay produces the exact same state as if the replica had never crashed. This combination — consensus for ordering, determinism for consistency, and log replay for recovery — is what makes SMR the foundational technique behind virtually every strongly consistent replicated system, from replicated databases to distributed lock services like Chubby and ZooKeeper.
