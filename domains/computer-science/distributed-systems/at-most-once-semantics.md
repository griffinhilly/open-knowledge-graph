---
id: at-most-once-semantics
title: At-Most-Once Delivery Semantics
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

# At-Most-Once Delivery Semantics

## Core Idea
At-most-once semantics guarantee zero or one delivery, never more. This is the weakest guarantee: senders do not retry, so messages may be lost. Implementation is simple and low-overhead. This semantic is acceptable for fire-and-forget operations like metrics or logs where occasional loss does not compromise correctness.

## Explainer

In any distributed system, sending a message between two nodes involves uncertainty. The network might drop the packet, the receiver might crash before processing it, or the acknowledgment might get lost on the way back. From your introduction to distributed systems, you know that these failures are not edge cases — they are the normal operating conditions of networked software. **Delivery semantics** describe the guarantees a system provides about how many times a message will be processed, and at-most-once is the simplest of the three main options.

**At-most-once** means the sender transmits the message exactly once and does not retry. If the message arrives, it gets processed once. If it is lost — due to network failure, receiver crash, or anything else — it is simply gone. The sender does not know whether delivery succeeded, and it does not try again. This is the easiest semantic to implement because it requires no acknowledgment tracking, no retry logic, no deduplication, and no persistent state. The sender fires the message and moves on.

The tradeoff is obvious: you accept that some messages will be lost. This is acceptable when the cost of a lost message is low and the cost of a duplicate would be high or complicated. Consider metrics reporting: if a monitoring agent sends CPU utilization readings every second and one reading is lost, the dashboard shows a tiny gap — no harm done. But if the agent retried aggressively and the same reading was processed twice, it could skew averages or trigger false alerts. Similarly, log shipping, heartbeat pings, and cache invalidation hints are all cases where occasional loss is tolerable and simplicity is valuable.

At-most-once becomes dangerous when applied to operations that must not be skipped. A payment request, an inventory decrement, or a user registration cannot simply be lost without consequence. For those operations, you need **at-least-once** semantics (retry until acknowledged, accepting possible duplicates) or **exactly-once** semantics (retry with deduplication to guarantee single processing). Understanding at-most-once first gives you the baseline: it shows what you get for free with no extra machinery, and it frames the additional complexity that stronger guarantees require. Every retry mechanism, idempotency token, and deduplication log you encounter later exists precisely because at-most-once was not strong enough for the use case.
