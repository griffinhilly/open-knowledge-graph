---
id: black-holes-schwarzschild
title: Black Holes (Schwarzschild)
domain: physics
course: general-relativity
prerequisites:
- id: schwarzschild-solution
  type: hard
tags:
- black-holes
- event-horizon
- singularity
- schwarzschild
- causal-structure
- kruskal-coordinates
stage: expert
status: validated
---

# Black Holes (Schwarzschild)

## Core Idea
A Schwarzschild black hole forms when a spherically symmetric mass collapses within its Schwarzschild radius r_s = 2GM/c². The event horizon at r = r_s is a one-way causal boundary: particles and light can fall in but nothing can escape. Inside the horizon, the radial coordinate r becomes timelike — all future-directed paths lead inexorably to the singularity at r = 0, which is a moment in the future rather than a place in space. The singularity represents a genuine breakdown of spacetime geometry where curvature diverges. Kruskal-Szekeres coordinates reveal the maximal analytic extension of the Schwarzschild geometry, which includes a white hole and a second asymptotically flat region — though only the black hole exterior and interior are physically realized in gravitational collapse. For a distant observer, an infalling object appears to asymptotically approach the horizon due to extreme gravitational time dilation and redshift, never appearing to cross it in finite coordinate time.

## Questions

```yaml
- question: "Inside the event horizon of a Schwarzschild black hole, the radial coordinate r becomes timelike. What is the physical consequence?"
  type: multiple-choice
  options:
    - "An observer inside can still orbit at constant r if they accelerate hard enough"
    - "All future-directed worldlines lead to decreasing r, making the singularity at r = 0 inevitable regardless of the observer's actions"
    - "The observer experiences time running backward"
    - "The distinction between space and time disappears entirely"
  answer: 1
  explanation: "Inside the horizon, the signs of g_{tt} and g_{rr} swap: r becomes the timelike coordinate and t becomes spacelike. Since all observers must move forward in time (toward decreasing r inside the horizon), reaching r = 0 is as inevitable as reaching tomorrow. No amount of rocket thrust can reverse the inward 'fall' because it is not motion through space but progress through time. The observer's proper time remains well-defined and forward-moving — it is the coordinate roles that have swapped, not the experience of time."

- question: "A distant observer watching an astronaut fall into a Schwarzschild black hole will see the astronaut cross the event horizon in finite time."
  type: true-false
  answer: false
  explanation: "In the distant observer's Schwarzschild coordinate time t, the astronaut asymptotically approaches the horizon but never crosses it. Light signals from the astronaut become increasingly redshifted and delayed — the last photon emitted just before crossing takes (in principle) infinite coordinate time to reach the distant observer. However, the astronaut's own proper time is finite: they cross the horizon and reach the singularity in a finite, often quite short, proper time. The 'infinite time' is a coordinate effect in the distant frame, not a physical barrier."

- question: "Explain why the singularity at r = 0 inside a Schwarzschild black hole is better described as a moment in time than a point in space."
  type: short-answer
  answer: "Inside the horizon, the Schwarzschild coordinate r is timelike (its metric coefficient changes sign from positive to negative). The singularity r = 0 is therefore a surface of constant 'time' — it lies in the future of every observer who has crossed the horizon, regardless of their spatial position or direction of motion. You cannot point toward the singularity or try to avoid it by moving sideways; it is not located at a particular place in space but rather occurs at a particular moment along every possible future worldline. This is fundamentally different from a Newtonian point mass, which occupies a definite spatial location."
  explanation: "This reinterpretation of the singularity is one of the most conceptually striking features of black hole physics. It means that inside the horizon, the question 'where is the singularity?' is ill-posed — the correct question is 'when will I reach it?'"

- question: "What is the maximal analytic extension of the Schwarzschild spacetime, and why is most of it not physically realized?"
  type: short-answer
  answer: "The Kruskal-Szekeres coordinates reveal that the full analytic extension contains four regions: (I) the exterior of the black hole, (II) the black hole interior (future singularity), (III) a 'parallel' asymptotically flat exterior, and (IV) a white hole interior (past singularity). The white hole is the time-reverse of a black hole — matter can emerge from it but nothing can enter. Regions III and IV are connected to I and II through the Einstein-Rosen bridge (wormhole). However, in a realistic gravitational collapse, a star forms the black hole at a finite time, so the spacetime before collapse is not vacuum Schwarzschild. The white hole, the parallel universe, and the wormhole are artifacts of the eternal vacuum solution and are not present in the spacetime of a collapsing star."
  explanation: "The maximal extension is a mathematical curiosity of the exact vacuum solution. Penrose diagrams make the causal structure transparent and show that the wormhole is non-traversable even in the extended solution — no timelike or null path can travel from region I to region III."
```

## Explainer

The Schwarzschild solution describes the spacetime outside any spherically symmetric mass, but its most dramatic implications emerge when the mass is compact enough to be enclosed within its own Schwarzschild radius r_s = 2GM/c². In that case, the vacuum solution extends all the way to r_s, and the surface r = r_s becomes an event horizon — the defining feature of a black hole. The event horizon is not a physical surface or barrier; it is a causal boundary defined by the property that no future-directed causal signal (timelike or null worldline) from inside can reach the exterior. An astronaut crossing the horizon would notice nothing locally unusual — the equivalence principle guarantees that local physics remains that of special relativity at the horizon. The tidal forces (Riemann curvature) at the horizon are finite and, for a sufficiently massive black hole, can even be negligibly small.

The behavior seen by a distant observer is strikingly different. Light emitted by the astronaut near the horizon is gravitationally redshifted by a factor (1 - r_s/r)^{1/2}, which goes to zero at the horizon. The coordinate time between successive light-signal arrivals diverges: the distant observer sees the astronaut slow down, redden, and fade, asymptotically approaching but never quite reaching the horizon. This is a coordinate effect in Schwarzschild time, not a physical freezing — the astronaut's own proper time ticks normally, and they cross the horizon and reach the singularity in finite proper time (of order GM/c³ for a free-fall from rest near the horizon).

Inside the horizon (r < r_s), the character of the coordinates inverts. The metric coefficient g_{tt} = -(1 - r_s/r) becomes positive and g_{rr} = (1 - r_s/r)⁻¹ becomes negative. This means r is now the timelike direction and t is spacelike. Since all observers must move forward in the timelike direction, and r decreases in the future-directed sense inside the horizon, reaching r = 0 is inevitable. No rocket engine, no matter how powerful, can prevent an observer inside the horizon from hitting the singularity — for the same reason that nothing can prevent you from moving forward in time. The singularity at r = 0 is a genuine curvature singularity where the tidal forces (Kretschner scalar R_{μνρσ}R^{μνρσ} = 48G²M²/c⁴r⁶) diverge. General relativity itself breaks down here, and a quantum theory of gravity is presumably needed.

Kruskal-Szekeres coordinates (T, X, θ, φ) provide a coordinate system that is non-singular at the horizon and covers the entire maximal analytic extension of the Schwarzschild geometry. In these coordinates, the horizon at r = r_s becomes a pair of null surfaces (the lines T = ±X), and the spacetime diagram reveals four distinct regions: the exterior (region I), the black hole interior (region II), a second exterior (region III), and a white hole (region IV). The white hole is the time-reverse of the black hole — a singularity in the past from which matter can emerge. Regions I and III are connected by a non-traversable wormhole (Einstein-Rosen bridge). For a real astrophysical black hole formed by stellar collapse, only regions I and II are present; the white hole and second exterior are mathematical artifacts of the eternal vacuum solution that are replaced by the collapsing-star interior in a physical spacetime.
