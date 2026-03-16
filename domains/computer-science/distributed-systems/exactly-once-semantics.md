---
id: exactly-once-semantics
title: Exactly-Once Delivery Semantics
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-systems-overview
  type: hard
builds-toward:
- idempotent-operations
- distributed-transactions-2pc
tags:
- semantics
- delivery
- correctness
stage: advanced
status: draft
---

# Exactly-Once Delivery Semantics

## Core Idea
Exactly-once semantics guarantee that a message is delivered and processed exactly one time, neither zero nor multiple. This is the strongest correctness guarantee but requires deduplication state and coordination. It is essential for operations with side effects (charging a payment, updating a counter) where duplicates would cause data corruption.

## Explainer

From your distributed systems overview, you know that networks are unreliable — messages can be lost, duplicated, or delayed. This creates a fundamental delivery spectrum. **At-most-once** delivery sends a message and never retries; the message might be lost, but it will never be processed twice. **At-least-once** delivery retries until an acknowledgment is received; the message will definitely arrive, but it might be processed multiple times if the acknowledgment is lost and the sender retries. **Exactly-once** semantics aim for the best of both: the message is processed exactly one time, no matter what goes wrong with the network.

Here's why exactly-once is hard. Suppose a payment service sends a "charge $50" message to a billing system. The billing system processes the charge and sends back an acknowledgment, but the ack is lost in the network. The payment service, having received no confirmation, retries the message. Now the billing system receives "charge $50" again. Without additional machinery, it processes the charge a second time — the customer is billed $100 instead of $50. At-least-once delivery guarantees the charge gets through, but it doesn't prevent this duplication.

Exactly-once semantics are achieved not by preventing duplicate delivery (which is impossible in an unreliable network) but by ensuring that **duplicate processing has no additional effect**. The standard technique is **deduplication**: each message carries a unique identifier, and the receiver maintains a log of all message IDs it has already processed. When a duplicate arrives, the receiver recognizes the ID, skips processing, and re-sends the original response. This requires the receiver to maintain **deduplication state** — a potentially large table of processed message IDs — and to make the check-and-process operation atomic so that no window exists where a duplicate could slip through.

In practice, exactly-once semantics are often described more precisely as **effectively-once**: the message may be *delivered* more than once, but the *effect* occurs exactly once. Systems like Apache Kafka achieve this through a combination of producer-side sequence numbers, broker-side deduplication logs, and transactional writes that atomically commit message processing and offset advancement. The cost is real — deduplication state must be stored reliably, lookups add latency, and the state must eventually be garbage-collected. For operations without side effects (reading a value, computing a pure function), at-least-once delivery with idempotent processing is simpler and cheaper. Exactly-once semantics are worth the overhead specifically when operations have non-reversible side effects: financial transactions, counter increments, inventory adjustments, or any mutation where "do it twice" and "do it once" produce different outcomes.
