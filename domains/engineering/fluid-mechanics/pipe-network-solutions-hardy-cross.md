---
id: pipe-network-solutions-hardy-cross
title: 'Pipe Network Analysis: Hardy-Cross Iteration Method'
domain: engineering
course: fluid-mechanics
prerequisites:
- id: mechanical-energy-balance-pump-turbine
  type: hard
- id: minor-loss-coefficients-fittings
  type: soft
tags:
- networks
- iteration
- branching-pipes
stage: formal-systems
status: draft
---

# Pipe Network Analysis: Hardy-Cross Iteration Method

## Core Idea
Complex branching pipe systems cannot be solved directly; the Hardy-Cross method uses iterative correction of assumed loop flows until convergence to a solution satisfying both continuity (flow in = flow out at junctions) and energy (head loss around each loop sums to zero). Modern software implements this method, but understanding the principle is essential for validation and troubleshooting.
