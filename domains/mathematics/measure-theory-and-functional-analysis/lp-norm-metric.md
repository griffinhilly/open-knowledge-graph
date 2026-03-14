---
id: lp-norm-metric
title: L^p Norm and Metric Structure
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lp-spaces-definition
  type: hard
- id: metric-spaces-definition
  type: soft
builds-toward:
- holders-inequality
- minkowski-inequality-lp
tags:
- lp-spaces
- norms
stage: abstract-reasoning
status: draft
---

# L^p Norm and Metric Structure

## Core Idea
The L^p norm ‖f‖_p = (∫|f|^p dμ)^(1/p) defines a metric d(f,g) = ‖f - g‖_p on L^p. Proving this is a norm requires Minkowski's inequality, making L^p a normed (hence metric) space.
