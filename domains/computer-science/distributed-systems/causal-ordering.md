---
id: causal-ordering
title: Causal Ordering and Happened-Before Relations
domain: computer-science
course: distributed-systems
prerequisites:
- id: vector-clocks
  type: hard
builds-toward:
- causal-consistency
tags:
- causality
- ordering
- happened-before
stage: advanced
status: draft
---

# Causal Ordering and Happened-Before Relations

## Core Idea
Causal ordering (happened-before relation) is a partial order on events: A happened-before B if A executed before B on the same process, or if A sent a message that B received. Systems that preserve causal ordering deliver updates respecting these dependencies, preventing anomalies like receiving a reply before its question.
