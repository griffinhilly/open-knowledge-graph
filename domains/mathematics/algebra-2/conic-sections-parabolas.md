---
id: conic-sections-parabolas
title: 'Conic Sections: Parabolas'
domain: mathematics
course: algebra-2
prerequisites:
- id: graphing-quadratic-functions
  type: hard
- id: solving-quadratic-equations-completing-the-square
  type: hard
- id: coordinate-geometry-proofs
  type: soft
builds-toward:
- conic-sections-ellipses
- conic-sections-overview
tags:
- conics
- parabolas
- focus
- directrix
stage: abstract-reasoning
status: validated
---
# Conic Sections: Parabolas

## Core Idea
A parabola is the set of all points equidistant from a fixed point (focus) and a fixed line (directrix). Standard forms: vertical axis (x-h)^2 = 4p(y-k) or horizontal axis (y-k)^2 = 4p(x-h), where (h,k) is the vertex and p is the distance from vertex to focus. If p > 0, the parabola opens toward the focus. This geometric definition extends the algebraic view from quadratic functions and connects parabolas to the family of conic sections.

## How It's Best Learned
Start from the distance definition: derive the equation by setting distance to focus equal to distance to directrix. Identify the vertex, focus, directrix, and axis of symmetry from the equation. Practice converting between standard form and general form via completing the square. Graph using key features. Discuss reflective properties (satellite dishes, headlights).

## Common Misconceptions
- Thinking all parabolas open upward (they can open in any of four directions).
- Confusing the vertex with the focus.
- Getting the sign of p wrong and placing the focus on the wrong side of the vertex.
- Not recognizing that y = ax^2 + bx + c is a special case of the conic section parabola.

## Questions

```yaml
- question: "A parabola has equation (y − 2)² = −8(x + 1). In which direction does it open?"
  type: multiple-choice
  options:
    - "Upward, because 4p = −8 is negative"
    - "Downward, because the y-term is squared"
    - "Left, because y is squared and p < 0"
    - "Right, because y is squared"
  answer: 2
  explanation: "When y is squared, the axis of symmetry is horizontal and the equation has the form (y−k)² = 4p(x−h). The parabola opens right when p > 0 and left when p < 0. Here 4p = −8, so p = −2 < 0, giving a leftward-opening parabola. Options A and B are the typical errors: assuming all parabolas open up or down and reading the sign incorrectly."

- question: "A point P lies on a parabola with focus F(0, 3) and directrix y = −3. The distance from P to the focus is 7. What is the distance from P to the directrix?"
  type: multiple-choice
  options:
    - "3 — the distance from the vertex to the directrix"
    - "4 — the difference between the focus distance and the focal length"
    - "7 — equal to the distance to the focus by definition"
    - "10 — the sum of the focus distance and the focal length"
  answer: 2
  explanation: "The geometric definition of a parabola states that every point on it is equidistant from the focus and the directrix. If |PF| = 7, then the distance from P to the directrix must also equal 7. This is not a coincidence — it is the defining property. Students who confuse the focus with the directrix distance, or use the focal length (p = 3) instead, arrive at wrong answers."

- question: "A horizontal-axis parabola of the form (y − k)² = 4p(x − h) is not a function because it fails the vertical line test."
  type: true-false
  answer: true
  explanation: "A horizontal parabola opens left or right, so for a single x-value there are typically two y-values (one above and one below the axis of symmetry). This fails the vertical line test — the definition of a function. This is why algebra courses introduce only vertical parabolas: they are functions. As conic sections, both orientations are equally valid geometric objects."

- question: "The vertex of a parabola and its focus are the same point."
  type: true-false
  answer: false
  explanation: "The vertex is the turning point of the parabola; the focus is a distinct point located p units from the vertex along the axis of symmetry, inside the curve. They coincide only in the degenerate case p = 0, which is not a real parabola. Confusing vertex and focus is one of the most common errors in this topic — the vertex sits on the parabola, while the focus is interior to it."

- question: "Satellite dishes and headlight reflectors use a paraboloid shape to concentrate signals or light. What property of the parabola — derived from its geometric definition — makes this work?"
  type: short-answer
  answer: "Any ray traveling parallel to the axis of symmetry reflects off the parabola and passes through the focus. This reflective property follows from the equidistance definition: the tangent at any point bisects the angle between the line to the focus and the perpendicular to the directrix, causing parallel rays to converge at the focus."
  explanation: "This is not an incidental engineering trick — it is a geometric theorem. A satellite dish collects parallel rays from a distant source and focuses them at the receiver at the focus point. A car headlight reverses the process: a bulb at the focus emits rays that reflect off the paraboloid surface as parallel beams. Understanding that the reflective property is a consequence of the geometric definition (not a separate fact) shows mastery of what the definition is actually doing."
```

## Explainer

You already know the parabola as the graph of a quadratic function f(x) = ax² + bx + c. That algebraic view is useful for solving equations, but it obscures the geometric essence. The **geometric definition** gives the parabola its real identity: it is the set of all points equidistant from a fixed point called the **focus** and a fixed line called the **directrix**. Every point P on a parabola satisfies |PF| = |PD|, where F is the focus and D is the nearest point on the directrix. This definition explains why parabolas have the shape they do — the curve is being "pulled" symmetrically toward a point and away from a line simultaneously.

To connect this to the algebra you know, take the focus at (0, p) and the directrix y = −p. A point (x, y) is on the parabola when its distance to (0, p) equals its distance to the line y = −p. Setting these equal: √(x² + (y − p)²) = |y + p|. Squaring and simplifying yields x² = 4py. This is the **standard form** for a vertical parabola with vertex at the origin. The number p — the **focal length** — is the distance from the vertex to the focus. If p > 0 the parabola opens upward (focus above vertex, directrix below); if p < 0 it opens downward. The completing-the-square technique you already know converts f(x) = ax² + bx + c into vertex form, which then maps onto (x − h)² = 4p(y − k) with p = 1/(4a). So your quadratic function was a vertical parabola all along, with focus at (h, k + p).

The standard form reveals four possible orientations. A vertical parabola (x − h)² = 4p(y − k) opens up or down. A horizontal parabola (y − k)² = 4p(x − h) opens right or left. Horizontal-axis parabolas are not functions (they fail the vertical-line test), which is why your earlier algebra course only showed you the vertical case. But as geometric objects, all four orientations are on equal footing. The key skill is reading the equation: which variable is squared? That axis is the one perpendicular to the axis of symmetry. Then determine the sign of p to find which direction the parabola opens, and locate the focus exactly p units from the vertex along the axis of symmetry.

The reflective property of parabolas is not incidental — it is a direct consequence of the focus-directrix definition. Any ray traveling parallel to the axis of symmetry reflects off the parabola and passes through the focus (and vice versa). This is why satellite dishes and headlight reflectors are paraboloids: signals from a distant source arrive as parallel rays, and the parabolic shape concentrates them at the focus where the receiver sits. Deriving this requires showing that the tangent at any point bisects the angle between the line to the focus and the perpendicular to the directrix — a proof that uses only the equidistance definition and basic geometry.
