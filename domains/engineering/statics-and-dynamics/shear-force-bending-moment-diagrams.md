---
id: shear-force-bending-moment-diagrams
title: Shear Force and Bending Moment Diagrams
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: distributed-loads-beams
  type: hard
- id: support-reactions-beams
  type: hard
- id: internal-forces-members
  type: soft
builds-toward:
- rigid-body-kinetics-force-acceleration
tags:
- statics
- beams
- shear force
- bending moment
- V and M diagrams
stage: formal-systems
status: validated
---
# Shear Force and Bending Moment Diagrams

## Core Idea
Shear force (V) and bending moment (M) diagrams graphically display the internal forces along a beam's length, revealing the locations and magnitudes of maximum internal loading. At any cross section, the internal shear V and moment M are found by summing forces and moments on a free body to one side of the cut. The key differential relationships are dV/dx = -w(x) and dM/dx = V, where w(x) is the distributed load intensity. These relationships mean that the shear diagram is the negative integral of the loading diagram, and the moment diagram is the integral of the shear diagram. Concentrated forces cause jumps in the shear diagram; concentrated couples cause jumps in the moment diagram. The maximum bending moment typically occurs where the shear diagram crosses zero.

## How It's Best Learned
Find all support reactions first, then move along the beam from left to right, constructing the V and M diagrams using the area method: the change in shear between two points equals the negative of the area under the load diagram, and the change in moment equals the area under the shear diagram. Check your work by verifying that V and M both return to zero at the free end (or match the known reaction at the right support).

## Common Misconceptions
- Forgetting the sign convention: the standard convention is that positive shear causes clockwise rotation of the beam element, and positive bending causes the beam to sag (concave up).
- Missing the jump in the moment diagram at the location of an applied couple (external moment).
- Assuming the maximum moment always occurs at midspan — it occurs where V = 0 or changes sign, which depends on the loading configuration.

## Questions

```yaml
- question: "A simply-supported beam carries a single concentrated load that is placed one-third of the way from the left support. Where does the maximum bending moment occur?"
  type: multiple-choice
  options:
    - "At midspan, because that is always the point farthest from both supports"
    - "At the location of the concentrated load, because the shear diagram crosses zero there"
    - "At the left support, because the reaction force is larger for an off-center load"
    - "Evenly distributed between the load point and midspan"
  answer: 1
  explanation: "The maximum bending moment occurs where the shear diagram crosses zero (where dM/dx = V = 0). For a single off-center concentrated load, the shear diagram has a positive constant value from the left support to the load, then jumps down at the load and is negative from there to the right support. The zero-crossing is exactly at the load location — not midspan. Midspan is only the correct answer for a symmetric loading case (e.g., uniform load or central point load on a simply-supported beam)."

- question: "A simply-supported beam carries a uniformly distributed load w (force per unit length) along its entire span. What shape does the shear force diagram take?"
  type: multiple-choice
  options:
    - "Constant (horizontal line) across the span"
    - "Parabolic, because the load intensity is squared in the integral"
    - "Linearly varying, because dV/dx = -w is a constant"
    - "Stepped, with a jump at midspan where shear changes sign"
  answer: 2
  explanation: "The relationship dV/dx = -w(x) means the slope of the shear diagram equals the negative distributed load intensity. For a uniform load, w is constant, so dV/dx is constant — producing a straight line (linear shear diagram). The shear starts at the left reaction (positive), decreases linearly to zero at midspan, and continues to the right reaction (negative). The bending moment diagram, being the integral of the shear diagram, is then parabolic — not the shear diagram itself."

- question: "The maximum bending moment in a beam usually occurs at the midspan of the beam."
  type: true-false
  answer: false
  explanation: "The maximum bending moment occurs where the shear diagram crosses zero (V = 0), which is only at midspan for symmetric loading on a simply-supported beam. For a concentrated load placed off-center, the zero-crossing shifts toward the heavier reaction. For a cantilever beam, the maximum moment is at the fixed support, not midspan. Always locate the zero-crossing of the shear diagram — not midspan — to identify the critical cross-section."

- question: "An applied concentrated couple (external moment) at a point on a beam causes a sudden jump in the bending moment diagram at that location."
  type: true-false
  answer: true
  explanation: "Concentrated forces cause jumps in the shear diagram; concentrated couples (external moments) cause jumps in the bending moment diagram. This follows from the equilibrium equations: summing moments about a cut just before vs. just after the applied couple gives values that differ by the magnitude of the couple. The shear diagram is unaffected at that location (no vertical force is added), but M jumps by the applied couple's magnitude. Forgetting this jump is one of the most common errors in constructing M diagrams."

- question: "Explain why the maximum bending moment in a beam occurs at the location where the shear force is zero."
  type: short-answer
  answer: "The bending moment and shear force are related by dM/dx = V. The maximum of M occurs where its derivative is zero — i.e., where V = 0. This is a direct consequence of calculus: a function reaches a local extremum where its first derivative vanishes. Physically, at the cross-section where shear changes sign, the internal forces on either side are in 'balance' with respect to bending — the tendency to rotate the beam clockwise from the left equals the tendency to rotate it counterclockwise from the right, producing the peak moment."
  explanation: "This relationship is also why the area method works: M changes by the area under the V diagram, and M stops increasing (reaches its peak) when V transitions through zero. In structural design, identifying this location determines which cross-section must be sized to carry the largest bending stress. The flexure formula σ = Mc/I then gives the maximum stress at that critical section."
```

## Explainer

A beam is a structural element designed to carry loads perpendicular to its length. When you apply loads to a beam, the beam's cross-sections push and pull on one another internally to resist those loads. **Shear force** V at a cross-section is the internal force that prevents one part of the beam from sliding vertically past the other; **bending moment** M is the internal couple that prevents the beam from rotating at that section. These internal forces are invisible — you cannot see them — but they determine whether the beam will survive or fail. The V and M diagrams make the distribution of these internal forces visible along the beam's entire length.

The method of sections operationalizes this: pick any cross-section, make a mental cut, and apply equilibrium to the free body on one side of the cut. Your prerequisite on support reactions gives you all the external forces; the internal V and M at the cut are whatever values are required to keep the cut-off portion in equilibrium. This works but is tedious for many cross-sections. The differential relationships dV/dx = −w(x) and dM/dx = V make it systematic: the shear diagram's slope at any point equals the negative of the distributed load intensity there, and the moment diagram's slope equals the shear value there. You do not need to re-cut for every point — you can trace the entire diagram by integration.

The **area method** makes this integration concrete without calculus. Moving from left to right along the beam: the change in shear between two points equals the negative of the area under the load diagram between those points; the change in moment equals the area under the shear diagram. A concentrated force causes a sudden jump in the shear diagram equal to the force magnitude (upward forces jump V upward on the left-to-right convention). A concentrated couple causes a sudden jump in the moment diagram. The shapes are predictable: uniform load produces linearly varying shear and parabolically varying moment; no load produces constant shear and linearly varying moment. Recognizing these shapes lets you sketch diagrams quickly and catch errors.

The most structurally important point is where the maximum bending moment occurs, because bending moment drives the tensile and compressive stresses that cause beams to fracture. The maximum M occurs where dM/dx = V = 0 — where the shear diagram crosses zero. This may be at midspan for a symmetric simply-supported beam with uniform load (the familiar textbook case), but for unsymmetric loading or cantilevered beams the location shifts. Always locate the zero-crossing of the shear diagram before identifying the critical cross-section. In design, the cross-section at maximum M must be sized to carry that bending without exceeding the material's allowable stress — which connects directly to the flexure formula σ = Mc/I that you will use in mechanics of materials.
