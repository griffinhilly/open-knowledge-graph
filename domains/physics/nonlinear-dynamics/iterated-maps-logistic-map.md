---
id: iterated-maps-logistic-map
title: Iterated Maps and the Logistic Map
domain: physics
course: nonlinear-dynamics
prerequisites:
- id: fixed-points-and-stability
  type: hard
- id: chaos-definition-and-properties
  type: hard
builds-toward:
- period-doubling-route-to-chaos
- smale-horseshoe
tags:
- logistic-map
- iterated-maps
- discrete-dynamics
- cobweb-diagram
stage: expert
status: validated
---

# Iterated Maps and the Logistic Map

## Core Idea
An iterated map x_{n+1} = f(x_n) defines a discrete dynamical system where the state updates in steps rather than flowing continuously. The logistic map x_{n+1} = rx_n(1 - x_n) is the simplest example that exhibits the full range of nonlinear phenomena: fixed points, period doubling, chaos, and periodic windows — all in one dimension. Unlike continuous flows, where chaos requires at least three dimensions (by Poincare-Bendixson), discrete maps can be chaotic in just one dimension because the non-crossing constraint doesn't apply.

## Questions

```yaml
- question: "The logistic map x_{n+1} = rx_n(1 - x_n) has a fixed point at x* = 1 - 1/r for r > 1. This fixed point is stable when |f'(x*)| < 1. For what range of r is it stable?"
  type: multiple-choice
  options:
    - "1 < r < 2"
    - "1 < r < 3"
    - "All r > 1"
    - "r > 3"
  answer: 1
  explanation: "f'(x) = r(1 - 2x). At x* = 1 - 1/r, f'(x*) = r(1 - 2(1 - 1/r)) = r(2/r - 1) = 2 - r. Stability requires |2 - r| < 1, which gives 1 < r < 3. At r = 3, the fixed point loses stability (|f'(x*)| = 1) and a period-2 cycle is born via a period-doubling bifurcation. Below r = 1, the fixed point at 0 is the only attractor."

- question: "Why can a one-dimensional map like the logistic map exhibit chaos, even though a one-dimensional continuous ODE ẋ = f(x) cannot?"
  type: multiple-choice
  options:
    - "One-dimensional maps can't actually be chaotic — only higher-dimensional maps can"
    - "The discrete time step allows the map to 'jump' over barriers that would block a continuous trajectory. In a continuous 1D flow, a trajectory moving right can't reverse without passing through a fixed point. In a discrete map, x_{n+1} can be anywhere the map sends it — there's no continuity constraint between successive states that prevents folding."
    - "One-dimensional ODEs can also be chaotic; the claim that they can't is incorrect"
    - "The logistic map is actually a hidden two-dimensional system"
  answer: 1
  explanation: "In a continuous 1D flow, the uniqueness theorem and the intermediate value theorem trap trajectories — they can't cross fixed points, so they must monotonically approach a fixed point or diverge. A discrete map has no such constraint: f can fold the interval back on itself (like x → 4x(1-x), which maps [0,1] → [0,1] non-monotonically). This folding is the mechanism that creates chaos. The map stretches (the slope |f'| > 1 in some regions) and folds (the interval gets mapped non-monotonically), producing sensitive dependence and mixing in just one dimension."

- question: "At r = 4, the logistic map x_{n+1} = 4x(1-x) maps [0,1] onto [0,1] and is fully chaotic. The trajectory of almost every initial condition is dense in [0,1]."
  type: true-false
  answer: true
  explanation: "At r = 4, the logistic map is conjugate to the tent map and to the doubling map, both known to be fully chaotic on [0,1]. The Lyapunov exponent is λ = ln 2 ≈ 0.693 > 0. Almost every orbit (in the measure-theoretic sense) is dense in [0,1] — it visits every subinterval, no matter how small, given enough iterations. The invariant measure is the arcsine distribution ρ(x) = 1/(π√(x(1-x))), which concentrates near 0 and 1 where the map spends more time."

- question: "What is a cobweb diagram and how does it help visualize the dynamics of an iterated map?"
  type: short-answer
  answer: "A cobweb diagram plots y = f(x) and y = x on the same axes. Starting from x₀ on the x-axis, draw vertically to the curve y = f(x₀), then horizontally to the line y = x (which converts the output back to an input). Repeat. The resulting staircase or spiral pattern shows whether the iteration converges to a fixed point (spiral inward), diverges (spiral outward), or exhibits more complex behavior. Fixed points occur where y = f(x) crosses y = x. The cobweb makes stability visually apparent: if |f'(x*)| < 1, the cobweb spirals in; if |f'(x*)| > 1, it spirals out."
  explanation: "For the logistic map with r = 2.5, the cobweb spirals into the stable fixed point x* = 0.6. For r = 3.2, it oscillates between two values (period-2 orbit). For r = 4, the cobweb bounces chaotically throughout [0,1]. The cobweb diagram is the discrete-time analog of a phase portrait — it shows the complete qualitative dynamics at a glance."
```

## Explainer

Continuous flows and discrete maps are the two fundamental types of dynamical systems. You've been studying flows — systems where time is continuous and the state evolves according to differential equations. Iterated maps are the discrete counterpart: the state updates in discrete steps according to x_{n+1} = f(x_n). Maps arise naturally as Poincare sections of continuous flows (sample the flow once per cycle), as models in ecology (non-overlapping generations), and as mathematical laboratories for chaos (because they can exhibit chaos in just one dimension, making visualization and analysis far simpler than 3D flows).

The logistic map x_{n+1} = rx_n(1 - x_n) is the central example. It models population growth with a carrying capacity: x represents the population fraction (between 0 and 1), r is the growth rate, and the (1 - x) factor models crowding. For small r, the population settles to a stable equilibrium — the map has an attracting fixed point. As r increases past 3, this fixed point loses stability and a period-2 cycle appears: the population oscillates between two values every other generation. Further increase yields period-4, period-8, and so on — a cascade of period-doubling bifurcations that accelerates and culminates in chaos at r ≈ 3.57.

The transition from order to chaos in the logistic map is remarkable for its universality and its richness. Beyond the onset of chaos, the bifurcation diagram shows periodic windows — islands of order within the chaos where the system temporarily locks into periodic behavior. The most prominent is the period-3 window near r ≈ 3.83. The theorem "period 3 implies chaos" (Sharkovskii's theorem, generalized) says that a one-dimensional continuous map with a period-3 orbit must have periodic orbits of every integer period — and must also have uncountably many chaotic orbits. The logistic map packs an astonishing amount of mathematical structure into a single one-dimensional equation.

What makes maps different from flows is the absence of the continuity constraint that prevents trajectory crossing. In a one-dimensional flow, a trajectory moving to the right cannot reverse direction without hitting a fixed point (where ẋ = 0). In a map, x_{n+1} can be anywhere — the map can fold the interval back on itself, sending nearby points far apart and distant points close together. This folding is the discrete-time analog of stretching and folding in continuous flows, and it is what makes one-dimensional chaos possible. The logistic map at r = 4 is fully chaotic: its Lyapunov exponent is ln 2, every orbit is either periodic or dense in [0,1], and nearby initial conditions diverge at an exponential rate.
