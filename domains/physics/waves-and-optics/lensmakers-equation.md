---
id: lensmakers-equation
title: The Lensmaker's Equation
domain: physics
course: waves-and-optics
prerequisites:
- id: thin-lens-equation
  type: hard
- id: snells-law
  type: hard
tags:
- lensmaker's equation
- radius of curvature
- index of refraction
- focal length
stage: formal-systems
status: validated
---

# The Lensmaker's Equation

## Core Idea
The lensmaker's equation relates a lens's focal length to its geometry and material: 1/f = (n−1)(1/R₁ − 1/R₂), where n is the refractive index of the lens and R₁, R₂ are the radii of curvature of the two surfaces (positive if center is to the right). This equation connects the macroscopic optics of image formation to the microscopic material property (n) and physical shape, and explains why a lens with the same shape has different focal lengths in different media.

## How It's Best Learned
Compare the focal lengths of lenses with identical shapes but different glass types (n = 1.5 vs. n = 1.7) using the lensmaker's equation. Then work backwards from a desired focal length to design lens geometry.

## Common Misconceptions
- The sign convention for R₁ and R₂ is the trickiest part; always define the convention first and apply it to the specific lens orientation.
- A lens in water has a longer focal length than the same lens in air because (n_glass − n_water) < (n_glass − n_air).

## Explainer

You already know from the thin-lens equation that a converging lens with focal length f forms images according to 1/do + 1/di = 1/f. But where does f come from? The thin-lens equation treats f as a given, leaving the origin of focal length in a black box. The **lensmaker's equation** opens that box: 1/f = (n − 1)(1/R₁ − 1/R₂). It connects the focal length to two physical properties — the refractive index n of the lens material, and the radii of curvature R₁ and R₂ of its two surfaces.

The refractive index n is the same quantity from Snell's law: it measures how much slower light travels in the glass compared to vacuum (n = c/v). A higher n means light bends more steeply at each surface. The factor (n − 1) in the lensmaker's equation captures exactly this: a lens made from high-index glass (n = 1.7) is more powerful than an identical-shaped lens in low-index glass (n = 1.5) because each surface bends the rays more. This is why optical designers can make thinner, lighter lenses by choosing high-index materials — the same focal length can be achieved with gentler, flatter curves.

The radii of curvature R₁ and R₂ describe the shape of each surface. The sign convention follows a consistent rule: a radius is positive if the center of curvature lies to the right of the surface, and negative if it lies to the left. For a standard biconvex lens, R₁ is positive (first surface curves toward the incoming light) and R₂ is negative (second surface curves away from it), making 1/R₁ − 1/R₂ positive overall — which gives a positive f, a converging lens. Flip the geometry to a biconcave lens and the subtraction reverses sign, yielding negative f and a diverging lens. The equation correctly handles any combination of surface shapes.

The most important insight from the lensmaker's equation is that **focal length depends on the surrounding medium**. The full form uses (n_lens/n_medium − 1) in place of (n − 1). In air (n_medium ≈ 1), this reduces to the familiar form. But submerge a glass lens in water, where n_water ≈ 1.33, and the effective index contrast drops sharply. A lens that strongly converges light in air becomes nearly flat — barely converging — in water. This explains why your vision blurs underwater without goggles: the cornea of your eye acts as a lens, and immersed in water it almost entirely loses its refractive power. A swimming mask restores the air gap, reinstating the full index contrast and your sharp vision.
