---
id: distributed-tracing
title: Distributed Tracing and Observability
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-system-models
  type: hard
tags:
- observability
- debugging
- monitoring
stage: advanced
status: validated
---

# Distributed Tracing and Observability

## Core Idea
Distributed tracing tracks requests as they propagate through multiple services and systems. A trace is a tree of spans, each representing a unit of work (RPC, database query, cache lookup). Spans are linked via trace IDs and parent-child relationships. Tracing enables root-cause analysis of latency, error diagnosis, and understanding of service dependencies.

## Questions

```yaml
- question: "A user reports that a checkout request is taking 4 seconds. Your system logs each microservice independently but has no distributed tracing. What critical diagnostic information is UNAVAILABLE without tracing?"
  type: multiple-choice
  options:
    - "The HTTP status code returned to the user at the end of the request"
    - "The exact error message from any service that returned a 500 response"
    - "The causal sequence and duration of each service call — specifically which service consumed the 4 seconds and whether calls were sequential or parallel"
    - "Which services were involved in processing the request at all"
  answer: 2
  explanation: "Per-service logs can tell you what happened inside each service in isolation, but they cannot reconstruct the cross-service causal timeline. Without tracing, you cannot determine whether the payment service called the inventory service (or vice versa), whether two calls ran in parallel, or how long each leg took within the overall 4-second wall clock time. Distributed tracing supplies exactly this: a linked, time-stamped tree of spans across all services, enabling root-cause diagnosis of where the latency actually lives."

- question: "How is the parent-child relationship between spans in a distributed trace established across service boundaries?"
  type: multiple-choice
  options:
    - "The tracing backend infers relationships by matching timestamps across service logs after the fact"
    - "Each service calls a central tracing coordinator to register its work before processing"
    - "The calling service embeds its span ID in outbound request headers; the receiving service reads this as its parent span ID and creates a child span"
    - "Spans are linked retroactively by matching shared user session IDs in log records"
  answer: 2
  explanation: "Trace context propagation via headers is the mechanism that makes distributed tracing possible. When Service A calls Service B, Service A's span ID is injected into the outgoing request headers (using standards like W3C Trace Context or B3). Service B extracts this header, uses the received span ID as its parent span ID, and creates a new child span. This chaining continues across every service boundary, producing a complete tree — all without requiring a central coordinator at call time."

- question: "A single trace can contain spans from dozens of different services, all sharing a trace ID that was generated when the request first entered the system."
  type: true-false
  answer: true
  explanation: "The trace ID is assigned once — typically at the entry point (API gateway or first service) — and propagated in headers through every service call for the lifetime of that request. Every span created anywhere in the call graph uses this same trace ID, which is how the tracing backend can assemble thousands of individual spans from many services into a single coherent trace tree."

- question: "Capturing a full trace for every request is standard practice in high-throughput production systems because the per-trace storage overhead is negligible."
  type: true-false
  answer: false
  explanation: "Full-fidelity tracing of every request generates enormous data volumes in high-throughput systems. A service processing 100,000 requests/second would produce millions of spans per second, creating storage, ingestion, and query performance problems. Production systems use sampling strategies — head-based sampling (decide at request start whether to trace), tail-based sampling (decide after completion, keeping only errors or slow outliers), or probabilistic sampling (trace 1–10% of requests) — to manage volume while retaining diagnostic value."

- question: "How does distributed tracing complement metrics and logs? What can it reveal that the other two pillars of observability cannot?"
  type: short-answer
  answer: "Metrics tell you that something is wrong (e.g., p99 latency spiked to 3 seconds), and per-service logs tell you what happened locally within each service. Neither can reconstruct the cross-service causal flow of a specific request. Distributed tracing links spans from all services into a single tree with timing, revealing which service caused a slowdown, whether service calls were sequential or parallel, how errors propagated through the dependency graph, and what the request looked like end-to-end — information that is structurally unavailable from per-service observations alone."
  explanation: "The three pillars are complementary precisely because they answer different questions: metrics surface the problem, logs explain local behavior, and traces reveal causality across service boundaries. High-latency incidents in microservice architectures almost always require all three to diagnose definitively."
```

## Explainer

In a monolithic application, debugging a slow request is straightforward: you look at a single stack trace or profile and find the bottleneck. In a distributed system with dozens or hundreds of services, a single user request might fan out across an API gateway, an authentication service, a product catalog, an inventory check, a payment processor, and a notification system. When that request takes 3 seconds instead of 300 milliseconds, which service is responsible? Logs from individual services cannot answer this question alone because they lack the cross-service context. **Distributed tracing** solves this by stitching together the full journey of a request across every service it touches.

The core abstraction is the **trace** and the **span**. A trace represents the entire lifecycle of a request and is identified by a globally unique **trace ID**. Each unit of work within the trace — an HTTP call, a database query, a cache lookup, a message published to a queue — is a **span**. Spans have a start time, duration, metadata (tags and logs), and crucially, a **parent span ID** that links them into a tree. When Service A calls Service B, Service A's span becomes the parent of Service B's span. The trace ID and parent span ID are propagated in request headers (typically via standards like W3C Trace Context or B3), so every service in the chain can create its own spans and attach them to the same trace.

The resulting trace tree is a powerful debugging tool. Visualized as a timeline (often called a **Gantt chart** or **waterfall view**), you can immediately see which service call took the longest, whether calls were sequential or parallel, and where errors occurred. If the payment service took 2.5 seconds of a 3-second request, you have found your bottleneck. Beyond individual requests, aggregating traces reveals systemic patterns: which service pairs have the highest latency, which endpoints are called most frequently, and how dependency chains create cascading failures.

In practice, tracing at full fidelity for every request generates enormous data volumes, so most systems use **sampling** — capturing only a fraction of traces (say, 1% or 10%) or using head-based sampling (decide at the start of a request) versus tail-based sampling (decide after the request completes, keeping only interesting traces like errors or outliers). Tracing is one pillar of the broader concept of **observability**, alongside metrics (aggregated numerical measurements) and logs (discrete event records). Metrics tell you something is wrong, logs tell you what happened in one place, and traces tell you why a request was slow across the entire system.
