---
id: quadric-surfaces
title: Cylinders and Quadric Surfaces
domain: mathematics
course: multivariable-calculus
prerequisites:
  - id: 3d-coordinate-systems
    type: hard
  - id: conic-sections-overview
    type: hard
  - id: equations-lines-planes-3d
    type: soft
builds-toward:
  - functions-of-several-variables
tags: [multivariable-calculus, quadric-surfaces, traces, ellipsoid, paraboloid, hyperboloid, 3d-graphing]
stage: formal-systems
status: validated
---

# Cylinders and Quadric Surfaces

## Core Idea
A quadric surface is the graph of a second-degree equation in x, y and z. After shifting and rotating axes, a quadric surface that is not a cylinder or a degenerate case (such as a pair of planes) fits one of six standard types: ellipsoid, elliptic paraboloid, hyperbolic paraboloid, elliptic cone, hyperboloid of one sheet, and hyperboloid of two sheets. The main tool for recognizing and sketching them is the trace, the curve cut out by a plane such as z = k; every trace of a quadric surface is a conic section, possibly a degenerate one. A cylinder is the simpler case where one variable is missing, so the surface is a curve in the plane extended straight along that axis.

## How It's Best Learned
For each standard equation, compute traces in planes x = k, y = k and z = k, identify each as an ellipse, parabola or hyperbola, and assemble the surface from those slices. Physical or software models help students connect the equations to the shapes. Practice with equations that need completing the square or that have the variables in a different role (such as y = x² + z²).

## Common Misconceptions
- An equation with only x and y, such as x² + y² = 4, describes a circle. (In three dimensions it describes a circular cylinder, because z can take any value.)
- The hyperboloid of one sheet and the hyperboloid of two sheets differ only in size. (One sheet has one minus sign and is connected; two sheets has two minus signs and splits into two separate pieces.)
- A saddle surface has a highest point at its center. (The hyperbolic paraboloid z = x² - y² curves up along the x-direction and down along the y-direction, so the origin is neither a maximum nor a minimum.)

## Questions

```yaml
- question: "Which surface is described by x²/4 + y²/9 - z² = 1?"
  type: multiple-choice
  options: ["Ellipsoid", "Hyperboloid of one sheet", "Hyperboloid of two sheets", "Elliptic cone"]
  answer: 1
  explanation: "Two squared terms are positive and one is negative, with 1 on the right side. The traces z = k are ellipses x²/4 + y²/9 = 1 + k², which exist for every k, so the surface is a single connected piece: a hyperboloid of one sheet."

- question: "In three-dimensional space, the equation x² + y² = 4 describes a circle of radius 2."
  type: true-false
  answer: false
  explanation: "Because z does not appear, the equation places no restriction on z. Every horizontal plane z = k contains the same circle, so the graph is a circular cylinder of radius 2 around the z-axis."

- question: "Describe the traces of z = x² - y² in the planes y = 0, x = 0 and z = 1, and name the surface."
  type: short-answer
  answer: "y = 0 gives the upward parabola z = x²; x = 0 gives the downward parabola z = -y²; z = 1 gives the hyperbola x² - y² = 1. The surface is a hyperbolic paraboloid (saddle)."
  explanation: "Opposite-facing parabolas in perpendicular directions are the signature of a saddle. Horizontal traces are hyperbolas, except at z = 0, where the trace is the pair of lines y = ±x."

- question: "Which equation describes an elliptic paraboloid opening along the positive y-axis?"
  type: multiple-choice
  options: ["y = x² + z²", "y² = x² + z²", "x² + y² + z² = 1", "y = x² - z²"]
  answer: 0
  explanation: "The variable that appears to the first power marks the axis of the paraboloid. In y = x² + z², the traces y = k > 0 are circles and y ≥ 0 everywhere, so it opens toward positive y. y² = x² + z² is a cone and y = x² - z² is a saddle."
```

## Explainer

In the plane, second-degree equations in x and y give the conic sections: ellipses, parabolas and hyperbolas. In space, second-degree equations in x, y and z give surfaces called quadric surfaces. The way to understand them is to slice them.

A trace of a surface is its intersection with a plane. Setting z = k in the equation turns it into an equation in x and y, which describes a curve in that horizontal plane. For a quadric surface, every trace is a conic (or a degenerate case such as a point or a pair of lines). Taking traces parallel to all three coordinate planes and stacking them gives a reliable picture of the surface.

Start with the simplest case, a cylinder. If one variable is missing, as in x² + y² = 4, the trace in every plane z = k is the same circle. The surface is that circle slid along the z-axis, a circular cylinder. In the same way, z = y² is a parabolic cylinder running along the x-axis.

The six standard quadric surfaces are worth knowing by their equations.

- Ellipsoid: x²/a² + y²/b² + z²/c² = 1. All traces are ellipses, and the surface is a closed, egg-like shape. When a = b = c it is a sphere.
- Elliptic paraboloid: z = x²/a² + y²/b². Horizontal traces are ellipses, vertical traces are parabolas, and the surface is a bowl.
- Hyperbolic paraboloid: z = x²/a² - y²/b². Vertical traces are parabolas opening in opposite directions, horizontal traces are hyperbolas, and the surface is a saddle.
- Elliptic cone: z² = x²/a² + y²/b². Horizontal traces are ellipses that shrink to a point at the origin, giving two cones meeting tip to tip.
- Hyperboloid of one sheet: x²/a² + y²/b² - z²/c² = 1. Horizontal traces are ellipses for every z, so the surface is one connected tube that narrows at z = 0.
- Hyperboloid of two sheets: z²/c² - x²/a² - y²/b² = 1. The horizontal trace is empty when |z| < c, so the surface has two separate bowls.

To identify a surface, count signs and look for a variable to the first power. A first-power variable signals a paraboloid along that axis. With all variables squared, three plus signs suggest an ellipsoid, one minus sign a hyperboloid of one sheet, and two minus signs a hyperboloid of two sheets.

These shapes return throughout the course. Graphs of functions z = f(x, y) are often quadrics, and the saddle z = x² - y² is the standard picture of a critical point that is neither a maximum nor a minimum.
