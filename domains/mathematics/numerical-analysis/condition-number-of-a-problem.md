---
id: condition-number-of-a-problem
title: Condition Number of a Problem
domain: mathematics
course: numerical-analysis
prerequisites:
- id: numerical-stability-and-conditioning
  type: hard
builds-toward:
- condition-number-of-a-matrix
tags:
- condition-number
- ill-conditioning
- sensitivity
stage: advanced
status: draft
---

# Condition Number of a Problem

## Core Idea
The condition number of a problem quantifies how much the relative solution change is amplified by relative changes in the input data. A large condition number indicates an ill-conditioned problem where small input perturbations cause large solution changes. Condition numbers provide fundamental limits on achievable accuracy regardless of algorithm choice or precision used.
