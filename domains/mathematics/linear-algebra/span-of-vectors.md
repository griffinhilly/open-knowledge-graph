---
id: span-of-vectors
title: Span of a Set of Vectors
domain: mathematics
course: linear-algebra
prerequisites:
- id: vectors-in-rn
  type: hard
- id: vector-spaces
  type: soft
builds-toward:
- linear-independence
- column-space
- basis-and-dimension
tags:
- span
- linear combination
- generating set
- all possible combinations
stage: formal-systems
status: validated
---

# Span of a Set of Vectors

## Core Idea
The span of a set of vectors {v₁, v₂, …, vₖ} is the set of all possible linear combinations c₁v₁ + c₂v₂ + … + cₖvₖ where the cᵢ are real scalars. Geometrically, spanning a single nonzero vector gives a line; spanning two non-parallel vectors gives a plane; spanning enough independent vectors eventually fills Rⁿ. The span of any set of vectors is always a subspace. Asking whether a vector b lies in the span of {v₁, …, vₖ} is equivalent to asking whether the system [v₁ | v₂ | … | vₖ | b] is consistent.

## How It's Best Learned
Start with visual examples in R² and R³: what does the span of one vector look like? Of two? Then connect span to consistency of linear systems by reformulating 'is b in Span{v₁, v₂}?' as a matrix-vector equation.

## Common Misconceptions
- The span of an empty set is {0}, not the empty set — by convention, the empty sum is the zero vector.
- Adding a vector to a spanning set might not increase the span if the new vector is already in the span.
- Students sometimes confuse spanning with independence; a set can span a space without being minimal (basis) or independent.
