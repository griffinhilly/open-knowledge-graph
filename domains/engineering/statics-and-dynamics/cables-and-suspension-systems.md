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

## Explainer

The key to cable analysis is recognizing what is constant and what varies along the cable. Because a flexible cable can transmit no bending moment or shear — it can only pull — every internal force along the cable is purely tensile and directed along the cable's tangent. This constraint, combined with your equilibrium skills, produces a powerful result: the **horizontal component of tension** is the same at every point along the cable. Think of it as the "throughput" of horizontal force that must be consistent end-to-end for equilibrium.

The shape a cable takes depends on how the load is distributed. When a cable supports a load that is **uniform per unit horizontal distance** (like the deck of a suspension bridge, where hangers are evenly spaced horizontally), the cable hangs in a **parabolic** shape. You can derive this by applying the distributed-load analysis you already know: cut the cable at position x, replace the distributed load with its resultant, and write ΣFx = 0 and ΣFy = 0 for the free-body diagram. The result is a second-order differential equation whose solution is a parabola y = x²·w/(2T₀), where w is load per unit length and T₀ is the horizontal tension. When a cable supports only its own weight — distributed uniformly along its arc length rather than horizontally — the true shape is a **catenary**, a hyperbolic cosine curve. For many engineering problems the parabola is a sufficient approximation when the sag is small relative to the span.

For cables loaded by **discrete point loads**, the geometry is even simpler: the cable forms a series of straight segments connecting the load application points. Between loads, there is no distributed force, so each segment must be straight. Your approach here uses moment equations: write equilibrium for the entire cable, find support reactions, then cut at each joint and apply ΣFx = 0, ΣFy = 0. The angles of the segments set the geometry, and the horizontal tension threads consistently through every segment.

The practical payoff of constant horizontal tension is computational leverage. Once you determine T₀ — typically from the geometry at one known point, such as the lowest point of a symmetric cable — you have a fixed quantity that connects every other calculation. The total tension at any point is T = T₀/cos(θ), where θ is the local slope angle. Maximum tension always occurs at the supports, where the cable is steepest. This hierarchy — find T₀ from geometry, derive everything else from T₀ — is the standard solution pathway for all cable problems, whether parabolic, catenary, or piecewise-linear.
