---
id: causal-consistency
title: Causal Consistency
domain: computer-science
course: distributed-systems
prerequisites:
- id: consistency-models
  type: hard
- id: happened-before-relation-causality
  type: hard
builds-toward:
- crdts-convergent-replicated-types
tags:
- causal-consistency
- consistency
- causality
stage: advanced
status: validated
---

# Causal Consistency

## Core Idea
Causal consistency is stronger than eventual consistency but weaker than strong consistency: it respects causal dependencies (if write A happened-before write B, all processes see A before B), but concurrent writes can be observed in different orders. This model avoids anomalies like receiving replies before questions while maintaining good availability.

## Questions

```yaml
- question: "Alice posts 'What time is dinner?' on a shared forum. Bob reads her post and replies '6pm.' Under causal consistency, which of the following is guaranteed for any user Carol reading the forum?"
  type: multiple-choice
  options:
    - "Carol sees both posts but may see Bob's reply before Alice's question"
    - "Carol sees all posts in the exact wall-clock order they were written"
    - "Carol always sees Alice's question before Bob's reply, because Bob's reply is causally dependent on Alice's question"
    - "Carol may not see either post until both have propagated to all replicas"
  answer: 2
  explanation: "Bob's post causally depends on Alice's — he read her question before writing his reply. Under causal consistency, all processes must observe causally related operations in causal order. So Carol must see Alice's question before Bob's reply. Option A describes eventual consistency, where even causally related events can appear out of order. Option B is too strong — causal consistency does not enforce wall-clock ordering for causally unrelated events, only causal ordering."

- question: "Dan and Eve independently post unrelated status updates on a geo-replicated social network at roughly the same time. Under causal consistency, what is guaranteed?"
  type: multiple-choice
  options:
    - "All users see Dan's post before Eve's, because geo-replicated systems serialize all updates"
    - "All users eventually see both posts, but different users may see them in different orders"
    - "Dan's post is always delivered before Eve's because the system respects chronological order"
    - "Neither post is visible to anyone until both have been replicated to all data centers"
  answer: 1
  explanation: "Dan and Eve's posts are concurrent — neither causally depends on the other. Causal consistency only enforces ordering for causally related operations; concurrent operations can be observed in any order by different nodes. Some users may see Dan's first; others may see Eve's first. This is permitted and is part of what allows causal consistency to avoid the coordination costs of strong consistency."

- question: "Under causal consistency, if operation A causally precedes operation B, every process in the system must observe A before B."
  type: true-false
  answer: true
  explanation: "True. This is the defining property of causal consistency: causal ordering is preserved everywhere. If A happened-before B (using Lamport's relation — B could have been influenced by A), no process is permitted to observe B without having first observed A. The system tracks dependencies using mechanisms like vector clocks and delays delivering an update until all causally prior updates have been applied."

- question: "Causal consistency guarantees that all nodes observe all operations in the same total order."
  type: true-false
  answer: false
  explanation: "False. Causal consistency only guarantees that causally related operations appear in causal order. Concurrent operations (no causal relationship) can be observed in different orders by different nodes. A total order over all operations is the property of strong (linearizable) consistency, which requires global coordination. Causal consistency deliberately relaxes this requirement for concurrent events, which is what makes it achievable without global synchronization."

- question: "Why can causal consistency be implemented in a geo-replicated system without global synchronization, while strong consistency cannot?"
  type: short-answer
  answer: "Causal consistency only requires that a node delay delivering an update until all causally prior updates have been applied — it does not require coordination with all other replicas before accepting a write. Replicas track causal dependencies locally (via vector clocks or dependency metadata) and apply updates in dependency order. Strong consistency, by contrast, requires every read to reflect the globally latest write, necessitating cross-replica coordination (quorum reads/writes or consensus) that adds latency proportional to inter-datacenter round-trip times."
  explanation: "This is why causal consistency is attractive for geo-replicated systems: the coordination cost scales with the depth of causal chains, not with the number of concurrent operations. Systems like COPS implement causal consistency across data centers while maintaining low latency for the common case where operations are causally independent."
```

## Explainer

From your study of consistency models, you know the spectrum ranges from strong consistency (every read sees the latest write, but at the cost of availability and latency) to eventual consistency (all replicas converge eventually, but reads can return stale or out-of-order data). **Causal consistency** sits in between, enforcing a specific constraint: if two operations are causally related — meaning one could have influenced the other — then every process in the system must observe them in causal order. Operations that are not causally related (concurrent operations) can be observed in any order.

The intuition comes from everyday conversation. If Alice posts a question and Bob posts an answer, anyone reading the forum should see the question before the answer — because the answer was caused by the question. But if Alice and Carol independently post unrelated messages at roughly the same time, it does not matter whether a reader sees Alice's or Carol's message first. Causal consistency captures exactly this: it preserves the ordering that humans intuitively expect while relaxing ordering constraints on truly independent events.

From your prerequisite on **causal ordering**, you know that happened-before relationships (Lamport's relation) define which events are causally connected. Causal consistency uses this same structure: if write A happened-before write B (because B read the value written by A, or because B followed A at the same process), then all processes must see A before B. The system tracks these dependencies using mechanisms like vector clocks or explicit dependency lists. When a replica receives an update, it checks whether all causally prior updates have already been applied; if not, it delays the update until the dependencies are satisfied.

The practical appeal of causal consistency is that it avoids the most jarring anomalies of eventual consistency without paying the steep coordination cost of strong consistency. Under eventual consistency, you might see a reply to a message before seeing the original message, or see someone's profile picture change before seeing the post that announced the change. Causal consistency eliminates these anomalies. Meanwhile, unlike strong consistency, it does not require global synchronization — replicas can accept writes independently and propagate them asynchronously, as long as causal dependencies are tracked and respected. This makes it a popular choice for geo-replicated systems where latency between data centers makes strong consistency impractical.
