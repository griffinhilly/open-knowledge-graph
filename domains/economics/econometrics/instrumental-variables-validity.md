---
id: instrumental-variables-validity
title: 'Instrumental Variables: Validity Assumptions'
domain: economics
course: econometrics
prerequisites:
- id: instrumental-variables
  type: hard
- id: endogenous-regressors-bias
  type: hard
builds-toward:
- two-stage-least-squares-procedure
tags:
- instrumental-variables
- exogeneity
- relevance
stage: formal-systems
status: draft
---

# Instrumental Variables: Validity Assumptions

## Core Idea
A valid instrument Z must satisfy: (1) Relevance—Cov(Z, X) ≠ 0; (2) Exogeneity—E[Zu] = 0. Weak instruments (low correlation with X) yield biased 2SLS estimates even in large samples. Exogeneity is untestable; justification rests on theory or research design.
