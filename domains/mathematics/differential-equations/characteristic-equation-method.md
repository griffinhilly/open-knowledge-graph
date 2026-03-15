---
id: characteristic-equation-method
title: Characteristic Equation Method for Linear ODEs
domain: mathematics
course: differential-equations
prerequisites:
- id: second-order-linear-homogeneous-odes
  type: hard
- id: quadratic-formula
  type: hard
builds-toward:
- complex-roots-oscillatory-solutions
- repeated-roots-reduction-of-order
tags:
- characteristic-equation
- constant-coefficients
- solution-method
stage: formal-systems
status: draft
---

# Characteristic Equation Method for Linear ODEs

## Core Idea
For constant-coefficient linear ODEs, assume a solution y = e^(rx) and substitute to obtain a characteristic equation. For y'' + py' + qy = 0, the characteristic equation is r² + pr + q = 0. The roots r determine the solution form: distinct real roots give y = c₁e^(r₁x) + c₂e^(r₂x); complex roots give oscillatory solutions; repeated roots require x factors. This algebraic approach elegantly solves a wide class of equations.
