---
id: overidentification-test
title: 'Test of Overidentification: Hansen J-Test'
domain: economics
course: econometrics
prerequisites:
- id: two-stage-least-squares-procedure
  type: hard
- id: reduced-form-equations
  type: soft
tags:
- instrumental-variables
- overidentification
- hypothesis-testing
stage: formal-systems
status: draft
---

# Test of Overidentification: Hansen J-Test

## Core Idea
The Hansen J-test checks whether extra instruments are exogenous. Under H₀ that E[Zᵢuᵢ] = 0, the statistic J = n · gₙ'Ŵ⁻¹gₙ ~ χ²₍ₘ₋ₖ₎, where m is the number of instruments and k is the number of endogenous regressors. Rejection suggests at least one instrument is invalid.
