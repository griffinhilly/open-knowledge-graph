---
id: multivariable-limits
title: Limits and Continuity in Multiple Variables
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: functions-of-several-variables
  type: hard
- id: limit-laws
  type: hard
- id: continuity-definition
  type: hard
builds-toward:
- partial-derivatives
tags:
- limits
- continuity
- multivariable
- epsilon-delta
stage: formal-systems
status: validated
---

# Limits and Continuity in Multiple Variables

## Core Idea
The limit lim_{(x,y)→(a,b)} f(x, y) = L means f(x, y) approaches L as (x, y) approaches (a, b) along every possible path. This is fundamentally harder than single-variable limits: one-variable limits require checking only two directions (left and right), but in ℝ² there are infinitely many paths of approach. A function is continuous at (a, b) if the limit equals f(a, b). Showing a limit does not exist is typically done by finding two paths that give different limiting values.

## How It's Best Learned
Emphasize the path-dependence issue with a concrete example, such as f(x,y) = xy/(x²+y²) near the origin. Show that different approach paths (y=0, y=x, y=x²) give different limits. Then show how the squeeze theorem can establish that a limit does exist. The contrast between existence proofs and non-existence proofs builds the key skill.

## Common Misconceptions
- It is NOT sufficient to check finitely many paths to prove a limit exists; existence proofs require general arguments (squeeze theorem, delta-epsilon).
- Showing the limit along y=mx is 0 for all slopes m does not prove the limit is 0 — it might still fail along y=x².
- A function can be discontinuous at a point even if it is defined there.
