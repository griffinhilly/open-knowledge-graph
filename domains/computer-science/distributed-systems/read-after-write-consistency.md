---
id: read-after-write-consistency
title: Read-After-Write Consistency
domain: computer-science
course: distributed-systems
prerequisites:
- id: consistency-models
  type: hard
builds-toward:
- strong-eventual-consistency
tags:
- consistency
- session-consistency
- guarantees
stage: advanced
status: draft
---

# Read-After-Write Consistency

## Core Idea
Read-after-write (RaW) consistency, also called session consistency, guarantees that if a client writes data, all its subsequent reads will reflect that write. This is weaker than linearizability but captures a natural expectation: 'I just wrote my profile, I should see it when I reload.' It is often sufficient for user-facing applications.

## Explainer

From your study of consistency models, you know that distributed systems offer a spectrum of guarantees ranging from strong (linearizability) to weak (eventual consistency). **Read-after-write consistency** sits in a practical sweet spot on this spectrum: it guarantees that after you write a value, your own subsequent reads will always see that write — but it makes no promises about what other clients see. This is sometimes called **session consistency** because the guarantee is scoped to a single client's session rather than the entire system.

Consider a concrete scenario. You update your display name on a social media platform. The write goes to a primary database node and begins replicating to read replicas. If your very next page load hits a replica that has not yet received the update, you see your old name — even though you just changed it. This feels broken, even though the system is technically functioning correctly under eventual consistency. Read-after-write consistency eliminates exactly this class of surprise: the system ensures that your reads always reflect your own prior writes, even if the underlying replication has not fully propagated.

There are several common implementation strategies. The simplest is **read-your-writes routing**: after a client performs a write, the system routes that client's subsequent reads to the node that processed the write (often the primary) for a brief window, then falls back to replicas once replication has caught up. Another approach uses **logical timestamps or version vectors**: the client remembers the version of its last write, and any replica serving a read must have at least that version before responding — otherwise the request is forwarded or delayed. A third approach uses **sticky sessions**, pinning a client to a specific replica so that reads and writes flow through the same node.

The key insight is that read-after-write consistency is dramatically cheaper than linearizability while eliminating the most common user-visible anomaly in replicated systems. Linearizability requires global coordination on every operation, which imposes latency and reduces availability. Read-after-write only requires coordination within a single client's session — a much smaller scope. This is why it appears so frequently in practice: systems like Amazon DynamoDB, MongoDB, and most cloud databases offer read-after-write guarantees as a default or configurable option, because it matches user expectations without the performance cost of full strong consistency.
