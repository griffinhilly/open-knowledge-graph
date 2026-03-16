---
id: operational-transformation
title: Operational Transformation for Collaborative Editing
domain: computer-science
course: distributed-systems
prerequisites:
- id: consistency-models
  type: hard
- id: crdts-convergent-replicated-types
  type: soft
tags:
- collaboration
- conflict-resolution
- editing
stage: advanced
status: draft
---

# Operational Transformation for Collaborative Editing

## Core Idea
Operational transformation (OT) enables real-time collaborative editing by transforming concurrent edits to commute, ensuring all replicas converge. When edits arrive out of order, OT 'rewrites' them relative to other concurrent operations. This requires defining transformation functions for all operation pairs and carefully handling causality and intention preservation.

## Explainer

When multiple users edit a shared document simultaneously, their edits can conflict. You already know from consistency models that replicas must eventually agree on the same state. **Operational transformation** solves this specific problem: given two edits made concurrently at different sites, how do you apply both so that every replica converges to the same result — and the result matches what both users intended?

Consider a concrete example. Two users start with the string "abc". User A inserts "X" at position 1, producing "aXbc". Concurrently, User B deletes the character at position 2 (the "c"), intending to produce "ab". When User B's delete arrives at User A's replica, position 2 no longer refers to "c" — it now refers to "b" because the insertion shifted everything. Applying the delete blindly would corrupt the document. OT solves this by **transforming** User B's operation against User A's: since A inserted before position 2, B's delete index must shift right by one. The transformed delete targets position 3, correctly removing "c" from "aXbc" to produce "aXb".

The core abstraction is the **transformation function** T(op1, op2), which takes two concurrent operations and returns modified versions that, when applied in either order, produce the same final state. For a text editor, you need transformation rules for every pair of operation types: insert-vs-insert, insert-vs-delete, delete-vs-delete. Each rule adjusts indices based on whether the other operation shifted characters left or right. This is conceptually simple for two operations but becomes surprisingly subtle when you must transform against chains of concurrent operations — getting the composition order wrong leads to divergence bugs that are notoriously difficult to reproduce and debug.

Unlike CRDTs, which you may have encountered, OT requires a **central server** (or agreed-upon total order) to serialize operations and resolve ambiguities. Google Docs, for instance, uses an OT-based protocol where a central server determines the canonical operation order and broadcasts transformed operations to all clients. This centralization simplifies correctness but introduces a single point of coordination. The tradeoff is fundamental: OT achieves compact operations and familiar editing semantics at the cost of requiring a serialization point, while CRDTs achieve decentralized convergence at the cost of more complex data structures and metadata overhead.
