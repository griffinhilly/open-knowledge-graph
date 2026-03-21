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

## Questions

```yaml
- question: "A planet detected by the radial velocity method produces a signal with M sin i = 2.0 Jupiter masses. What can be concluded about the planet's true mass?"
  type: multiple-choice
  options:
    - "The true mass is exactly 2.0 Jupiter masses, since M sin i gives the actual mass"
    - "The true mass is at least 2.0 Jupiter masses — it could be higher depending on orbital inclination"
    - "The true mass is at most 2.0 Jupiter masses — sin i ≤ 1 means M sin i overestimates mass"
    - "The true mass cannot be determined at all without direct imaging"
  answer: 1
  explanation: "Radial velocity measures only the component of stellar wobble along our line of sight. The true wobble amplitude is larger by a factor of 1/sin i. Since sin i ≤ 1, dividing by sin i gives a value ≥ M sin i. The minimum mass occurs when i = 90° (edge-on orbit, sin i = 1) — if the orbit is more face-on, the true mass is larger. We can only say the planet is at least 2.0 MJ; it could be a brown dwarf or even a star if the orbital plane happens to be nearly face-on."

- question: "A star shows both periodic radial velocity variations AND transits by the same planet. What does combining these two detections reveal that neither method alone can provide?"
  type: multiple-choice
  options:
    - "The planet's atmospheric composition — transit spectroscopy combined with RV mass constrains chemistry"
    - "The planet's true mass and mean density — transit resolves the sin i ambiguity, and density distinguishes rocky from gaseous worlds"
    - "The planet's surface temperature — the mass-radius combination constrains internal heat sources"
    - "The orbital eccentricity — transits reveal the shape of the orbit that RV alone cannot"
  answer: 1
  explanation: "The key contribution of combining methods is resolving the sin i ambiguity. A transit occurs only if the orbit is nearly edge-on (i ≈ 90°), so sin i ≈ 1, and M sin i ≈ true mass. The transit also gives the planet's radius from the depth of the brightness dip. With both true mass and radius, you can calculate mean density (mass/volume) — the single most diagnostic quantity for distinguishing rocky terrestrial planets from gas giants with similar masses."

- question: "The transit method measures a planet's mass directly from the depth of the brightness dip when the planet crosses its star."
  type: true-false
  answer: false
  explanation: "The transit depth measures the fraction of starlight blocked by the planet — proportional to the ratio of their cross-sectional areas, not to mass. This gives the planet's radius (relative to the stellar radius), not its mass. Mass information comes from the radial velocity method (stellar wobble amplitude) or transit timing variations (gravitational perturbations). It's a common misconception that transit depth encodes mass; it encodes size."

- question: "The radial velocity method is more sensitive to massive planets in short-period orbits than to Earth-mass planets in wide orbits."
  type: true-false
  answer: true
  explanation: "Radial velocity amplitude scales with planet mass — a more massive planet pulls the star harder, producing a larger Doppler shift. Short orbital periods mean more orbits observed per year, and the star's orbital velocity around the barycenter is higher for close-in planets. This creates a strong selection bias: RV surveys detect 'hot Jupiters' (massive, close-in) far more easily than Earth-analogs (low mass, wide orbit). Understanding these biases is essential for interpreting exoplanet statistics — the observed population is not a random sample of what exists."

- question: "Why does the radial velocity method yield only a minimum mass for a planet, and how does combining it with the transit method resolve this ambiguity?"
  type: short-answer
  answer: "Radial velocity measures the component of the star's orbital velocity along our line of sight. If the planet's orbital plane is tilted relative to our line of sight (inclination i < 90°), we only see a fraction sin i of the full stellar wobble. The measured quantity is M sin i, not M. The true mass M = (M sin i) / sin i is larger whenever i < 90°. A transit can only occur when the orbital plane is nearly edge-on (i ≈ 90°), so if the same planet both transits and produces an RV signal, sin i ≈ 1 and the minimum mass is very close to the true mass — resolving the ambiguity."
  explanation: "This is the power of multi-method astronomy: each method's limitation is another method's strength. Radial velocity is degenerate in inclination; transits require a specific inclination. When both are observed, the degeneracy breaks and the physical parameters become fully determined. Adding the transit radius to the RV mass then enables density estimates, which would otherwise be impossible."
```

## Explainer

From Kepler's laws you already know that a planet's orbital period and semi-major axis are linked to the mass of the system. The key insight behind exoplanet detection is that a planet does not simply orbit a star — the star and planet both orbit their common center of mass, called the **barycenter**. Even a massive star wobbles slightly in response to a planet's gravitational pull, and that wobble encodes information about the planet's orbit. The two most productive detection methods exploit this wobble in different ways.

The **radial velocity method** measures the star's wobble along our line of sight using the Doppler effect. As the star moves toward us, its light shifts slightly blueward; as it moves away, the shift is redward. The period of this oscillation gives the planet's orbital period directly, and the amplitude of the velocity shift reveals how hard the planet is tugging — which depends on the planet's mass and the orbital inclination. Because we only measure motion along the line of sight, radial velocity yields a **minimum mass** (M sin i), not the true mass. A face-on orbit, for example, would produce no radial motion at all even though the star wobbles just as much in the plane of the sky.

The **transit method** works from a different geometric vantage. When a planet's orbit is nearly edge-on to us, the planet passes in front of its star once per orbit, blocking a fraction of the starlight. The depth of the brightness dip tells you the ratio of the planet's cross-sectional area to the star's — giving the planet's radius directly. The timing of repeated transits pins down the orbital period with extraordinary precision. Crucially, a transit also tells you the orbital inclination is close to 90°, which resolves the sin i ambiguity from radial velocity. Combining transit radius with radial velocity mass gives you the planet's **mean density**, the single most diagnostic quantity for distinguishing rocky worlds from gas giants.

Other methods fill important niches. **Direct imaging** captures photons from the planet itself, but requires the planet to be bright, far from its star, and young (so it still glows from formation heat). **Astrometry** measures the star's wobble in the plane of the sky rather than along the line of sight, complementing radial velocity. **Transit timing variations** detect unseen planets through the gravitational tugs they exert on a known transiting planet, shifting its transit times forward or backward by seconds to minutes. Each method has its own selection biases — radial velocity favors massive, close-in planets; transits require edge-on geometry; direct imaging favors wide, luminous companions — so a complete census of exoplanets requires all of them working together.
