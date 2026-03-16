---
id: compound-optical-systems
title: 'Compound Optical Systems: Lenses and Mirrors in Combination'
domain: physics
course: waves-and-optics
prerequisites:
- id: lens-combinations
  type: hard
builds-toward:
- optical-instruments
tags:
- compound-systems
- lens-combinations
- system-design
stage: formal-systems
status: draft
---

# Compound Optical Systems: Lenses and Mirrors in Combination

## Core Idea
In compound systems, the image from one lens/mirror serves as the object for the next. Overall magnification is the product of individual magnifications: M_total = M₁ × M₂ × ... Effective focal length can be calculated from component powers: 1/f_eff = 1/f₁ + 1/f₂ - d/(f₁f₂) with separation d.

## Explainer

From your study of lens combinations, you know the thin-lens equation (1/f = 1/dₒ + 1/dᵢ) and how to calculate where a lens forms an image and how magnified it is. A compound optical system is just the logical extension: instead of stopping after one lens, you take the image that first lens produces and treat it as the object for the next lens. The chain rule of optics — each element's output becomes the next element's input — is the foundational idea.

Here is the procedure concretely. For a two-lens system, first apply the thin-lens equation to lens 1 alone: given the object distance dₒ₁, find image distance dᵢ₁ and magnification M₁ = −dᵢ₁/dₒ₁. Now that image becomes the object for lens 2. If the lenses are separated by distance d, then the object distance for lens 2 is dₒ₂ = d − dᵢ₁. Apply the thin-lens equation again to find dᵢ₂ and M₂. The **total magnification** is M_total = M₁ × M₂ — the magnifications multiply. If M₁ = −3 and M₂ = −2, the system magnifies by 6 and produces an upright image (two sign flips cancel).

The compound microscope is the canonical example. An **objective lens** with short focal length sits close to the specimen, forming a greatly magnified real intermediate image somewhere inside the instrument body. An **eyepiece lens** then acts like a magnifying glass, re-magnifying that intermediate image as you look through it. Neither lens alone could achieve the combined magnification without requiring physically impractical distances. The telescope works similarly but in reverse priority — the objective collects distant parallel light, the eyepiece magnifies the intermediate image — and here angular magnification (ratio of apparent size with vs. without the instrument) is more useful than lateral magnification.

The **effective focal length** formula 1/f_eff = 1/f₁ + 1/f₂ − d/(f₁f₂) handles the general case with arbitrary separation d. Notice the limiting case: when d = 0 (lenses in contact), the last term vanishes and 1/f_eff = 1/f₁ + 1/f₂. This is the **optical power** (in diopters, P = 1/f) additive rule — powers add when elements are in contact. Optometrists use this directly when combining corrective lens prescriptions. Increasing d from zero reduces the effective focal length (for two converging lenses), which is why long-focal-length objectives combined with eyepieces in a telescope tube achieve better magnification than either element alone.
