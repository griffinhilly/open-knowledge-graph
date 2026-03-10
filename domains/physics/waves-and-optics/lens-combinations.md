---
id: lens-combinations
title: Lens Combinations and Multi-Element Systems
domain: physics
course: waves-and-optics
prerequisites:
- id: thin-lens-equation
  type: hard
builds-toward:
- optical-instruments
tags:
- lens combination
- compound lens
- effective focal length
- image relay
stage: formal-systems
status: draft
---

# Lens Combinations and Multi-Element Systems

## Core Idea
When two thin lenses are in contact, their effective focal length is 1/f_eff = 1/f₁ + 1/f₂. For separated lenses, the image formed by the first lens serves as the object for the second; image location and magnification are computed sequentially using the thin lens equation at each stage. The total magnification is the product of individual magnifications. All real optical instruments — cameras, microscopes, telescopes — are multi-element lens systems analyzed this way.

## How It's Best Learned
Work through a two-lens problem step by step: find the image from lens 1, use it as the object for lens 2, and compute total magnification. Then verify with a direct calculation using 1/f_eff for lenses in contact.

## Common Misconceptions
- For separated lenses, you cannot simply add 1/f values; the intermediate image location depends on the separation distance.
- A virtual image from lens 1 can serve as a real object for lens 2 — track whether the intermediate image falls before or after the second lens.
