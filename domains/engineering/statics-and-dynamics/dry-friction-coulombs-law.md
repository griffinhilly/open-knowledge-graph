---
id: dry-friction-coulombs-law
title: Dry Friction and Coulomb's Law
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: equilibrium-rigid-bodies
  type: hard
- id: friction-forces
  type: soft
builds-toward:
- friction-wedges-screws-belts
tags:
- statics
- friction
- Coulomb friction
- static friction
- kinetic friction
stage: formal-systems
status: draft
---

# Dry Friction and Coulomb's Law

## Core Idea
Coulomb's law states that the maximum static friction force is F_s,max = μ_s·N, where μ_s is the static friction coefficient and N is the normal contact force. Kinetic friction is F_k = μ_k·N with μ_k < μ_s. Friction is reactive: it takes whatever value is needed for equilibrium up to its maximum. Three states are possible — static equilibrium (F < μ_s·N), impending motion (F = μ_s·N), or sliding (F = μ_k·N). The angle of friction φ_s = arctan(μ_s) gives the angle of the resultant contact force from the normal at impending slip.

## How It's Best Learned
Identify which friction state applies (equilibrium, impending, or sliding) before setting up equations. Assume a friction direction in the FBD, solve, and verify the result is consistent with the assumed state.

## Common Misconceptions
- Using kinetic friction when the problem involves impending (not actual) motion.
- Assuming friction always acts in a fixed direction — it opposes the tendency of motion.
- Thinking friction force equals μN always, rather than at most μ_s·N.
