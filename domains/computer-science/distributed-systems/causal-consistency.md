---
id: causal-consistency
title: Causal Consistency
domain: computer-science
course: distributed-systems
prerequisites:
- id: consistency-models
  type: hard
- id: causal-ordering
  type: hard
builds-toward:
- crdts-convergent-replicated-types
tags:
- causal-consistency
- consistency
- causality
stage: advanced
status: draft
---

# Causal Consistency

## Core Idea
Causal consistency is stronger than eventual consistency but weaker than strong consistency: it respects causal dependencies (if write A happened-before write B, all processes see A before B), but concurrent writes can be observed in different orders. This model avoids anomalies like receiving replies before questions while maintaining good availability.

## Explainer

From your study of consistency models, you know the spectrum ranges from strong consistency (every read sees the latest write, but at the cost of availability and latency) to eventual consistency (all replicas converge eventually, but reads can return stale or out-of-order data). **Causal consistency** sits in between, enforcing a specific constraint: if two operations are causally related — meaning one could have influenced the other — then every process in the system must observe them in causal order. Operations that are not causally related (concurrent operations) can be observed in any order.

The intuition comes from everyday conversation. If Alice posts a question and Bob posts an answer, anyone reading the forum should see the question before the answer — because the answer was caused by the question. But if Alice and Carol independently post unrelated messages at roughly the same time, it does not matter whether a reader sees Alice's or Carol's message first. Causal consistency captures exactly this: it preserves the ordering that humans intuitively expect while relaxing ordering constraints on truly independent events.

From your prerequisite on **causal ordering**, you know that happened-before relationships (Lamport's relation) define which events are causally connected. Causal consistency uses this same structure: if write A happened-before write B (because B read the value written by A, or because B followed A at the same process), then all processes must see A before B. The system tracks these dependencies using mechanisms like vector clocks or explicit dependency lists. When a replica receives an update, it checks whether all causally prior updates have already been applied; if not, it delays the update until the dependencies are satisfied.

The practical appeal of causal consistency is that it avoids the most jarring anomalies of eventual consistency without paying the steep coordination cost of strong consistency. Under eventual consistency, you might see a reply to a message before seeing the original message, or see someone's profile picture change before seeing the post that announced the change. Causal consistency eliminates these anomalies. Meanwhile, unlike strong consistency, it does not require global synchronization — replicas can accept writes independently and propagate them asynchronously, as long as causal dependencies are tracked and respected. This makes it a popular choice for geo-replicated systems where latency between data centers makes strong consistency impractical.
