---
id: penrose-diagrams
title: Penrose Diagrams
domain: physics
course: general-relativity
prerequisites:
- id: black-holes-schwarzschild
  type: hard
- id: spacetime-diagrams-minkowski
  type: soft
tags:
- penrose-diagram
- conformal-compactification
- causal-structure
- carter-penrose
- infinity
stage: expert
status: validated
---

# Penrose Diagrams

## Core Idea
Penrose diagrams (Carter-Penrose diagrams) are conformal spacetime diagrams that map the entire spacetime — including points at infinity — onto a finite region while preserving the causal structure (light cones at 45 degrees everywhere). They are constructed by a conformal transformation g_μν → Ω²g_μν that compresses infinite distances to finite coordinate ranges, bringing spatial infinity (i⁰), past/future null infinity (J⁻/J⁺), and past/future timelike infinity (i⁻/i⁺) to the boundary of the diagram. Light rays always travel at 45 degrees, timelike curves travel at less than 45 degrees from vertical, and spacelike curves at more than 45 degrees. Penrose diagrams make the global causal structure transparent: event horizons, the black hole interior, white holes, the causal disconnection of separate regions, and the structure of cosmological spacetimes are all immediately visible.

## Questions

```yaml
- question: "On a Penrose diagram, light rays always travel at 45-degree angles. What property of the conformal transformation guarantees this?"
  type: multiple-choice
  options:
    - "The transformation preserves all distances and angles"
    - "The transformation preserves the causal structure (null cones) — a conformal rescaling g_μν → Ω²g_μν does not change which curves are null"
    - "The transformation maps all geodesics to straight lines"
    - "The transformation preserves the Riemann curvature tensor"
  answer: 1
  explanation: "A conformal transformation multiplies the metric by a positive scalar function Ω²(x). Since null curves are defined by ds² = g_μν dx^μ dx^ν = 0, and Ω² > 0 does not change whether this expression vanishes, all null curves remain null under conformal transformations. Light cones are therefore preserved, which is why light rays can always be drawn at 45 degrees. The transformation does change distances, curvature, and the distinction between timelike curves of different proper lengths — but not the causal structure."

- question: "On the Penrose diagram for the maximally extended Schwarzschild spacetime, the singularity at r = 0 appears as a horizontal (spacelike) line."
  type: true-false
  answer: true
  explanation: "The Schwarzschild singularity at r = 0 is spacelike — it lies in the future (or past) of observers who cross the horizon, not at a fixed spatial location. On the Penrose diagram, it appears as a horizontal line at the top of region II (the black hole interior) and at the bottom of region IV (the white hole). Its spacelike character means it cannot be avoided once the horizon is crossed: all future-directed causal paths from inside the horizon terminate at the singularity. This visual representation makes the inevitability of hitting the singularity geometrically obvious."

- question: "Explain how the Penrose diagram of a collapsing star differs from the maximally extended Schwarzschild Penrose diagram."
  type: short-answer
  answer: "The maximally extended Schwarzschild diagram has four regions: exterior (I), black hole interior (II), second exterior (III), and white hole (IV). For a realistic collapsing star, the spacetime before collapse is not vacuum — the star's interior replaces part of the diagram. The left half of the diagram (regions III and IV) is replaced by the interior of the collapsing star, which is described by a different metric (e.g., Oppenheimer-Snyder for a dust collapse). The result is a diagram with only the right exterior (I) and the black hole interior (II), with the star's surface worldline appearing as a timelike curve that crosses the horizon and hits the singularity. The white hole and second exterior are absent because they require the spacetime to have been vacuum for all past time."
  explanation: "This distinction is physically important: the wormhole (Einstein-Rosen bridge) connecting regions I and III in the eternal solution does not exist for a physically formed black hole. Penrose diagrams make this immediately clear by showing which regions of the maximal extension are actually realized."

- question: "Identify and explain the five types of 'infinity' that appear on the boundary of a Penrose diagram for Minkowski spacetime."
  type: short-answer
  answer: "The five types are: (1) Future timelike infinity i⁺ — where all timelike geodesics end (the endpoint of the worldline of any massive particle that exists forever). (2) Past timelike infinity i⁻ — where all timelike geodesics begin. (3) Future null infinity J⁺ (scri-plus) — where all outgoing light rays end. (4) Past null infinity J⁻ (scri-minus) — where all incoming light rays originate. (5) Spatial infinity i⁰ — the single point representing all spatial directions at infinite distance at any given time. On the Penrose diagram for Minkowski space, these form the boundary of a diamond shape: i⁺ at the top vertex, i⁻ at the bottom, i⁰ at the right vertex, J⁺ as the upper-right diagonal edge, and J⁻ as the lower-right diagonal edge."
  explanation: "These five infinities provide a precise language for discussing the global behavior of fields and particles. For example, gravitational radiation is defined by the behavior of the gravitational field at J⁺ (future null infinity), and the Bondi mass measures the total energy remaining after radiation has escaped to J⁺."
```

## Explainer

Ordinary spacetime diagrams have a fundamental limitation: infinity is infinitely far away, so the global causal structure of a spacetime cannot be displayed on a finite diagram. Penrose diagrams solve this by applying a conformal transformation that compresses infinite distances to finite coordinate ranges while preserving the light-cone structure. The idea is to replace the physical metric g_μν with a conformally related metric g̃_μν = Ω²g_μν, where Ω(x) is a positive function that goes to zero at the boundary (at "infinity"). Since ds² = 0 if and only if ds̃² = Ω²ds² = 0, null curves in the original spacetime remain null in the conformally rescaled spacetime. Light rays therefore travel at 45 degrees on the Penrose diagram, just as on a Minkowski spacetime diagram, and the causal relationships between events are immediately readable from the diagram.

For Minkowski spacetime, the Penrose diagram is a diamond (or triangle, if spherical symmetry is used to suppress angular dimensions). The boundary of the diamond represents "infinity" in five distinct senses: future timelike infinity i⁺ (top vertex, where massive particles end up if they travel forever), past timelike infinity i⁻ (bottom vertex), spatial infinity i⁰ (right vertex, infinitely far away in space), future null infinity J⁺ (upper-right edge, where outgoing light rays arrive), and past null infinity J⁻ (lower-right edge, where incoming light rays originate). Every point in the interior of the diamond represents a two-sphere's worth of events (the angular dimensions are suppressed), and every causal relationship in the entire infinite Minkowski spacetime is captured in this finite diagram.

The Penrose diagram for the maximally extended Schwarzschild black hole is one of the most illuminating diagrams in physics. It consists of four triangular regions arranged in a square pattern: region I (the exterior we live in), region II (the black hole interior, bounded above by the spacelike singularity at r = 0), region III (a second asymptotically flat exterior), and region IV (the white hole interior, bounded below by a past singularity). The event horizon appears as a pair of diagonal null lines (45-degree lines) separating these regions. From the diagram, it is immediately clear that no causal curve from region II can reach region I (the definition of the event horizon), that every future-directed curve in region II hits the singularity (because it is a horizontal line at the top, and you cannot avoid moving upward on the diagram), and that no causal curve can travel from region I to region III (the wormhole is non-traversable).

For a realistic black hole formed by gravitational collapse, the Penrose diagram is modified: the left half of the Schwarzschild diagram (regions III and IV) is replaced by the interior of the collapsing star, which is not vacuum. Only regions I and II survive. The star's surface appears as a timelike curve that starts in the lower part of the diagram (before collapse) and eventually crosses the horizon into region II. This modification makes physically clear what the maximal extension obscures: white holes and parallel universes are mathematical artifacts of the eternal vacuum solution, not features of real black holes. Penrose diagrams for other spacetimes — Reissner-Nordstrom (charged), Kerr (rotating), de Sitter (cosmological constant), and Friedmann cosmological models — each have distinctive shapes that immediately communicate their causal structure, making these diagrams an indispensable tool in general relativity.
