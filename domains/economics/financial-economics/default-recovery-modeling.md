---
id: default-recovery-modeling
title: Default Probability and Recovery Rate Estimation
domain: economics
course: financial-economics
prerequisites:
- id: credit-risk-and-default
  type: hard
- id: corporate-bond-credit-spreads
  type: soft
builds-toward:
- credit-analysis-bond-selection
tags:
- credit-risk
- default
- recovery
- modeling
stage: formal-systems
status: draft
---

# Default Probability and Recovery Rate Estimation

## Core Idea
Default probability (PD) and loss given default (LGD, or recovery rate R = 1 - LGD) are critical parameters for credit risk management. Expected loss equals PD × LGD × Exposure, and bond yields must compensate for expected losses plus credit risk premium. Recovery rates vary substantially by seniority, collateral, and industry, requiring careful empirical estimation.
