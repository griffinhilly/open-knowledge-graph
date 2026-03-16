---
id: exoplanet-orbital-determination-methods
title: Exoplanet Detection and Orbital Parameters
domain: earth-and-space-sciences
course: astronomy
prerequisites:
- id: kepler-laws-orbital-motion-derivation
  type: hard
- id: stellar-parallax-distance-measurement
  type: soft
builds-toward:
- planetary-mass-determination-techniques
tags:
- exoplanets
- detection-methods
- orbital-dynamics
stage: formal-systems
status: draft
---

# Exoplanet Detection and Orbital Parameters

## Core Idea
The radial velocity method detects planets through periodic Doppler shifts in stellar light caused by the star's orbital motion around the system's barycenter, revealing minimum planetary mass and orbital period. The transit method measures the dimming of starlight as a planet passes in front of its host star, yielding planetary radius and orbital inclination. Combining both methods yields the actual mass and complete orbital characterization. Direct imaging, astrometry, and timing variations provide complementary detections.

## Explainer

From Kepler's laws you already know that a planet's orbital period and semi-major axis are linked to the mass of the system. The key insight behind exoplanet detection is that a planet does not simply orbit a star — the star and planet both orbit their common center of mass, called the **barycenter**. Even a massive star wobbles slightly in response to a planet's gravitational pull, and that wobble encodes information about the planet's orbit. The two most productive detection methods exploit this wobble in different ways.

The **radial velocity method** measures the star's wobble along our line of sight using the Doppler effect. As the star moves toward us, its light shifts slightly blueward; as it moves away, the shift is redward. The period of this oscillation gives the planet's orbital period directly, and the amplitude of the velocity shift reveals how hard the planet is tugging — which depends on the planet's mass and the orbital inclination. Because we only measure motion along the line of sight, radial velocity yields a **minimum mass** (M sin i), not the true mass. A face-on orbit, for example, would produce no radial motion at all even though the star wobbles just as much in the plane of the sky.

The **transit method** works from a different geometric vantage. When a planet's orbit is nearly edge-on to us, the planet passes in front of its star once per orbit, blocking a fraction of the starlight. The depth of the brightness dip tells you the ratio of the planet's cross-sectional area to the star's — giving the planet's radius directly. The timing of repeated transits pins down the orbital period with extraordinary precision. Crucially, a transit also tells you the orbital inclination is close to 90°, which resolves the sin i ambiguity from radial velocity. Combining transit radius with radial velocity mass gives you the planet's **mean density**, the single most diagnostic quantity for distinguishing rocky worlds from gas giants.

Other methods fill important niches. **Direct imaging** captures photons from the planet itself, but requires the planet to be bright, far from its star, and young (so it still glows from formation heat). **Astrometry** measures the star's wobble in the plane of the sky rather than along the line of sight, complementing radial velocity. **Transit timing variations** detect unseen planets through the gravitational tugs they exert on a known transiting planet, shifting its transit times forward or backward by seconds to minutes. Each method has its own selection biases — radial velocity favors massive, close-in planets; transits require edge-on geometry; direct imaging favors wide, luminous companions — so a complete census of exoplanets requires all of them working together.
