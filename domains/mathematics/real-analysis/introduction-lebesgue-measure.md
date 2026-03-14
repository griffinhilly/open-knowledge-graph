---
id: introduction-lebesgue-measure
title: Introduction to Lebesgue Measure
domain: mathematics
course: real-analysis
prerequisites:
- id: open-closed-sets-real-line
  type: hard
- id: riemann-integrability-criteria
  type: soft
builds-toward:
- introduction-lebesgue-integral
tags:
- lebesgue-measure
- measure-theory
- measurable-sets
stage: abstract-reasoning
status: draft
---

# Introduction to Lebesgue Measure

## Core Idea
Lebesgue measure extends the notion of length to general sets on ℝ. A set E is measurable if for every set A, m(A) = m(A ∩ E) + m(A ∩ E^c). Lebesgue measure assigns 0 to countable sets, assigns to each interval [a,b] measure b−a, and is countably additive. This allows for more powerful integration theory than Riemann.
