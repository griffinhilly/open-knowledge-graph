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
