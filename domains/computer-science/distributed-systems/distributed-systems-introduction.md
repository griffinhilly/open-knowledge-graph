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
stage: abstract-reasoning
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

## Explainer

From your overview of distributed systems, you have a high-level sense of what they are and why they exist. This topic sharpens that understanding by focusing on the fundamental challenges that make distributed systems qualitatively harder than single-machine systems. The core issue is deceptively simple: once your computation spans multiple machines connected by a network, you lose three things you took for granted — reliable communication, synchronized time, and the ability to observe the full system state.

**Unreliable networks** are the first challenge. Messages between machines can be delayed, reordered, duplicated, or lost entirely. When machine A sends a request to machine B and gets no response, A cannot distinguish between three very different situations: B never received the message, B received it and crashed while processing, or B processed it and replied but the response was lost. This ambiguity is not an edge case — it is the default state of networked communication, and every protocol in a distributed system must handle it explicitly. Timeouts help, but they introduce their own problems: a slow response looks identical to a lost one.

**The absence of a global clock** is the second challenge. On a single machine, events have a clear ordering — the CPU executes instructions sequentially, and the system clock provides timestamps. In a distributed system, each machine has its own clock, and those clocks drift apart. Two machines might disagree about whether event X happened before or after event Y. This makes "what happened first?" — a question that is trivial on one machine — a deep theoretical problem in distributed systems, eventually addressed by concepts like logical clocks and vector clocks.

**Partial failure** is the third and most distinctive challenge. A single machine either works or it does not — failure is total. In a distributed system, some nodes can fail while others continue operating. A three-node database might have one node crash, one node running correctly, and one node running but returning stale data due to a network partition. The system must continue providing useful service despite this partial failure, which means every component must be designed to tolerate the failure of components it depends on. This is why distributed systems engineering is largely the art of building reliable systems from unreliable parts — and why the field exists as a discipline distinct from single-machine programming.
