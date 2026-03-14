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
