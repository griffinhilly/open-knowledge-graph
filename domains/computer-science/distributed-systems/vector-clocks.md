---
id: vector-clocks
title: Vector Clocks and Capturing Causality
domain: computer-science
course: distributed-systems
prerequisites:
- id: logical-clocks
  type: hard
builds-toward:
- causal-ordering
- causal-consistency
tags:
- vector-clocks
- causality
- ordering
stage: advanced
status: draft
---

# Vector Clocks and Capturing Causality

## Core Idea
Vector clocks extend logical clocks with a vector of integers (one per process). Each process increments its own entry on local events and sets each entry to the maximum of its value and the sender's on message receipt. Vector clocks precisely capture causality: event A happened-before B iff A's vector is less than B's element-wise, and concurrent events have incomparable vectors.

## How It's Best Learned
Implement vector clock logic and trace scenarios with concurrent writes and message chains.

## Common Misconceptions
Vector clocks require clock synchronization; they can totally order all events; they are necessary for all distributed algorithms.

## Explainer

From your study of logical clocks (Lamport clocks), you know that distributed systems can assign timestamps to events without relying on synchronized physical clocks. Lamport clocks give you a useful property: if event A happened before event B, then A's timestamp is less than B's. But the converse is not true — if A's timestamp is less than B's, you cannot conclude that A actually caused B. They might be completely independent events that happened to get ordered by the counter. **Vector clocks** solve this limitation by making causality detection precise in both directions.

A vector clock is an array of integers, one entry per process in the system. If there are three processes (P1, P2, P3), every event carries a vector like [2, 0, 1]. Each process maintains its own vector and follows two rules. First, before recording a local event, a process increments its own entry in the vector. Second, when a process receives a message, it takes the **element-wise maximum** of its own vector and the vector attached to the message, then increments its own entry. These two rules are all it takes to capture the full causal history of every event.

The comparison rule is what makes vector clocks powerful. Event A **happened before** event B if and only if every entry in A's vector is less than or equal to the corresponding entry in B's vector, and at least one entry is strictly less. If neither A ≤ B nor B ≤ A — that is, A has some entries larger than B's and B has some entries larger than A's — then A and B are **concurrent**. They occurred independently, with no causal chain connecting them. This is information that Lamport clocks simply cannot provide. For example, if A = [2, 3, 1] and B = [3, 1, 2], then A and B are concurrent: A knows more about P2's history, B knows more about P1 and P3. Neither could have influenced the other.

This concurrency detection is essential for conflict resolution in distributed databases. Systems like Amazon's Dynamo use vector clocks (or their compressed variants, version vectors) to detect when two replicas have diverged. If two updates to the same key have comparable vector clocks, the system can automatically keep the later one. If the vectors are incomparable, the system knows a genuine conflict has occurred and can flag it for resolution — either by the application or through a merge function like last-writer-wins. Without vector clocks, the system would have no principled way to distinguish "one update supersedes the other" from "two updates happened independently and both matter."
