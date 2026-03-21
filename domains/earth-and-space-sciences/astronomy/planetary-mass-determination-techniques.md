---
id: planetary-mass-determination-techniques
title: Planetary Mass Determination
domain: earth-and-space-sciences
course: astronomy
prerequisites:
- id: kepler-laws-orbital-motion-derivation
  type: hard
- id: exoplanet-orbital-determination-methods
  type: soft
builds-toward:
- planetary-structure-and-internal-composition
tags:
- planetary-science
- mass
- composition
stage: formal-systems
status: draft
---

# Planetary Mass Determination

## Core Idea
Planetary mass is determined through orbital dynamics: a planet's mass is inferred from the gravitational perturbations it produces on its host star (radial velocity) or on transiting planet timing. For moons, orbital velocities of satellites yield the primary body's mass. Combining mass with radius (from transit photometry) enables determination of mean density, providing strong constraints on planetary composition and internal structure.

## Questions

```yaml
- question: "A planet is detected via transit photometry, and astronomers measure a precise planet radius from the dip in starlight. A student says 'Now we know what the planet is made of.' An astronomer disagrees. Why?"
  type: multiple-choice
  options:
    - "Transit photometry cannot reliably measure radius — only radial velocity can determine planetary size"
    - "Radius alone cannot determine composition because a rocky super-Earth and a puffy mini-Neptune can have identical radii but very different masses and densities"
    - "Planetary composition can only be inferred from atmospheric spectroscopy, not from radius measurements"
    - "The transit radius is the planet's atmospheric radius, not its solid surface radius, making all composition inferences invalid"
  answer: 1
  explanation: "Knowing radius alone is insufficient because density — the key discriminator of composition — requires both mass and volume. A rocky super-Earth and a water-rich mini-Neptune or a gas-dominated sub-Neptune can occupy the same radius while differing by a factor of 3–10 in mass. Only by combining transit-derived radius with mass from radial velocity or transit timing can you compute mean density and constrain composition. This is why mass determination is called the 'essential second measurement' — a radius without a mass is an incomplete characterization."

- question: "Radial velocity measurements of a host star yield 'M sin i' rather than the planet's true mass. Under what condition does this ambiguity resolve?"
  type: multiple-choice
  options:
    - "When the planet's orbital period exceeds one Earth year"
    - "When the host star's spectral type is precisely determined by spectroscopy"
    - "When the planet also transits, confirming a nearly edge-on orbit so sin i ≈ 1 and the true mass is recovered"
    - "When at least three complete orbital cycles have been observed"
  answer: 2
  explanation: "Radial velocity measures the star's reflex motion along our line of sight. If the orbital plane is tilted at angle i to our line of sight, we only see the component v sin i of the star's true velocity amplitude. This gives M sin i — always a lower bound on the planet's mass. If the planet transits, the geometry is constrained: the planet must pass directly across the star's disk, requiring a nearly edge-on orbit (i close to 90°). When sin i ≈ 1, the measured M sin i equals the true mass to good approximation. Combining transit geometry with radial velocity is how most exoplanet masses are precisely determined."

- question: "A planet with a mean density below 1.5 g/cm³ almost certainly has a thick hydrogen-helium atmosphere, because such a low density cannot be achieved by rock or water alone."
  type: true-false
  answer: true
  explanation: "Rock has density ~3–8 g/cm³ depending on composition; water ice is ~1 g/cm³. A planet composed predominantly of these materials will have a mean density well above 1.5 g/cm³ for any realistic mass. Hydrogen and helium are the only abundant materials with sufficiently low density to bring a planet's mean density below ~1.5 g/cm³ — they must form a significant fraction of the planet's mass. This is why density is such a powerful compositional diagnostic: very low density is nearly unambiguous evidence for a gas-dominated envelope."

- question: "Radial velocity measurements give you the planet's full, true mass in all cases, as long as the spectral data is precise enough."
  type: true-false
  answer: false
  explanation: "Radial velocity yields M sin i — the planet's mass multiplied by the sine of the orbital inclination. Since inclination is generally unknown from radial velocity data alone, you get a minimum mass, not the true mass. If the orbit is face-on (i = 0°), you would detect no Doppler shift at all despite the planet's gravity. Inclination can only be independently constrained by other observations — most usefully, a transit detection, which requires i close to 90°. Without inclination information, radial velocity gives a lower bound on mass, and the true mass could be significantly larger."

- question: "Why is knowing both a planet's mass and its radius more scientifically valuable than knowing either alone? What additional quantity does the combination enable, and why does that quantity matter?"
  type: short-answer
  answer: "Mass and radius together give you mean density (density = mass / volume). Density is the single most powerful constraint on planetary composition available from indirect observation. A rocky, Earth-like planet has density ~5–6 g/cm³; a gas giant like Jupiter has density ~1.3 g/cm³; a water-dominated world might be ~2–3 g/cm³. Without density, a measured radius of 2 Earth radii is ambiguous — it could be a dense rocky super-Earth or a low-density sub-Neptune with a thick gas envelope. Without density, a measured mass of 10 Earth masses could be a rocky object or one with substantial water. The combination breaks this degeneracy and allows planets to be placed on a mass-density diagram that physically distinguishes composition classes."
  explanation: "This is the central payoff of combining multiple measurement techniques. Transit photometry and radial velocity individually produce incomplete characterizations; together, they unlock composition constraints that transform a 'detected planet' into a 'characterized world.' This is why astronomers invest heavily in follow-up mass measurements for every transiting planet candidate — the radius alone, however precisely measured, cannot tell you what you actually want to know about the planet's nature."
```

## Explainer

You already know from Kepler's third law that orbital period and semi-major axis are related to the total mass of a gravitationally bound system. Planetary mass determination is the art of inverting this relationship — using observed orbital motions to solve for the mass that produces them. The challenge is that planets are faint and small compared to their host stars, so we almost never weigh a planet directly. Instead, we measure the gravitational effects it produces on things we *can* observe.

The most common technique uses **radial velocity measurements** of the host star. As a planet orbits, the star responds with a reflex motion around the barycenter. The amplitude of the star's velocity wobble depends on the planet's mass, the orbital period, and the inclination of the orbit to our line of sight. From the Doppler data alone, you get M sin i — a minimum mass. If the planet also transits (meaning the orbit is nearly edge-on, so sin i ≈ 1), the inclination ambiguity vanishes and you recover the true mass. For systems with multiple transiting planets, **transit timing variations** offer an independent mass measurement: gravitational interactions between planets shift transit times by detectable amounts, and modeling those shifts reveals the masses involved without any spectroscopic data at all.

For bodies in our own solar system, mass determination is more direct. A planet's mass can be measured by tracking the orbit of a natural satellite — apply Kepler's third law to the moon's orbit and you solve for the planet's mass. Spacecraft flybys offer similar precision: the trajectory deflection of a probe passing near a planet is governed entirely by the planet's gravitational field, yielding mass to high accuracy. This is how we first obtained precise masses for Mercury and Pluto, which lack large natural satellites.

The real scientific payoff comes when you combine mass with radius. A transit gives you the planet's radius from the depth of the brightness dip; radial velocity or timing variations give you the mass. Dividing mass by volume yields **mean density**, and density is the single most powerful discriminator of composition. A density near 5.5 g/cm³ suggests a rocky, Earth-like interior. A density below 1.5 g/cm³ points to a thick hydrogen-helium envelope — a gas giant or sub-Neptune. Intermediate densities might indicate water-rich worlds or rocky cores with modest atmospheres. Without mass, a transit radius alone cannot distinguish a dense rocky super-Earth from a puffy mini-Neptune of the same size, which is why mass determination is the essential second measurement that turns a detected planet into a characterized world.
