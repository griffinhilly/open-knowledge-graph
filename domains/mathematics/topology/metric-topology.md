---
id: metric-topology
title: Metric Topology
domain: mathematics
course: topology
prerequisites:
- id: metric-spaces-definition
  type: hard
- id: basis-for-topology
  type: soft
builds-toward:
- completeness-metric-spaces
tags:
- metric
- induced-topology
stage: advanced
status: draft
---

# Metric Topology

## Core Idea
Every metric induces a topology: U is open iff it is a union of open balls B(x, ε) = {y : d(x,y) < ε}. Open balls form a basis. Every metrizable topological space admits such a metric, making metric spaces a major class of topological spaces.
