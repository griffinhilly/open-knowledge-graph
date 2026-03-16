---
id: causal-ordering
title: Causal Ordering and Happened-Before Relations
domain: computer-science
course: distributed-systems
prerequisites:
- id: vector-clocks
  type: hard
builds-toward:
- causal-consistency
tags:
- causality
- ordering
- happened-before
stage: advanced
status: draft
---

# Causal Ordering and Happened-Before Relations

## Core Idea
Causal ordering (happened-before relation) is a partial order on events: A happened-before B if A executed before B on the same process, or if A sent a message that B received. Systems that preserve causal ordering deliver updates respecting these dependencies, preventing anomalies like receiving a reply before its question.

## Explainer

From your study of vector clocks, you know how to assign timestamps to events in a distributed system such that you can determine whether one event causally preceded another. Causal ordering takes that mechanism and turns it into a delivery guarantee: messages are delivered to each process in an order that respects causal dependencies. If event A caused event B — because A happened before B on the same process, or because A's message was received before B was sent — then every process in the system must see A before B.

The **happened-before relation**, formalized by Lamport, defines causality through three rules: (1) if A and B occur on the same process and A executes first, then A happened-before B; (2) if A is the sending of a message and B is the receipt of that same message, then A happened-before B; (3) if A happened-before B and B happened-before C, then A happened-before C (transitivity). Events that are not related by happened-before are **concurrent** — they have no causal relationship, and the system is free to deliver them in either order. This is a **partial order**, not a total order: not every pair of events is comparable, and that is intentional. Forcing a total order on causally independent events would sacrifice performance for an ordering guarantee nobody needs.

Consider a concrete example: in a group chat, Alice posts "Should we meet at 3pm?" and Bob replies "Sure, 3pm works." Carol, on a third node, must see Alice's question before Bob's reply — otherwise the conversation is nonsensical. But if Dave independently posts "Nice weather today" with no causal relationship to Alice's message, Carol can see Dave's message before or after Alice's without any confusion. A causally ordered system enforces the first constraint (question before reply) while remaining flexible about the second (independent messages).

Implementing causal ordering relies on the vector clocks you already understand. Each message carries the sender's vector timestamp. When a process receives a message, it checks whether all causally preceding messages have already been delivered — specifically, it verifies that for every other process, it has seen at least as many messages from that process as the sender had seen when it sent this message. If not, the message is buffered until the missing predecessors arrive. This buffering is the cost of causal ordering: messages may be delayed even though they have physically arrived, waiting for their causal predecessors to catch up. The benefit is a consistency model that prevents the most confusing class of anomalies while remaining far cheaper than enforcing a total order on all events.
