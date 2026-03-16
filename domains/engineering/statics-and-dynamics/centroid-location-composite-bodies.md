---
id: centroid-location-composite-bodies
title: Centroid Location in Composite Bodies
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: centroid-areas-composite
  type: soft
builds-toward:
- area-moment-inertia-applications
tags:
- centroid
- center of gravity
- first moment
- composite shapes
- distributed forces
stage: formal-systems
status: draft
---

# Centroid Location in Composite Bodies

## Core Idea
The centroid is the geometric center of an area or volume, found as the first moment of the shape divided by its total area: x_c = ∫x dA / ∫dA. For composite bodies made of standard shapes, the centroid is the weighted average of component centroids, essential for locating where distributed forces (like weight or pressure) act as concentrated resultants.

## Explainer

The centroid is the point at which an entire area (or volume) "balances" — if you hung a flat plate from that point, it would hang perfectly level. You already know from your prerequisite work how to find centroids of simple shapes like rectangles, triangles, and semicircles. The power of the composite method is that you never have to integrate again for those standard shapes: you look up their centroids from a table and use them as inputs to a weighted average.

The key formula is x̄ = (Σ Aᵢ x̄ᵢ) / (Σ Aᵢ), and similarly for ȳ. Think of it as a balance scale where each piece of the shape has both a weight (its area Aᵢ) and a moment arm (its centroid location x̄ᵢ). A large piece near the edge contributes more to pulling the centroid toward that edge than a small piece at the same location would. The composite centroid is simply where all those moment contributions equilibrate.

Cutouts work by treating the removed area as negative. If you have an L-shaped bracket, you can think of it as a rectangle minus a corner rectangle. The negative area reduces both the numerator (Σ Aᵢ x̄ᵢ) and the denominator (Σ Aᵢ) in your weighted-average formula. This is a cleaner approach than subdividing into L-shaped primitives, which have no standard centroid formula. When applying the subtraction method, the centroid of the removed piece is its own geometric center — the shape you cut out "pulls" the final centroid away from where it was removed.

The practical payoff connects directly to the first moment of area concept you built earlier. When engineers analyze beams, slabs, or pressure vessels, distributed forces — gravity acting on a beam's weight, hydrostatic pressure on a dam face, or wind load on a wall panel — don't act at a single point. The centroid tells you where to place the equivalent concentrated resultant force. This is exactly the first moment of area calculation in disguise: ∫x dA divided by ∫dA, but evaluated using the composite method rather than integration. Mastering this procedure is the foundation for computing **area moments of inertia** in your next topic, where the same composite logic applies but squared distances replace the linear ones.

When setting up a composite centroid problem, choose a reference origin systematically — usually a corner or an axis of symmetry — and measure all component centroids from that same origin. Sign errors are the main failure mode: assign consistent positive directions for x and y at the start and apply them uniformly to every piece. Drawing a labeled sketch with each component's centroid marked before writing any numbers dramatically reduces mistakes in complex shapes.

