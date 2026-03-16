---
id: at-least-once-semantics
title: At-Least-Once Delivery Semantics
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-systems-overview
  type: hard
builds-toward:
- exactly-once-semantics
- distributed-transactions-2pc
tags:
- semantics
- delivery
- correctness
stage: advanced
status: draft
---

# At-Least-Once Delivery Semantics

## Core Idea
At-least-once semantics guarantee delivery one or more times through retries until acknowledgment. This prevents message loss but allows duplication. It sits between at-most-once and exactly-once. Applications must either be idempotent or handle duplicates explicitly. It is simpler than exactly-once but stronger than at-most-once.

## Explainer

From your overview of distributed systems, you know that networks are unreliable — messages can be lost, delayed, or arrive out of order. When a sender transmits a message, it faces a fundamental question: did the receiver get it? If the sender waits for an acknowledgment and none arrives, there are two possibilities: the message was lost, or the acknowledgment was lost. The sender cannot distinguish between these cases. **At-least-once semantics** resolve this ambiguity by choosing the safe side: if in doubt, retransmit.

The mechanism is straightforward. The sender transmits a message and starts a timer. If an acknowledgment arrives before the timer expires, delivery is confirmed and the sender moves on. If the timer expires without an acknowledgment, the sender retransmits the same message. This retry continues until an acknowledgment is finally received. The guarantee is that the message will eventually be delivered — it will not silently disappear. But the cost is obvious: if the original message *was* received and only the acknowledgment was lost, the receiver now gets the same message twice.

This is where **idempotency** becomes critical. An operation is idempotent if performing it multiple times produces the same result as performing it once. Setting a value (`balance = 500`) is idempotent — doing it twice leaves the balance at 500. Incrementing a value (`balance += 100`) is not — doing it twice adds 200 instead of 100. If your application's message handlers are idempotent, duplicate delivery is harmless. If they are not, you need explicit deduplication — typically by assigning each message a unique ID and having the receiver track which IDs it has already processed.

At-least-once delivery is the pragmatic sweet spot for many real-world systems. **At-most-once** (send and forget, never retry) risks silent data loss. **Exactly-once** requires complex coordination — typically combining at-least-once delivery with idempotent processing or transactional deduplication on the receiver side. Most message queues (RabbitMQ, SQS, Kafka with default settings) provide at-least-once guarantees out of the box. The design question then shifts from the transport layer to the application layer: can you make your handlers idempotent, or do you need to build deduplication logic? This framing — reliable transport plus application-level safety — is the foundation for understanding how stronger delivery guarantees are built.
