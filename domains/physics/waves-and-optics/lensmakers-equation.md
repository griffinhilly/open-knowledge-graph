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
- id: paraxial-ray-approximation
  type: soft
- id: thin-lenses-focal-length
  type: soft
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

## Questions

```yaml
- question: "A glass lens (n = 1.5) has focal length f in air. The same lens is submerged in water (n = 1.33). What happens to its focal length?"
  type: multiple-choice
  options:
    - "It decreases — the lens is more powerful in water because light bends more"
    - "It stays the same — focal length depends only on the lens geometry, not the medium"
    - "It increases — the effective index contrast between lens and medium is smaller, reducing bending power"
    - "It becomes negative — the lens becomes diverging in water"
  answer: 2
  explanation: "The full lensmaker's equation includes (n_lens/n_medium − 1). In air, this factor is (1.5/1.0 − 1) = 0.5. In water, it becomes (1.5/1.33 − 1) ≈ 0.128 — about four times smaller. So the focal length increases by roughly that factor: the same glass lens is a much weaker converging lens in water. This is why your cornea (which acts as a lens) loses most of its refracting power when submerged — the index contrast with water is nearly gone. Option B is the key misconception: focal length is NOT just a property of the glass shape."

- question: "A lens designer wants to achieve a given focal length using a thinner, lighter lens with flatter surfaces. Which material property should she choose to maximize?"
  type: multiple-choice
  options:
    - "Lower refractive index — less dense glass curves light more per unit thickness"
    - "Higher refractive index — more index contrast means each surface bends light more, so less curvature is needed"
    - "Lower density — thinner lenses require less mass, not a different optical property"
    - "Higher dispersion — spreading colors more gives more overall focusing power"
  answer: 1
  explanation: "The lensmaker's equation shows that focal length is inversely proportional to (n − 1). A higher n makes (n − 1) larger, increasing 1/f and thus shortening the focal length — meaning more power per unit of surface curvature. To get the same focal length with a higher-n material, you can use flatter (larger-radius) surfaces, making the lens thinner and lighter. This is exactly why high-index glass is used in modern thin eyeglass lenses. Dispersion (option D) describes how n varies with wavelength, which causes chromatic aberration — not overall focusing power."

- question: "The focal length of a lens is determined solely by the refractive index of the lens material and the radii of curvature of its surfaces — the medium surrounding the lens plays no role."
  type: true-false
  answer: false
  explanation: "This is false. The lensmaker's equation in its full form is 1/f = (n_lens/n_medium − 1)(1/R₁ − 1/R₂). The surrounding medium enters through n_medium. In air (n_medium ≈ 1) the equation simplifies to the familiar (n − 1) form, but this is a special case. Immerse any lens in a medium with refractive index closer to that of the lens and the focal length increases dramatically. A lens immersed in a fluid with the exact same refractive index has infinite focal length — it doesn't bend light at all."

- question: "For a biconvex lens oriented so the first surface faces incoming light, the lensmaker's sign convention assigns a positive radius of curvature to the first surface and a negative radius to the second."
  type: true-false
  answer: true
  explanation: "Correct. The standard sign convention defines R as positive if the center of curvature lies to the right of the surface, and negative if it lies to the left. For a biconvex lens in the standard orientation: the first surface bulges toward incoming light, so its center of curvature is to the right — R₁ > 0. The second surface bulges away from outgoing light, so its center of curvature is to the left — R₂ < 0. This makes 1/R₁ − 1/R₂ = (positive) − (negative) = a positive sum, giving a positive 1/f, confirming a converging lens."

- question: "Why does human vision blur when opening your eyes underwater, and why does wearing swim goggles restore clear vision?"
  type: short-answer
  answer: "The cornea normally forms images by refracting light at the air-cornea interface, where there is a large difference in refractive index (air ≈ 1.0, cornea ≈ 1.376). When submerged in water (n ≈ 1.33), the index contrast at the cornea drops from about 0.376 to about 0.046 — a factor of ~8 reduction. By the lensmaker's equation, this collapse in (n_lens/n_medium − 1) increases the focal length enormously, leaving the eye far too weak to focus on the retina. Swim goggles trap an air pocket in front of the eyes, restoring the original air-cornea index contrast and therefore the normal focusing power."
  explanation: "This question tests whether students understand the key insight: focal length depends on the surrounding medium, not just the lens material. The cornea functions as a lens, and like any lens, its power depends on the index contrast with its environment. Underwater, that contrast nearly vanishes. The goggles solution is elegant precisely because it requires no change to the optical components — just restoring the air interface."
```

## Explainer

You already know from the thin-lens equation that a converging lens with focal length f forms images according to 1/do + 1/di = 1/f. But where does f come from? The thin-lens equation treats f as a given, leaving the origin of focal length in a black box. The **lensmaker's equation** opens that box: 1/f = (n − 1)(1/R₁ − 1/R₂). It connects the focal length to two physical properties — the refractive index n of the lens material, and the radii of curvature R₁ and R₂ of its two surfaces.

The refractive index n is the same quantity from Snell's law: it measures how much slower light travels in the glass compared to vacuum (n = c/v). A higher n means light bends more steeply at each surface. The factor (n − 1) in the lensmaker's equation captures exactly this: a lens made from high-index glass (n = 1.7) is more powerful than an identical-shaped lens in low-index glass (n = 1.5) because each surface bends the rays more. This is why optical designers can make thinner, lighter lenses by choosing high-index materials — the same focal length can be achieved with gentler, flatter curves.

The radii of curvature R₁ and R₂ describe the shape of each surface. The sign convention follows a consistent rule: a radius is positive if the center of curvature lies to the right of the surface, and negative if it lies to the left. For a standard biconvex lens, R₁ is positive (first surface curves toward the incoming light) and R₂ is negative (second surface curves away from it), making 1/R₁ − 1/R₂ positive overall — which gives a positive f, a converging lens. Flip the geometry to a biconcave lens and the subtraction reverses sign, yielding negative f and a diverging lens. The equation correctly handles any combination of surface shapes.

The most important insight from the lensmaker's equation is that **focal length depends on the surrounding medium**. The full form uses (n_lens/n_medium − 1) in place of (n − 1). In air (n_medium ≈ 1), this reduces to the familiar form. But submerge a glass lens in water, where n_water ≈ 1.33, and the effective index contrast drops sharply. A lens that strongly converges light in air becomes nearly flat — barely converging — in water. This explains why your vision blurs underwater without goggles: the cornea of your eye acts as a lens, and immersed in water it almost entirely loses its refractive power. A swimming mask restores the air gap, reinstating the full index contrast and your sharp vision.
