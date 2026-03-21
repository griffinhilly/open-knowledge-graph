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

## Questions

```yaml
- question: "A ray of light travels from air (n = 1.0) into a glass block (n = 1.5). What happens to the ray at the boundary?"
  type: multiple-choice
  options:
    - "It speeds up and bends away from the normal, because glass is denser"
    - "It slows down and bends toward the normal"
    - "It maintains the same speed but changes direction due to a force exerted by the glass surface"
    - "It slows down and bends away from the normal"
  answer: 1
  explanation: "Glass has a higher index of refraction (n = 1.5 > 1.0), which means light travels more slowly in glass than in air (n = c/v, so higher n means lower v). When light slows down at a boundary, the wavefront pivots toward the normal — the slower edge gets 'left behind' as the faster portion catches up. Option A reverses both facts: light slows down (doesn't speed up) and bends toward the normal (not away). Option D gets the speed right but the direction wrong — this is the most common misconception. Option C is wrong because refraction is caused by speed change, not by any surface force."

- question: "What is the correct physical explanation for why a wave changes direction when it crosses a boundary between two media?"
  type: multiple-choice
  options:
    - "The wave is deflected by an electromagnetic force at the boundary between the two materials"
    - "The change in wave speed causes the wavefront to pivot — one side of the wavefront reaches the boundary and slows while the other still travels at the original speed"
    - "Gravity pulls the wave toward denser media, bending its path"
    - "Surface tension at the boundary redirects the wave's momentum"
  answer: 1
  explanation: "Refraction is entirely caused by the difference in wave speed on each side of the boundary — no force is needed. Huygens's principle gives the mechanism: when a wavefront hits the boundary at an angle, the portion that enters the slower medium first is slowed while the portion still in the faster medium continues at full speed. This differential speed causes the wavefront to pivot, changing the direction of propagation. Options A, C, and D all invoke forces or mechanisms that don't exist — refraction is purely a geometric consequence of speed difference."

- question: "When light exits water (n = 1.33) into air (n = 1.0), it bends toward the normal."
  type: true-false
  answer: false
  explanation: "Light bends *toward* the normal when entering a medium where it slows down (going from lower n to higher n). Exiting water into air means going from higher n to lower n — the light speeds up. When light speeds up at a boundary, the wavefront pivots away from the normal. This is the straw-in-water illusion: light from the submerged portion bends away from the normal as it exits the water, making the straw appear displaced. The rule: toward the normal when slowing, away from the normal when speeding up."

- question: "The index of refraction n = c/v is always greater than or equal to 1 for any physical medium, because light cannot travel faster in a medium than it does in a vacuum."
  type: true-false
  answer: true
  explanation: "The vacuum speed c = 3 × 10⁸ m/s is the maximum speed at which light can propagate. In any physical medium — glass, water, air, diamond — the interaction of the electromagnetic wave with matter slows the propagation speed, so v ≤ c and therefore n = c/v ≥ 1. Vacuum has n = 1 exactly. Air is approximately 1.0003 (essentially 1). Water is 1.33, glass ranges from 1.5 to 1.9, and diamond is about 2.4. A value of n < 1 would imply faster-than-c propagation, which is not possible for ordinary light in bulk media."

- question: "Use Huygens's principle to explain why a wavefront bends toward the normal when it enters a medium where the wave travels more slowly."
  type: short-answer
  answer: "Imagine a straight wavefront — a row of crests — approaching a boundary at an angle. The left edge of the wavefront hits the slower medium first and immediately decelerates, while the right edge is still traveling at full speed in the original medium. Because the two edges are moving at different speeds, the wavefront pivots: the slow left edge falls behind while the fast right edge advances. The direction of wave travel is always perpendicular to the wavefront, so as the wavefront pivots, the direction of propagation rotates toward the normal of the boundary. The greater the speed difference, the more the wavefront pivots, and the more the ray bends."
  explanation: "This Huygens argument is more satisfying than just memorizing 'bends toward the normal when slowing' because it shows *why* — the geometry of a non-uniform wavefront pivot. It also immediately tells you the opposite case: when the wave speeds up, the edge entering the faster medium accelerates first, the wavefront pivots the other way, and the ray bends away from the normal."
```

## Explainer

From your study of wave speed in different media, you know that the speed at which a wave travels depends on the properties of the medium — light slows down in glass compared to air, and sound speeds up in water compared to air. Refraction is what happens at the *boundary* between two such media. When a wave crosses from one medium into another where it travels at a different speed, its direction changes. Understanding *why* this happens is more satisfying than memorizing a rule.

The clearest explanation comes from Huygens's principle, which you have encountered as a prerequisite. Imagine a plane wavefront — a straight row of crests — approaching a glass surface at an angle. The left edge of the wavefront hits the glass first and immediately slows down, while the right edge is still traveling at full speed in air. This speed difference causes the wavefront to pivot: the slower left edge gets "left behind" while the faster right edge catches up, rotating the wavefront toward the normal. The direction of wave travel — perpendicular to the wavefront — therefore bends toward the normal when entering the slower medium. The geometry here is trigonometric: the ratio of sines of the angles equals the ratio of speeds, which is why sin θ₁ / sin θ₂ = v₁/v₂.

The **index of refraction** n = c/v is a compact way to characterize how much a medium slows light relative to its vacuum speed c = 3 × 10⁸ m/s. Vacuum has n = 1; air is approximately 1; water is about 1.33; glass ranges from 1.5 to 1.9 depending on composition. A higher index means slower light. The rule for bending now becomes: light bends *toward* the normal when going from a lower-n to a higher-n medium (slowing down), and *away* from the normal when going from higher-n to lower-n (speeding up). The straw-in-water illusion you can demonstrate at home is a direct consequence: light from the submerged straw bends away from the normal as it exits the water, so the straw appears to be at a different position than it actually occupies.

This concept leads directly to Snell's law (n₁ sin θ₁ = n₂ sin θ₂), which is just the precise version of the geometric relationship above. It also sets up total internal reflection — the case where the bending away from the normal is so extreme that no refracted ray can exist at all. And it explains how lenses work: by using curved surfaces to systematically redirect wavefronts, a lens can bring parallel rays to a focus or spread them apart. Refraction is not an exotic phenomenon; it is what every glass lens, eyeglass, camera, and optical fiber relies on.
