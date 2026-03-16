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
status: draft
---

# Distributed Tracing and Observability

## Core Idea
Distributed tracing tracks requests as they propagate through multiple services and systems. A trace is a tree of spans, each representing a unit of work (RPC, database query, cache lookup). Spans are linked via trace IDs and parent-child relationships. Tracing enables root-cause analysis of latency, error diagnosis, and understanding of service dependencies.

## Explainer

In a monolithic application, debugging a slow request is straightforward: you look at a single stack trace or profile and find the bottleneck. In a distributed system with dozens or hundreds of services, a single user request might fan out across an API gateway, an authentication service, a product catalog, an inventory check, a payment processor, and a notification system. When that request takes 3 seconds instead of 300 milliseconds, which service is responsible? Logs from individual services cannot answer this question alone because they lack the cross-service context. **Distributed tracing** solves this by stitching together the full journey of a request across every service it touches.

The core abstraction is the **trace** and the **span**. A trace represents the entire lifecycle of a request and is identified by a globally unique **trace ID**. Each unit of work within the trace — an HTTP call, a database query, a cache lookup, a message published to a queue — is a **span**. Spans have a start time, duration, metadata (tags and logs), and crucially, a **parent span ID** that links them into a tree. When Service A calls Service B, Service A's span becomes the parent of Service B's span. The trace ID and parent span ID are propagated in request headers (typically via standards like W3C Trace Context or B3), so every service in the chain can create its own spans and attach them to the same trace.

The resulting trace tree is a powerful debugging tool. Visualized as a timeline (often called a **Gantt chart** or **waterfall view**), you can immediately see which service call took the longest, whether calls were sequential or parallel, and where errors occurred. If the payment service took 2.5 seconds of a 3-second request, you have found your bottleneck. Beyond individual requests, aggregating traces reveals systemic patterns: which service pairs have the highest latency, which endpoints are called most frequently, and how dependency chains create cascading failures.

In practice, tracing at full fidelity for every request generates enormous data volumes, so most systems use **sampling** — capturing only a fraction of traces (say, 1% or 10%) or using head-based sampling (decide at the start of a request) versus tail-based sampling (decide after the request completes, keeping only interesting traces like errors or outliers). Tracing is one pillar of the broader concept of **observability**, alongside metrics (aggregated numerical measurements) and logs (discrete event records). Metrics tell you something is wrong, logs tell you what happened in one place, and traces tell you why a request was slow across the entire system.
