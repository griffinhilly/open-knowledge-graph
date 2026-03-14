---
id: multistep-methods-adams
title: 'Multistep Methods: Adams-Bashforth and Adams-Moulton'
domain: mathematics
course: numerical-analysis
prerequisites:
- id: runge-kutta-methods
  type: hard
builds-toward:
- stiff-equations
tags:
- multistep
- adams
- ode
stage: abstract-reasoning
status: draft
---

# Multistep Methods: Adams-Bashforth and Adams-Moulton

## Core Idea
Multistep methods use information from several previous steps to compute y_{n+1}. Adams-Bashforth (explicit) uses past y and f values; Adams-Moulton (implicit) includes f(t_{n+1}, y_{n+1}). Multistep methods are efficient when solution history is available but require startup (using a single-step method for the first few steps) and careful error monitoring.
