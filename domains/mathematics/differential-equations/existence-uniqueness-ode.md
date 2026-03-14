---
id: existence-uniqueness-ode
title: Existence and Uniqueness Theorems (Picard-Lindelöf Theorem)
domain: mathematics
course: differential-equations
prerequisites:
- id: exact-differential-equations
  type: soft
- id: continuity-definition
  type: hard
builds-toward:
- autonomous-equations-phase-lines
tags:
- existence
- uniqueness
- theoretical
stage: advanced
status: draft
---

# Existence and Uniqueness Theorems (Picard-Lindelöf Theorem)

## Core Idea
The Picard-Lindelöf theorem establishes conditions under which an initial value problem dy/dx = f(x,y), y(x₀) = y₀ has a unique solution. If f and ∂f/∂y are continuous in a rectangular region around (x₀, y₀), then a unique solution exists in some neighborhood of x₀. This is foundational for understanding when solutions are guaranteed and where they may fail to exist or be non-unique.
