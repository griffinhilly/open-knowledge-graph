---
id: at-least-once-semantics
title: At-Least-Once Delivery Semantics
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-systems-introduction
  type: hard
builds-toward:
- exactly-once-semantics
- two-phase-commit-protocol
tags:
- semantics
- delivery
- correctness
stage: advanced
status: validated
---

# At-Least-Once Delivery Semantics

## Core Idea
At-least-once semantics guarantee delivery one or more times through retries until acknowledgment. This prevents message loss but allows duplication. It sits between at-most-once and exactly-once. Applications must either be idempotent or handle duplicates explicitly. It is simpler than exactly-once but stronger than at-most-once.

## Questions

```yaml
- question: "A payment service receives a 'charge $100' message via a queue with at-least-once delivery. The charge is processed successfully, but the acknowledgment is lost in the network. What happens next, and what is the consequence?"
  type: multiple-choice
  options:
    - "The sender marks the transaction failed and requires the user to retry manually"
    - "The message is redelivered and, without deduplication logic, the customer is charged again"
    - "The queue detects the duplicate and automatically cancels the second charge before it is processed"
    - "The sender waits indefinitely for an acknowledgment without ever retransmitting"
  answer: 1
  explanation: "At-least-once semantics guarantee delivery by retransmitting until an acknowledgment is received. Since the sender cannot distinguish 'message lost' from 'acknowledgment lost,' it retransmits the original message. If the payment handler simply processes every message it receives, the customer gets charged twice. At-least-once queues (RabbitMQ, SQS) provide no automatic deduplication — that is the application's responsibility. This is why idempotency or explicit deduplication logic is essential for financial and state-mutating operations over at-least-once transports."

- question: "Which property of an operation makes it safe to use with at-least-once delivery without explicit deduplication logic?"
  type: multiple-choice
  options:
    - "Commutativity — the operation can be applied in any order without changing the result"
    - "Idempotency — applying the operation multiple times produces the same result as applying it once"
    - "Atomicity — the operation completes fully or not at all"
    - "Determinism — the operation always produces the same output for the same input"
  answer: 1
  explanation: "Idempotency is the key property: f(f(x)) = f(x). Setting a field to a specific value ('status = PAID') is idempotent — doing it twice leaves the record in the same state as doing it once. Incrementing a counter is not idempotent — doing it twice adds twice. Commutativity is a different property (about ordering, not repetition) and does not help with duplicates. Atomicity prevents partial execution but doesn't prevent re-execution. Determinism alone doesn't help — a deterministic non-idempotent operation executed twice still causes double application."

- question: "At-least-once delivery is strictly stronger than exactly-once delivery because it guarantees nearly every message arrives, while exactly-once mainly guarantees messages are not duplicated."
  type: true-false
  answer: false
  explanation: "This reverses the strength ordering. Exactly-once is strictly stronger: it guarantees both that every message arrives (no loss) AND that it arrives exactly once (no duplicates). At-least-once only guarantees no loss — it explicitly allows duplicates. A system with exactly-once guarantees satisfies all the requirements of at-least-once, but not vice versa. The confusion likely comes from reading 'at least one' as 'at minimum one, therefore guaranteed.' The 'at least' means the count is ≥ 1, which includes 1, 2, 3, ... — duplicates are the cost, not a feature."

- question: "The fundamental reason at-least-once delivery can produce duplicate messages is that a sender cannot determine whether a missing acknowledgment means the message was lost or the acknowledgment was lost."
  type: true-false
  answer: true
  explanation: "This is the core insight. From the sender's perspective, a timeout after sending is ambiguous: (1) the message was lost and the receiver never saw it, or (2) the message arrived, was processed, and the acknowledgment was lost. In case 1, retransmitting is correct; in case 2, retransmitting causes a duplicate. Since the sender cannot distinguish the two cases, the safe choice (at-least-once) is to retransmit in both cases. Exactly-once delivery requires additional coordination (idempotency tokens, transactional guarantees) to resolve this ambiguity at the receiver side."

- question: "Explain why idempotency at the application layer is often preferred over exactly-once delivery at the transport layer as a solution to the duplicate message problem."
  type: short-answer
  answer: "Exactly-once delivery requires coordination between sender and receiver — typically a two-phase commit or a distributed transaction — which adds latency, complexity, and failure modes. Achieving exactly-once at the transport layer requires the infrastructure to maintain state about which messages have been delivered, which can be expensive and may fail under partitions. Idempotency, by contrast, moves the burden to the application layer: if the handler is designed so that processing a message twice has the same effect as processing it once, duplicate delivery becomes harmless without any coordination overhead. Most real systems (Kafka, SQS) default to at-least-once delivery and expect consumers to either be idempotent or implement deduplication via message IDs — a pattern that scales better than distributed transaction coordination."
  explanation: "The tradeoff is: exactly-once is simpler to reason about but expensive to implement correctly at infrastructure level. Idempotency requires careful application design but composes better with the realities of distributed networks, where exactly-once guarantees often break down under failure scenarios anyway."
```

## Explainer

From your overview of distributed systems, you know that networks are unreliable — messages can be lost, delayed, or arrive out of order. When a sender transmits a message, it faces a fundamental question: did the receiver get it? If the sender waits for an acknowledgment and none arrives, there are two possibilities: the message was lost, or the acknowledgment was lost. The sender cannot distinguish between these cases. **At-least-once semantics** resolve this ambiguity by choosing the safe side: if in doubt, retransmit.

The mechanism is straightforward. The sender transmits a message and starts a timer. If an acknowledgment arrives before the timer expires, delivery is confirmed and the sender moves on. If the timer expires without an acknowledgment, the sender retransmits the same message. This retry continues until an acknowledgment is finally received. The guarantee is that the message will eventually be delivered — it will not silently disappear. But the cost is obvious: if the original message *was* received and only the acknowledgment was lost, the receiver now gets the same message twice.

This is where **idempotency** becomes critical. An operation is idempotent if performing it multiple times produces the same result as performing it once. Setting a value (`balance = 500`) is idempotent — doing it twice leaves the balance at 500. Incrementing a value (`balance += 100`) is not — doing it twice adds 200 instead of 100. If your application's message handlers are idempotent, duplicate delivery is harmless. If they are not, you need explicit deduplication — typically by assigning each message a unique ID and having the receiver track which IDs it has already processed.

At-least-once delivery is the pragmatic sweet spot for many real-world systems. **At-most-once** (send and forget, never retry) risks silent data loss. **Exactly-once** requires complex coordination — typically combining at-least-once delivery with idempotent processing or transactional deduplication on the receiver side. Most message queues (RabbitMQ, SQS, Kafka with default settings) provide at-least-once guarantees out of the box. The design question then shifts from the transport layer to the application layer: can you make your handlers idempotent, or do you need to build deduplication logic? This framing — reliable transport plus application-level safety — is the foundation for understanding how stronger delivery guarantees are built.
