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
status: draft
---

# Paxos Algorithm: From Theory to Practice

## Core Idea
Paxos is a consensus algorithm for solving agreement in asynchronous systems with crashes. Its classical three-phase presentation is abstract; practical variants (Multi-Paxos) optimize for repeated consensus by electing a leader and pipelining proposals, reducing latency and message complexity.

## How It's Best Learned
Understand the basic protocol (prepare/promise/accept/accepted), then explore how a single leader (master) reduces messages and improves latency, and why that leader must handle failures (via re-election when it is suspected to be crashed).

## Explainer

From your study of the basic Paxos algorithm, you know the three roles — **proposers**, **acceptors**, and **learners** — and the two-phase structure of prepare/promise followed by accept/accepted. You also know this protocol is correct: no two different values can both be chosen, and progress is guaranteed as long as a majority of acceptors are reachable. But if you tried to build a real replicated system using textbook Paxos, you would immediately hit a wall. Each consensus instance requires two round-trips of messages across all participants, and every proposer must compete for proposal numbers. In a system processing thousands of requests per second, this overhead is unacceptable.

**Multi-Paxos** solves this by observing that most of the cost in basic Paxos comes from the prepare phase, which exists only to discover whether some other proposer has already gotten a value partially accepted. If a single node acts as the **stable leader**, it can run the prepare phase once and then skip it for all subsequent consensus instances, reducing each decision to a single round-trip: the leader sends accept messages, the acceptors respond, and the value is chosen. This is the key insight — a distinguished proposer eliminates contention and halves message latency in the common case.

The leader maintains a **log** of consensus instances, each corresponding to a slot in the replicated state machine's command sequence. When a client submits a request, the leader assigns it the next available slot and runs the accept phase for that slot. Because there is no competing proposer, the accept phase succeeds immediately. The leader can even **pipeline** multiple slots, sending accept messages for several pending commands without waiting for earlier ones to complete, dramatically increasing throughput.

Of course, a single leader creates a single point of failure. When the leader crashes or becomes unreachable, the remaining nodes must detect the failure (typically via heartbeat timeouts) and elect a new leader. The new leader must run the full prepare phase for any slots that might have been in progress, discovering and completing any partially accepted values before proposing new ones. This recovery process is where the full complexity of basic Paxos reasserts itself — but it happens only during leader transitions, not during normal operation. The practical art of Paxos implementation lies in making the common case fast (stable leader, pipelined accepts) while ensuring the rare case (leader failure and recovery) remains correct.

Real systems built on Multi-Paxos — such as Google's Chubby lock service and Spanner database — add further practical concerns: snapshotting the log to bound memory usage, reconfiguring the set of participants without stopping the system, and batching client requests to amortize message overhead. Each of these extensions builds on the same foundation: the basic Paxos safety guarantees are never violated, but the protocol is restructured so that the expensive phases run only when something goes wrong.
