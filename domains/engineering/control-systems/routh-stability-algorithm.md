---
id: routh-stability-algorithm
title: 'Routh-Hurwitz Stability Test: Algorithm and Application'
domain: engineering
course: control-systems
prerequisites:
- id: transfer-function-derivation-differential-equations
  type: hard
builds-toward:
- compensation-design-tradeoffs-cascadefeedback
tags:
- routh-hurwitz
- stability-test
- pole-locations
- characteristic-equation
stage: concrete-operations
status: draft
---

# Routh-Hurwitz Stability Test: Algorithm and Application

## Core Idea
Routh-Hurwitz test determines stability without computing poles: arrange characteristic polynomial coefficients in a tableau, compute rows using specific rules. Number of sign changes in the first column equals number of poles in right half-plane. Test fails if any element is zero (repeated root on jω-axis); special cases require auxiliary polynomials.
