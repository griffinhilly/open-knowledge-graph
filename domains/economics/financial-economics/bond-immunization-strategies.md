---
id: bond-immunization-strategies
title: Bond Immunization Strategies
domain: economics
course: financial-economics
prerequisites:
- id: duration-and-convexity
  type: hard
builds-toward:
- interest-rate-risk-management
tags:
- bonds
- duration
- immunization
stage: formal-systems
status: draft
---

# Bond Immunization Strategies

## Core Idea
Immunization matches the duration of a bond portfolio to the time horizon of liabilities, protecting against interest rate changes. A portfolio immunized at time t will have value sufficient to meet obligations at time t+H, regardless of parallel yield curve shifts. Higher-order immunization (contingent immunization) addresses convexity and nonparallel shifts.

## How It's Best Learned
Construct a simple two-bond portfolio matched to a single liability horizon, calculate duration, and verify the immunization works across different interest rate scenarios.
