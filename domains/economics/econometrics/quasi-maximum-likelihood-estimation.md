---
id: quasi-maximum-likelihood-estimation
title: Quasi-Maximum Likelihood Estimation (QMLE)
domain: economics
course: econometrics
prerequisites:
- id: maximum-likelihood-econometrics
  type: hard
- id: heteroskedasticity
  type: soft
builds-toward:
- logit-probit-models
tags:
- estimation
- likelihood
- qmle
stage: formal-systems
status: draft
---

# Quasi-Maximum Likelihood Estimation (QMLE)

## Core Idea
QMLE maximizes a potentially misspecified likelihood to estimate parameters; under regularity conditions, the estimator remains consistent and asymptotically normal with a sandwich (Huber-White) covariance estimator. This robustness makes QMLE useful when the true distribution is unknown but a working model is available.
