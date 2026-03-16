---
id: satellite-tidal-evolution
title: Satellite Orbital Evolution and Tidal Dissipation
domain: earth-and-space-sciences
course: planetary-science
prerequisites:
- id: satellite-formation-and-orbital-mechanics
  type: hard
- id: tidal-heating-moon-interiors
  type: hard
tags:
- satellites
- tides
- orbital-evolution
- dissipation
stage: advanced
status: draft
---

# Satellite Orbital Evolution and Tidal Dissipation

## Core Idea
Satellites gradually migrate due to tidal dissipation in their interiors or their parent planet. Earth's Moon recedes at ~3.8 cm/yr; many moons migrated substantially from their formation locations. Migration rates depend on tidal dissipation factors and orbital parameters. Understanding tidal evolution explains present-day orbital configurations and infers past dynamical states.

## How It's Best Learned
Calculate tidal dissipation rates using Love numbers and orbital elements. Integrate orbital evolution equations to predict future satellite positions.

## Common Misconceptions
- All satellites move outward; some moons in resonances or irregular orbits can migrate inward.
- Tidal dissipation is negligible in modern satellites; it remains significant and drives ongoing evolution.

## Explainer

You already know that tidal forces heat satellite interiors — Io's volcanism is the dramatic example. But tidal interactions do more than generate heat: they systematically reshape orbits over billions of years. The core mechanism is a **transfer of angular momentum** between a planet's rotation and a satellite's orbit, mediated by the tidal bulge. When a moon orbits slower than its planet rotates (as our Moon does relative to Earth), the planet's tidal bulge is carried slightly ahead of the moon by the planet's faster rotation. This offset bulge exerts a gravitational tug that pulls the moon forward in its orbit, adding energy and causing it to **spiral outward**. Simultaneously, the moon's gravity pulls back on the bulge, slowing the planet's rotation. Earth's day is getting longer by about 2.3 milliseconds per century, and the Moon recedes at roughly 3.8 cm per year — both consequences of the same angular momentum transfer.

The rate of orbital migration depends on the **tidal dissipation factor** (often written as Q), which quantifies how efficiently a body converts tidal flexing into heat. A low Q means high dissipation — the body is "squishy" and absorbs tidal energy readily, producing large tidal bulges with significant lag angles. A high Q means the body responds nearly elastically, with small bulge offsets and slow orbital evolution. Earth's Q for the Moon is roughly 12, meaning it dissipates tidal energy fairly efficiently. Jupiter's Q is much higher (~10⁵), but its enormous mass still drives significant migration of its moons. The **Love number** (k₂) quantifies the amplitude of the tidal deformation itself, and the ratio k₂/Q determines the overall migration rate.

The direction of migration is not always outward. If a satellite orbits *inside* the planet's synchronous orbit — faster than the planet rotates — the tidal bulge lags behind the moon rather than leading it. The gravitational torque then pulls the moon backward, causing it to **spiral inward** and eventually risk destruction at the Roche limit. Phobos, Mars's inner moon, is a textbook case: it orbits faster than Mars rotates and is predicted to either crash into Mars or be torn apart within roughly 50 million years. This inward-versus-outward distinction is determined entirely by whether the satellite's orbital period is shorter or longer than the planet's rotation period.

Tidal evolution also explains **orbital resonances** — the striking integer ratios between orbital periods seen in systems like Jupiter's Galilean moons (Io:Europa:Ganymede in a 1:2:4 resonance). As moons migrate outward at different rates, they can become locked into resonances where gravitational kicks at regular intervals prevent further divergence. Once captured in resonance, the moons' eccentricities are pumped up, intensifying tidal heating — which is precisely why Europa maintains a subsurface ocean and Io is the most volcanically active body in the solar system. The present-day orbital architecture of satellite systems is thus a fossil record of billions of years of tidal evolution, and running the orbital equations backward lets us reconstruct where moons formed and how they reached their current configurations.
