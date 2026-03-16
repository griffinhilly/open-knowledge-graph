---
id: floating-body-stability-metacentric-height
title: Floating Body Stability and Metacentric Height
domain: engineering
course: fluid-mechanics
prerequisites:
- id: buoyancy-and-archimedes
  type: hard
- id: hydrostatic-force-vertical-surfaces
  type: soft
builds-toward:
- open-channel-flow
tags:
- buoyancy
- stability
- naval-architecture
stage: formal-systems
status: draft
---

# Floating Body Stability and Metacentric Height

## Core Idea
A floating body is stable if the metacenter (intersection of buoyant force line with centerline) lies above the center of gravity. Metacentric height quantifies stability; larger values provide greater resistance to tipping. Ships, barges, and other floating structures must be designed to maintain positive metacentric height across all operating conditions to prevent capsizing.

## Explainer

From Archimedes' principle, you know that a floating body displaces fluid equal in weight to its own weight. The buoyant force acts upward through the **center of buoyancy** (B) — the centroid of the displaced fluid volume. The body's weight acts downward through the **center of gravity** (G). At rest on calm water, B lies directly below G (or they coincide for a symmetric body at rest), and the system is in static equilibrium. So far, this is just Archimedes. The interesting question is what happens when something disturbs the vessel — a wave, a shifting load, a gust of wind — causing it to tilt.

When a ship heels by a small angle θ, the geometry of the submerged volume changes: more volume enters the water on the leaning side, less on the other. The **center of buoyancy** shifts laterally toward the submerged side, because the submerged volume's centroid moves in that direction. The buoyant force still acts vertically, but now through this displaced B location. If you trace that vertical line of action upward, it intersects the vessel's original vertical centerline at a point called the **metacenter** (M). The crucial fact: for small heeling angles, M is fixed regardless of the heel angle, because the shift of B is approximately proportional to θ.

Stability is determined entirely by the relative positions of M and G. If M lies above G (positive **metacentric height** GM = height of M minus height of G), then when the vessel tilts, the offset buoyant force creates a **righting moment** pulling the ship back upright — analogous to a pendulum returning to center. The restoring torque is approximately W · GM · sin(θ) ≈ W · GM · θ for small angles. Larger GM means a stronger righting moment: a stiffer, more stable vessel. If M falls below G, the buoyant force creates an **overturning moment** that amplifies the tilt — the vessel is inherently unstable and will capsize.

Metacentric height is not a fixed property — it changes with loading. A container ship with cargo stacked high on deck raises G and reduces GM. A ship taking on water in its upper decks can go from positive to negative GM in minutes. This is why vessels carry **ballast** water in tanks near the keel: lowering G to maintain adequate GM under all loading conditions. Naval architects calculate GM curves across all planned loading configurations — not just the designed operating condition. Too little GM risks capsizing; too much GM causes rapid, violent rolling (a stiff ship is uncomfortable and can stress cargo and structure). Designing for an appropriate GM range under all conditions, from empty to fully loaded, is the central stability calculation in naval architecture.

## How It's Best Learned
Sketch the tilted ship showing B shift and the metacentric triangle (BM, BG, GM). Compute metacentric height from first principles for a simple rectangular barge, then check how GM changes when you add top weight versus ballast.
