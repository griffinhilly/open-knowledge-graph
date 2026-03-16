---
id: idempotent-operations
title: Idempotent Operations in Distributed Systems
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-systems-overview
  type: hard
builds-toward:
- exactly-once-semantics
- distributed-transactions-2pc
tags:
- retry
- fault-tolerance
- semantics
stage: advanced
status: draft
---

# Idempotent Operations in Distributed Systems

## Core Idea
An operation is idempotent if applying it multiple times has the same effect as applying it once. In distributed systems, idempotency enables safe retry mechanisms: if a request fails or times out, the client can safely retry without risking duplication or corruption. Making operations idempotent often requires careful design with request deduplication.

## Explainer

From your distributed systems overview, you know that networks are unreliable — messages can be delayed, duplicated, or lost, and neither the sender nor receiver can always tell what happened. When a client sends a request and gets no response, it faces an impossible question: did the server process the request and the response was lost, or did the request never arrive? The safest choice is to retry, but retrying a non-idempotent operation can cause real damage. **Idempotency** is the property that makes retries safe: if an operation produces the same result whether executed once or many times, the client can retry freely without worrying about which scenario occurred.

Some operations are **naturally idempotent**. Setting a value — "set account balance to $500" — produces the same state no matter how many times you execute it. HTTP PUT and DELETE are designed to be idempotent for this reason: putting the same resource twice results in one resource, and deleting an already-deleted resource is a no-op. Other operations are **naturally non-idempotent**. "Add $100 to the account balance" changes the result every time it runs — retry it three times and you have added $300 instead of $100. "Insert a new order" creates a duplicate row on every retry. These operations require explicit design to become safe under retries.

The standard technique for making non-idempotent operations safe is **request deduplication using idempotency keys**. The client generates a unique identifier (UUID) for each logical operation and includes it with every request and retry. The server stores this key alongside the result of the first successful execution. On subsequent requests with the same key, the server recognizes the duplicate, skips the operation, and returns the stored result. Payment APIs like Stripe use this pattern — you include an idempotency key with a charge request, and no matter how many times you retry, the customer is charged exactly once.

Designing for idempotency is not just a nice-to-have — it is a fundamental requirement for building reliable distributed systems. Without it, every timeout and retry becomes a potential source of data corruption, duplicate charges, or inconsistent state. The principle extends beyond individual API calls to larger patterns: message queues that may deliver messages more than once need idempotent consumers, event-driven systems need deduplication at processing boundaries, and database operations wrapped in retryable transactions need to account for partial failures. Thinking about idempotency early in system design — asking "what happens if this runs twice?" for every operation — prevents entire categories of production bugs.
