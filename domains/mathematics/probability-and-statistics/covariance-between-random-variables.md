---
id: covariance-between-random-variables
title: Covariance and Correlation of Random Variables
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: expected-value
  type: hard
- id: variance-of-random-variables
  type: hard
builds-toward:
- joint-probability-distributions
- linear-regression
tags:
- dependence
- covariance
- correlation
stage: formal-systems
status: draft
---

# Covariance and Correlation of Random Variables

## Core Idea
Covariance measures how two random variables vary together: Cov(X,Y) = E[(X-μ_X)(Y-μ_Y)]. Correlation ρ = Cov(X,Y)/(σ_X σ_Y) scales covariance to [-1,1]. Correlation measures linear association; covariance incorporates both direction and scale.

## How It's Best Learned
Calculate covariance and correlation from bivariate data. Visualize relationships with scatterplots. Understand that correlation ≠ causation. Examine how transformations affect covariance.

## Common Misconceptions
Assuming zero correlation means independence. Thinking high covariance means strong relationship (it depends on variable scales). Interpreting correlation causally. Forgetting that covariance and correlation only measure linear association.
