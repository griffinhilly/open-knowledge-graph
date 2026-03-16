---
id: exoplanet-detection-methods
title: Exoplanet Detection Methods
domain: earth-and-space-sciences
course: astronomy
prerequisites:
- id: doppler-effect
  type: hard
- id: binary-stars-and-stellar-systems
  type: soft
- id: solar-system-structure
  type: soft
- id: keplers-laws
  type: soft
- id: binomial-distribution
  type: soft
- id: hypothesis-testing-framework
  type: soft
tags:
- exoplanets
- transit-method
- radial-velocity
- direct-imaging
- gravitational-microlensing
- hot-Jupiters
- Kepler-mission
stage: abstract-reasoning
status: validated
---

# Exoplanet Detection Methods

## Core Idea
Exoplanets — planets orbiting other stars — are almost never detected directly because they are overwhelmed by their host star's light. The transit method detects the periodic fractional dimming of a star when a planet crosses in front of it, yielding the planet's orbital period and radius ratio. The radial velocity method detects the reflex Doppler wobble a planet induces in its star's spectral lines, yielding minimum mass and orbital parameters. Both methods are biased toward large planets in close orbits, explaining the prevalence of 'hot Jupiters' in early catalogs. The Kepler and TESS space missions have discovered thousands of exoplanet candidates using the transit method.

## How It's Best Learned
Analyze a real transit light curve to extract orbital period and planet-to-star radius ratio. Calculate the expected radial velocity amplitude for planets of different masses and orbital distances to understand why Earth-mass planets are difficult to detect.

## Common Misconceptions
- The absence of Earth-like planets in early exoplanet surveys did not mean they were rare — it reflected observational bias toward large, close-in planets that produce the strongest signals.
- Transit detection gives only the radius; determining whether a planet is rocky or gaseous requires combining transit and radial velocity measurements.

## Explainer

Finding planets around other stars is an extraordinary challenge because of the contrast problem: a star like the Sun is roughly a billion times brighter than an Earth-like planet in visible light, and the angular separation between them, as seen from interstellar distances, is vanishingly small. Direct imaging — simply taking a picture — works only for the largest, hottest, youngest planets orbiting far from faint stars. For the vast majority of exoplanets, detection relies on indirect methods that observe the planet's *effect* on its host star rather than the planet itself.

The **radial velocity method** exploits the Doppler effect you studied as a prerequisite. A planet does not orbit a stationary star; both the star and planet orbit their common center of mass. As the star moves toward us in its small reflex orbit, its spectral lines shift slightly blue; as it moves away, they shift red. By measuring these periodic shifts with extreme precision (modern spectrographs can detect velocity changes of less than 1 meter per second), astronomers can infer the planet's orbital period, its minimum mass (the true mass depends on the unknown orbital inclination), and the orbit's eccentricity. This method is most sensitive to massive planets in close orbits, since they induce larger stellar wobbles — which is why the first exoplanet discovered around a Sun-like star, 51 Pegasi b, was a "hot Jupiter" with half Jupiter's mass orbiting in just 4.2 days.

The **transit method** detects the tiny dip in a star's brightness when a planet passes in front of it as seen from Earth. The fractional dimming equals the ratio of the planet's cross-sectional area to the star's — a Jupiter-sized planet blocks about 1% of a Sun-like star's light, while an Earth-sized planet blocks only 0.01%. By measuring the dimming depth you get the planet-to-star radius ratio, and by measuring the interval between successive transits you get the orbital period. The catch is geometric: transits are only visible if the orbital plane is nearly edge-on to our line of sight, which for an Earth-Sun analog happens only about 0.5% of the time. This means transit surveys must monitor enormous numbers of stars to find the rare, favorably aligned systems — exactly what the Kepler and TESS space missions were designed to do.

Each method has characteristic **selection biases** that shape the population of planets we discover. Radial velocity favors massive planets (bigger wobble) in short-period orbits (more observations per unit time, and the wobble amplitude scales with the inverse of orbital distance). Transits favor large planets (deeper dips) that are close to their stars (higher geometric probability of alignment, and more frequent transits). Together, these biases explain why early exoplanet catalogs were dominated by hot Jupiters — not because such planets are common, but because they are the easiest to detect by both methods. As instruments have improved, surveys have pushed toward smaller, longer-period planets, revealing that super-Earths and sub-Neptunes are actually the most common planet types in the galaxy. Combining transit and radial velocity data for the same planet is especially powerful: the transit gives the radius, the radial velocity gives the mass, and dividing mass by volume gives the bulk density — the first clue to whether a planet is rocky, icy, or gaseous.
