---
id: equilibrium-rigid-bodies
title: Equilibrium of Rigid Bodies
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: support-reactions-beams
  type: hard
- id: equivalent-force-systems
  type: hard
- id: static-equilibrium
  type: soft
- id: torque
  type: soft
- id: equilibrium-particles-3d
  type: soft
builds-toward:
- truss-method-of-joints
- frames-machines-analysis
- dry-friction-coulombs-law
tags:
- statics
- equilibrium
- rigid body
- moment equilibrium
stage: formal-systems
status: validated
---
# Equilibrium of Rigid Bodies

## Core Idea
A rigid body is in static equilibrium when both the resultant force and the resultant moment about any point are zero: ΣF = 0 and ΣM_O = 0. In 2D, this yields three scalar equations (ΣFx = 0, ΣFy = 0, ΣM_O = 0), permitting solution of three unknowns. Choosing the moment reference point at the intersection of unknown forces eliminates those unknowns from the moment equation. Statically determinate structures have exactly as many unknowns as equilibrium equations; indeterminate structures have surplus constraints requiring additional analysis.

## How It's Best Learned
Choose the moment point strategically to eliminate the most unknowns simultaneously. After solving, verify equilibrium about a second point as a check. For distributed loads, replace them with equivalent point loads (resultant force at centroid of the load diagram) before applying equilibrium.

## Common Misconceptions
- Choosing a poor moment point that unnecessarily includes multiple unknowns.
- Forgetting that distributed loads must be converted to resultant forces before summing moments.
- Confusing a statically indeterminate structure with one that is simply harder to analyze.
