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
stage: formal-systems
status: validated
---

# Floating Body Stability and Equilibrium

## Core Idea
A floating body is in equilibrium when the buoyant force (weight of displaced fluid) equals the weight of the body. Stability depends on the relative positions of the center of buoyancy and center of gravity; the metacenter determines whether a floating body returns to its original orientation after small disturbances. These principles govern ship design and the behavior of floating structures.

## How It's Best Learned
Float objects of different shapes in water and gently tilt them. Observe how narrow-based objects are unstable (metacenter below center of gravity) while wide-based objects return to upright position (metacenter above center of gravity).

## Common Misconceptions
- A floating body is stable if the center of buoyancy is above the center of gravity (stability depends on the metacenter being above the center of gravity, not the center of buoyancy).
- All floating objects have the same stability (stability depends on geometry and weight distribution, not on the fluid density alone).

## Questions

```yaml
- question: "A narrow cylindrical buoy floats vertically with its center of buoyancy (B) located below its center of gravity (G). What can be correctly concluded about its stability?"
  type: multiple-choice
  options:
    - "It is definitely unstable — buoyancy must act above gravity for a floating body to be stable"
    - "It may still be stable if the metacenter (M) is located above the center of gravity (G)"
    - "It is definitely stable — all floating objects in equilibrium are stable by definition"
    - "It is neutrally stable — B and G being on the same vertical line means the body is in balance"
  answer: 1
  explanation: "The most common misconception is that B must be above G for stability. This is only true for fully submerged bodies. For floating bodies, B can be below G and the body can still be stable — as long as the metacenter M lies above G. When the body tilts, B shifts toward the submerged side, and the line of action of the buoyant force rises to intersect the original centerline at M. If M is above G, this creates a restoring moment. Narrow cylinders often have B below G; their stability depends on whether BM (= I/V) is large enough to raise M above G."

- question: "A ship designer wants to increase a vessel's metacentric height (GM) to improve stability. Which modification most directly achieves this?"
  type: multiple-choice
  options:
    - "Raising heavy machinery from the keel to the upper deck to elevate the center of gravity"
    - "Widening the hull at the waterline to increase the second moment of the waterplane area"
    - "Replacing dense steel plating with lighter aluminum to reduce total displacement"
    - "Increasing the vessel's draft by adding ballast, which lowers the center of buoyancy"
  answer: 1
  explanation: "GM = KB + BM − KG. BM = I/V, where I is the second moment of the waterplane area about the longitudinal axis and V is displaced volume. Widening the hull dramatically increases I (which scales as the cube of half-width), raising BM and therefore M. This is the dominant geometric effect in ship stability — flat-bottomed barges are stable precisely because their wide waterplane creates a large I. Option A raises G, which decreases GM. Options C and D have secondary effects but do not directly target the largest term in BM."

- question: "For a floating body, achieving stable equilibrium requires that the metacenter (M) lie above the center of gravity (G), not merely that the center of buoyancy (B) lie above G."
  type: true-false
  answer: true
  explanation: "This is the core principle. For fully submerged bodies (submarines, balloons), B must be above G — there is no shift of B when the body tilts, so no metacenter. For floating bodies, B shifts when the body tilts, and the metacenter M defines where the resulting buoyant force acts. Stability requires M above G (positive metacentric height GM > 0), regardless of the relative positions of B and G in equilibrium. A body with B below G can be perfectly stable if BM is large enough to raise M above G."

- question: "A floating body that is in equilibrium — meaning the buoyant force exactly equals its weight — is necessarily in stable equilibrium."
  type: true-false
  answer: false
  explanation: "Equilibrium and stability are distinct conditions. Equilibrium simply means net force and net moment are zero. Stability asks what happens when the body is perturbed. A pencil balanced vertically on its tip is in equilibrium but unstable. A floating body is in unstable equilibrium when the metacenter M is below G (negative GM): any tilt creates a capsizing moment that increases the tilt rather than restoring it. Equilibrium is necessary but not sufficient for stability."

- question: "Explain why a wide flat-bottomed barge is more stable than a narrow upright log of the same weight, using the concept of how the center of buoyancy moves when each body is tilted."
  type: short-answer
  answer: "When the barge tilts, its wide bottom means the submerged volume shifts dramatically toward the lower side — the center of buoyancy (B) moves far in the direction of tilt. The line of action of the buoyant force then intersects the original vertical axis at a metacenter (M) high above the center of gravity (G), creating a strong restoring couple that rights the barge. The narrow log, when tilted, shifts very little submerged volume — B moves only slightly, placing M close to B and possibly below G. If G is also elevated (e.g., dense wood floating mostly above water), GM becomes negative and the log is unstable. The key is that wide waterplane area shifts B far on tilt, raising M."
  explanation: "This is captured in the formula BM = I/V, where I is the second moment of the waterplane area. For a rectangle of width w, I scales as w³. Doubling the width multiplies BM by 8, raising M substantially. Ship designers exploit this by preferring wide, low hull forms, and use ballast to lower G when wide hulls aren't possible (e.g., sailing yacht keels)."
```

## Explainer

From Archimedes' principle, you know that a floating body is in equilibrium when the upward buoyant force equals the body's weight — the body sinks until it displaces a volume of fluid whose weight matches its own. But equilibrium and stability are different questions. A pencil balanced on its tip is in equilibrium; it is not stable. Understanding floating body stability requires tracking two centers: where the body's mass is concentrated, and where the displaced fluid's volume is concentrated.

The **center of gravity** (G) is the point through which the body's weight acts — the centroid of the mass distribution. The **center of buoyancy** (B) is the point through which the buoyant force acts — the centroid of the displaced fluid volume. In equilibrium, these two points lie on the same vertical line, with the buoyant force acting upward through B and gravity acting downward through G. For a fully submerged body, B must be directly above G for stable equilibrium; if B is below G, any tilt causes a capsizing moment. For floating bodies, the situation is more forgiving because B can move.

When a floating body tilts, the shape of the displaced volume changes, so the **center of buoyancy shifts** toward the side that sinks deeper. The buoyant force now acts along a new vertical line through the shifted B. The point where this new line of action intersects the original vertical axis through the body's centerline is the **metacenter** (M). If M lies above G, the shifted buoyant force creates a restoring couple that rights the body — this is stable equilibrium. If M lies below G, the couple tips the body further — this is unstable. The distance GM is the **metacentric height**: positive means stable, negative means unstable, and larger positive GM means more vigorous self-righting.

Geometry governs where M ends up. Wide, low-profile bodies have their center of buoyancy shift dramatically when tilted — B moves far to the tilted side, placing M high above G. This is why flat-bottomed barges are so stable. Narrow, tall bodies (a log standing upright, a narrow sailboat hull) shift B very little on tilt, so M barely rises above B, and if G is already high (masts, cargo, passengers), GM can go negative. This is why container ships monitor their stability calculations obsessively — adding deck cargo raises G, potentially inverting the GM sign.

Engineers control stability by lowering G through ballast (heavy material placed low in the hull), widening the hull form, and restricting the height of heavy cargo. Naval architects compute the metacentric height as GM = KB + BM − KG, where K is the keel, BM = I/V (second moment of the waterplane area divided by displaced volume), and each term has a direct physical meaning. A ship's intact stability curve — GM as a function of tilt angle — is regulated by maritime authorities. The core intuition remains: stability is not about where the buoyant force acts in equilibrium, but about how that force's line of action moves when the body is disturbed.
