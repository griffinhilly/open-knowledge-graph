---
id: bifurcation-theory-transcritical-pitchfork
title: Transcritical and Pitchfork Bifurcations
domain: physics
course: nonlinear-dynamics
prerequisites:
- id: bifurcation-theory-saddle-node
  type: hard
builds-toward:
- hopf-bifurcation
- pattern-formation-turing
tags:
- transcritical
- pitchfork
- symmetry-breaking
- bifurcation
stage: advanced
status: validated
---

# Transcritical and Pitchfork Bifurcations

## Core Idea
The transcritical bifurcation (normal form ẋ = rx - x²) occurs when two fixed points exchange stability as a parameter crosses a critical value — neither is created nor destroyed. The pitchfork bifurcation (normal form ẋ = rx - x³ for supercritical, ẋ = rx + x³ for subcritical) occurs in systems with symmetry: a symmetric fixed point loses stability and two new symmetric fixed points emerge (or vice versa). Both require structural conditions that the saddle-node does not — the transcritical requires a fixed point to exist for all parameter values, and the pitchfork requires x → -x symmetry.

## Questions

```yaml
- question: "In the transcritical bifurcation ẋ = rx - x², x = 0 is always a fixed point. What happens at r = 0?"
  type: multiple-choice
  options:
    - "The fixed point at x = 0 disappears"
    - "A new fixed point is created at x = 0"
    - "The fixed points x = 0 and x = r exchange stability — for r < 0, x = 0 is stable and x = r is unstable; for r > 0, x = 0 becomes unstable and x = r becomes stable"
    - "Both fixed points become stable simultaneously"
  answer: 2
  explanation: "The two fixed points of ẋ = rx - x² = x(r - x) are x = 0 and x = r. For r < 0, the eigenvalue at x = 0 is r < 0 (stable) and at x = r it's -r > 0 (unstable). For r > 0, the eigenvalue at x = 0 is r > 0 (unstable) and at x = r it's -r < 0 (stable). At r = 0, the fixed points collide and exchange stability. Neither is created or destroyed — they pass through each other on the bifurcation diagram."

- question: "The supercritical pitchfork bifurcation ẋ = rx - x³ models a system that spontaneously breaks symmetry. Which physical scenario best illustrates this?"
  type: multiple-choice
  options:
    - "A ball rolling in a single-well potential that gradually deepens"
    - "An Euler column under increasing compressive load — below the critical load, the straight configuration is stable; above it, the column buckles to one side or the other"
    - "A pendulum with increasing friction that gradually stops oscillating"
    - "A chemical reaction that reaches equilibrium faster as temperature increases"
  answer: 1
  explanation: "The Euler buckling problem has perfect x → -x symmetry (buckling left or right are equally likely). Below the critical load, the symmetric (straight) state is stable. Above it, the straight state becomes unstable and two stable buckled states appear symmetrically. This is exactly the supercritical pitchfork: one symmetric equilibrium loses stability and bifurcates into two asymmetric stable equilibria plus the now-unstable original. The symmetry of the problem dictates the pitchfork structure."

- question: "A subcritical pitchfork bifurcation is more dangerous than a supercritical one because the emerging branches are unstable, leaving no nearby stable state after the bifurcation."
  type: true-false
  answer: true
  explanation: "In a supercritical pitchfork, the new branches born at the bifurcation are stable — the system transitions smoothly to a nearby asymmetric state. In a subcritical pitchfork, the new branches are unstable. When the symmetric state loses stability, there is no nearby stable equilibrium to catch the system. The state must jump to a distant attractor, often resulting in a sudden, large-amplitude transition. This makes subcritical bifurcations associated with catastrophic events, similar to the saddle-node."

- question: "Why can't a pitchfork bifurcation occur in a generic system without symmetry?"
  type: short-answer
  answer: "The pitchfork requires f(x) = -f(-x) symmetry so that whenever x* is a fixed point, -x* is also one. Without this symmetry, small perturbations break the pitchfork into a saddle-node plus an isolated branch — the two branches no longer meet at the same point. Generically, the cubic term x³ that creates the pitchfork requires the quadratic term x² to vanish, which only happens when the system has the x → -x symmetry. Breaking the symmetry 'unfolds' the pitchfork into structurally stable components."
  explanation: "This is the concept of structural stability and unfolding. The pitchfork is structurally unstable — adding a small asymmetric perturbation (like εx²) destroys the simultaneous creation of two branches. In applications, perfect pitchforks are rare unless enforced by physical symmetry (like left-right symmetry in buckling, or up-down symmetry in convection). Imperfect pitchforks, where slight asymmetry disconnects the branches, are more common in practice."
```

## Explainer

The saddle-node bifurcation is generic — it happens without any special conditions. The transcritical and pitchfork bifurcations are more specialized: they require structural features that constrain which fixed points exist and how they interact. Understanding what conditions produce each bifurcation type is essential for recognizing them in physical systems and for understanding why some transitions are smooth and others are catastrophic.

The **transcritical bifurcation** occurs when a fixed point must exist for all parameter values — typically because x = 0 represents a physically meaningful state that can't disappear (like zero population in ecology, or zero infection in epidemiology). The normal form ẋ = rx - x² always has x = 0 as a fixed point, plus x = r. As r passes through zero, these two fixed points collide and exchange stability. For r < 0, the origin is stable and x = r is unstable; for r > 0, the origin becomes unstable and x = r becomes the stable attractor. No fixed points are created or destroyed — they just trade roles. This is less dramatic than the saddle-node because a stable state always exists; the system transitions smoothly from one equilibrium to another.

The **pitchfork bifurcation** requires symmetry: the system must be unchanged under x → -x (meaning f(-x) = -f(x), so f has only odd powers of x). The supercritical normal form ẋ = rx - x³ has a single fixed point at x = 0 for r < 0 (stable), which becomes unstable at r = 0 while two new stable fixed points x = ±√r emerge for r > 0. The system spontaneously breaks symmetry — both branches are equally valid, and which one the system chooses depends on tiny perturbations. This is the mechanism behind phase transitions in physics (like ferromagnetic ordering below the Curie temperature) and symmetry-breaking in pattern formation.

The subcritical pitchfork (ẋ = rx + x³) is its dangerous cousin. Here, unstable fixed points x = ±√(-r) exist for r < 0 and disappear at r = 0. When the origin loses stability at r = 0, there are no nearby stable states to catch the system — it must jump to a distant attractor. This produces a sudden, hysteretic transition rather than a gradual one. The distinction between supercritical (soft, continuous) and subcritical (hard, discontinuous) bifurcations recurs throughout nonlinear dynamics: it appears again in the Hopf bifurcation and in the onset of turbulence, and it determines whether transitions in real systems are gentle or catastrophic.
