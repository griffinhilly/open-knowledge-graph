---
id: strong-consistency-models
title: 'Strong Consistency: Linearizability and Sequential Consistency'
domain: computer-science
course: distributed-systems
prerequisites:
- id: consistency-models
  type: hard
builds-toward:
- state-machine-replication
tags:
- linearizability
- sequential-consistency
- strong-consistency
stage: advanced
status: draft
---

# Strong Consistency: Linearizability and Sequential Consistency

## Core Idea
Linearizability is the strongest consistency: the system appears as a single copy and each operation takes effect instantaneously between invocation and response. Sequential consistency is slightly weaker: operations appear in a total order respecting program order on each process. Both prevent anomalies but require coordination, increasing latency and reducing availability.
