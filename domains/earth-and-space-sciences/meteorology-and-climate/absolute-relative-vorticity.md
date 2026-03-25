---
id: absolute-relative-vorticity
title: Absolute and Relative Vorticity
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: coriolis-effect
  type: hard
- id: wind-shear-and-vorticity
  type: hard
- id: moisture-transport-and-advection
  type: soft
builds-toward:
- potential-vorticity-conservation
tags:
- rotation
- vorticity
- wind
- shear
stage: advanced
status: validated
---
# Absolute and Relative Vorticity

## Core Idea
Absolute vorticity is the sum of the planet's rotation (planetary vorticity, 2Ω) and the wind's rotation relative to the Earth (relative vorticity). In the Northern Hemisphere, planetary vorticity is always positive, meaning even still air has vorticity due to Earth's rotation. Cyclones have large positive relative vorticity, while anticyclones have negative relative vorticity that can partially cancel planetary vorticity.

## How It's Best Learned
Calculate relative vorticity from wind field divergence using finite differences. Trace how total absolute vorticity changes along a parcel trajectory.

## Questions

```yaml
- question: "An air parcel at 45°N has zero relative vorticity and moves poleward to 60°N. What happens to its relative vorticity, and why?"
  type: multiple-choice
  options:
    - "Relative vorticity increases (becomes more cyclonic) because faster Coriolis deflection at higher latitudes generates additional spin"
    - "Relative vorticity remains zero because the parcel started with no spin and nothing has changed the local wind field"
    - "Relative vorticity decreases (becomes more anticyclonic) because absolute vorticity is approximately conserved — as planetary vorticity f increases with latitude, relative vorticity ζ must decrease to compensate"
    - "Relative vorticity increases because upper-level wind shear intensifies at higher latitudes"
  answer: 2
  explanation: "Absolute vorticity (ζ + f) is approximately conserved following an air parcel. At 45°N, f is some value f₁; at 60°N, f₂ > f₁. To maintain ζ + f = constant, ζ must decrease by the same amount f increased. The parcel that started with zero relative vorticity develops negative (anticyclonic) relative vorticity. This is the fundamental mechanism driving Rossby wave propagation — poleward displacement generates anticyclonic curvature that turns the parcel back equatorward."

- question: "At the equator, why is planetary vorticity zero even though Earth is continuously rotating?"
  type: multiple-choice
  options:
    - "The Coriolis effect is zero at the equator, which eliminates the contribution of Earth's rotation to vorticity"
    - "Equatorial air masses move faster than air at higher latitudes, which cancels Earth's rotational contribution"
    - "Planetary vorticity (f = 2Ω sinφ) measures the component of Earth's rotation about a vertical axis; at the equator Earth's rotation axis is horizontal, so there is no vertical-axis spin component to contribute"
    - "Equatorial winds are predominantly zonal, so there is no meridional component to generate vertical vorticity"
  answer: 2
  explanation: "Planetary vorticity measures how much of Earth's rotation acts about a local vertical axis. At the poles (φ = 90°), the Earth's rotation axis is vertical, so all of Earth's spin contributes: f = 2Ω. At the equator (φ = 0°), Earth's rotation axis is horizontal — the axis points parallel to the surface, not perpendicular to it — so it contributes zero spin about the local vertical. The sin(φ) factor captures this geometry: it is the projection of Earth's angular velocity vector onto the local vertical."

- question: "A cyclone in the Northern Hemisphere has positive relative vorticity, and since planetary vorticity at that latitude is also positive, the cyclone's absolute vorticity exceeds its relative vorticity alone."
  type: true-false
  answer: true
  explanation: "Absolute vorticity = ζ (relative) + f (planetary). In the Northern Hemisphere, f = 2Ω sinφ > 0 everywhere. A cyclone has ζ > 0 by definition (counterclockwise rotation). Therefore ζ + f > ζ: absolute vorticity exceeds relative vorticity. This means that even a very weakly rotating cyclone has substantial absolute vorticity because planetary vorticity adds to it. At mid-latitudes, f ≈ 10⁻⁴ s⁻¹, which is comparable to or larger than relative vorticity in many synoptic systems."

- question: "When an upper-level air parcel moves equatorward, its relative vorticity decreases because it is moving away from the high-latitude source of planetary rotation."
  type: true-false
  answer: false
  explanation: "Equatorward movement decreases planetary vorticity f (since f = 2Ω sinφ decreases toward the equator). To conserve absolute vorticity (ζ + f = constant), relative vorticity ζ must *increase* to compensate. The parcel develops positive (cyclonic) relative vorticity — it begins spinning counterclockwise in the Northern Hemisphere. This cyclonic curvature eventually turns the parcel back poleward, setting up the oscillating Rossby wave pattern. The common error is forgetting the conservation relationship and thinking the parcel simply 'loses' rotation."

- question: "Explain how conservation of absolute vorticity causes air parcels displaced poleward to develop anticyclonic curvature, and how this produces the wavelike Rossby wave pattern in the mid-latitude upper atmosphere."
  type: short-answer
  answer: "When a parcel moves poleward, f increases. To conserve ζ + f, relative vorticity ζ decreases — the parcel acquires anticyclonic (clockwise in the NH) curvature. This curves the flow back equatorward. Once moving equatorward, f decreases and ζ must increase — the parcel acquires cyclonic curvature, turning it poleward again. This oscillation between poleward displacement (anticyclonic response, equatorward turning) and equatorward displacement (cyclonic response, poleward turning) produces the large-scale wave pattern. These planetary waves, known as Rossby waves, propagate westward relative to the mean flow and steer surface weather systems."
  explanation: "The key is that absolute vorticity conservation makes the atmosphere behave like a restoring-force system: poleward displacement generates the anticyclonic curvature that returns the parcel equatorward, and equatorward displacement generates the cyclonic curvature that returns it poleward. The result is a standing or slowly propagating wave rather than unlimited straight-line motion. The wavelength and propagation speed of Rossby waves depend on the meridional gradient of f (the β effect), which is why they only form in rotating systems and are absent at the equator."
```

## Explainer

You already know from studying the Coriolis effect that Earth's rotation deflects moving air, and from wind shear and vorticity that spinning motion in the atmosphere can be measured as vorticity — the tendency of air to rotate about a vertical axis. The next step is recognizing that the atmosphere always has two sources of rotation happening simultaneously, and separating them is essential for understanding how weather systems develop and move.

**Relative vorticity** is the spin of the wind as seen by someone standing on Earth's surface. A counterclockwise-rotating low-pressure system in the Northern Hemisphere has positive relative vorticity; a clockwise-spinning anticyclone has negative relative vorticity. You can estimate it by looking at how wind speed and direction change across a region — if the winds curve cyclonically or if there is strong speed shear across the flow, relative vorticity is large. Think of it as the local spin the atmosphere has generated through its own dynamics — pressure gradients, friction, and convergence.

**Planetary vorticity** is the spin that Earth's rotation contributes, even to perfectly still air. At the poles, a stationary air parcel completes one full rotation per day relative to the stars, so planetary vorticity is at its maximum. At the equator, a parcel sitting on the surface has no vertical-axis rotation from Earth's spin, so planetary vorticity is zero. The quantity varies smoothly with latitude and equals 2Ω sin(φ), where Ω is Earth's angular velocity and φ is latitude. This is the same Coriolis parameter f you encountered earlier.

**Absolute vorticity** is simply the sum of these two: relative vorticity plus planetary vorticity (ζ + f). It represents the total spin of an air parcel as viewed from space. This quantity matters because it is approximately conserved as air parcels move — a principle that leads directly to potential vorticity conservation. When a parcel moves poleward, f increases, so ζ must decrease to compensate: the flow becomes more anticyclonic. When a parcel moves equatorward, f decreases and ζ increases, promoting cyclonic curvature. This trade-off between planetary and relative vorticity explains why upper-level troughs and ridges develop wavelike patterns — the atmosphere is constantly adjusting its spin budget as parcels shift latitude, producing the Rossby waves that steer weather systems across the mid-latitudes.
