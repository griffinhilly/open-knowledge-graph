---
id: friction-forces
title: 'Friction: Static and Kinetic'
domain: physics
course: classical-mechanics
prerequisites:
- id: free-body-diagrams
  type: hard
- id: newtons-second-law
  type: hard
- id: newtons-third-law
  type: soft
builds-toward:
- work-and-energy
- conservation-of-energy
tags:
- friction
- static-friction
- kinetic-friction
- normal-force
stage: concrete-operations
status: validated
---
# Friction: Static and Kinetic

## Core Idea
Friction is a contact force that opposes relative sliding motion between surfaces. Static friction (f_s ≤ μ_s N) prevents surfaces from sliding; it adjusts up to its maximum. Kinetic friction (f_k = μ_k N) acts once surfaces are sliding and has a fixed magnitude. Both are proportional to the normal force N through coefficients μ that depend on the materials in contact.

## How It's Best Learned
Solve inclined-plane problems systematically: decompose weight into components parallel and perpendicular to the slope, find N, then compute friction. Check whether the object is on the verge of sliding (use static friction inequality) or already sliding (use kinetic friction equation).

## Common Misconceptions
- Thinking friction always equals μN — static friction only equals μ_s N at its maximum.
- Believing friction always opposes motion: static friction opposes the tendency of motion, which may not align with the direction of motion.
- Assuming μ depends on surface area — it depends on material properties, not contact area.

## Explainer

From your work with free-body diagrams and Newton's second law, you know how to identify forces and apply ΣF = ma. Friction is a contact force that appears at the interface between surfaces — it always acts tangent to the surface (parallel to it), in the direction that opposes relative sliding or the tendency of sliding. Understanding friction requires recognizing that it comes in two fundamentally different regimes depending on whether the surfaces are moving relative to each other.

**Static friction** acts when two surfaces are in contact but not sliding. Its crucial property is that it is *variable*, not fixed. When you push gently on a heavy box and it doesn't move, static friction adjusts to exactly cancel your push — it takes whatever value is needed to maintain equilibrium. Push harder and static friction increases to match. This continues until you reach the maximum static friction force: f_{s,max} = μ_s N, where μ_s is the **coefficient of static friction** and N is the normal force. At that point, if you push any harder, the box starts to slide. Static friction is a **constraint force** — it enforces the constraint that the surfaces don't slide, up to a limit.

Once surfaces are sliding, **kinetic friction** takes over. Unlike static friction, kinetic friction has a single fixed value: f_k = μ_k N, where μ_k is the **coefficient of kinetic friction**. It always acts opposite to the velocity of sliding. Importantly, μ_k < μ_s for most material pairs, which is why it takes more force to start an object sliding than to keep it sliding — you have likely noticed this when pushing furniture. Both coefficients depend only on the materials in contact (wood on wood, rubber on concrete, etc.), not on the contact area or the speed of sliding.

The inclined-plane problem makes these ideas concrete. A block of weight W sits on a slope at angle θ. Decompose W: the component perpendicular to the slope is W cos θ (balanced by the normal force N = W cos θ), and the component parallel to the slope, pulling the block downhill, is W sin θ. The maximum static friction force is μ_s N = μ_s W cos θ. The block slides when the downhill pull exceeds this maximum — when W sin θ > μ_s W cos θ, which simplifies to tan θ > μ_s. This gives the **critical angle**: the steepest slope a block can sit on without sliding, equal to arctan(μ_s). Once sliding, the net force downhill is W sin θ − μ_k W cos θ = W(sin θ − μ_k cos θ), which by Newton's second law gives the acceleration. All of classical friction analysis is built from this one technique: find N, determine which regime applies, compute the friction force, and include it in ΣF = ma.
