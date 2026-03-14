---
id: expected-shortfall-tail-risk
title: Expected Shortfall and Tail Risk Measurement
domain: economics
course: financial-economics
prerequisites:
- id: value-at-risk-measurement
  type: hard
- id: risk-and-return-tradeoff
  type: soft
builds-toward:
- risk-and-return-tradeoff
tags:
- risk-management
- var
- tail-risk
- measurement
stage: formal-systems
status: draft
---

# Expected Shortfall and Tail Risk Measurement

## Core Idea
Expected shortfall (ES) or conditional value-at-risk measures the expected loss in the tail beyond the VaR threshold, addressing VaR's key weakness: it ignores loss severity. ES = E[Loss | Loss > VaR], and is coherent, satisfying desirable risk measure properties that VaR violates. ES is increasingly preferred for capital allocation and stress testing in regulated financial institutions.

## How It's Best Learned
Calculate both VaR and ES for a portfolio at the same confidence level and observe how ES better captures tail risk from extreme scenarios.
