---
id: distributed-systems-introduction
title: Introduction to Distributed Systems
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-systems-overview
  type: hard
builds-toward:
- distributed-system-communication-models
- network-partition-tolerance
tags:
- fundamentals
- motivation
- challenges
stage: advanced
status: draft
---

# Introduction to Distributed Systems

## Core Idea
Distributed systems are collections of autonomous computers that communicate through networks to achieve a common goal. Unlike centralized systems, distributed systems must handle unreliable networks, independent failures, and the absence of a global clock, making reasoning about correctness significantly more difficult.

## How It's Best Learned
Start by understanding why distribution is necessary (scalability, availability, fault tolerance), then gradually work through what becomes hard (ordering, failure detection, consensus) in real systems.

## Common Misconceptions
- Distributed systems are always better than centralized ones; in fact, they add complexity and should be used only when necessary.
- All machines in a distributed system have synchronized clocks; real systems have significant clock skew.

## Questions

```yaml
- question: "Machine A sends a request to Machine B in a distributed system and receives no reply after a timeout. Which situations can A NOT distinguish between based solely on the absence of a reply?"
  type: multiple-choice
  options:
    - "B is running the correct software version vs. an outdated version"
    - "A sent the request once vs. A sent it twice"
    - "B never received the message, B received it and crashed while processing, and B processed it and replied but the reply was lost"
    - "The network is slow vs. the network is partitioned"
  answer: 2
  explanation: "A timeout is ambiguous by design — it only tells you 'no reply arrived in time,' which is consistent with at least three distinct failure modes: (1) the message was never delivered, (2) B received it and crashed mid-processing, (3) B processed it successfully and sent a reply that was lost. These have very different implications: case 3 means retrying would process the request twice, which can corrupt state (double-charging, duplicate records). This ambiguity is not an edge case — it is the fundamental communication challenge of distributed systems, motivating idempotency and exactly-once semantics in protocol design."

- question: "A software architect proposes: 'We can avoid all distributed systems complexity by using a sufficiently powerful single machine.' When does this reasoning hold, and when does it break down?"
  type: multiple-choice
  options:
    - "It never holds — all modern applications require distribution regardless of scale"
    - "It always holds — distributed systems are only used for academic research and theoretical study"
    - "It holds when the workload fits on one machine, but breaks down when scale, fault tolerance, or geographic distribution genuinely require multiple nodes"
    - "It breaks down only when the application handles more than one million users simultaneously"
  answer: 2
  explanation: "Distribution adds real complexity — unreliable networks, no global clock, partial failures. A monolith on a powerful single machine is often simpler, faster to develop, and easier to reason about. The architect's reasoning holds when a single machine is sufficient. It breaks down when requirements genuinely exceed one machine: workloads too large for one node's memory or compute, fault tolerance requirements that demand eliminating single points of failure, or geographic distribution for latency. The decision to distribute should be driven by genuine need, not fashion or premature optimization."

- question: "In a distributed system, even if all nodes are operating correctly, events on different machines cannot be reliably ordered by wall-clock timestamps alone."
  type: true-false
  answer: true
  explanation: "Each machine has its own hardware clock, and clocks drift at different rates and can be set differently. Even with NTP synchronization, clocks can disagree by milliseconds to seconds. Two machines might assign timestamps showing that event X on Machine A happened before event Y on Machine B, when the actual causal order was the reverse. This is not a technical failure — it is the fundamental absence of a global clock in distributed systems. Solving ordering requires logical clocks (Lamport timestamps) or vector clocks that track causal relationships rather than relying on physical time."

- question: "Partial failure in distributed systems — where some nodes fail while others continue — is an uncommon edge case that can be handled with standard exception handling in application code."
  type: true-false
  answer: false
  explanation: "Partial failure is the *defining* challenge of distributed systems, not an edge case. On a single machine, failure is total — the machine either works or it doesn't. In a distributed system, some nodes fail while others continue, and the surviving nodes must decide how to respond. A three-node database with one crashed node, one working, and one returning stale data cannot be handled with a try-catch block — it requires explicit protocols for consistency, replication, and fault tolerance. This is why distributed systems engineering is a distinct discipline: it is primarily the art of building reliable systems from unreliable parts."

- question: "Why is partial failure considered the most distinctive challenge of distributed systems compared to single-machine programming?"
  type: short-answer
  answer: "On a single machine, failure is binary — the machine works or it doesn't. In a distributed system, components fail independently: some nodes crash while others run correctly; some networks partition while others stay up; some nodes return stale data rather than failing cleanly. Surviving nodes must continue operating usefully despite not knowing the state of failed components, and they cannot even reliably determine whether a remote node has failed or is just slow. This uncertainty — compounded by message loss ambiguity and the absence of a global clock — is qualitatively different from any challenge in single-machine programming."
  explanation: "The key insight is that distributed failure is *partial* and *ambiguous* in ways that single-machine failure is not. A crashed thread produces an exception; a crashed remote node produces... silence, or a timeout, or a stale response. Single-machine code can trust that if a function returns a value, it ran to completion. Distributed code cannot make this assumption. Every component must be designed to tolerate the failure of components it depends on, which requires explicit choices about consistency vs. availability tradeoffs — the territory mapped by CAP theorem and related results."
```

## Explainer

From your overview of distributed systems, you have a high-level sense of what they are and why they exist. This topic sharpens that understanding by focusing on the fundamental challenges that make distributed systems qualitatively harder than single-machine systems. The core issue is deceptively simple: once your computation spans multiple machines connected by a network, you lose three things you took for granted — reliable communication, synchronized time, and the ability to observe the full system state.

**Unreliable networks** are the first challenge. Messages between machines can be delayed, reordered, duplicated, or lost entirely. When machine A sends a request to machine B and gets no response, A cannot distinguish between three very different situations: B never received the message, B received it and crashed while processing, or B processed it and replied but the response was lost. This ambiguity is not an edge case — it is the default state of networked communication, and every protocol in a distributed system must handle it explicitly. Timeouts help, but they introduce their own problems: a slow response looks identical to a lost one.

**The absence of a global clock** is the second challenge. On a single machine, events have a clear ordering — the CPU executes instructions sequentially, and the system clock provides timestamps. In a distributed system, each machine has its own clock, and those clocks drift apart. Two machines might disagree about whether event X happened before or after event Y. This makes "what happened first?" — a question that is trivial on one machine — a deep theoretical problem in distributed systems, eventually addressed by concepts like logical clocks and vector clocks.

**Partial failure** is the third and most distinctive challenge. A single machine either works or it does not — failure is total. In a distributed system, some nodes can fail while others continue operating. A three-node database might have one node crash, one node running correctly, and one node running but returning stale data due to a network partition. The system must continue providing useful service despite this partial failure, which means every component must be designed to tolerate the failure of components it depends on. This is why distributed systems engineering is largely the art of building reliable systems from unreliable parts — and why the field exists as a discipline distinct from single-machine programming.
