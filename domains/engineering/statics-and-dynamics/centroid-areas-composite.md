---
id: centroid-areas-composite
title: Centroids of Areas and Composite Shapes
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: area-of-rectangles
  type: hard
- id: area-of-circles
  type: hard
- id: area-of-triangles
  type: hard
- id: definite-integral-definition
  type: soft
builds-toward:
- area-moment-of-inertia-engineering
tags:
- statics
- centroid
- center of area
- composite areas
stage: formal-systems
status: validated
---

# Centroids of Areas and Composite Shapes

## Core Idea
The centroid of an area is its geometric center, found for composite shapes using x̄ = ΣAᵢx̄ᵢ / ΣAᵢ and ȳ = ΣAᵢȳᵢ / ΣAᵢ, where (x̄ᵢ, ȳᵢ) are centroids and Aᵢ are areas of sub-shapes. Standard shape centroids (rectangle, triangle, semicircle, quarter-circle) are tabulated. Holes and cutouts are treated as negative areas subtracted from the total. For continuous area distributions, integration gives x̄ = ∫x dA / ∫dA.

## How It's Best Learned
Organize calculations in a table with columns for shape, area, x̄ᵢ, ȳᵢ, Aᵢx̄ᵢ, and Aᵢȳᵢ. Sum the last two columns and divide by total area. Tabular organization prevents sign and arithmetic errors.

## Common Misconceptions
- Using the wrong reference point for standard shape centroids.
- Forgetting to subtract cutout areas (use negative area for holes).
- Confusing centroid (geometric property) with center of mass (requires uniform density to coincide with centroid).

## Explainer

The **centroid** of an area is its geometric center — the point where the shape would balance perfectly if it were a flat plate of uniform density. From your work with areas of basic shapes, you know how to calculate the area of a rectangle, circle, or triangle. The centroid extends that knowledge by asking: where is each shape centered, and how do those centers combine for a complex shape made of simpler parts?

Think of it like a see-saw with multiple weights placed at different positions. The balance point isn't simply where most of the mass is — it's the weighted average position. The centroid formula does exactly this in two dimensions, using area as the "weight." The formula x̄ = ΣAᵢx̄ᵢ / ΣAᵢ is a weighted average: each sub-shape contributes its centroid coordinate scaled by how much area it has. A larger piece pulls the centroid toward itself more strongly than a small piece.

The practical technique works by decomposing any irregular shape into simple pieces whose centroids are tabulated — rectangles at their geometric midpoints, triangles at one-third from the base, semicircles at 4r/3π from the flat edge. Organize this in a table with columns for shape, area, x̄ᵢ, ȳᵢ, Aᵢx̄ᵢ, and Aᵢȳᵢ. Sum the last two columns and divide by total area. This tabular approach prevents sign and arithmetic errors and makes it easy to check your work.

Cutouts and holes use the same principle: a hole is simply a **negative area**. If you have a plate with a circular hole punched out, treat the full plate as a positive-area shape and the removed circle as a shape with negative area. The weighted average naturally cancels out the removed material. You never need to work out the geometry of the irregular boundary — the negative-area trick handles it automatically.

For shapes defined by continuous distributions rather than discrete sub-pieces, the formula extends to integration: x̄ = ∫x dA / ∫dA. If you've done definite integrals, you'll recognize this as a weighted average summed continuously over area. Whether you use tabulation or integration, the underlying concept is identical: the centroid is a balance point, found by weighting each area element by its position. This concept reappears immediately in the next topic — area moment of inertia — where position is squared, not linear.
