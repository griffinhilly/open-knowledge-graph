---
id: exactly-once-semantics
title: Exactly-Once Delivery Semantics
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-systems-introduction
  type: hard
builds-toward:
- idempotent-operations
- two-phase-commit-protocol
tags:
- semantics
- delivery
- correctness
stage: advanced
status: validated
---

# Exactly-Once Delivery Semantics

## Core Idea
Exactly-once semantics guarantee that a message is delivered and processed exactly one time, neither zero nor multiple. This is the strongest correctness guarantee but requires deduplication state and coordination. It is essential for operations with side effects (charging a payment, updating a counter) where duplicates would cause data corruption.

## Questions

```yaml
- question: "A payment service sends a 'charge $50' message to a billing system. The billing system processes the charge and sends an acknowledgment, but the acknowledgment is lost in the network. The payment service retries. Under at-least-once semantics, what happens next?"
  type: multiple-choice
  options:
    - "The billing system detects the duplicate automatically via TCP checksums and discards the second message"
    - "The billing system receives the duplicate message and, without additional deduplication logic, charges the customer $100 total"
    - "The payment service detects the timeout and cancels both the original and retry charges"
    - "At-least-once semantics prevents retries; only at-most-once semantics would retry the message"
  answer: 1
  explanation: "Under at-least-once delivery, the sender retries until it gets an acknowledgment. The receiver has no obligation to detect duplicates — that's not part of at-least-once semantics. When the billing system receives the second 'charge $50' message, it has no way to know (without additional machinery) that it already processed this exact request, so it processes it again. This is the fundamental problem that exactly-once semantics (via deduplication) solves. The key insight is that the acknowledgment loss is the trigger: the sender *cannot know* whether the original was processed or not, so it must retry."

- question: "A system is described as providing 'exactly-once semantics' for message processing. What is the core technical mechanism that makes this possible?"
  type: multiple-choice
  options:
    - "The network layer guarantees each packet is only ever transmitted once, so no duplicates reach the application"
    - "The sender assigns each message a unique ID; the receiver maintains a log of processed IDs and skips processing if the ID has been seen before"
    - "The sender and receiver use a two-phase commit protocol to agree on whether each message was processed"
    - "Messages are buffered and batched, so duplicates within the same batch cancel each other out before processing"
  answer: 1
  explanation: "Exactly-once semantics cannot be achieved by preventing duplicate delivery — unreliable networks make that impossible. Instead, the receiver maintains a deduplication log: every message carries a unique identifier, and before processing, the receiver checks whether that ID has already been processed. If so, it skips processing and re-sends the original response. This means a message may be *delivered* more than once, but the *effect* occurs exactly once — hence the term 'effectively-once.' The deduplication check and the processing must be atomic to close any race condition window."

- question: "Exactly-once semantics prevent a message from ever being physically delivered to the receiver more than once."
  type: true-false
  answer: false
  explanation: "This is the most important misconception about exactly-once semantics. The name is somewhat misleading. Exactly-once semantics do not — and cannot — guarantee that the underlying network delivers a message only once. Networks will always have the possibility of retransmission. What exactly-once semantics guarantee is that the *processing effect* occurs exactly once: through deduplication, the receiver recognizes and discards redundant deliveries. Systems like Kafka even document this as 'effectively-once': duplicate delivery may occur, but duplicate processing is prevented."

- question: "Exactly-once semantics are most important for operations with non-idempotent side effects, such as charging a payment or incrementing a counter, where processing the same message twice produces incorrect results."
  type: true-false
  answer: true
  explanation: "This is precisely the right framing. For idempotent operations — reading a value, setting a field to a specific value, or any operation where 'do it twice' equals 'do it once' — at-least-once delivery is sufficient and much simpler. The overhead of exactly-once (deduplication state storage, atomic check-and-process, ID management) is only justified when duplicates cause real harm. Financial transactions are the canonical example: charging $50 twice causes a real $50 error. Counter increments are another: incrementing a view count twice gives wrong analytics. The design decision is always: is this operation idempotent, or does it require exactly-once protection?"

- question: "Exactly-once semantics are often described as 'effectively-once.' What does this mean, and what must a system do to achieve this guarantee?"
  type: short-answer
  answer: "Effectively-once means a message may be physically delivered more than once, but its effect on the system state occurs exactly once. The system achieves this through deduplication: each message carries a unique identifier, and the receiver maintains a persistent log of all message IDs it has already processed. When a duplicate arrives, the receiver recognizes the ID, skips processing, and re-sends the original acknowledgment. The deduplication check and processing must be atomic to ensure no duplicate can slip through in a concurrent environment. The key insight is that the problem is not preventing duplicate *delivery* (impossible in unreliable networks) but ensuring duplicate *processing* has no additional effect."
  explanation: "The terminology matters because it clarifies where the guarantee lives: not in the transport layer (which may deliver duplicates) but in the application layer (which detects and ignores duplicate processing). This framing also explains the cost: the receiver must maintain deduplication state reliably, which means persistent storage, atomic operations, and eventual garbage collection of old IDs."
```

## Explainer

From your distributed systems overview, you know that networks are unreliable — messages can be lost, duplicated, or delayed. This creates a fundamental delivery spectrum. **At-most-once** delivery sends a message and never retries; the message might be lost, but it will never be processed twice. **At-least-once** delivery retries until an acknowledgment is received; the message will definitely arrive, but it might be processed multiple times if the acknowledgment is lost and the sender retries. **Exactly-once** semantics aim for the best of both: the message is processed exactly one time, no matter what goes wrong with the network.

Here's why exactly-once is hard. Suppose a payment service sends a "charge $50" message to a billing system. The billing system processes the charge and sends back an acknowledgment, but the ack is lost in the network. The payment service, having received no confirmation, retries the message. Now the billing system receives "charge $50" again. Without additional machinery, it processes the charge a second time — the customer is billed $100 instead of $50. At-least-once delivery guarantees the charge gets through, but it doesn't prevent this duplication.

Exactly-once semantics are achieved not by preventing duplicate delivery (which is impossible in an unreliable network) but by ensuring that **duplicate processing has no additional effect**. The standard technique is **deduplication**: each message carries a unique identifier, and the receiver maintains a log of all message IDs it has already processed. When a duplicate arrives, the receiver recognizes the ID, skips processing, and re-sends the original response. This requires the receiver to maintain **deduplication state** — a potentially large table of processed message IDs — and to make the check-and-process operation atomic so that no window exists where a duplicate could slip through.

In practice, exactly-once semantics are often described more precisely as **effectively-once**: the message may be *delivered* more than once, but the *effect* occurs exactly once. Systems like Apache Kafka achieve this through a combination of producer-side sequence numbers, broker-side deduplication logs, and transactional writes that atomically commit message processing and offset advancement. The cost is real — deduplication state must be stored reliably, lookups add latency, and the state must eventually be garbage-collected. For operations without side effects (reading a value, computing a pure function), at-least-once delivery with idempotent processing is simpler and cheaper. Exactly-once semantics are worth the overhead specifically when operations have non-reversible side effects: financial transactions, counter increments, inventory adjustments, or any mutation where "do it twice" and "do it once" produce different outcomes.
