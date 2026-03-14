---
id: hardness-approximation
title: Hardness of Approximation Introduction
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: approximation-algorithms
  type: hard
- id: three-sat-reductions
  type: hard
tags:
- approximation-hardness
- inapproximability
- reductions
- lower-bounds
stage: advanced
status: draft
---

# Hardness of Approximation Introduction

## Core Idea
Even when a problem is NP-hard, we sometimes compute approximate solutions rather than exact ones. Hardness of approximation results show that some NP-hard problems are also hard to approximate: there exist constants c > 1 such that achieving a c-approximation is NP-hard. These results reveal fundamental limits to what approximation algorithms can achieve.

## How It's Best Learned
Study the PCP (Probabilistically Checkable Proofs) theorem at an intuitive level. Work through one inapproximability result, like the maximal independent set hardness.
