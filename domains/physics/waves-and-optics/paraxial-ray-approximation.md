---
id: paraxial-ray-approximation
title: Paraxial Ray Approximation in Geometrical Optics
domain: physics
course: waves-and-optics
prerequisites:
- id: geometric-optics-ray-approximation
  type: hard
builds-toward:
- thin-lenses
- lensmakers-equation
tags:
- paraxial-approximation
- geometrical-optics
- thin-lens
stage: formal-systems
status: draft
---

# Paraxial Ray Approximation in Geometrical Optics

## Core Idea
The paraxial approximation assumes rays travel at small angles to the optical axis (θ ≈ sin θ ≈ tan θ). This simplification yields linear relationships between object distance, image distance, and focal length, making lens and mirror equations tractable. Non-paraxial rays produce spherical aberration.

## Questions

```yaml
- question: "A photographer shoots wide-open (large aperture), and the center of the image is sharp but the edges are blurry. Which phenomenon best explains this?"
  type: multiple-choice
  options:
    - "Diffraction, because the aperture is too small to resolve edge detail"
    - "Spherical aberration, because marginal rays hitting the outer lens fall outside the paraxial regime and focus at a different distance"
    - "Chromatic aberration, because different wavelengths bend differently at the lens edge"
    - "Vignetting, because the lens blocks light at steep angles"
  answer: 1
  explanation: "Wide aperture means more light passes through the outer portions of the lens, where rays strike at steeper angles. These marginal rays are non-paraxial: the approximation sin θ ≈ θ breaks down, so they refract more strongly than paraxial rays and focus at a shorter distance. The result is that the image plane satisfying the paraxial thin-lens equation is sharp for center rays but blurry for edge rays — spherical aberration. This is exactly why professional lenses use aspherical elements: to satisfy the exact focusing condition for marginal rays without relying on the paraxial assumption."

- question: "Why does the paraxial approximation make lens and mirror optics analytically tractable in a way that full trigonometric ray tracing does not?"
  type: multiple-choice
  options:
    - "It eliminates reflections at lens surfaces, reducing the number of equations needed"
    - "It replaces sin θ ≈ θ, making Snell's law linear and ensuring all rays from one point converge to one image point"
    - "It assumes rays travel parallel to the optical axis, so only one angle needs to be tracked"
    - "It ignores diffraction effects, simplifying the wave optics to pure geometry"
  answer: 1
  explanation: "The key is linearity. Full Snell's law is n₁ sin θ₁ = n₂ sin θ₂ — a transcendental equation. Under the paraxial approximation sin θ ≈ θ, it becomes n₁θ₁ = n₂θ₂, which is linear. Linear optics is powerful: superposition holds, rays from different points don't interfere with each other, and the entire system behavior is captured by a small number of parameters (focal length, object distance). Crucially, all paraxial rays from a single object point converge to a single image point — the condition for a well-formed image. The thin-lens equation 1/f = 1/d_o + 1/d_i holds exactly in this regime. Without linearity, you'd need to ray-trace every individual ray numerically."

- question: "A spherical lens will focus all paraxial rays from a single object point to a single image point, but marginal (non-paraxial) rays from the same point will focus at a slightly different distance."
  type: true-false
  answer: true
  explanation: "This is the definition and consequence of spherical aberration. Paraxial rays — those traveling close to the optical axis at small angles — satisfy the approximation sin θ ≈ θ, producing the clean convergence guaranteed by the linear paraxial theory. Marginal rays hit the lens at steeper angles where the approximation fails; they bend more strongly and focus closer to the lens. The result is a distribution of focal points along the axis rather than a single point — the 'circle of least confusion' in the image plane. Aspherical lenses fix this by deliberately departing from a spherical shape so that the exact refraction condition is satisfied for rays at all heights."

- question: "The paraxial approximation holds as long as the wavelength of light is much smaller than the lens aperture — making it a wave optics condition rather than a geometric one."
  type: true-false
  answer: false
  explanation: "The paraxial approximation is purely geometric and depends on the angle of rays to the optical axis, not on wavelength. It states that sin θ ≈ θ (equivalently tan θ ≈ θ), which holds when θ is small in radians — roughly θ < 0.2 rad for errors under 1%. The wavelength-vs-aperture condition you might be thinking of is the criterion for diffraction vs. geometric optics: geometric optics holds when λ is much smaller than aperture features. These are entirely separate conditions. A system can be in the geometric optics regime (small wavelength) but violate the paraxial approximation if marginal rays hit the lens at steep angles."

- question: "Explain why the paraxial approximation produces a simple, linear relationship between object distance, image distance, and focal length — and describe what physically breaks down when the approximation fails."
  type: short-answer
  answer: "The approximation replaces sin θ with θ, linearizing Snell's law. This ensures that all paraxial rays from one object point converge to exactly one image point, and that the convergence depends linearly on object distance — yielding the thin-lens equation 1/f = 1/d_o + 1/d_i. When the approximation fails (marginal rays at steep angles), the exact sin θ refraction causes different rays to focus at different distances, destroying the single focal point and producing spherical aberration."
  explanation: "Linearity is the operative mathematical concept. Linear systems obey superposition, can be described by matrices (the ray-transfer matrix formalism builds on this directly), and guarantee that each object point maps to a unique image point. Once non-linear terms in the angle become significant — scaling as θ³ and higher — the one-to-one mapping from object point to image point breaks. Each annular zone of the lens focuses at a slightly different distance, smearing what should be a point into a circle. Aspherical surfaces and multi-element designs correct for these higher-order terms."
```

## Explainer

From geometric optics, you know that light travels in straight lines called rays and obeys Snell's law at interfaces and the law of reflection at mirrors. In principle, if you know the shape of every optical surface, you could trace any ray through a system exactly. In practice, doing this with the full trigonometric expressions for every ray hitting every curved surface produces equations too complicated to yield insight. The **paraxial approximation** is the controlled simplification that makes lens and mirror optics analytically tractable.

The approximation rests on a Taylor series fact: for small angles θ measured in radians, sin θ ≈ θ and tan θ ≈ θ, with errors that scale as θ³. In a paraxial system — one where all rays stay close to the central **optical axis** — the angles are small enough that this substitution is accurate. Snell's law n₁ sin θ₁ = n₂ sin θ₂ becomes the linear relation n₁θ₁ = n₂θ₂, which is far easier to work with. The consequence is that all paraxial rays from a single object point converge to a single image point. This is the regime where the thin-lens equation 1/f = 1/d_o + 1/d_i holds exactly — the clean, linear relationship you will use throughout geometric optics.

The failure mode of the approximation reveals the physics of **spherical aberration**. For a spherical lens or mirror, rays that arrive far from the axis (marginal rays) hit the surface at steeper angles, where the sin θ ≈ θ approximation breaks down. These rays bend more sharply than paraxial rays and focus at a slightly different distance. Instead of a perfect point image, you get a blurry circle — the circle of least confusion. This is why high-quality camera lenses and telescopes use aspherical optics: by carefully deviating from a spherical shape, optical engineers can satisfy an exact focusing condition for marginal rays without relying on the paraxial approximation.

Think of the paraxial approximation as defining the regime where the optics of a system is **linear**. Linear systems are mathematically powerful: superposition holds, rays from different object points don't interfere with each other's images, and the behavior is fully captured by a small set of parameters (focal length, object distance). This is why paraxial optics forms the foundation for the matrix (ray-transfer matrix) formalism used to design multi-element optical systems — each lens or mirror is represented by a 2×2 matrix, and rays traveling through a sequence of elements are analyzed by matrix multiplication. All of this mathematical structure collapses cleanly from the one assumption: angles are small.
