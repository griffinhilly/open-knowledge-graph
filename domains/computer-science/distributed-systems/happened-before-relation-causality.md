---
id: happened-before-relation-causality
title: Happened-Before Relation and Causal Ordering
domain: computer-science
course: distributed-systems
prerequisites:
- id: lamport-timestamps
  type: hard
- id: vector-clocks
  type: hard
builds-toward:
- causal-consistency-implementation
- distributed-snapshots-chandy-lamport
- total-order-broadcast
tags:
- causality
- ordering
- logical-clocks
- partial-order
stage: abstract-reasoning
status: draft
---

# Happened-Before Relation and Causal Ordering

## Core Idea
The happened-before relation (→) defines a partial order on events: event A happened before event B if A caused B (through message exchange or local sequencing). This relation is the foundation for reasoning about distributed computations without requiring synchronized physical clocks, and it distinguishes causally-dependent events from concurrent ones.

## How It's Best Learned
Draw message diagrams with labeled events and identify the partial order. Use Lamport timestamps and vector clocks to detect causality. Understand that concurrency (neither A→B nor B→A) means events can be ordered arbitrarily without violating causality.

## Common Misconceptions
- Happened-before is the same as physical time ordering; it depends only on communication and local computation, not wall-clock time.
- If two events are not ordered by →, one must be reordered to fix 'bugs'; actually, concurrent events can remain unordered.

## Explainer

From your work with Lamport timestamps and vector clocks, you have the tools to assign logical timestamps to events. The **happened-before relation** is the conceptual framework that gives those tools their meaning. Defined by Leslie Lamport in 1978, it captures the idea of **potential causality** in a distributed system: event A happened before event B (written A → B) if A could have influenced B. This is a precise, formal replacement for the intuitive but unreliable notion of "A occurred earlier than B in real time."

The relation is defined by three rules. First, if A and B are events in the same process and A occurs before B in that process's local execution order, then A → B. Second, if A is the sending of a message and B is the receipt of that same message by another process, then A → B — because the send necessarily precedes the receive. Third, the relation is **transitive**: if A → B and B → C, then A → C. These three rules — local ordering, message causality, and transitivity — are the only ways to establish happened-before. If none of these chains connect two events, they are **concurrent** (written A ‖ B), meaning neither could have caused the other, regardless of what wall-clock time says.

This is why the relation is a **partial order** rather than a total order. In a total order, every pair of events is comparable — one always comes before the other. In the happened-before partial order, concurrent events are genuinely incomparable. Two users on different continents editing different documents at the "same time" have no causal connection, and the system need not — and should not — impose an artificial ordering between them. Lamport timestamps give you a total order that is *consistent with* happened-before (if A → B then L(A) < L(B)), but the converse is not true: L(A) < L(B) does not mean A → B. Vector clocks are more powerful because they capture the full partial order: V(A) < V(B) if and only if A → B.

The practical consequence is that any distributed system that needs to reason about causality — whether for consistent snapshots, causal message delivery, conflict detection in replicated data, or debugging concurrent operations — must track the happened-before relation rather than relying on synchronized physical clocks. Physical clocks drift, have finite precision, and can disagree across machines. The happened-before relation depends only on the actual communication pattern between processes, making it robust to clock skew and physically meaningful: it tells you exactly which events could have influenced which others, and nothing more.