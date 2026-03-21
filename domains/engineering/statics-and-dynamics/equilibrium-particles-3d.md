---
id: equilibrium-particles-3d
title: Equilibrium of Particles in 3D
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: equilibrium-particles-2d
  type: hard
- id: vectors-in-3d
  type: hard
builds-toward:
- equilibrium-rigid-bodies
tags:
- statics
- equilibrium
- particles
- 3D
- space structures
stage: formal-systems
status: validated
---

# Equilibrium of Particles in 3D

## Core Idea
In 3D, particle equilibrium requires ΣF = 0, yielding three scalar equations: ΣFx = 0, ΣFy = 0, ΣFz = 0. Forces in 3D are expressed using Cartesian unit vectors, and cables or rod members with known geometry have their force directions determined using unit position vectors: T = T·(r_AB / |r_AB|). Setting up these unit vectors systematically from coordinate geometry is the primary skill required.

## How It's Best Learned
Practice writing 3D forces in Cartesian form using direction cosines or position vectors from geometry. Organize force components in a table before summing in each direction.

## Common Misconceptions
- Errors in computing unit vectors from position vector geometry.
- Forgetting the z-direction equation in 3D.
- Sign errors when resolving inclined cables or rods into Cartesian components.

## Questions

```yaml
- question: "A cable runs from the origin O(0, 0, 0) to point A(3, 4, 0) m and carries tension T = 50 N. What are the correct x and y components of this cable force?"
  type: multiple-choice
  options:
    - "Tx = 50·(3/4) = 37.5 N, Ty = 50·(4/3) = 66.7 N"
    - "Tx = 3 N, Ty = 4 N (the raw coordinate differences)"
    - "Tx = 50·(3/5) = 30 N, Ty = 50·(4/5) = 40 N"
    - "Tx = 50·cos(3°) = 49.9 N, Ty = 50·cos(4°) = 49.8 N"
  answer: 2
  explanation: "The position vector is r = 3i + 4j, with magnitude |r| = √(9 + 16) = 5. The unit vector is û = (3/5)i + (4/5)j. Cable force = T·û = 50·(3/5)i + 50·(4/5)j = 30i + 40j N. Option A uses the ratio of the two components rather than dividing by the magnitude. Option B forgets to divide by the magnitude and multiply by T. The key step is always: find the magnitude of the position vector, then divide."

- question: "How many independent scalar equilibrium equations does a particle in 3D space provide, and what is the maximum number of unknown forces they can determine?"
  type: multiple-choice
  options:
    - "Two equations (ΣFx = 0, ΣFy = 0); up to two unknowns — same as 2D"
    - "Three equations (ΣFx = 0, ΣFy = 0, ΣFz = 0); up to three unknowns"
    - "Six equations (three force, three moment); up to six unknowns"
    - "Three equations, but only two are independent because ΣF = 0 in vector form is one equation"
  answer: 1
  explanation: "The vector equation ΣF = 0 in 3D breaks into three independent scalar equations — one per Cartesian direction. This allows solving for at most three unknowns (e.g., three cable tensions). Six equations would apply to rigid body equilibrium in 3D, which also includes moment equations. Option D misunderstands vector equations: ΣF = 0 in 3D is equivalent to three separate scalar equations."

- question: "If all the forces acting on a particle in a 3D problem happen to lie entirely in the x-y plane, then the ΣFz = 0 equation is automatically satisfied (0 = 0) and provides no useful information."
  type: true-false
  answer: true
  explanation: "When all forces are coplanar in x-y, every force has zero z-component. Summing zeros gives 0 = 0, which is trivially true and imposes no constraint. This is exactly the 2D special case embedded in 3D. You can use this as a check: if your 3D setup is correct, collapsing to 2D should reproduce your 2D results exactly — including a trivial ΣFz = 0."

- question: "In 3D particle equilibrium, you can find the unknown tension in a cable directly from the geometry without computing a unit vector, as long as you know the cable's length."
  type: true-false
  answer: false
  explanation: "Knowing the cable length gives you the magnitude of the position vector, but you still need to divide by that magnitude to obtain the unit vector in order to decompose the tension into Cartesian components. The unit vector (and hence the direction cosines) is essential to writing the force in i, j, k form. There is no shortcut: tension × unit vector is the only systematic way to express a cable force as Cartesian components for equilibrium equations."

- question: "Describe the systematic procedure for expressing a cable force in 3D Cartesian form given the coordinates of the two endpoints of the cable."
  type: short-answer
  answer: "Step 1: Compute the position vector r from the particle to the anchor point: r = (Bx−Ax)i + (By−Ay)j + (Bz−Az)k. Step 2: Find its magnitude: |r| = √(Δx² + Δy² + Δz²). Step 3: Divide to get the unit vector: û = r / |r|. Step 4: Multiply by the tension magnitude: F = T · û. This gives the three Cartesian components (Tx, Ty, Tz) ready to substitute into ΣFx = 0, ΣFy = 0, ΣFz = 0."
  explanation: "The procedure is the same every time regardless of geometry. The key insight is that the force direction is entirely encoded in the geometry of where the cable goes — you don't need angles or trigonometry separately. Once all forces in the problem are in Cartesian form, equilibrium reduces to solving a system of linear equations. Most errors in 3D statics happen in steps 1–3, not in the algebra."
```

## Explainer

You already know how to solve 2D particle equilibrium — you set ΣFx = 0 and ΣFy = 0, then solve for unknowns. The 3D case adds one more equation: ΣFz = 0. In principle, this is a straightforward extension; in practice, the challenge is almost entirely geometric. Writing a cable or rod force in Cartesian component form when it points in an arbitrary direction in 3D space is where most errors occur.

The systematic approach is to find a **unit position vector** from the particle to the point where the cable or rod is anchored. If a cable runs from point A to point B, the position vector is **r**_AB = (B_x − A_x)**i** + (B_y − A_y)**j** + (B_z − A_z)**k**. The unit vector along that direction is **û** = **r**_AB / |**r**_AB|, where |**r**_AB| = √(Δx² + Δy² + Δz²). Then the cable force is **T** = T·**û**, giving you the three components Tx, Ty, Tz directly. This process — compute the position vector, find its magnitude, divide to get the unit vector, multiply by the force magnitude — should become automatic.

Once all forces in the problem are expressed in Cartesian form, equilibrium is mechanical: collect all the x-components and set their sum to zero, do the same for y and z. You get a system of three equations in however many unknowns you have. For a particle held by three cables, you typically have three unknown tensions — one equation per unknown. The geometry you computed at the start does all the structural work; the algebra at the end is just solving a 3×3 linear system.

A useful mental check: if you collapse the geometry to 2D (all forces in the x-y plane), your z-equation becomes 0 = 0 trivially, and the x and y equations should reproduce exactly what you would have gotten using your 2D equilibrium method. If they don't, you've made an error in the 3D setup. This check costs nothing and catches sign errors before you submit a wrong answer. The 3D skill is foundational for the space truss problems coming next, where you'll apply this exact process at every joint in a three-dimensional framework.
