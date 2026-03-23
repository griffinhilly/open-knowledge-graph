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
status: validated
---

# Effective Potential in Central Force Motion

## Core Idea
For central force motion, the centrifugal effect can be included as an effective potential U_eff = U(r) + L²/(2mr²), converting a two-dimensional problem into an equivalent one-dimensional radial motion. This allows graphical analysis of orbits.

## How It's Best Learned
Plot effective potentials for gravity and springs. Identify turning points, circular orbits, and escape conditions. Compare with true trajectories in the full 2D space.

## Common Misconceptions
The centrifugal force is not real but an artifact of using energy in the radial direction. The effective potential works in the center-of-mass frame where total momentum is zero.

## Questions

```yaml
- question: "For a particle moving under gravity with nonzero angular momentum, what happens to the radial motion as r → 0?"
  type: multiple-choice
  options:
    - "The particle spirals into the center because gravity is attractive"
    - "The centrifugal barrier L²/(2mr²) grows without bound, making small r energetically inaccessible"
    - "The particle oscillates through the origin in harmonic motion"
    - "Nothing special happens — radial motion continues unchanged toward smaller r"
  answer: 1
  explanation: "The centrifugal barrier term L²/(2mr²) grows as r → 0 (like 1/r²), which is stronger than the gravitational attraction −GMm/r. For any nonzero angular momentum, the effective potential diverges to +∞ at small r, creating an energetically forbidden region near the origin. This is why planets do not spiral into the Sun despite gravity being attractive: angular momentum prevents radial collapse. Only if L = 0 (purely radial motion) does the particle actually reach r = 0."

- question: "A particle moving in a gravitational potential has total energy E = U_eff(r_min), where r_min is the location of the minimum of the effective potential. What kind of orbit does this describe?"
  type: multiple-choice
  options:
    - "A hyperbolic orbit — the particle has enough energy to escape"
    - "An elliptical orbit — the particle oscillates between two turning points"
    - "A circular orbit — the particle moves at constant radius"
    - "A parabolic orbit — the particle just barely escapes to infinity"
  answer: 2
  explanation: "The minimum of U_eff is the point where dU_eff/dr = 0 — where centrifugal and gravitational forces balance, so the net radial force is zero. If E exactly equals U_eff at this minimum, the horizontal energy line just touches the curve; there is only one radial position the particle can occupy, meaning r is constant. That is a circular orbit. For E slightly above the minimum, there are two turning points and the orbit is elliptical. For E ≥ 0, there is one turning point at large r and the orbit is hyperbolic or parabolic."

- question: "The effective potential U_eff = U(r) + L²/(2mr²) represents a real physical force acting on the particle in addition to the central force."
  type: true-false
  answer: false
  explanation: "The centrifugal barrier L²/(2mr²) is not a real force — it is a mathematical artifact of using conservation of angular momentum to eliminate the tangential velocity and reduce the problem to one radial dimension. The particle is subject only to the actual central force (e.g., gravity). The effective potential is a computational tool that encodes all r-dependent physics, not a new physical interaction."

- question: "If angular momentum L doubles while total energy E stays the same, a gravitationally bound orbit will become more tightly bound (smaller semi-major axis)."
  type: true-false
  answer: false
  explanation: "Doubling L raises the centrifugal barrier everywhere, lifting the entire effective potential curve and shifting its minimum to a larger radius. If E is held fixed, the inner turning point moves outward (the barrier pushes the particle away from the center), resulting in a more extended orbit, not a more compact one. More angular momentum generally means a wider, less tightly bound orbit shape."

- question: "Explain how the effective potential reduces a two-dimensional orbital problem to a one-dimensional problem, and what physical insight this reveals about orbit types."
  type: short-answer
  answer: "Conservation of angular momentum (L = mr²ω) lets us write the tangential kinetic energy ½mr²ω² as L²/(2mr²), a function of r alone. Adding this to U(r) gives U_eff(r) = U(r) + L²/(2mr²). The total energy equation becomes E = ½m(dr/dt)² + U_eff(r) — identical in form to a 1D particle in potential U_eff. Plotting U_eff versus r and drawing a horizontal line at energy E immediately reveals the orbit type: two intersections mean elliptical, one tangent at the minimum means circular, one intersection at large r means hyperbolic."
  explanation: "The key is that angular momentum conservation removes one degree of freedom exactly. The angular coordinate θ is hidden inside the constant L, so only r needs tracking. Orbit classification becomes a graphical exercise rather than a differential-equations problem — a major analytical payoff from identifying the right conserved quantity."
```

## Explainer

From conservation of energy you know that for a particle moving in a potential, the total mechanical energy E = ½mv² + U(r) is constant. From angular momentum you know that for a central force (one directed along the line connecting two bodies), angular momentum L = mr²ω is also conserved. Together these two conserved quantities let you dramatically simplify orbital problems. The key insight is to use L to eliminate the angular part of the motion entirely, reducing a two-dimensional problem to an equivalent one-dimensional one in the radial coordinate r alone.

Start from the total kinetic energy. Because velocity has both a radial component (dr/dt) and a tangential component (rω = rθ̇), the kinetic energy splits into two parts: ½m(dr/dt)² + ½mr²ω². Since L = mr²ω, we can write the tangential kinetic energy as L²/(2mr²). The total energy is then E = ½m(dr/dt)² + L²/(2mr²) + U(r). Gathering everything that depends on r into a single function defines the **effective potential**: U_eff(r) = U(r) + L²/(2mr²). The term L²/(2mr²) is called the **centrifugal barrier** — it acts like a repulsive potential that grows very large as r → 0, preventing the particle from reaching the origin (as long as L ≠ 0). With this substitution, the energy equation looks exactly like a one-dimensional particle: E = ½m(dr/dt)² + U_eff(r). All the angular complexity is encoded in U_eff.

This reduction has immediate graphical payoff. Plot U_eff(r) as a function of r, and draw a horizontal line at height E. The motion in r is confined to regions where E ≥ U_eff(r) — anywhere U_eff exceeds E is energetically forbidden. **Turning points** are where the horizontal E-line intersects U_eff — the radial velocity is zero there and the particle reverses direction in r. For a gravitational potential U(r) = −GMm/r, the effective potential has a characteristic shape: the attractive −1/r term dominates at large r while the repulsive centrifugal L²/2mr² term dominates at small r, producing a minimum at a particular radius r₀. A particle with exactly E = U_eff(r₀) moves at constant r — this is a **circular orbit**. A particle with slightly higher energy oscillates in r between two turning points — this corresponds to an elliptical orbit. If E ≥ 0, there is only one turning point and the orbit is hyperbolic (or parabolic at exactly E = 0): the particle comes in from infinity, swings around, and escapes to infinity. Reading off orbit types directly from the shape of U_eff, without solving differential equations, is one of the most powerful tools in orbital mechanics.
