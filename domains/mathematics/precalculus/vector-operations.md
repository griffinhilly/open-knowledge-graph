---
id: vector-operations
title: "Vector Operations: Addition, Subtraction, and Scalar Multiplication"
domain: mathematics
course: precalculus
prerequisites:
  - id: vectors-in-two-dimensions
    type: hard
builds-toward:
  - dot-product
tags: [vectors, operations, linear-combinations]
stage: formal-systems
status: validated
---

# Vector Operations: Addition, Subtraction, and Scalar Multiplication

## Core Idea
Vectors can be added (tip-to-tail or component-wise), subtracted (add the negative), and scaled by a scalar (multiply each component). These operations are performed component-wise: (a1, b1) + (a2, b2) = (a1 + a2, b1 + b2) and c*(a, b) = (ca, cb). Linear combinations of vectors (c1*v1 + c2*v2) span the plane and are the foundation of linear algebra.

## How It's Best Learned
Practice both graphically (tip-to-tail addition, parallelogram rule) and algebraically (component-wise). Show that scalar multiplication stretches or shrinks and can reverse direction. Connect to physics: net force is vector addition, scaling a velocity vector changes speed.

## Common Misconceptions
- Adding magnitudes instead of adding components.
- Confusing vector subtraction direction: u - v points from the tip of v to the tip of u.
- Thinking scalar multiplication can change the direction to any angle (it can only reverse or preserve direction).

## Questions

```yaml
- question: "Vectors u = (3, 4) and v = (1, -2) are given. What is u + v?"
  type: multiple-choice
  options:
    - "(4, 2)"
    - "(2, 6)"
    - "(3, -8)"
    - "(4, 6)"
  answer: 0
  explanation: "Vector addition is component-wise: (3+1, 4+(-2)) = (4, 2). The common error is adding magnitudes (|u| = 5, |v| = √5) and getting a scalar — but that ignores direction entirely. Each component is handled independently."

- question: "You want to rotate vector (1, 0) so it points in the direction (0, 1). Which scalar multiple of (1, 0) achieves this?"
  type: multiple-choice
  options:
    - "Multiply by -1 to reverse direction, then the perpendicular component appears"
    - "Multiply by a sufficiently large positive scalar"
    - "No scalar multiple of (1, 0) can ever point in the direction (0, 1)"
    - "Multiply by i (the imaginary unit) to rotate 90°"
  answer: 2
  explanation: "Scalar multiplication c·(a, b) = (ca, cb) scales both components by the same factor c. It can stretch, shrink, or reverse a vector, but it cannot rotate it to any arbitrary direction — a negative scalar reverses direction (180°), and a positive scalar preserves it. To change direction by any angle other than 0° or 180°, you need vector addition. This is one of the most important constraints of scalar multiplication."

- question: "Multiplying a vector by the scalar -3 reverses its direction and triples its magnitude."
  type: true-false
  answer: true
  explanation: "For c·(a, b) = (-3a, -3b): the magnitude scales by |c| = |-3| = 3 (tripled), and the negative sign reverses direction (equivalent to a 180° rotation). Both effects happen simultaneously. This is precisely what scalar multiplication can do — scale and optionally reverse — but nothing else with respect to direction."

- question: "Vector subtraction is commutative: u - v equals v - u."
  type: true-false
  answer: false
  explanation: "u - v = u + (-v) points from the tip of v to the tip of u. Swapping gives v - u = v + (-u), which points in exactly the opposite direction. Geometrically, u - v and v - u are negatives of each other. This is analogous to scalar subtraction: 5 - 3 ≠ 3 - 5. Vector subtraction is not commutative."

- question: "Explain geometrically what the vector u - v represents, and how its direction differs from v - u."
  type: short-answer
  answer: "u - v is the displacement vector pointing from the tip of v to the tip of u (when both are drawn from the same origin). It represents 'how you get from v to u.' v - u points in the exact opposite direction — from the tip of u to the tip of v. They have the same magnitude but opposite directions, so u - v = -(v - u)."
  explanation: "The geometric interpretation of u - v comes from rewriting it as: 'start at v, what do you add to reach u?' That answer is u - v. This is why u - v is sometimes written as the 'vector from v to u.' Confusing the order is a persistent error; always ask 'which tip am I pointing toward?'"
```

## Explainer

From your study of vectors in two dimensions, you know that a **vector** represents both a magnitude and a direction, written as an ordered pair (a, b) in component form. The operations on vectors — addition, subtraction, and scalar multiplication — are all defined **component-wise**, which means you apply the operation separately to each coordinate. This design ensures that vector operations are consistent with the geometric interpretations you already have in mind.

**Vector addition** (a₁, b₁) + (a₂, b₂) = (a₁+a₂, b₁+b₂) has a precise geometric meaning: the **tip-to-tail rule**. Draw the first vector from the origin, then place the tail of the second at the tip of the first. The sum is the vector from the origin to the new tip. The parallelogram rule is equivalent — place both vectors tail-to-tail and complete the parallelogram; the diagonal is the sum. Either way, the result is the component-wise sum, and both geometric pictures are saying the same thing in different arrangements. In physics, this is how you add forces or velocities: a boat moving at (3, 0) m/s in a river with current (0, 2) m/s ends up moving at (3, 2) m/s.

**Scalar multiplication** c·(a, b) = (ca, cb) scales both components by the same factor. Geometrically, it stretches or shrinks the vector by |c| and reverses its direction if c is negative. The direction can only be preserved (c > 0) or reversed (c < 0) — scalar multiplication cannot rotate a vector to any arbitrary angle. That is a key constraint: to change direction to something other than 180°, you need vector addition. **Vector subtraction** u - v is defined as u + (-v), where -v = (-1)·v is the reversal. Geometrically, u - v is the vector pointing from the tip of v to the tip of u — the "displacement" from v to u.

**Linear combinations** c₁v₁ + c₂v₂ are the core of linear algebra. By varying c₁ and c₂ over all real numbers, you generate every vector in the plane (assuming v₁ and v₂ point in different directions). This is what "spanning the plane" means. If you think of v₁ = (1, 0) and v₂ = (0, 1), then c₁·(1,0) + c₂·(0,1) = (c₁, c₂) — any point in the plane is reachable. This idea extends directly to higher dimensions and to abstract vector spaces, making the three operations you are learning now the foundation of all of linear algebra.
