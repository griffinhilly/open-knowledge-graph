---
id: paxos-made-practical
title: 'Paxos Algorithm: From Theory to Practice'
domain: computer-science
course: distributed-systems
prerequisites:
- id: paxos-algorithm
  type: hard
- id: state-machine-replication
  type: soft
builds-toward:
- byzantine-agreement-algorithms
tags:
- paxos
- consensus
- algorithm
- replication
stage: advanced
status: validated
---

# Paxos Algorithm: From Theory to Practice

## Core Idea
Paxos is a consensus algorithm for solving agreement in asynchronous systems with crashes. Its classical three-phase presentation is abstract; practical variants (Multi-Paxos) optimize for repeated consensus by electing a leader and pipelining proposals, reducing latency and message complexity.

## How It's Best Learned
Understand the basic protocol (prepare/promise/accept/accepted), then explore how a single leader (master) reduces messages and improves latency, and why that leader must handle failures (via re-election when it is suspected to be crashed).

## Questions

```yaml
- question: "Why can a stable Multi-Paxos leader skip the prepare phase for most consensus slots, while basic Paxos requires it every time?"
  type: multiple-choice
  options:
    - "The leader skips prepare because it has already established the highest proposal number in the system; no other proposer can win"
    - "The prepare phase exists to discover whether any other proposer has partially accepted a value; a stable single leader eliminates competing proposers, making this discovery unnecessary in the common case"
    - "Multi-Paxos bypasses prepare because the leader uses a replicated log that automatically sequences proposals"
    - "The leader skips prepare because acceptors remember the leader's identity and automatically reject other proposers"
  answer: 1
  explanation: "The prepare phase serves one purpose in basic Paxos: learning whether any value has been partially accepted by a majority, so the proposer doesn't overwrite a potentially chosen value. When there is a stable leader with no competing proposers, no other value can have been partially accepted — only the leader has been sending accept messages. Therefore the leader already knows the state of every slot and can safely skip prepare, sending accept messages directly. This reduces each consensus decision from two round-trips to one. Option A partially captures it but misstates the mechanism — it's the absence of competitors that makes prepare redundant, not a number comparison."

- question: "A Multi-Paxos leader crashes midway through processing client requests. Several consensus slots were in progress when it failed. The new leader must:"
  type: multiple-choice
  options:
    - "Start fresh from the first uncommitted slot, since crashed-leader state cannot be trusted"
    - "Run the full prepare phase for all potentially in-progress slots to discover and complete any partially accepted values before proposing new commands"
    - "Ask a majority of acceptors to roll back their accepted values and then resume from the last committed slot"
    - "Wait until the crashed leader recovers to determine which slots were committed, then take over from that point"
  answer: 1
  explanation: "This is where the full power of basic Paxos reasserts itself during recovery. The new leader does not know which slots the old leader completed before crashing. It must run a prepare phase for each uncertain slot to ask acceptors 'was anything accepted here?' If acceptors return a value, the new leader must complete that slot with the discovered value (it cannot override it — Paxos's safety guarantee requires this). Only after completing all uncertain slots can the new leader safely begin proposing new commands. Rolling back accepted values (option C) would violate safety. Waiting for the old leader (option D) is impractical and defeats the purpose of leader election."

- question: "In Multi-Paxos, a new leader must run the full prepare/promise phase when taking over from a failed leader, even though the stable leader skips this phase during normal operation."
  type: true-false
  answer: true
  explanation: "This is the fundamental design tension in Multi-Paxos: the optimization (skipping prepare) is only safe when you know no other proposer has been active. A new leader cannot assume this — the old leader may have partially accepted values that must be discovered and completed. The prepare phase is the mechanism for this discovery. The practical art of Multi-Paxos implementation is making normal operation fast (one round-trip) while keeping leader transitions safe (full two-phase recovery)."

- question: "In Multi-Paxos, the stable leader eliminates the prepare phase permanently; once a leader is elected, prepare messages are never sent again."
  type: true-false
  answer: false
  explanation: "The leader only skips the prepare phase during *normal operation* — when it is stable and there are no competing proposers. Prepare messages re-appear in two situations: (1) when a new leader is elected after failure, it must run prepare for all in-progress slots to ensure safety, and (2) if any node suspects the current leader has failed and attempts to become the new leader, it also runs prepare. The optimization is conditional, not permanent."

- question: "What problem does the single stable leader solve in Multi-Paxos, and what new problem does this leader-centric approach create?"
  type: short-answer
  answer: "The stable leader solves message complexity and latency: by eliminating contention between proposers, it allows the prepare phase to be skipped for each slot, reducing consensus from two round-trips to one, and enabling pipelining of multiple slots simultaneously. The new problem is that the leader becomes a single point of failure. When the leader crashes or becomes unreachable, the system must detect the failure (via timeout), elect a new leader, and run the full prepare phase for all in-progress slots before resuming. This recovery process reintroduces the full two-phase complexity but — critically — only during transitions, not in the common case."
  explanation: "This tradeoff is central to understanding all practical consensus systems. Pure multi-proposer Paxos is theoretically clean but practically unusable at scale due to message overhead and potential livelock from competing proposers. Multi-Paxos's leader-based design makes the common path fast, accepting the cost of a recovery protocol during the rare failure path. Systems like Raft make this leader model even more explicit and make the recovery rules easier to reason about, which is why Raft became the preferred consensus algorithm for many new distributed systems despite Paxos's historical primacy."
```

## Explainer

From your study of the basic Paxos algorithm, you know the three roles — **proposers**, **acceptors**, and **learners** — and the two-phase structure of prepare/promise followed by accept/accepted. You also know this protocol is correct: no two different values can both be chosen, and progress is guaranteed as long as a majority of acceptors are reachable. But if you tried to build a real replicated system using textbook Paxos, you would immediately hit a wall. Each consensus instance requires two round-trips of messages across all participants, and every proposer must compete for proposal numbers. In a system processing thousands of requests per second, this overhead is unacceptable.

**Multi-Paxos** solves this by observing that most of the cost in basic Paxos comes from the prepare phase, which exists only to discover whether some other proposer has already gotten a value partially accepted. If a single node acts as the **stable leader**, it can run the prepare phase once and then skip it for all subsequent consensus instances, reducing each decision to a single round-trip: the leader sends accept messages, the acceptors respond, and the value is chosen. This is the key insight — a distinguished proposer eliminates contention and halves message latency in the common case.

The leader maintains a **log** of consensus instances, each corresponding to a slot in the replicated state machine's command sequence. When a client submits a request, the leader assigns it the next available slot and runs the accept phase for that slot. Because there is no competing proposer, the accept phase succeeds immediately. The leader can even **pipeline** multiple slots, sending accept messages for several pending commands without waiting for earlier ones to complete, dramatically increasing throughput.

Of course, a single leader creates a single point of failure. When the leader crashes or becomes unreachable, the remaining nodes must detect the failure (typically via heartbeat timeouts) and elect a new leader. The new leader must run the full prepare phase for any slots that might have been in progress, discovering and completing any partially accepted values before proposing new ones. This recovery process is where the full complexity of basic Paxos reasserts itself — but it happens only during leader transitions, not during normal operation. The practical art of Paxos implementation lies in making the common case fast (stable leader, pipelined accepts) while ensuring the rare case (leader failure and recovery) remains correct.

Real systems built on Multi-Paxos — such as Google's Chubby lock service and Spanner database — add further practical concerns: snapshotting the log to bound memory usage, reconfiguring the set of participants without stopping the system, and batching client requests to amortize message overhead. Each of these extensions builds on the same foundation: the basic Paxos safety guarantees are never violated, but the protocol is restructured so that the expensive phases run only when something goes wrong.
