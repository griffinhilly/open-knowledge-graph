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

## Questions

```yaml
- question: "A rectangular steel plate (area = 20 cm², centroid at x = 5 cm) has a circular hole punched out at x = 8 cm (area of hole = 4 cm²). Where is the centroid of the remaining plate?"
  type: multiple-choice
  options:
    - "At x = 5.0 cm — removing material doesn't change the geometric center of the original rectangle"
    - "At x = 4.25 cm — the removed material on the right side shifts the centroid leftward"
    - "At x = 5.75 cm — the hole at x = 8 cm pulls the centroid toward the right"
    - "At x = 6.5 cm — the centroid moves to the midpoint between the plate's center and the hole"
  answer: 1
  explanation: "Using the negative area method: x̄ = (20×5 − 4×8) / (20 − 4) = (100 − 32) / 16 = 68/16 = 4.25 cm. The hole removed area from the right side (x = 8 is right of center at x = 5), so the remaining shape is heavier on the left, pulling the centroid leftward. Option A incorrectly treats the original centroid as unchanged. Option C inverts the effect — removing right-side material shifts the balance leftward, not rightward."

- question: "An L-shaped bracket is decomposed into two rectangles: Rectangle A has area 8 cm² with centroid at ȳ = 6 cm; Rectangle B has area 6 cm² with centroid at ȳ = 2 cm. What is ȳ for the composite shape?"
  type: multiple-choice
  options:
    - "ȳ = 4.0 cm — the simple average of 6 and 2"
    - "ȳ = 4.29 cm — the weighted average, with Rectangle A (larger area) pulling the centroid upward"
    - "ȳ = 3.71 cm — the weighted average, with Rectangle B (lower centroid) pulling the result down"
    - "ȳ = 8.0 cm — the sum of the two centroid y-values"
  answer: 1
  explanation: "ȳ = ΣAᵢȳᵢ / ΣAᵢ = (8×6 + 6×2) / (8+6) = (48 + 12) / 14 = 60/14 ≈ 4.29 cm. Rectangle A is larger and its centroid is higher (ȳ = 6), so it pulls the composite centroid upward past the simple average of 4. Option A (simple average) ignores area weighting. Option C inverts which rectangle has more influence — the larger rectangle dominates."

- question: "The centroid of a shape must always lie within the physical boundary of that shape."
  type: true-false
  answer: false
  explanation: "The centroid is a mathematical balance point, and for concave shapes or shapes with holes, it can lie entirely outside the material. A C-shaped bracket, a ring, or a hollow square tube all have centroids located in the empty interior space. This is not an error — it is the correct geometric center for those shapes. The negative-area technique works precisely because the formula does not require the centroid to be located on material."

- question: "A cutout or hole in a composite shape can be handled by assigning it a negative area and including it in the weighted-average formula alongside the positive sub-shapes."
  type: true-false
  answer: true
  explanation: "This is the key practical technique: you never need to calculate the irregular geometry of the remaining boundary. Treat the full solid shape as a positive area with its known centroid, and the removed piece as a shape with negative area using the centroid of the removed piece. The weighted average naturally cancels the removed material's contribution. This approach generalizes to any number of cutouts and is far less error-prone than attempting to integrate the complex remaining boundary."

- question: "Why is the centroid formula x̄ = ΣAᵢx̄ᵢ / ΣAᵢ described as a 'weighted average'? What is being weighted, and what are the weights?"
  type: short-answer
  answer: "The formula computes the average x-position of the shape, weighted by how much area each part contributes. Each sub-shape's centroid coordinate (x̄ᵢ) is multiplied by its area (Aᵢ), and the sum is divided by total area. A larger sub-shape has more 'pull' on the overall centroid than a smaller one — analogous to heavier weights on a see-saw having more influence on the balance point. The areas are the weights; the centroid coordinates are the values being averaged."
  explanation: "The weighted-average framing makes the behavior intuitive: adding a large sub-shape far from the current centroid pulls it strongly in that direction; adding a small sub-shape barely moves it. The negative-area technique for holes fits the same framework naturally — a negative weight pulls the centroid away from the removed material, which is exactly what physical intuition demands."
```

## Explainer

The **centroid** of an area is its geometric center — the point where the shape would balance perfectly if it were a flat plate of uniform density. From your work with areas of basic shapes, you know how to calculate the area of a rectangle, circle, or triangle. The centroid extends that knowledge by asking: where is each shape centered, and how do those centers combine for a complex shape made of simpler parts?

Think of it like a see-saw with multiple weights placed at different positions. The balance point isn't simply where most of the mass is — it's the weighted average position. The centroid formula does exactly this in two dimensions, using area as the "weight." The formula x̄ = ΣAᵢx̄ᵢ / ΣAᵢ is a weighted average: each sub-shape contributes its centroid coordinate scaled by how much area it has. A larger piece pulls the centroid toward itself more strongly than a small piece.

The practical technique works by decomposing any irregular shape into simple pieces whose centroids are tabulated — rectangles at their geometric midpoints, triangles at one-third from the base, semicircles at 4r/3π from the flat edge. Organize this in a table with columns for shape, area, x̄ᵢ, ȳᵢ, Aᵢx̄ᵢ, and Aᵢȳᵢ. Sum the last two columns and divide by total area. This tabular approach prevents sign and arithmetic errors and makes it easy to check your work.

Cutouts and holes use the same principle: a hole is simply a **negative area**. If you have a plate with a circular hole punched out, treat the full plate as a positive-area shape and the removed circle as a shape with negative area. The weighted average naturally cancels out the removed material. You never need to work out the geometry of the irregular boundary — the negative-area trick handles it automatically.

For shapes defined by continuous distributions rather than discrete sub-pieces, the formula extends to integration: x̄ = ∫x dA / ∫dA. If you've done definite integrals, you'll recognize this as a weighted average summed continuously over area. Whether you use tabulation or integration, the underlying concept is identical: the centroid is a balance point, found by weighting each area element by its position. This concept reappears immediately in the next topic — area moment of inertia — where position is squared, not linear.
