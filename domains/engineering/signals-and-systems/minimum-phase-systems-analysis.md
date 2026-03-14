---
id: minimum-phase-systems-analysis
title: Minimum Phase Systems and Factorization
domain: engineering
course: signals-and-systems
prerequisites:
- id: all-pass-filters-phase-shaping
  type: hard
- id: transfer-function-poles-zeros
  type: hard
tags:
- minimum-phase
- all-pass
- transfer-function
- stability
stage: advanced
status: draft
---

# Minimum Phase Systems and Factorization

## Core Idea
A minimum-phase system has all poles and zeros inside the unit circle (digital) or left half-plane (analog), resulting in minimum group delay for its magnitude response. Any transfer function factors as H(z) = Hmin(z)·Hap(z), where Hmin is minimum-phase and Hap is all-pass. This decomposition enables simultaneous specification of magnitude response and phase characteristics.
