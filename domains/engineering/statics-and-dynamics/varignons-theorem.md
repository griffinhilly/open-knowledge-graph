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
status: validated
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

## Explainer

You already know that the moment of a force about a point is the cross product M_O = r × F, with magnitude Fd⊥ where d⊥ is the perpendicular distance from point O to the force's line of action. The problem in practice is that d⊥ can be geometrically messy — when the force acts at an angle and the geometry involves multiple dimensions, finding the exact perpendicular distance requires trigonometry that is easy to set up incorrectly. Varignon's theorem is the shortcut: you never have to find d⊥ directly.

The theorem follows from the distributive property of the cross product over vector addition. If F = Fx î + Fy ĵ, then r × F = r × (Fx î) + r × (Fy ĵ). Each component force is horizontal or vertical, so its perpendicular distance to any conveniently placed point is simply a horizontal or vertical coordinate. The moment of a horizontal force Fx acting at height y from O is just Fx · y. The moment of a vertical force Fy acting at horizontal distance x from O is just Fy · x. Sum the two, applying correct signs, and you have the total moment — no awkward perpendicular distance calculation required.

The sign rule is critical: use a consistent positive-rotation convention (typically counterclockwise positive) and apply it to every component separately. Fx creates a moment with lever arm equal to the y-coordinate of the force's point of application; Fy creates a moment with lever arm equal to the x-coordinate. A common strategy is to pick the reference point O at the foot of the force's mounting (an anchor pin, a wall attachment) so that one component's lever arm vanishes entirely, reducing the problem to a single multiplication.

Varignon's theorem connects back to your earlier work on force resultants. When you replace a distributed load with a single resultant force, you require that the resultant produce the same moment about every point as the original distribution — this is enforced using the moment equivalence that Varignon's theorem helps verify. For equivalent force systems, you'll extend this idea: two force systems are statically equivalent if and only if they produce the same resultant force and the same total moment about any chosen point. Varignon's theorem gives you the computational tool to check or construct those moment conditions without wrestling with awkward geometry.

Practice the theorem by choosing the point O to be as convenient as possible. If the force is applied at the end of an angled member, O placed at the pin joint means the position vector r is just the member itself — its x and y components directly become the moment arms for the two force components. This pin-joint-as-origin strategy appears constantly in truss and frame analysis and in equilibrium problems for rigid bodies: your two upcoming builds-toward topics lean heavily on exactly this combination of force decomposition and moment calculation.

