---
id: idempotent-operations
title: Idempotent Operations in Distributed Systems
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-systems-overview
  type: hard
builds-toward:
  - distributed-transactions-2pc
tags:
- retry
- fault-tolerance
- semantics
stage: advanced
status: validated
---
# Idempotent Operations in Distributed Systems

## Core Idea
An operation is idempotent if applying it multiple times has the same effect as applying it once. In distributed systems, idempotency enables safe retry mechanisms: if a request fails or times out, the client can safely retry without risking duplication or corruption. Making operations idempotent often requires careful design with request deduplication.

## Questions

```yaml
- question: "A payment service receives two HTTP requests with identical idempotency keys — the second is a retry after a network timeout. What should the server do?"
  type: multiple-choice
  options:
    - "Process both requests to ensure the payment completes — network timeouts mean the first may not have succeeded"
    - "Reject the second request with an error, forcing the client to generate a new idempotency key before retrying"
    - "Recognize the duplicate key, skip the second operation, and return the result of the first successful execution"
    - "Block all subsequent requests for that account until the first request's outcome is manually confirmed"
  answer: 2
  explanation: "This is exactly what idempotency keys are designed for. The server stores the outcome of the first successful operation alongside its idempotency key. When the second request arrives with the same key, the server detects the duplicate, skips re-execution, and returns the cached result. The client gets the same response regardless of how many times it retried — the customer is charged exactly once. Options A would charge twice; B defeats the purpose of retrying; D creates unacceptable latency and complexity."

- question: "An API has two balance endpoints: POST /accounts/{id}/credit with body {amount: 100} and PUT /accounts/{id}/balance with body {balance: 600}. A network fault causes each request to be delivered twice. Which outcome is correct?"
  type: multiple-choice
  options:
    - "Both endpoints charge twice — all POST and PUT requests must be treated as non-idempotent by default"
    - "The POST endpoint adds $200 total (non-idempotent: each delivery executes the increment), while the PUT endpoint sets the balance to $600 exactly once (idempotent: repeated sets produce the same result)"
    - "The PUT endpoint is non-idempotent because PUT creates a new resource on each call"
    - "Both endpoints are safe to retry because modern databases handle duplicate detection automatically"
  answer: 1
  explanation: "This scenario captures the core distinction. 'Add $100' is non-idempotent: applying it twice changes the outcome (adds $200 instead of $100). 'Set balance to $600' is idempotent: applying it twice leaves the balance at $600 — the second application has no additional effect. HTTP PUT is designed to be idempotent (setting a resource to a specific state), while POST for incremental operations typically is not. Idempotency depends on the operation's semantics, not the HTTP method alone."

- question: "If an operation fails and returns an error response, the client can safely retry it because a failed operation cannot have partially changed server state."
  type: true-false
  answer: false
  explanation: "This is the core problem idempotency solves. In a distributed system, 'failure' is ambiguous: a timeout means the client never received a response, but the server may have already completed the operation successfully before the response was lost in transit. The operation may have fully executed on the server — it is the confirmation that was lost. Retrying a non-idempotent operation in this scenario causes double execution. The client has no way to distinguish 'request never arrived' from 'request completed but response was lost' without additional mechanisms like idempotency keys."

- question: "HTTP DELETE is designed to be idempotent: sending the same DELETE request multiple times should produce the same server state as sending it once."
  type: true-false
  answer: true
  explanation: "By HTTP specification, DELETE is idempotent: if a resource is deleted, it no longer exists, and deleting a non-existent resource is a no-op (the resource remains gone). The state after one DELETE equals the state after ten DELETEs. This does not mean the server must return the same status code — a first DELETE might return 200, subsequent ones might return 404 — but the state of the system (resource absent) is unchanged by repetition. This is exactly what idempotency means: same effect, not necessarily same response."

- question: "A developer argues that idempotency is only important for payment systems and financial APIs. Why is this reasoning too narrow?"
  type: short-answer
  answer: "Idempotency is required anywhere messages can be delivered more than once or where retries occur — which is nearly everywhere in distributed systems. Message queues (Kafka, SQS) commonly deliver messages at least once, so consumers must be idempotent. Event-driven systems fire events that may be processed more than once across restarts. Database writes wrapped in retryable transactions must account for partial failures where the write succeeded but the commit confirmation was lost. Any microservice making outbound API calls over a network faces the same problem. The question 'what happens if this runs twice?' should be asked of every operation in a distributed system, not just payments."
  explanation: "The financial example is memorable because the consequences are obvious (double charges), but the distributed systems challenge is universal. A non-idempotent email-sending operation retried after a timeout sends duplicate emails. A non-idempotent inventory decrement retried doubles the deduction. Idempotency is a correctness property for any system where 'at-least-once delivery' is the reliability guarantee — which covers most practical distributed systems."
```

## Explainer

From your distributed systems overview, you know that networks are unreliable — messages can be delayed, duplicated, or lost, and neither the sender nor receiver can always tell what happened. When a client sends a request and gets no response, it faces an impossible question: did the server process the request and the response was lost, or did the request never arrive? The safest choice is to retry, but retrying a non-idempotent operation can cause real damage. **Idempotency** is the property that makes retries safe: if an operation produces the same result whether executed once or many times, the client can retry freely without worrying about which scenario occurred.

Some operations are **naturally idempotent**. Setting a value — "set account balance to $500" — produces the same state no matter how many times you execute it. HTTP PUT and DELETE are designed to be idempotent for this reason: putting the same resource twice results in one resource, and deleting an already-deleted resource is a no-op. Other operations are **naturally non-idempotent**. "Add $100 to the account balance" changes the result every time it runs — retry it three times and you have added $300 instead of $100. "Insert a new order" creates a duplicate row on every retry. These operations require explicit design to become safe under retries.

The standard technique for making non-idempotent operations safe is **request deduplication using idempotency keys**. The client generates a unique identifier (UUID) for each logical operation and includes it with every request and retry. The server stores this key alongside the result of the first successful execution. On subsequent requests with the same key, the server recognizes the duplicate, skips the operation, and returns the stored result. Payment APIs like Stripe use this pattern — you include an idempotency key with a charge request, and no matter how many times you retry, the customer is charged exactly once.

Designing for idempotency is not just a nice-to-have — it is a fundamental requirement for building reliable distributed systems. Without it, every timeout and retry becomes a potential source of data corruption, duplicate charges, or inconsistent state. The principle extends beyond individual API calls to larger patterns: message queues that may deliver messages more than once need idempotent consumers, event-driven systems need deduplication at processing boundaries, and database operations wrapped in retryable transactions need to account for partial failures. Thinking about idempotency early in system design — asking "what happens if this runs twice?" for every operation — prevents entire categories of production bugs.
