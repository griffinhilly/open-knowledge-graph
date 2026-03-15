---
id: item-response-theory-assumptions
title: 'Item Response Theory: Assumptions and Fundamentals'
domain: psychology
course: psychometrics
prerequisites:
- id: item-response-functions
  type: hard
- id: classical-test-theory
  type: hard
- id: probability-density-functions-theory
  type: soft
- id: normal-distribution
  type: soft
builds-toward:
- ability-parameter-estimation-theta-estimation
- classical-vs-irt-item-analysis
tags:
- irt
- assumptions
- unidimensionality
- local-independence
stage: advanced
status: draft
---

# Item Response Theory: Assumptions and Fundamentals

## Core Idea
IRT assumes unidimensionality (one latent ability drives responses), local independence (responses independent given ability), and monotonic item response functions. These assumptions are more restrictive than classical test theory but enable item-level precision and ability-independent item statistics. Testing assumptions is essential before IRT application.

## How It's Best Learned
Fit IRT models to real datasets and examine residuals and goodness-of-fit indices. Use dimensionality tests and compare unidimensional vs. multidimensional models.

## Common Misconceptions
- Assuming unidimensionality requires perfect homogeneity (acceptable even with small secondary factors)
- Local independence is violated when content is highly related (it means independence GIVEN ability, not necessarily in raw data)
