---
id: constant-propagation
title: Constant Propagation and Folding
domain: computer-science
course: compilers
prerequisites:
- id: reaching-definitions-analysis
  type: hard
tags:
- optimization
- constant-propagation
- algebraic-simplification
stage: advanced
status: draft
---

# Constant Propagation and Folding

## Core Idea
Constant propagation identifies variables assigned constant values and replaces their uses with the constant. Constant folding evaluates constant expressions at compile-time. For example, `x = 5; y = x + 3` becomes `y = 8`. This simple optimization enables further simplifications and can expose dead code.
