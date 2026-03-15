---
id: conformal-mappings
title: Conformal Mappings
domain: mathematics
course: complex-analysis
prerequisites:
- id: holomorphic-functions
  type: hard
- id: complex-differentiability
  type: soft
builds-toward:
- mobius-transformations
tags:
- conformal-mappings
- angle-preserving
- geometry
stage: advanced
status: draft
---

# Conformal Mappings

## Core Idea
A holomorphic function f with f'(z₀) ≠ 0 is conformal (angle-preserving) near z₀: it scales lengths by |f'(z₀)| and rotates by arg(f'(z₀)), preserving angles between curves. Conformal maps are essential in applications: they transform boundary value problems from complicated regions to simple ones (like the unit disk) where solutions are known.

## How It's Best Learned
Visualize f(z) = e^z and see how it maps vertical lines to rays and horizontal lines to circles. Understand why angles are preserved: f'(z) = e^z is nonzero everywhere.

## Common Misconceptions
Thinking all angle-preserving functions are holomorphic; orientation-reversing maps (like conjugation) also preserve angles. Assuming conformal maps are easy to find; finding the right map for a given boundary value problem requires skill and often tables of known maps.
