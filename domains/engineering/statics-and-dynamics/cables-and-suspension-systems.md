---
id: cables-and-suspension-systems
title: Analysis of Cables and Suspension Systems
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: distributed-loads-beams
  type: hard
- id: equilibrium-particles-2d
  type: hard
tags:
- cables
- suspension
- parabolic
- catenary
stage: formal-systems
status: draft
---

# Analysis of Cables and Suspension Systems

## Core Idea
Cables that support uniformly distributed loads (like their own weight) hang in a parabolic shape and can be analyzed using distributed load concepts. Cables supporting point loads hang in straight segments between loads. The horizontal tension in a cable is constant throughout, while vertical components vary depending on the load distribution and geometry.

## How It's Best Learned
Analyze symmetric cable configurations first (like suspension bridges with uniform loading), then progress to asymmetric cases. Use moment equations about a point to relate geometry and load to tension.

## Questions

```yaml
- question: "A symmetric suspension bridge cable hangs between two towers with a uniformly distributed deck load. You have calculated the horizontal tension T₀ at the lowest point. Where is the total cable tension T greatest?"
  type: multiple-choice
  options:
    - "At the midpoint (lowest point) of the cable, where the vertical load is most concentrated"
    - "At the quarter-span points, where bending stress is typically maximum in beams"
    - "At the supports (top of the towers), where the cable angle is steepest"
    - "Total tension is constant throughout because horizontal tension is constant"
  answer: 2
  explanation: "Total cable tension at any point is T = T₀/cos(θ), where θ is the angle of the cable from horizontal. At the lowest point, θ = 0 and T = T₀ (minimum tension). As you move toward the supports, the cable angle steepens, cos(θ) decreases, and T increases. Maximum tension always occurs at the supports where the cable is steepest. This is a common error: students confuse 'constant horizontal tension' with 'constant total tension.' Only the horizontal component is constant — the total tension varies with slope."

- question: "A cable supports three point loads hanging at equal horizontal spacings. To find the tension in the middle segment, you should:"
  type: multiple-choice
  options:
    - "Apply the parabolic cable formula y = x²w/(2T₀) using the distributed load equivalent"
    - "Use the catenary equation since the cable's own weight dominates with point loads"
    - "Cut the cable at the middle segment, draw a free-body diagram, and apply ΣFx = 0, ΣFy = 0 using the known geometry and support reactions"
    - "Set the middle segment tension equal to T₀ because horizontal tension is constant"
  answer: 2
  explanation: "For cables with discrete point loads, each segment is straight and the analysis uses equilibrium on free-body diagrams, not continuous load formulas. You find support reactions first using overall equilibrium, then cut at each segment and apply the equilibrium equations. The horizontal component of tension is constant across segments, but the segment angle changes at each load point — so you must use the actual geometry (angles) to find total tensions. Parabolic and catenary formulas apply to continuously distributed loads, not point loads."

- question: "The horizontal component of tension is the same at every point along a cable, regardless of loading type or cable shape."
  type: true-false
  answer: true
  explanation: "This is the fundamental result of cable analysis. Because a flexible cable can carry no bending moment or shear — only tension along its tangent — applying ΣFx = 0 to any free-body diagram cut anywhere along the cable always yields the same horizontal tension T₀. This is true for parabolic cables (uniform horizontal load), catenary cables (self-weight), and piecewise-linear cables (point loads). The shape changes, but the horizontal component is invariant throughout."

- question: "A cable hanging under its own weight takes a parabolic shape because the self-weight is uniformly distributed per unit horizontal distance."
  type: true-false
  answer: false
  explanation: "This is a common confusion between two physically different loading cases. A cable under its own weight hangs in a **catenary** — a hyperbolic cosine curve — because self-weight is distributed uniformly along the arc length of the cable, not per unit horizontal distance. A **parabola** results when the load is uniform per unit horizontal distance, which is the case for a suspension bridge deck where the hangers are evenly spaced horizontally. For small sag-to-span ratios, a catenary is well-approximated by a parabola, which is why the distinction is sometimes glossed over in engineering practice."

- question: "Why does knowing the horizontal tension T₀ at one point (like the cable's lowest point) allow you to find the total tension at any other point along the cable?"
  type: short-answer
  answer: "Because the horizontal component of tension is constant throughout the cable, T₀ measured at any one point equals T₀ everywhere. The total tension at any other point is T = T₀/cos(θ), where θ is the cable's slope angle at that point. So once you know T₀ — typically from the geometry at the lowest point where the cable is horizontal and θ = 0 — you can find the tension anywhere by determining the local slope angle. This makes T₀ the anchor of the entire solution: all other tensions, geometry, and load relationships flow from this single quantity."
  explanation: "The invariance of horizontal tension is a direct consequence of the cable being unable to carry bending moment. Every free-body diagram cut, regardless of location, yields ΣFx = 0 with the same T₀. This transforms a seemingly complex distributed problem into a structured calculation: find T₀ from geometry at a convenient point, then derive all other quantities from it."
```

## Explainer

The key to cable analysis is recognizing what is constant and what varies along the cable. Because a flexible cable can transmit no bending moment or shear — it can only pull — every internal force along the cable is purely tensile and directed along the cable's tangent. This constraint, combined with your equilibrium skills, produces a powerful result: the **horizontal component of tension** is the same at every point along the cable. Think of it as the "throughput" of horizontal force that must be consistent end-to-end for equilibrium.

The shape a cable takes depends on how the load is distributed. When a cable supports a load that is **uniform per unit horizontal distance** (like the deck of a suspension bridge, where hangers are evenly spaced horizontally), the cable hangs in a **parabolic** shape. You can derive this by applying the distributed-load analysis you already know: cut the cable at position x, replace the distributed load with its resultant, and write ΣFx = 0 and ΣFy = 0 for the free-body diagram. The result is a second-order differential equation whose solution is a parabola y = x²·w/(2T₀), where w is load per unit length and T₀ is the horizontal tension. When a cable supports only its own weight — distributed uniformly along its arc length rather than horizontally — the true shape is a **catenary**, a hyperbolic cosine curve. For many engineering problems the parabola is a sufficient approximation when the sag is small relative to the span.

For cables loaded by **discrete point loads**, the geometry is even simpler: the cable forms a series of straight segments connecting the load application points. Between loads, there is no distributed force, so each segment must be straight. Your approach here uses moment equations: write equilibrium for the entire cable, find support reactions, then cut at each joint and apply ΣFx = 0, ΣFy = 0. The angles of the segments set the geometry, and the horizontal tension threads consistently through every segment.

The practical payoff of constant horizontal tension is computational leverage. Once you determine T₀ — typically from the geometry at one known point, such as the lowest point of a symmetric cable — you have a fixed quantity that connects every other calculation. The total tension at any point is T = T₀/cos(θ), where θ is the local slope angle. Maximum tension always occurs at the supports, where the cable is steepest. This hierarchy — find T₀ from geometry, derive everything else from T₀ — is the standard solution pathway for all cable problems, whether parabolic, catenary, or piecewise-linear.
