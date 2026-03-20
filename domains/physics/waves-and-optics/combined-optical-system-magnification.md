---
id: combined-optical-system-magnification
title: Compound Optical Systems and Total Magnification
domain: physics
course: waves-and-optics
prerequisites:
- id: lens-equation-magnification-formula
  type: hard
tags:
- optics
- magnification
- instruments
stage: advanced
status: draft
---

# Compound Optical Systems and Total Magnification

## Core Idea
Two or more lenses in sequence create compound systems like microscopes and telescopes. The image from the first lens becomes the object for the second. Total magnification is the product of individual magnifications: M_total = m₁ × m₂ × ... Proper spacing and focal length choice determine whether the system produces erect or inverted images and its resolving power.

## How It's Best Learned
Design a simple two-lens magnifier: place a strong converging lens (high power) near the object, then a weaker lens farther away to form a virtual image.

## Common Misconceptions
Magnification and resolution are separate properties—high magnification without sufficient aperture produces a blurry, magnified image.

## Explainer

You already know the lens equation (1/f = 1/dₒ + 1/dᵢ) and that the lateral magnification of a single lens is m = −dᵢ/dₒ. A compound optical system simply chains this process: the image formed by the first lens becomes the **object** for the second lens. The light doesn't "know" it passed through two separate lenses — it just continues propagating, and the second lens treats the incoming wavefronts exactly as if a physical object were sitting at the position of the intermediate image. This is the key insight: you can apply single-lens analysis twice in sequence.

The **total magnification** of a two-lens system is M = m₁ × m₂. This multiplicative rule follows directly from the definition of magnification as a ratio of image size to object size. If the first lens makes the image 5× larger, and the second lens magnifies that image 10×, the final image is 50× the original object. A compound microscope exploits this: an **objective lens** with short focal length is placed very close to the specimen, producing a large intermediate image inside the tube. An **eyepiece** then acts like a simple magnifier, enlarging that intermediate image for the eye. A refracting telescope uses the same structure but with different focal lengths — a long-focal-length **objective** collects light from distant objects and forms a diminished intermediate image near its focal point, then a short-focal-length eyepiece magnifies it again.

Sign conventions matter here. Each lens in the chain produces an image that can be real (on the far side of the lens) or virtual (on the near side), and erect or inverted. The first lens in a microscope typically produces a real, inverted intermediate image, which the eyepiece then re-inverts — so the final image as seen by the eye is inverted relative to the original specimen. Telescopes are often designed to accept this inversion (stars don't have an "up"), but terrestrial scopes add a third optical element or prism to restore orientation.

The product rule for magnification tempts students to think bigger lenses always help. But magnification and **angular resolution** are independent. Resolution is set by the **numerical aperture** (NA) — the ability to collect light at wide angles and distinguish closely spaced features. A system with ×1000 total magnification but low NA produces what microscopists call "empty magnification": the image is large but shows no new detail. Useful magnification is bounded by ~500–1000× NA. This is why choosing objectives with high NA (large diameter, short working distance) is just as important as choosing high magnification values.
