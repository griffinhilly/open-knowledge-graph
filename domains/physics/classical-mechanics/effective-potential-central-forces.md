---
id: effective-potential-central-forces
title: Effective Potential in Central Force Motion
domain: physics
course: classical-mechanics
prerequisites:
- id: angular-momentum
  type: hard
- id: total-mechanical-energy-conservation
  type: hard
- id: newtons-law-of-gravitation
  type: soft
builds-toward:
- orbital-stability-mechanics
- orbital-mechanics
tags:
- central-forces
- effective-potential
- orbits
stage: formal-systems
status: draft
---

# Effective Potential in Central Force Motion

## Core Idea
For central force motion, the centrifugal effect can be included as an effective potential U_eff = U(r) + L²/(2mr²), converting a two-dimensional problem into an equivalent one-dimensional radial motion. This allows graphical analysis of orbits.

## How It's Best Learned
Plot effective potentials for gravity and springs. Identify turning points, circular orbits, and escape conditions. Compare with true trajectories in the full 2D space.

## Common Misconceptions
The centrifugal force is not real but an artifact of using energy in the radial direction. The effective potential works in the center-of-mass frame where total momentum is zero.

## Explainer

From conservation of energy you know that for a particle moving in a potential, the total mechanical energy E = ½mv² + U(r) is constant. From angular momentum you know that for a central force (one directed along the line connecting two bodies), angular momentum L = mr²ω is also conserved. Together these two conserved quantities let you dramatically simplify orbital problems. The key insight is to use L to eliminate the angular part of the motion entirely, reducing a two-dimensional problem to an equivalent one-dimensional one in the radial coordinate r alone.

Start from the total kinetic energy. Because velocity has both a radial component (dr/dt) and a tangential component (rω = rθ̇), the kinetic energy splits into two parts: ½m(dr/dt)² + ½mr²ω². Since L = mr²ω, we can write the tangential kinetic energy as L²/(2mr²). The total energy is then E = ½m(dr/dt)² + L²/(2mr²) + U(r). Gathering everything that depends on r into a single function defines the **effective potential**: U_eff(r) = U(r) + L²/(2mr²). The term L²/(2mr²) is called the **centrifugal barrier** — it acts like a repulsive potential that grows very large as r → 0, preventing the particle from reaching the origin (as long as L ≠ 0). With this substitution, the energy equation looks exactly like a one-dimensional particle: E = ½m(dr/dt)² + U_eff(r). All the angular complexity is encoded in U_eff.

This reduction has immediate graphical payoff. Plot U_eff(r) as a function of r, and draw a horizontal line at height E. The motion in r is confined to regions where E ≥ U_eff(r) — anywhere U_eff exceeds E is energetically forbidden. **Turning points** are where the horizontal E-line intersects U_eff — the radial velocity is zero there and the particle reverses direction in r. For a gravitational potential U(r) = −GMm/r, the effective potential has a characteristic shape: the attractive −1/r term dominates at large r while the repulsive centrifugal L²/2mr² term dominates at small r, producing a minimum at a particular radius r₀. A particle with exactly E = U_eff(r₀) moves at constant r — this is a **circular orbit**. A particle with slightly higher energy oscillates in r between two turning points — this corresponds to an elliptical orbit. If E ≥ 0, there is only one turning point and the orbit is hyperbolic (or parabolic at exactly E = 0): the particle comes in from infinity, swings around, and escapes to infinity. Reading off orbit types directly from the shape of U_eff, without solving differential equations, is one of the most powerful tools in orbital mechanics.
