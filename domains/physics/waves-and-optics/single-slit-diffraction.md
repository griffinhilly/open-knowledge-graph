---
id: single-slit-diffraction
title: Single-Slit Diffraction
domain: physics
course: waves-and-optics
prerequisites:
- id: wave-interference
  type: hard
- id: youngs-double-slit
  type: soft
- id: huygens-principle
  type: soft
builds-toward:
- diffraction-gratings
tags:
- diffraction
- single slit
- Huygens principle
- minima
- central maximum
stage: formal-systems
status: validated
---
# Single-Slit Diffraction

## Core Idea
When light passes through a single finite-width slit, it diffracts and produces a pattern with a wide bright central maximum flanked by narrower secondary maxima. Dark fringes (minima) occur at angles where asinθ = mλ (m = ±1, ±2, …), where a is the slit width. Narrower slits produce wider central maxima — an inverse relationship between slit width and diffraction spreading that fundamentally limits optical resolution.

## How It's Best Learned
Shine a laser through progressively narrower slits and observe the central maximum widening. Compare single-slit and double-slit patterns to understand how single-slit diffraction modulates the double-slit fringe envelope.

## Common Misconceptions
- Diffraction minima for a single slit are at integer multiples of λ/a (unlike double-slit maxima), leading to sign/condition confusion.
- Diffraction occurs for any wave passing any opening; it becomes visible when aperture size is comparable to wavelength.

## Explainer

From your work on wave interference, you know that two coherent waves can add constructively (crest meets crest) or destructively (crest meets trough). In double-slit diffraction, you treated each slit as a point source. Single-slit diffraction asks: what happens when the slit has a finite width and cannot be treated as a point? The answer comes from **Huygens's principle**: every point across the width of the slit acts as an independent point source of secondary wavelets. The single slit is not one source — it is many sources spread across the aperture, all interfering with each other at the screen.

To find the **dark fringes**, divide the slit of width a into pairs of sources separated by half the slit width. At a specific angle θ, the path difference between the top of the slit and the point a/2 below it is (a/2)sinθ. When that path difference equals λ/2, those two sources cancel. But if those two cancel, you can pair up every source in the top half with one in the bottom half — the entire slit cancels, producing the first dark fringe. This occurs when (a/2)sinθ = λ/2, or equivalently asinθ = λ. Repeating the argument by dividing the slit into 4, 6, 8... equal parts gives the general condition for minima: asinθ = mλ for m = ±1, ±2, ….

The inverse relationship between slit width and diffraction spread is the most important takeaway. A narrow slit (a small) requires a smaller θ for path differences to reach λ — so the first minimum appears far from center, and the **central maximum** is wide. A wide slit has many sources that quickly cancel at small angles — the central maximum is narrow. In the limit of a very wide slit, diffraction spreading becomes negligible and you get a sharp geometric shadow. This trade-off — wide aperture gives sharp edges but poor resolving power for closely spaced features, narrow aperture gives broad diffraction but finer angular sensitivity — is fundamental to telescope and microscope design.

Comparing single-slit to double-slit patterns is illuminating. Double-slit produces equally spaced bright fringes. Single-slit produces a bright central maximum that is twice as wide as the secondary maxima, flanked by progressively dimmer bands. When you have both a double slit and finite slit width — the realistic case — the double-slit interference fringes are modulated by the single-slit envelope. Some double-slit maxima are suppressed entirely wherever they coincide with a single-slit minimum. Recognizing this modulation is what separates real optical analysis from idealized point-source models.
