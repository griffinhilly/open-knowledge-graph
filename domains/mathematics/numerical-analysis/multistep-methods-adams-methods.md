---
id: multistep-methods-adams-methods
title: Multistep Methods (Adams-Bashforth/Moulton)
domain: mathematics
course: numerical-analysis
prerequisites:
- id: runge-kutta-methods-for-odes
  type: hard
builds-toward:
- stiff-differential-equations
tags:
- multistep-methods
- adams-bashforth
- adams-moulton
stage: advanced
status: draft
---

# Multistep Methods (Adams-Bashforth/Moulton)

## Core Idea
Multistep methods use information from previous steps to advance the solution by integrating a polynomial interpolant of f through recent points. Adams-Bashforth methods are explicit; Adams-Moulton methods are implicit. These methods are efficient when f evaluation is expensive, using function values already computed from previous steps.
