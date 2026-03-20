---
id: floating-body-stability-equilibrium
title: Floating Body Stability and Equilibrium
domain: engineering
course: fluid-mechanics
prerequisites:
- id: buoyancy-and-archimedes
  type: hard
- id: forces-on-submerged-surfaces
  type: soft
tags:
- statics
- buoyancy
- applications
stage: advanced
status: draft
---

# Floating Body Stability and Equilibrium

## Core Idea
A floating body is in equilibrium when the buoyant force (weight of displaced fluid) equals the weight of the body. Stability depends on the relative positions of the center of buoyancy and center of gravity; the metacenter determines whether a floating body returns to its original orientation after small disturbances. These principles govern ship design and the behavior of floating structures.

## How It's Best Learned
Float objects of different shapes in water and gently tilt them. Observe how narrow-based objects are unstable (metacenter below center of gravity) while wide-based objects return to upright position (metacenter above center of gravity).

## Common Misconceptions
- A floating body is stable if the center of buoyancy is above the center of gravity (stability depends on the metacenter being above the center of gravity, not the center of buoyancy).
- All floating objects have the same stability (stability depends on geometry and weight distribution, not on the fluid density alone).

## Explainer

From Archimedes' principle, you know that a floating body is in equilibrium when the upward buoyant force equals the body's weight — the body sinks until it displaces a volume of fluid whose weight matches its own. But equilibrium and stability are different questions. A pencil balanced on its tip is in equilibrium; it is not stable. Understanding floating body stability requires tracking two centers: where the body's mass is concentrated, and where the displaced fluid's volume is concentrated.

The **center of gravity** (G) is the point through which the body's weight acts — the centroid of the mass distribution. The **center of buoyancy** (B) is the point through which the buoyant force acts — the centroid of the displaced fluid volume. In equilibrium, these two points lie on the same vertical line, with the buoyant force acting upward through B and gravity acting downward through G. For a fully submerged body, B must be directly above G for stable equilibrium; if B is below G, any tilt causes a capsizing moment. For floating bodies, the situation is more forgiving because B can move.

When a floating body tilts, the shape of the displaced volume changes, so the **center of buoyancy shifts** toward the side that sinks deeper. The buoyant force now acts along a new vertical line through the shifted B. The point where this new line of action intersects the original vertical axis through the body's centerline is the **metacenter** (M). If M lies above G, the shifted buoyant force creates a restoring couple that rights the body — this is stable equilibrium. If M lies below G, the couple tips the body further — this is unstable. The distance GM is the **metacentric height**: positive means stable, negative means unstable, and larger positive GM means more vigorous self-righting.

Geometry governs where M ends up. Wide, low-profile bodies have their center of buoyancy shift dramatically when tilted — B moves far to the tilted side, placing M high above G. This is why flat-bottomed barges are so stable. Narrow, tall bodies (a log standing upright, a narrow sailboat hull) shift B very little on tilt, so M barely rises above B, and if G is already high (masts, cargo, passengers), GM can go negative. This is why container ships monitor their stability calculations obsessively — adding deck cargo raises G, potentially inverting the GM sign.

Engineers control stability by lowering G through ballast (heavy material placed low in the hull), widening the hull form, and restricting the height of heavy cargo. Naval architects compute the metacentric height as GM = KB + BM − KG, where K is the keel, BM = I/V (second moment of the waterplane area divided by displaced volume), and each term has a direct physical meaning. A ship's intact stability curve — GM as a function of tilt angle — is regulated by maritime authorities. The core intuition remains: stability is not about where the buoyant force acts in equilibrium, but about how that force's line of action moves when the body is disturbed.
