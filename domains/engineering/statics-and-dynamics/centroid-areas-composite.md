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
