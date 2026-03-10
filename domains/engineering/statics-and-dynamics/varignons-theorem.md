---
id: varignons-theorem
title: Varignon's Theorem
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: moment-of-force-2d
  type: hard
- id: force-systems-resultants
  type: hard
builds-toward:
- equivalent-force-systems
- equilibrium-rigid-bodies
tags:
- statics
- moment
- principle of moments
- superposition
stage: formal-systems
status: draft
---

# Varignon's Theorem

## Core Idea
Varignon's theorem states that the moment of a force about any point equals the sum of the moments of its components about that same point. This follows directly from the distributive property of the cross product: M_O = r × F = r × (F_x i + F_y j). The theorem is extremely practical because it often replaces one difficult perpendicular distance calculation with two simpler component-distance calculations.

## How It's Best Learned
Apply Varignon's theorem on problems where the perpendicular distance to a force's line of action is geometrically awkward. Decompose the force into horizontal and vertical components at any convenient point on the line of action, then compute and sum the moments of each component.

## Common Misconceptions
- Summing force magnitudes rather than moment contributions of each component.
- Applying the theorem about different reference points for different components (must use the same point).
- Forgetting to apply correct signs to each component's moment contribution.
