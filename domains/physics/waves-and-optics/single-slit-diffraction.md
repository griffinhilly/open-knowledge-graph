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
- id: diffraction-and-huygen-principle
  type: hard
builds-toward:
- diffraction-gratings
tags:
- diffraction
- single slit
- Huygens principle
- minima
- central maximum
stage: advanced
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

## Questions

```yaml
- question: "A laser shines through a slit of width a and produces a diffraction pattern on a screen. The slit is then narrowed to a/2. What happens to the central maximum?"
  type: multiple-choice
  options:
    - "It becomes narrower, because less light passes through and the beam is more concentrated"
    - "It stays the same width, since the wavelength of light hasn't changed"
    - "It becomes wider, because narrowing the slit increases the angular spread of diffraction"
    - "It disappears, because slits narrower than the wavelength produce no diffraction pattern"
  answer: 2
  explanation: "The width of the central maximum is inversely proportional to slit width: the first minimum occurs at sinθ = λ/a, so halving a doubles the angle to the first minimum — the central maximum doubles in width. This is the key inverse relationship: wider slits produce sharper, more compact diffraction patterns; narrower slits produce wider, more spread-out patterns. Option A is the common misconception — students expect a smaller opening to confine the light, but diffraction works opposite to geometric optics."

- question: "Why does a single slit produce dark fringes? Which argument best explains the first minimum at asinθ = λ?"
  type: multiple-choice
  options:
    - "The slit absorbs light at the edges, creating periodic dark bands"
    - "The first minimum occurs when the path difference between the top and bottom of the slit equals exactly one full wavelength"
    - "The slit is divided into two halves; when each point in the top half cancels with the corresponding point in the bottom half (path difference λ/2), the entire slit destructively interferes"
    - "The dark fringes arise because single-slit diffraction and double-slit interference superpose and cancel at these angles"
  answer: 2
  explanation: "By pairing each point in the top half of the slit with a corresponding point half-a-slit-width below it, the path difference at the first minimum is (a/2)sinθ = λ/2 — causing destructive interference. Because EVERY pair across the entire slit cancels, the total amplitude at the screen is zero. The condition a sinθ = λ follows. The same pairing argument extends to higher minima by dividing the slit into 4, 6, 8 equal parts. Option B is wrong because it's the path difference between the top and midpoint (a/2) that equals λ/2, not the full slit width."

- question: "A narrower slit produces a narrower diffraction pattern because less light passes through, reducing the spread."
  type: true-false
  answer: false
  explanation: "This reverses the actual relationship. Narrowing the slit WIDENS the diffraction pattern — the central maximum grows broader and the secondary maxima spread out. This is captured by the inverse relationship in the minima condition: sinθ_min = λ/a. A smaller a means a larger θ for the first minimum, so the central maximum spans a wider angle. Geometric optics intuition (smaller hole = tighter beam) breaks down when the slit size approaches the wavelength; diffraction dominates and the pattern expands."

- question: "The central maximum of a single-slit diffraction pattern is twice as wide (in angular terms) as each of the secondary maxima."
  type: true-false
  answer: true
  explanation: "The central maximum spans from the first minimum on one side (θ = arcsin(λ/a)) to the first minimum on the other side — a total angular width of 2arcsin(λ/a), or approximately 2λ/a for small angles. The secondary maxima each span from one minimum to the next: from mλ/a to (m+1)λ/a — roughly λ/a wide. So the central maximum is indeed about twice the width of each secondary maximum. This asymmetry (wider central peak, progressively dimmer side bands) is the signature feature that distinguishes single-slit from double-slit patterns."

- question: "Why does making a slit narrower cause the diffraction pattern to become wider rather than narrower?"
  type: short-answer
  answer: "Single-slit diffraction arises from Huygens's principle: every point across the slit's width acts as an independent source of secondary wavelets, and these sources interfere with each other at the screen. Dark fringes appear where pairs of sources across the slit cancel destructively. The condition for the first dark fringe is asinθ = λ — where a is the slit width. A narrower slit (smaller a) requires a LARGER angle θ for this path difference to be reached, so the first dark fringe moves farther from center. The central maximum, bounded by the first dark fringes on either side, therefore becomes wider. The physical intuition is that a narrower aperture imposes a tighter spatial constraint, which by the wave uncertainty principle requires a broader angular spread."
  explanation: "This inverse relationship between aperture and diffraction spread is fundamental to optical instrument design: wide telescope mirrors give sharp images (narrow diffraction) but poor ability to resolve fine angular features near a bright source; narrow apertures give blurry images but reveal fine angular structure through wide diffraction."
```

## Explainer

From your work on wave interference, you know that two coherent waves can add constructively (crest meets crest) or destructively (crest meets trough). In double-slit diffraction, you treated each slit as a point source. Single-slit diffraction asks: what happens when the slit has a finite width and cannot be treated as a point? The answer comes from **Huygens's principle**: every point across the width of the slit acts as an independent point source of secondary wavelets. The single slit is not one source — it is many sources spread across the aperture, all interfering with each other at the screen.

To find the **dark fringes**, divide the slit of width a into pairs of sources separated by half the slit width. At a specific angle θ, the path difference between the top of the slit and the point a/2 below it is (a/2)sinθ. When that path difference equals λ/2, those two sources cancel. But if those two cancel, you can pair up every source in the top half with one in the bottom half — the entire slit cancels, producing the first dark fringe. This occurs when (a/2)sinθ = λ/2, or equivalently asinθ = λ. Repeating the argument by dividing the slit into 4, 6, 8... equal parts gives the general condition for minima: asinθ = mλ for m = ±1, ±2, ….

The inverse relationship between slit width and diffraction spread is the most important takeaway. A narrow slit (a small) requires a smaller θ for path differences to reach λ — so the first minimum appears far from center, and the **central maximum** is wide. A wide slit has many sources that quickly cancel at small angles — the central maximum is narrow. In the limit of a very wide slit, diffraction spreading becomes negligible and you get a sharp geometric shadow. This trade-off — wide aperture gives sharp edges but poor resolving power for closely spaced features, narrow aperture gives broad diffraction but finer angular sensitivity — is fundamental to telescope and microscope design.

Comparing single-slit to double-slit patterns is illuminating. Double-slit produces equally spaced bright fringes. Single-slit produces a bright central maximum that is twice as wide as the secondary maxima, flanked by progressively dimmer bands. When you have both a double slit and finite slit width — the realistic case — the double-slit interference fringes are modulated by the single-slit envelope. Some double-slit maxima are suppressed entirely wherever they coincide with a single-slit minimum. Recognizing this modulation is what separates real optical analysis from idealized point-source models.
