---
id: optical-path-length-definition
title: Optical Path Length and Its Role in Interference
domain: physics
course: waves-and-optics
prerequisites:
- id: optical-path-and-phase
  type: soft
- id: refractive-index-material-wavelength
  type: hard
builds-toward:
- thin-film-interference
tags:
- optical-path-length
- phase
- interference
stage: advanced
status: draft
---

# Optical Path Length and Its Role in Interference

## Core Idea
Optical path length is OPL = ∫n·ds along a ray path. It determines phase accumulation: phase = 2π·OPL/λ₀. Two rays with equal optical path length accumulate equal phase, making optical path length the relevant quantity for determining interference, not geometric path length alone.

## Explainer

You already know that the refractive index n of a material tells you how much slower light travels there compared to a vacuum: v = c/n. A direct consequence is that the **wavelength shortens** inside the medium. If the frequency stays constant (it must, since energy must cross the boundary continuously), and the speed drops by a factor of n, then λ_medium = λ₀/n. This means light waves oscillate more times per unit distance inside a denser material — they accumulate phase faster.

**Optical path length** (OPL) is the accounting tool for this. Instead of asking "how far did the ray travel geometrically?", you ask "how much of a vacuum-equivalent path would produce the same phase accumulation?" The answer is OPL = n × (geometric distance). If light travels 1 cm through glass with n = 1.5, it accumulates the same phase as if it had traveled 1.5 cm in vacuum. The phase gained is always φ = 2π × OPL / λ₀, where λ₀ is the free-space wavelength.

This matters enormously for interference. Two rays interfere constructively when their phase difference is 0, 2π, 4π, … and destructively when it is π, 3π, 5π, … The phase difference depends not on how far each ray traveled geometrically, but on the **optical path difference** (OPD = OPL₁ − OPL₂). Two rays that travel the same geometric distance can still interfere destructively if one passes through a denser medium — it has a longer OPL and therefore a different phase on arrival. Conversely, two rays that travel different geometric distances can interfere constructively if their OPLs happen to be equal.

A practical illustration: when a camera lens has an anti-reflection coating, the coating thickness is chosen so that the ray reflecting off the front surface of the coating and the ray reflecting off the back surface travel an OPD of exactly half a wavelength — producing destructive interference that suppresses glare. This is the concept of **thin-film interference**, which is where this topic builds toward. The entire calculation rests on computing OPL for each partial ray and finding their difference.

