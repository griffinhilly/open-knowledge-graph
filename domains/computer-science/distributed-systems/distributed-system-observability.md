---
id: distributed-system-observability
title: Observability, Tracing, and Debugging in Distributed Systems
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-snapshots
  type: hard
tags:
- observability
- tracing
- debugging
- monitoring
stage: advanced
status: validated
---

# Observability, Tracing, and Debugging in Distributed Systems

## Core Idea
Observability in distributed systems requires correlation of events across processes: distributed tracing (assigning request IDs that span processes) and the happened-before relation allow reconstruction of causality for debugging. Tools like Jaeger or Zipkin implement tracing; understanding causality is essential for interpreting traces.

## How It's Best Learned
Trace a multi-step request (HTTP → service A → service B → database) by hand, assigning trace IDs and span IDs. Then examine how the tracing tool reconstructs the critical path and identifies where time was spent.

## Common Misconceptions
- Logs alone are sufficient for debugging; in distributed systems, logs are scattered; you need correlation (tracing) to reconstruct causality.
- Distributed tracing adds negligible overhead; sampling and instrumentation overhead should be carefully measured and tuned.

## Questions

```yaml
- question: "A distributed order system spans 5 services. A customer reports their order was slow. Each service has detailed structured logs. What critical problem do the logs present without distributed tracing?"
  type: multiple-choice
  options:
    - "Each service logs in a different format that cannot be parsed by a single tool"
    - "The logs are scattered across 5 services with no way to identify which log entries from each service belong to this specific customer's request"
    - "Logs do not record timing information, so slowdowns cannot be detected"
    - "The sheer volume of logs from 5 services is too large to query efficiently"
  answer: 1
  explanation: "This is the core problem distributed tracing solves. Each service independently writes logs with no shared identifier linking them to a particular request. Without a trace ID propagated across service boundaries, you cannot correlate which log lines in Service A, B, C, D, and E all belong to the same user request — you have five separate, disconnected log streams rather than one coherent picture of what happened."

- question: "Why do most production distributed tracing systems sample only a small fraction of requests (e.g., 1%) rather than tracing every request?"
  type: multiple-choice
  options:
    - "The tracing protocol is inherently too slow to process every request at production throughput"
    - "Trace IDs must be globally unique, and generating unique IDs at 100% rate causes collisions"
    - "Instrumentation overhead (injecting headers, creating spans, transmitting data) and storage costs at full volume would significantly degrade system performance and economics"
    - "The happened-before relation only applies meaningfully to a sampled subset of requests"
  answer: 2
  explanation: "Full tracing at production scale means creating, transmitting, and storing spans for every single request — which can add meaningful latency overhead per request and requires enormous storage infrastructure. Sampling (typically 1–10%) captures enough traces to diagnose most issues while making the overhead manageable. Head-based sampling (decided at the entry point) and tail-based sampling (decided after seeing the full trace) are the two main strategies."

- question: "A fully reconstructed distributed trace encodes a partial ordering of events across services that corresponds to the happened-before relation: span A called service B, which completed before A continued."
  type: true-false
  answer: true
  explanation: "A trace is a practical implementation of the happened-before relation formalized by Lamport. Each parent-child span relationship encodes causality: the parent span called the child, so the child's start happened-after the parent initiated the call, and the parent's continuation happened-after the child completed. This partial ordering lets engineers reason about which events could have influenced which others — the same conceptual foundation as Lamport clocks and the Chandy-Lamport algorithm."

- question: "If nearly every service in a distributed system writes detailed, timestamped structured logs, those logs alone are sufficient to reconstruct the causal sequence of events for any specific user request."
  type: true-false
  answer: false
  explanation: "Timestamps alone cannot reconstruct causality in distributed systems because clocks are not perfectly synchronized across machines. More fundamentally, even with perfect timestamps, you cannot determine which log entries from Service A belong to the same request as specific entries from Service B without a shared correlation identifier. Logs tell you what each service did and when; tracing tells you which actions across services were causally connected to the same request."

- question: "Explain why a trace ID must be actively propagated through every downstream service call, and what breaks in the trace if even one service in the chain fails to pass it along."
  type: short-answer
  answer: "Each service must extract the trace ID from its incoming request (e.g., from an HTTP header) and inject it into every outgoing call it makes. If a service is not instrumented and fails to propagate the trace ID, the downstream services either generate a new, unrelated trace ID or produce no trace context at all. The trace breaks at that point: the upstream and downstream portions appear as two unrelated traces with no causal connection. The engineer sees the request 'disappear' mid-journey and cannot diagnose what happened in the uninstrumented service or attribute downstream latency to upstream causes."
  explanation: "This is why full instrumentation coverage matters. Partial instrumentation creates invisible gaps in the causality chain — precisely the blind spots that make distributed debugging hard in the first place. Tools like OpenTelemetry provide standardized libraries for automatic context propagation to reduce the instrumentation burden per service."
```

## Explainer

From the Chandy-Lamport algorithm, you know that capturing consistent global state in a distributed system is fundamentally hard — no single node can see everything at once. **Observability** is the practical discipline of making a distributed system's internal behavior visible enough to diagnose problems, even when you cannot pause the whole system and inspect it. It rests on three pillars: logs, metrics, and traces. Logs record discrete events. Metrics track numerical measurements over time. Traces follow individual requests as they flow across service boundaries.

The most important concept for distributed debugging is **distributed tracing**. When a user clicks "submit order" and that request touches an API gateway, an authentication service, an inventory service, and a payment processor, each service produces its own logs independently. Without correlation, you have four separate log streams with no way to connect them. Distributed tracing solves this by assigning a unique **trace ID** to the initial request and propagating it through every downstream call. Each service creates a **span** — a record of the work it performed, including start time, duration, and the trace ID. When you collect all spans sharing a trace ID, you can reconstruct the full request path as a tree: the API gateway span at the root, with child spans for each service call, nested to show which calls triggered which.

Tools like Jaeger, Zipkin, and OpenTelemetry implement this pattern by injecting trace context into HTTP headers, message queue metadata, or RPC frameworks. The key design decisions are **sampling** (tracing every request is expensive, so most systems trace a fraction — say 1% — of requests in production) and **instrumentation** (each service must be configured to create spans and propagate context). A well-instrumented system lets you answer questions like "why was this request slow?" by examining its trace and identifying which span consumed the most time. It also reveals dependency patterns, error propagation paths, and bottlenecks that are invisible in any single service's metrics or logs.

The deeper lesson connects back to causality. A trace is essentially a practical application of the **happened-before relation**: span A started before it called service B, which completed before A continued. The trace reconstructs a partial ordering of events across processes. But unlike Lamport timestamps, traces are designed for human consumption — they produce visual timelines and call graphs that engineers can inspect. The limitation is that traces only capture instrumented paths. If a background job or async message queue is not instrumented, the trace has a gap. Building effective observability means systematically closing those gaps so that the system's behavior can be understood from outside, without needing to reproduce the exact conditions that caused a failure.
