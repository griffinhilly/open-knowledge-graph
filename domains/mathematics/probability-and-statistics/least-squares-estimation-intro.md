---
id: least-squares-estimation-intro
title: Least Squares Estimation
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: linear-regression
  type: soft
builds-toward:
- regression-diagnostics
tags:
- estimation
- regression
- least-squares
stage: formal-systems
status: draft
---

# Least Squares Estimation

## Core Idea
Least squares estimation minimizes the sum of squared residuals: Σ(yᵢ - ŷᵢ)². For simple linear regression, this yields slope = r(s_y/s_x) and intercept = ȳ - b·x̄. Least squares is intuitive and optimal under normality.

## How It's Best Learned
Fit linear regression by hand for a small dataset. Visualize residuals and understand what minimizing their squared sum means geometrically. Compare least squares to other fitting methods.

## Common Misconceptions
Thinking least squares requires normal errors (it gives optimal linear fit regardless). Assuming high R² means good predictions. Not recognizing that outliers can heavily influence least squares estimates.
