---
id: refraction-intro
title: Refraction of Waves
domain: physics
course: waves-and-optics
prerequisites:
- id: wave-speed-medium
  type: hard
- id: reflection-law
  type: soft
- id: huygens-principle
  type: soft
- id: trigonometric-ratios-review
  type: soft
builds-toward:
- snells-law
- total-internal-reflection
- thin-lenses
tags:
- refraction
- bending
- index of refraction
- boundary
- Huygens
stage: formal-systems
status: validated
---
# Refraction of Waves

## Core Idea
When a wave crosses a boundary between two media in which it travels at different speeds, its direction changes — this is refraction. The wave bends toward the normal when slowing down (entering a denser medium) and away from the normal when speeding up. The index of refraction n = c/v quantifies how much a medium slows light compared to the vacuum speed c = 3 × 10⁸ m/s. Refraction is caused by the change in wave speed, not by any force on the wave.

## How It's Best Learned
Place a pencil in a glass of water and observe the apparent bend. Then use wavefront diagrams (Huygens construction) to show geometrically why the wave direction changes at a boundary where speed differs.

## Common Misconceptions
- Refraction is not caused by the wave 'hitting' the medium; it is a consequence of different propagation speeds on each side.
- A wave entering a denser medium bends toward the normal — many students expect it to bend away.

## Explainer

From your study of wave speed in different media, you know that the speed at which a wave travels depends on the properties of the medium — light slows down in glass compared to air, and sound speeds up in water compared to air. Refraction is what happens at the *boundary* between two such media. When a wave crosses from one medium into another where it travels at a different speed, its direction changes. Understanding *why* this happens is more satisfying than memorizing a rule.

The clearest explanation comes from Huygens's principle, which you have encountered as a prerequisite. Imagine a plane wavefront — a straight row of crests — approaching a glass surface at an angle. The left edge of the wavefront hits the glass first and immediately slows down, while the right edge is still traveling at full speed in air. This speed difference causes the wavefront to pivot: the slower left edge gets "left behind" while the faster right edge catches up, rotating the wavefront toward the normal. The direction of wave travel — perpendicular to the wavefront — therefore bends toward the normal when entering the slower medium. The geometry here is trigonometric: the ratio of sines of the angles equals the ratio of speeds, which is why sin θ₁ / sin θ₂ = v₁/v₂.

The **index of refraction** n = c/v is a compact way to characterize how much a medium slows light relative to its vacuum speed c = 3 × 10⁸ m/s. Vacuum has n = 1; air is approximately 1; water is about 1.33; glass ranges from 1.5 to 1.9 depending on composition. A higher index means slower light. The rule for bending now becomes: light bends *toward* the normal when going from a lower-n to a higher-n medium (slowing down), and *away* from the normal when going from higher-n to lower-n (speeding up). The straw-in-water illusion you can demonstrate at home is a direct consequence: light from the submerged straw bends away from the normal as it exits the water, so the straw appears to be at a different position than it actually occupies.

This concept leads directly to Snell's law (n₁ sin θ₁ = n₂ sin θ₂), which is just the precise version of the geometric relationship above. It also sets up total internal reflection — the case where the bending away from the normal is so extreme that no refracted ray can exist at all. And it explains how lenses work: by using curved surfaces to systematically redirect wavefronts, a lens can bring parallel rays to a focus or spread them apart. Refraction is not an exotic phenomenon; it is what every glass lens, eyeglass, camera, and optical fiber relies on.
