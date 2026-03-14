---
id: efficient-frontier-construction
title: Efficient Frontier Construction and Mean-Variance Analysis
domain: economics
course: financial-economics
prerequisites:
- id: two-asset-portfolio-optimization
  type: hard
- id: efficient-frontier-portfolio-theory
  type: soft
builds-toward:
- capital-market-line
tags:
- portfolio-theory
- optimization
- efficient-frontier
stage: formal-systems
status: draft
---

# Efficient Frontier Construction and Mean-Variance Analysis

## Core Idea
The efficient frontier is the set of portfolios that maximize return for a given variance (or minimize variance for a given return). Multi-asset efficient frontiers require solving constrained optimization problems using covariance matrices and expected returns.

## How It's Best Learned
Use historical returns to estimate covariance matrix. Solve for optimal weights across multiple assets subject to constraints (e.g., no short-selling). Plot the resulting efficient frontier and compare to naive portfolios.
