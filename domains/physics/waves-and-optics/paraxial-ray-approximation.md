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

## Explainer

From geometric optics, you know that light travels in straight lines called rays and obeys Snell's law at interfaces and the law of reflection at mirrors. In principle, if you know the shape of every optical surface, you could trace any ray through a system exactly. In practice, doing this with the full trigonometric expressions for every ray hitting every curved surface produces equations too complicated to yield insight. The **paraxial approximation** is the controlled simplification that makes lens and mirror optics analytically tractable.

The approximation rests on a Taylor series fact: for small angles θ measured in radians, sin θ ≈ θ and tan θ ≈ θ, with errors that scale as θ³. In a paraxial system — one where all rays stay close to the central **optical axis** — the angles are small enough that this substitution is accurate. Snell's law n₁ sin θ₁ = n₂ sin θ₂ becomes the linear relation n₁θ₁ = n₂θ₂, which is far easier to work with. The consequence is that all paraxial rays from a single object point converge to a single image point. This is the regime where the thin-lens equation 1/f = 1/d_o + 1/d_i holds exactly — the clean, linear relationship you will use throughout geometric optics.

The failure mode of the approximation reveals the physics of **spherical aberration**. For a spherical lens or mirror, rays that arrive far from the axis (marginal rays) hit the surface at steeper angles, where the sin θ ≈ θ approximation breaks down. These rays bend more sharply than paraxial rays and focus at a slightly different distance. Instead of a perfect point image, you get a blurry circle — the circle of least confusion. This is why high-quality camera lenses and telescopes use aspherical optics: by carefully deviating from a spherical shape, optical engineers can satisfy an exact focusing condition for marginal rays without relying on the paraxial approximation.

Think of the paraxial approximation as defining the regime where the optics of a system is **linear**. Linear systems are mathematically powerful: superposition holds, rays from different object points don't interfere with each other's images, and the behavior is fully captured by a small set of parameters (focal length, object distance). This is why paraxial optics forms the foundation for the matrix (ray-transfer matrix) formalism used to design multi-element optical systems — each lens or mirror is represented by a 2×2 matrix, and rays traveling through a sequence of elements are analyzed by matrix multiplication. All of this mathematical structure collapses cleanly from the one assumption: angles are small.
