---
id: characteristic-equation-and-stability
title: Characteristic Equation and Closed-Loop Stability
domain: engineering
course: control-systems
prerequisites:
- id: poles-zeros-stability-analysis
  type: hard
- id: feedback-control-fundamentals
  type: hard
- id: characteristic-polynomial
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
builds-toward:
- natural-frequency-damping-second-order
- routh-hurwitz-criterion
tags:
- characteristic-equation
- stability
- poles
- closed-loop
stage: advanced
status: draft
---

# Characteristic Equation and Closed-Loop Stability

## Core Idea
The characteristic equation is formed from the closed-loop transfer function denominator (1 + loop gain = 0). Its roots are the closed-loop poles, which determine stability: all roots must be in the left half-plane for BIBO stability. The characteristic equation connects open-loop plant and controller parameters to closed-loop pole locations, making it the central equation for analyzing how design choices affect stability.
